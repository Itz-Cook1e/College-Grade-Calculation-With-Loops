# Assignment:
# Prompt the user to enter an integer between 3 and 20. This will be the number of grades we will average.
# Use a while loop to make sure the input is good. I.e., if I enter a letter, float, or integer outside that range, ask me to try again until I enter a good number. Hint: initialize a sentinel value before the loop, and a try and except block inside the loop.)
# Use a for loop and the randint function to get the number of integers requested. Print out each one, and it's letter grade. Your letter grade function from the last assignment shouldn't have to be modified here.
# Average them. (Hint: You haven't been taught how to create an unknown number of variables, so I don't expect you to create grade1, grade2, etc. Just get a new grade each time through the loop, print it, and add it to a running total. When the loop is done, you should have a total of all of the grades, and simply divide that by the number of grades to get an average.)
# Print the average and its letter grade.
# Don't forget to put your name and date comment, as well as any other comments that will explain what you do!
# Was instructed to re-do as I did not include a function. One has now been added.

# Importing libraries
import random

# Start loop
while True:
    # Get user input
    gradeamount = input('Please enter an integer between 3 and 20: ')

    # Make sure input is an integer
    if gradeamount.isnumeric():
        gradeamount = int(gradeamount)
    else:
        print("Please enter an integer.")
        continue

    # Make sure input is within number range ()
    if 3 <= gradeamount <= 20:
        break
    else:
        print("Make sure the integer is between 3 and 20!")
        print(f'{gradeamount} is not between 3 and 20!')

# Create empty list (to fill and pull from later)
grades = []

# Generate and print grades
for i in range(gradeamount):

    grade = random.randint(50, 100)

    # Fill list (empty list above)
    grades.append(grade)

    if grade >= 90:
        givengrade = 'A'
    elif 89 > grade >= 80:
        givengrade = 'B'
    elif 79 > grade >= 70:
        givengrade = 'C'
    elif 69 > grade >= 60:
        givengrade = 'D'
    else:
        givengrade = 'F'
    print(f'Grade: {grade} {givengrade}')

# Calculate average grade(s)
avg_grades = sum(grades) / gradeamount


def average_grade_letter(grade):
    if avg_grades >= 90:
        return 'A'
    elif 89 > avg_grades >= 80:
        return 'B'
    elif 79 > avg_grades >= 70:
        return 'C'
    elif 69 > avg_grades >= 60:
        return 'D'
    else:
        return 'F'


print()
print(f'Average Grade: {avg_grades} {average_grade_letter(avg_grades)}')
# Comment with name, date, and assignment name redacted
