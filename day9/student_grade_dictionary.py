student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = student_scores
for name,score in student_grades.items(): #note
    if score <=70:
        student_grades[name] = "Fail" #to access value, we need to use key!
    elif score <=80:
        student_grades[name] = "Acceptable"
    elif score <= 90:
        student_grades[name] = "Exceeds Expectations"
    else:
        student_grades[name] = "Outstanding"


# 🚨 Don't change the code below 👇
print(student_grades)
