# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
import datetime as dt

app = FastAPI(title="Shopping Mall Analytics")

# --------------------------
# Load your data (CSV)
# --------------------------
df = pd.read_csv(r"C:\Users\sbert\Documents\MLOps\customer_shopping_data.csv", parse_dates=['invoice_date'])

@app.get("/")
def home():
    return {"message": "Welcome to the Shopping Mall Analytics API! Visit /docs for API docs."}

################################################## debugging





# --------------------------
# Mall performance endpoint
# --------------------------
from fastapi.responses import HTMLResponse

@app.get("/mall-performance-html", response_class=HTMLResponse)
def mall_performance_html():
    # Aggregate metrics per mall
    mall_summary = df.groupby('shopping_mall').agg(
        total_sales=('price', 'sum'),
        total_qty=('quantity', 'sum'),
        unique_customers=('customer_id', 'nunique'),
        num_invoices=('invoice_no', 'nunique'),
        avg_order_value=('price', 'mean')
    ).reset_index()

    # Format numbers: comma separated, 2 decimal places
    mall_summary['total_sales'] = mall_summary['total_sales'].map("{:,.2f}".format)
    mall_summary['avg_order_value'] = mall_summary['avg_order_value'].map("{:,.2f}".format)
    mall_summary['total_qty'] = mall_summary['total_qty'].map("{:,}".format)
    mall_summary['unique_customers'] = mall_summary['unique_customers'].map("{:,}".format)
    mall_summary['num_invoices'] = mall_summary['num_invoices'].map("{:,}".format)

    # Rename columns to Title Case
    mall_summary.columns = [col.replace('_', ' ').title() for col in mall_summary.columns]

    # Generate HTML table
    html_table = mall_summary.to_html(index=False, classes='table table-striped', justify='left', escape=False)

    # Add some styling
    html_content = f"""
    <html>
        <head>
            <title>Mall Performance</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;  /* Left-align headers & cells */
                }}
                th {{
                    background-color: #031278;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h2>Mall Performance Summary</h2>
            {html_table}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)



# --------------------------
# RFM Segmentation endpoint
# --------------------------
from fastapi.responses import HTMLResponse
import pandas as pd
import datetime as dt
import numpy as np

@app.get("/rfm-segmentation-html", response_class=HTMLResponse)
def rfm_segmentation_html():

    # Ensure invoice_date is datetime
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    df_clean = df.dropna(subset=['invoice_date'])

    # Create 'monetary' column = quantity * price
    df_clean['monetary'] = df_clean['quantity'] * df_clean['price']

    reference_date = df_clean['invoice_date'].max() + dt.timedelta(days=1)

    # Recency
    recency_df = df_clean.groupby('customer_id')['invoice_date'].max().reset_index()
    recency_df['recency'] = (reference_date - recency_df['invoice_date']).dt.days

    # Frequency
    frequency_df = df_clean.groupby('customer_id')['invoice_no'].nunique().reset_index().rename(columns={'invoice_no':'frequency'})

    # Monetary
    monetary_df = df_clean.groupby('customer_id')['monetary'].sum().reset_index()

    rfm = recency_df.merge(frequency_df, on='customer_id').merge(monetary_df, on='customer_id')

    # Fill NaNs
    rfm['recency'] = rfm['recency'].fillna(rfm['recency'].max())
    rfm['frequency'] = rfm['frequency'].fillna(0)
    rfm['monetary'] = rfm['monetary'].fillna(0)

    # ----------------------
    # Safe scoring function
    # ----------------------
    def score_column(series, ascending=True):
        ranked = series.rank(method='first', ascending=ascending)
        labels = [1,2,3,4,5]
        try:
            scored = pd.qcut(ranked, 5, labels=labels)
        except ValueError:  # not enough unique values
            scored = pd.Series(np.ones(len(series)), index=series.index)
        return scored.astype(int)

    rfm['R_score'] = score_column(rfm['recency'], ascending=False)
    rfm['F_score'] = score_column(rfm['frequency'], ascending=True)
    rfm['M_score'] = score_column(rfm['monetary'], ascending=True)

    rfm['RFM_Score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

    # Segment
    def segment_customer(score):
        if score >= 12: return 'Champions'
        elif score >= 9: return 'Loyal'
        elif score >= 6: return 'At Risk'
        else: return 'Lost'

    rfm['Segment'] = rfm['RFM_Score'].apply(segment_customer)

    # Prepare HTML table
    table_df = rfm[['customer_id','R_score','F_score','M_score','RFM_Score','Segment']].copy()
    table_df.columns = [col.replace('_',' ').title() for col in table_df.columns]  # Title Case

    # Format numbers
    table_df[['R Score','F Score','M Score','Rfm Score']] = table_df[['R Score','F Score','M Score','Rfm Score']].applymap("{:,}".format)

    html_table = table_df.to_html(index=False, classes='table table-striped', justify='left', escape=False)

    html_content = f"""
    <html>
        <head>
            <title>RFM Segmentation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #031278;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h2>RFM Segmentation Summary</h2>
            {html_table}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)




