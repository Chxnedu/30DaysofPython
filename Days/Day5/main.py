# Python Loops

# Code Challenge: Average Height Calculator
# Get the heights and turn them to a list with the split function
students_heights = input("Input a list of student heights ").split()
# the range in line 7 will generate a list of 0, 1, 2, 3, so the n variable 
# will take those values
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)
sum = 0
for height in students_heights:
    sum += height
print(sum)

no_of_students = 0
for height in students_heights:
    no_of_students += 1
print(no_of_students)

average = sum / no_of_students
print(f"The average height of the students is {average}")