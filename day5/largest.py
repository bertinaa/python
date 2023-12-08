# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
largest = 0
for i in range(1,len(student_scores)):
  if student_scores[i]>student_scores[largest]:
    largest = i
print(f"The highest score in the class is: {student_scores[largest]}")
