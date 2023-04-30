# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
name1 = name1+name2
count = 0
count1 = 0
#my solution
# for i in name1:
#     if i=='t':
#         count+=1
#     if i=='r':
#         count+=1
#     if i=='u':
#         count+=1
#     if i=='e':
#         count+=1
# count = str(count)
# for i in name1:
#     if i=='l':
#         count1+=1
#     if i=='o':
#         count1+=1
#     if i=='v':
#         count1+=1
#     if i=='e':
#         count1+=1
# count1 = str(count1)

#another solution 
t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
count = str(t+r+u+e)
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")
count1=str(l+o+v+e)
score = count + count1
score = int(score) 
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
