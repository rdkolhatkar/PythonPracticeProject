# To run the "TutorialSix.py" file use command: python src/code/basics/06_TutorialSix.py
# This is a Python script that demonstrates the use of conditionals.
print("Welcome to the Conditional Statements Tutorial!")
# Conditional statements allow you to execute code based on certain conditions.
# Let's define a variable to check its value.
age = 20
# Using an if statement to check the age
if( age >= 18):
    print("You are an adult.")
else:
    print("You are a minor.")
print("This is the end of the conditional statements program.")

age = int(input("Please enter your age: "))
# Using if-elif-else to handle multiple conditions
if(age > 18):
    print("You are eligible for driving.")
elif(age == 18):
    print("You become eligible for driving today!")
elif(age < 18 and age >= 16):
    print("You can apply for a learner's permit.")
else:
    print("You are not eligible for driving yet.")
print("Thank you for using the Conditional Statements Tutorial!")
# This script demonstrates basic conditional statements in Python.
# It includes comments explaining the use of if, elif, and else statements.