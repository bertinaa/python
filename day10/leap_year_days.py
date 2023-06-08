def is_leap(year):
    if ((year % 4 == 0 and year%100 != 0 ) or (year%400==0)):
        return True
    else:
        return False

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if month==2:
        leap_or_not = is_leap(year)
        if leap_or_not == True:
            return month_days[1]+1
        else:
            return month_days[1]
    return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







