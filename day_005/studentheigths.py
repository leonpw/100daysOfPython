
student_heights = input("Input a list of student heigths.\n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
print(student_heights)

########
#  get average height of student
# without using len() or sum()
########

total_height = 0
stud_count = 0

for student in student_heights:
    total_height += student
    stud_count += 1
    
print(f"The average height of the students is: {round(total_height / stud_count,0)}")
