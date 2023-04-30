#getting the input from the user -> height of all students with spaces separating them
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
c = 0
for height in student_heights:
    sum+=height
    c+=1
avg = round(sum/c)
print(avg)


