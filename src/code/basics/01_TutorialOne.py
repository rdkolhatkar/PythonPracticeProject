# This is a Python script that prints messages to the console.
# To run the "TutorialOne.py"file use command :  python src/code/basics/01_TutorialOne.py
print("Hello World!")
print("This is the main module of the code.")
print("How are you doing today?")
print(2)
# Variables and Data Types in Python
age  = 25  # Integer
name = "Alice"  # String
height = 5.5  # Float
is_student = True  # Boolean
list_of_numbers = [1, 2, 3, 4, 5]  # List
tuple_of_coordinates = (10.0, 20.0)  # Tuple
dictionary_of_person = {"name": "Alice", "age": 25, "height": 5.5}  # Dictionary
# ================================
# Difference between List, Tuple, and Dictionary in Python
# ================================

# 1) LIST
# - Ordered collection of items
# - Mutable (can be modified after creation)
# - Allows duplicate values
# - Defined using square brackets []

my_list = [10, 20, 30, 20]

# List is mutable
my_list.append(40)        # Adding element
my_list[0] = 100          # Modifying element

# --------------------------------

# 2) TUPLE
# - Ordered collection of items
# - Immutable (cannot be modified after creation)
# - Allows duplicate values
# - Defined using parentheses ()

my_tuple = (10, 20, 30, 20)

# Tuple is immutable
# my_tuple[0] = 100       # ❌ This will raise TypeError
# my_tuple.append(40)     # ❌ Tuples do not support append()

# --------------------------------

# 3) DICTIONARY
# - Unordered collection of key-value pairs (insertion order preserved in Python 3.7+)
# - Mutable
# - Keys must be unique
# - Defined using curly braces {key: value}

my_dict = {
    "name": "Ratnakar",
    "age": 25,
    "city": "Mumbai"
}

# Dictionary is mutable
my_dict["age"] = 26       # Modifying value
my_dict["country"] = "India"  # Adding new key-value pair

# --------------------------------

# Quick Summary:
# List       -> Ordered, Mutable, Allows duplicates         -> [ ]
# Tuple      -> Ordered, Immutable, Allows duplicates       -> ( )
# Dictionary -> Key-Value pairs, Mutable, Unique keys      -> { }

# Python is dynamically typed, so you don't need to declare data types explicitly.
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}") # Output: Name: Alice, Age: 25, Height: 5.5, Is Student: True
# Rules of defining variables in Python:
# 1. Variable names can contain letters, numbers, and underscores.
# 2. They cannot start with a number.
# 3. Variable names are case-sensitive.
# 4. Avoid using Python reserved keywords as variable names.
# 5. Use descriptive names for better readability.
# 6. Avoid using special characters or spaces and reserved keywords in variable names.
# Example of variable naming
user_name = "Bob"
user_age = 30
user_height = 6.0
is_active_user = False
# Printing the variables
print(f"User Name: {user_name}, User Age: {user_age}, User Height: {user_height}, Is Active User: {is_active_user}") # Output: User Name: Bob, User Age: 30, User Height: 6.0, Is Active User: False
# This script demonstrates basic variable usage and printing in Python.
# It also includes comments explaining the rules for defining variables.
# Identify the variable types and print their values.
# type() function is used to check the type of a variable.
print(type(age))  # <class 'int'>
print(type(name))  # <class 'str'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(list_of_numbers))  # <class 'list'>
print(type(tuple_of_coordinates))  # <class 'tuple'>
print(type(dictionary_of_person))  # <class 'dict'>
# The script ends here.
# You can add more functionality or examples as needed.