# --------------------------
# Repeat vs One-time endpoint
# --------------------------
@app.get("/repeat-vs-one-html", response_class=HTMLResponse)
def repeat_vs_one_html():
    # Ensure net_sales column exists
    df['net_sales'] = df['quantity'] * df['price']

    # Count number of invoices per customer
    customer_orders = df.groupby('customer_id')['invoice_no'].nunique().reset_index()
    customer_orders.rename(columns={'invoice_no': 'num_invoices'}, inplace=True)

    # Categorize customers
    customer_orders['Customer Type'] = np.where(customer_orders['num_invoices'] > 1,
                                                'Repeat Customer', 'One-time Customer')

    # Total spend per customer
    customer_spend = df.groupby('customer_id')['net_sales'].sum().reset_index()
    customer_orders = customer_orders.merge(customer_spend, on='customer_id', how='left')

    # Aggregate spend by customer type
    repeat_vs_one_df = customer_orders.groupby('Customer Type')['net_sales'].sum().reset_index()
    repeat_vs_one_df.rename(columns={'net_sales': 'Total Sales'}, inplace=True)

    # Format numbers
    repeat_vs_one_df['Total Sales'] = repeat_vs_one_df['Total Sales'].map("{:,.2f}".format)

    # Generate HTML table
    html_table = repeat_vs_one_df.to_html(index=False, classes='table table-striped', justify='left', escape=False)

    html_content = f"""
    <html>
        <head>
            <title>Repeat vs One-time Customers</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 50%;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #031278;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h2>Repeat vs One-time Customers</h2>
            {html_table}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# --------------------------
# Category insights endpoint
# --------------------------
@app.get("/category-insights-html", response_class=HTMLResponse)
def category_insights_html():
    # Ensure net_sales column exists
    df['net_sales'] = df['quantity'] * df['price']

    # Aggregate category metrics
    category_perf = df.groupby('category').agg(
        total_sales=('net_sales', 'sum'),
        total_qty=('quantity', 'sum'),
        num_customers=('customer_id', 'nunique'),
        num_invoices=('invoice_no', 'nunique')
    ).reset_index()

    # Average order value
    category_perf['avg_order_value'] = category_perf['total_sales'] / category_perf['num_invoices']

    # Format numbers: comma separated, 2 decimal places
    category_perf['total_sales'] = category_perf['total_sales'].map("{:,.2f}".format)
    category_perf['avg_order_value'] = category_perf['avg_order_value'].map("{:,.2f}".format)
    category_perf['total_qty'] = category_perf['total_qty'].map("{:,}".format)
    category_perf['num_customers'] = category_perf['num_customers'].map("{:,}".format)
    category_perf['num_invoices'] = category_perf['num_invoices'].map("{:,}".format)

    # Title case columns
    category_perf.columns = [col.replace('_', ' ').title() for col in category_perf.columns]

    # Generate HTML table
    html_table = category_perf.to_html(index=False, classes='table table-striped', justify='left', escape=False)

    html_content = f"""
    <html>
        <head>
            <title>Category Insights</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 80%;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #031278;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h2>Category Insights Summary</h2>
            {html_table}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

from fastapi.responses import HTMLResponse

# Mapping malls to regions
mall_region_map = {
    "Kanyon": "Europe",
    "Forum Istanbul": "Europe",
    "Metrocity": "Europe",
    "Istinye Park": "Europe",
    "Mall of Istanbul": "Europe",
    "Cevahir AVM": "Europe",
    "Zorlu Center": "Europe",
    "Metropol AVM": "Asia",
    "Emaar Square Mall": "Asia",
    "Viaport Outlet": "Asia"
}

