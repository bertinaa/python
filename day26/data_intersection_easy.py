with open("file1.txt") as file1:
    data1 = file1.readlines()

with open("file2.txt") as file2:
    data2 = file2.readlines()

result = [int(num) for num in data1 if num in data2]

print(result)



