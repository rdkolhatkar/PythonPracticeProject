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

"""
===========================================================
Python Program: Taking List, Tuple, and Dictionary Input
===========================================================

In Python, input() always returns data as a STRING.
So we must convert that string into the required data type.

This file demonstrates:
1) How to take List input
2) How to take Tuple input
3) How to take Dictionary input
4) Safe method using ast.literal_eval()
"""

# ---------------------------------------------------------
# 1️⃣ TAKING LIST AS USER INPUT
# ---------------------------------------------------------

print("----- LIST INPUT EXAMPLE -----")

# User enters values separated by space
# Example input: 10 20 30 40
list_input = input("Enter numbers separated by space: ")

# split() converts string into list of substrings
# map(int, ...) converts each element to integer
# list() converts map object to list
my_list = list(map(int, list_input.split()))

print("List is:", my_list) # Output: List is: [10, 20, 30, 40]
print("Type of my_list:", type(my_list)) # Output: Type of my_list: <class 'list'>

print("\n")  


# ---------------------------------------------------------
# 2️⃣ TAKING TUPLE AS USER INPUT
# ---------------------------------------------------------

print("----- TUPLE INPUT EXAMPLE -----")

# User enters values separated by comma
# Example input: 1,2,3,4
tuple_input = input("Enter numbers separated by comma: ")

# split(",") splits based on comma
# map(int, ...) converts to integers
# tuple() converts to tuple
my_tuple = tuple(map(int, tuple_input.split(",")))

print("Tuple is:", my_tuple) # Output: Tuple is: (1, 2, 3, 4)
print("Type of my_tuple:", type(my_tuple)) # Output: Type of my_tuple: <class 'tuple'>

print("\n")


# ---------------------------------------------------------
# 3️⃣ TAKING DICTIONARY AS USER INPUT (Multiple entries)
# ---------------------------------------------------------

print("----- DICTIONARY INPUT EXAMPLE -----")

# Ask user how many key-value pairs
n = int(input("How many key-value pairs do you want to enter? "))

my_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value   # Assign key-value pair

print("Dictionary is:", my_dict) # Output: Dictionary is: {'key1': 'value1', 'key2': 'value2',
print("Type of my_dict:", type(my_dict)) # Output: Type of my_dict: <class 'dict'>

print("\n")


# ---------------------------------------------------------
# 4️⃣ SINGLE LINE DICTIONARY INPUT
# ---------------------------------------------------------

print("----- SINGLE LINE DICTIONARY INPUT -----")

# Example input:
# name:Ratnakar,age:25,city:Mumbai
dict_input = input("Enter key:value pairs separated by comma: ")

pairs = dict_input.split(",")   # Split by comma
single_line_dict = {}

for pair in pairs:
    key, value = pair.split(":")   # Split key and value
    single_line_dict[key] = value

print("Dictionary from single line:", single_line_dict) # Output: Dictionary from single line: {'name': 'Ratnakar', 'age': '25', 'city': 'Mumbai'}
print("Type of single_line_dict:", type(single_line_dict)) # Output: Type of single

print("\n")


# ---------------------------------------------------------
# 5️⃣ SAFE ADVANCED METHOD USING ast.literal_eval()
# ---------------------------------------------------------

"""
literal_eval() safely converts a string containing
Python literal structures into actual Python objects.

It is safer than eval().
"""

import ast

print("----- SAFE INPUT USING literal_eval() -----")

# Example inputs:
# [1,2,3]
# (10,20,30)
# {'a':1,'b':2}

user_data = input("Enter any Python literal (list/tuple/dict): ")

converted_data = ast.literal_eval(user_data)

print("Converted Data:", converted_data) # Output depends on user input, e.g., Converted Data: [1, 2, 3]    
print("Type:", type(converted_data))    # Output depends on user input, e.g., Type: <class 'list'>


# ---------------------------------------------------------
# IMPORTANT NOTES
# ---------------------------------------------------------

"""
1) input() always returns STRING.
2) We must convert it using:
      list()
      tuple()
      dict()
      map()
      split()
      ast.literal_eval()
3) Avoid using eval() because it executes arbitrary code.
4) literal_eval() is the safest professional method.
"""