@app.get("/store-region-performance-html", response_class=HTMLResponse)
def store_region_performance_html():
    # Create net_sales
    df['net_sales'] = df['quantity'] * df['price']

    # Add region column
    df['region'] = df['shopping_mall'].map(mall_region_map)

    # Aggregate metrics
    store_region_perf = df.groupby(['region', 'shopping_mall']).agg(
        total_sales=('net_sales', 'sum'),
        total_qty=('quantity', 'sum'),
        num_customers=('customer_id', 'nunique'),
        num_invoices=('invoice_no', 'nunique')
    ).reset_index()

    # Average order value
    store_region_perf['avg_order_value'] = store_region_perf['total_sales'] / store_region_perf['num_invoices']

    # Format numbers
    store_region_perf['total_sales'] = store_region_perf['total_sales'].map("{:,.2f}".format)
    store_region_perf['avg_order_value'] = store_region_perf['avg_order_value'].map("{:,.2f}".format)
    store_region_perf['total_qty'] = store_region_perf['total_qty'].map("{:,}".format)
    store_region_perf['num_customers'] = store_region_perf['num_customers'].map("{:,}".format)
    store_region_perf['num_invoices'] = store_region_perf['num_invoices'].map("{:,}".format)

    # Title case headers
    store_region_perf.columns = [col.replace('_', ' ').title() for col in store_region_perf.columns]

    # Generate HTML table
    html_table = store_region_perf.to_html(index=False, classes='table table-striped', justify='left', escape=False)

    html_content = f"""
    <html>
        <head>
            <title>Store vs Region Performance</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 95%;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #031278;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
            </style>
        </head>
        <body>
            <h2>Store vs Region Performance Summary</h2>
            {html_table}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# --------------------------
# Top 10 Customers Endpoint
# --------------------------
@app.get("/top-customers")
def top_customers():
    try:
        # Calculate net sales if not already in df
        df['net_sales'] = df['quantity'] * df['price']

        # Aggregate sales per customer
        customer_sales = df.groupby("customer_id").agg(
            total_sales=("net_sales", "sum"),
            num_invoices=("invoice_no", "nunique"),
            total_quantity=("quantity", "sum")
        ).reset_index()

        # Sort customers by total sales
        customer_sales = customer_sales.sort_values(by="total_sales", ascending=False)

        # Take top 10 customers
        top_customers_df = customer_sales.head(10).copy()

        # Add % contribution to total revenue
        total_revenue = customer_sales["total_sales"].sum()
        top_customers_df["revenue_share"] = (top_customers_df["total_sales"] / total_revenue) * 100

        # Format numbers nicely
        top_customers_df["total_sales"] = top_customers_df["total_sales"].apply(lambda x: f"{x:,.2f}")
        top_customers_df["total_quantity"] = top_customers_df["total_quantity"].apply(lambda x: f"{x:,}")
        top_customers_df["num_invoices"] = top_customers_df["num_invoices"].apply(lambda x: f"{x:,}")
        top_customers_df["revenue_share"] = top_customers_df["revenue_share"].apply(lambda x: f"{x:.2f}%")

        # Rename columns to Title Case
        top_customers_df.columns = [col.replace('_', ' ').title() for col in top_customers_df.columns]


        # Convert to HTML
        html_table = top_customers_df.to_html(
            index=False,
            classes="table table-striped table-bordered",
            border=0,
            justify="left"
        )

        # Wrap in HTML
        html_content = f"""
        <html>
            <head>
                <title>Top 10 Customers</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 40px;
                    }}
                    h2 {{
                        color: #333;
                        margin-bottom: 20px;
                    }}
                    table {{
                        border-collapse: collapse;
                        width: 100%;
                        font-size: 14px;
                    }}
                    th {{
                        
                        text-align: left;
                        background-color: #031278;
                        color: white;
                        padding: 8px;
                        font-weight: bold;    
                        font-size: 15px; 
                    }}
                    td {{
                        padding: 8px;
                        text-align: left;
                    }}
                    tr:nth-child(even) {{
                        background-color: #fafafa;
                    }}
                </style>
            </head>
            <body>
                <h2>🏆 Top 10 Customers by Purchase Value</h2>
                {html_table}
            </body>
        </html>
        """

        return HTMLResponse(content=html_content)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# --------------------------
# High vs Low Value Segmentation
# --------------------------
@app.get("/high-vs-low-value")
def high_vs_low_value():
    # Calculate spend per customer
    customer_spend = df.groupby('customer_id')['price'].sum().reset_index()
    customer_spend.rename(columns={'price': 'total_spend'}, inplace=True)

    # Median spend as threshold
    threshold = customer_spend['total_spend'].median()

    # Classify customers
    customer_spend['segment'] = np.where(
        customer_spend['total_spend'] >= threshold, 
        'High Value', 
        'Low Value'
    )

    # Aggregate results
    segmentation = customer_spend.groupby('segment')['total_spend'].agg(
        total_spend='sum', 
        avg_spend='mean', 
        num_customers='count'
    ).reset_index()

    # Make column names Title Case
    segmentation.rename(columns={
        'segment': 'Segment',
        'total_spend': 'Total Spend',
        'avg_spend': 'Average Spend',
        'num_customers': 'Number of Customers'
    }, inplace=True)

    # Convert to HTML table
    html_table = segmentation.to_html(index=False, classes='table', escape=False)

    # Wrap in HTML
    html_content = f"""
    <html>
        <head>
            <title>High vs Low Value Segmentation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                h2 {{
                    color: #333;
                    margin-bottom: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    font-size: 14px;
                }}
                th {{
                    text-align: left;
                    background-color: #031278;
                    color: white;
                    padding: 8px;
                    font-weight: bold;
                    font-size: 15px;
                }}
                td {{
                    padding: 8px;
                    text-align: left;
                }}
                tr:nth-child(even) {{
                    background-color: #fafafa;
                }}
            </style>
        </head>
        <body>
            <h2>💰 High vs Low Value Customer Segmentation</h2>
            {html_table}
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)


