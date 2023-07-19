with open("file1.txt") as file1:
    data1 = file1.readlines()
    first = []
    first = [int(data.strip()) for data in data1]
    # for data in data1:
    #     new_data = data.strip()
    #     first.append(int(new_data))

with open("file2.txt") as file2:
    data2 = file2.readlines()
    second = []
    second = [int(data.strip()) for data in data2]
    # for data in data2:
    #     new_data = data.strip()
    #     second.append(int(new_data))

result = []
for data in first:
    if data in second:
        result.append(data)

print(result)



