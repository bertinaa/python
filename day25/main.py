import pandas

data = pandas.read_csv("squirrel.csv")

count_gray_squirrel = len(data[data["Primary Fur Color"]=="Gray"])
count_black_squirrel = len(data[data["Primary Fur Color"]=="Black"])
count_cinnomon_squirrel = len(data[data["Primary Fur Color"]=="Cinnamon"])




data_dict = {
    "fur" : ["Gray","Cinnamon","Black"],
    "count" : [count_gray_squirrel,count_cinnomon_squirrel,count_black_squirrel]
}

output = pandas.DataFrame(data_dict)
print(output)
#create new csv file
# data.to_csv("new_data.csv")
