# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_students_height = 0
no_of_students = 0
for student_height in student_heights:
  total_students_height += student_height
  no_of_students += 1

average = round(total_students_height / no_of_students)

print(f"total height = {total_students_height}")
print(f"number of students = {no_of_students}")
print(f"average height = {average}")