# --------------------------
# Seasonality Analysis (Monthly & Quarterly Trends)
# --------------------------
@app.get("/seasonality-analysis", response_class=HTMLResponse)
def seasonality_analysis():
    df_copy = df.copy()

    # Convert invoice_date with dayfirst=True
    df_copy['invoice_date'] = pd.to_datetime(df_copy['invoice_date'], dayfirst=True, errors='coerce')

    # Drop invalid dates if any
    df_copy = df_copy.dropna(subset=['invoice_date'])

    # Compute total sales
    df_copy['sales'] = df_copy['quantity'] * df_copy['price']

    # Add month and quarter columns
    df_copy['Month'] = df_copy['invoice_date'].dt.to_period('M').astype(str)
    df_copy['Quarter'] = df_copy['invoice_date'].dt.to_period('Q').astype(str)

    # Monthly sales trend
    monthly_trend = df_copy.groupby('Month').agg(
        Total_Sales=('sales', 'sum'),
        Total_Quantity=('quantity', 'sum'),
        Unique_Customers=('customer_id', 'nunique')
    ).reset_index()

    # Quarterly sales trend
    quarterly_trend = df_copy.groupby('Quarter').agg(
        Total_Sales=('sales', 'sum'),
        Total_Quantity=('quantity', 'sum'),
        Unique_Customers=('customer_id', 'nunique')
    ).reset_index()

    # Format numbers (commas + 2 decimals for sales, commas for integers)
    for df_temp in [monthly_trend, quarterly_trend]:
        df_temp['Total_Sales'] = df_temp['Total_Sales'].apply(lambda x: f"{x:,.2f}")
        df_temp['Total_Quantity'] = df_temp['Total_Quantity'].apply(lambda x: f"{x:,}")
        df_temp['Unique_Customers'] = df_temp['Unique_Customers'].apply(lambda x: f"{x:,}")

        # Ensure all column names are Title Case
        df_temp.columns = [col.replace('_', ' ').title() for col in df_temp.columns]

    # Convert both tables to HTML
    monthly_html = monthly_trend.to_html(index=False, classes='table', escape=False)
    quarterly_html = quarterly_trend.to_html(index=False, classes='table', escape=False)

    # Wrap in HTML
    html_content = f"""
    <html>
        <head>
            <title>Seasonality Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                h2 {{
                    color: #333;
                    margin-top: 40px;
                    margin-bottom: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    font-size: 14px;
                    margin-bottom: 40px;
                }}
                th {{
                    text-align: left;
                    background-color: #031278;
                    color: white;
                    padding: 8px;
                    font-weight: bold;
                    font-size: 15px;
                }}
                td {{
                    padding: 8px;
                    text-align: left;
                }}
                tr:nth-child(even) {{
                    background-color: #fafafa;
                }}
            </style>
        </head>
        <body>
            <h2>📅 Monthly Trends</h2>
            {monthly_html}

            <h2>📊 Quarterly Trends</h2>
            {quarterly_html}
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)

# --------------------------
# Payment Method Preference endpoint
# --------------------------
@app.get("/payment-method-preference", response_class=HTMLResponse)
def payment_method_preference():
    # Aggregate by payment method
    payment_df = df.groupby('payment_method').agg(
        Total_Transactions=('invoice_no', 'nunique'),
        Total_Quantity=('quantity', 'sum'),
        Total_Sales=('price', 'sum')
    ).reset_index()

    # Format numbers
    payment_df['Total_Transactions'] = payment_df['Total_Transactions'].apply(lambda x: f"{x:,}")
    payment_df['Total_Quantity'] = payment_df['Total_Quantity'].apply(lambda x: f"{x:,}")
    payment_df['Total_Sales'] = payment_df['Total_Sales'].apply(lambda x: f"{x:,.2f}")

    # Title case column headers
    payment_df.columns = [col.replace('_', ' ').title() for col in payment_df.columns]

    # Convert to HTML
    html_table = payment_df.to_html(index=False, classes='table', escape=False)

    # Wrap in HTML
    html_content = f"""
    <html>
        <head>
            <title>Payment Method Preference</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                h2 {{
                    color: #333;
                    margin-bottom: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    font-size: 14px;
                }}
                th {{
                    text-align: left;
                    background-color: #031278;
                    color: white;
                    padding: 8px;
                    font-weight: bold;
                    font-size: 15px;
                }}
                td {{
                    padding: 8px;
                    text-align: left;
                }}
                tr:nth-child(even) {{
                    background-color: #fafafa;
                }}
            </style>
        </head>
        <body>
            <h2>💳 Payment Method Preference</h2>
            {html_table}
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)

