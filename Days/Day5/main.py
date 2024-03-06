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

no_of_students = 0
for height in students_heights:
    no_of_students += 1

average = sum / no_of_students
print(f"The average height of the students is {average}")


# Code Challenge 2: Highest Score 
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"The highest score in the class is {high_score}")


# Code Challenge 3: Evens Calculator
total = 0
for number in range(2, 101, +2):
    total += number
print(total)


# Code Challenge 4: FizzBuzz
for number in range(1, 101):
# You could remove this first line and use else at the end
    if number % 3 != 0 and number % 5 != 0:
        print(number)
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")


    