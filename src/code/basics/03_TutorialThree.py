# Taking the user input in the Python Script
# This script demonstrates how to take user input in Python.
# To run the "TutorialThree.py" file use command: python src/code/basics/03_TutorialThree.py
# input() function is used to take input from the user.
a = input("Enter any number and then press Enter key to exit the program: ") # The input() function takes input from the user and returns it as a string.
print("The value of variable 'a' is: ", a) # Output: The value of variable 'a' is: <user_input>
print("The type of variable 'a' is: ", type(a)) # Output: The type of variable 'a' is: <class 'str'>
b = input("Enter Your Name: ") # The input() function takes input from the user and returns it as a string.
print("The Value of variable 'b' is: ", b) # Output: The Value of variable 'b' is: <user_input>
print("The type of variable 'b' is: ", type(b)) # Output: The type of variable 'b' is: <class 'str'>
# Write a program to take two numbers as input from the user and print their sum.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")  
# Since input() returns a string, we need to convert it to an integer for addition.
sum_result = int(num1) + int(num2)
print(f"The sum of {num1} and {num2} is: {sum_result}") # Alternatively, we can convert the inputs to integers before performing the addition.
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
addition_result = num3 + num4
print(f"The addition of {num3} and {num4} is: {addition_result}") # Output: The addition of <num3> and <num4> is: <addition_result>