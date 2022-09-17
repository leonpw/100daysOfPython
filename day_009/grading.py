student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇

student_grades = {}    

for student in student_scores:
    score = student_scores[student]
    if score > 82:
        student_grades[student] = 'Outstanding'
    elif score > 79:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 76:
        student_grades[student] = 'Acceptable'
    elif score > 65:
        student_grades[student] = 'Acceptable'
    else :
        student_grades[student] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)


# '{'Harry': 'Exceeds Expectations', 
# 'Ron': 'Acceptable', 
# 'Hermione': 'Outstanding', 
# 'Draco': 'Acceptable', 
# 'Neville': 'Fail'}'