# --------------------------
# Campaign Simulation endpoint
# --------------------------
@app.get("/campaign-simulation", response_class=HTMLResponse)
def campaign_simulation():
    # 1. Aggregate customer spend
    customer_spend = df.groupby('customer_id').agg(
        Total_Spend=('price', 'sum')
    ).reset_index()

    # 2. Identify high-value customers (top 20% spenders)
    threshold = customer_spend['Total_Spend'].quantile(0.8)
    customer_spend['Customer_Type'] = customer_spend['Total_Spend'].apply(
        lambda x: 'High-Value' if x >= threshold else 'Low-Value'
    )

    # 3. Simulate 10% discount for high-value customers
    discount_rate = 0.10
    customer_spend['Projected_Spend'] = customer_spend.apply(
        lambda row: row['Total_Spend'] * (1 + discount_rate) if row['Customer_Type']=='High-Value' else row['Total_Spend'],
        axis=1
    )

    # 4. Calculate ROI
    customer_spend['Discount_Offered'] = customer_spend.apply(
        lambda row: row['Total_Spend'] * discount_rate if row['Customer_Type']=='High-Value' else 0,
        axis=1
    )
    total_discount = customer_spend['Discount_Offered'].sum()
    total_projected_revenue = customer_spend['Projected_Spend'].sum()
    roi = (total_projected_revenue - df['price'].sum()) / total_discount if total_discount > 0 else 0

    # 5. Prepare summary table
    summary_df = customer_spend.groupby('Customer_Type').agg(
        Customers=('customer_id', 'nunique'),
        Current_Revenue=('Total_Spend', 'sum'),
        Projected_Revenue=('Projected_Spend', 'sum'),
        Total_Discount=('Discount_Offered', 'sum')
    ).reset_index()

    # Format numbers
    for col in ['Current_Revenue','Projected_Revenue','Total_Discount']:
        summary_df[col] = summary_df[col].apply(lambda x: f"{x:,.2f}")
    summary_df['Customers'] = summary_df['Customers'].apply(lambda x: f"{x:,}")

    # Title case column headers
    summary_df.columns = [col.replace('_',' ').title() for col in summary_df.columns]

    # Convert to HTML table
    html_table = summary_df.to_html(index=False, classes='table', escape=False)

    # Wrap in HTML with styling
    html_content = f"""
    <html>
        <head>
            <title>Campaign Simulation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                h2 {{
                    color: #333;
                    margin-bottom: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    font-size: 14px;
                }}
                th {{
                    text-align: left;
                    background-color: #031278;
                    color: white;
                    padding: 8px;
                    font-weight: bold;
                    font-size: 15px;
                }}
                td {{
                    padding: 8px;
                    text-align: left;
                }}
                tr:nth-child(even) {{
                    background-color: #fafafa;
                }}
            </style>
        </head>
        <body>
            <h2>🎯 Campaign Simulation - Targeting High-Value Customers</h2>
            {html_table}
            <p><strong>Overall Projected ROI:</strong> {roi:.2f}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)
