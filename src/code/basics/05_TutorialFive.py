# To run the "TutorialFive.py" file use command: python src/code/basics/05_TutorialFive.py
# Operators in Python
# Operators are used to perform operations on variables and values
# Python has various types of operators: 
# Arithmetic Operators, Assignment Operators, Comparison Operators, Logical Operators, Identity Operators, Membership Operators, Bitwise Operators, and Special Operators
# Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.
# + -> Addition
# - -> Subtraction
# * -> Multiplication
# / -> Division
# % -> Modulus (Remainder)
# ** -> Exponentiation (Power)
# // -> Floor Division (Quotient)
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
# Assignment Operators
# Assignment operators are used to assign values to variables
# = -> Assigns the value on the right to the variable on the left
# += -> Adds the right operand to the left operand and assigns the result to the left operand
# -= -> Subtracts the right operand from the left operand and assigns the result to the left operand
# *= -> Multiplies the left operand by the right operand and assigns the result to the left operand
# /= -> Divides the left operand by the right operand and assigns the result to the left operand
# %= -> Takes the modulus of the left operand by the right operand and assigns the result to the left operand
# **= -> Raises the left operand to the power of the right operand and assigns the result to the left operand
# //= -> Performs floor division on the left operand by the right operand and assigns the result to the left operand
print("\nAssignment Operators:")
a = 10
print("Initial value of a:", a)
a += 5
print("After += 5, a =", a)
a -= 3
print("After -= 3, a =", a)
a *= 2
print("After *= 2, a =", a)
a /= 4
print("After /= 4, a =", a)
a %= 3
print("After %= 3, a =", a)
a **= 2
print("After **= 2, a =", a)
a //= 3
print("After //= 3, a =", a)    
# Comparison Operators
# Comparison operators are used to compare two values and return a boolean result (True or False)
# == -> Equal to        
# != -> Not equal to
# > -> Greater than
# < -> Less than
# >= -> Greater than or equal to
# <= -> Less than or equal to
print("\nComparison Operators:")
x = 5   
y = 10
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
# Logical Operators
# Logical operators are used to combine conditional statements
# and return a boolean result (True or False)
# and -> Returns True if both statements are true
# or -> Returns True if at least one statement is true
# not -> Reverses the result, returns True if the result is false
print("\nLogical Operators:")
a = True
b = False
print("a and b:", a and b)  # Returns False
print("a or b:", a or b)
print("not a:", not a)  # Returns False
# Identity Operators
# Identity operators are used to compare the memory locations of two objects
# is -> Returns True if both variables point to the same object     
# is not -> Returns True if both variables do not point to the same object
print("\nIdentity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)
print("x is z:", x is z)  # Returns False, as x and z are different objects
print("x is not z:", x is not z)  # Returns True, as x and z are different objects
# Membership Operators
# Membership operators are used to test if a value is present in a sequence (like a list, tuple, or string)
# in -> Returns True if the value is found in the sequence
# not in -> Returns True if the value is not found in the sequence
print("\nMembership Operators:")
my_list = [1, 2, 3, 4, 5]
print("2 in my_list:", 2 in my_list)  # Returns True
print("6 not in my_list:", 6 not in my_list)  # Returns True
# Bitwise Operators
# Bitwise operators are used to perform operations on binary representations of integers
# & -> Bitwise AND
# | -> Bitwise OR
# ^ -> Bitwise XOR (Exclusive OR)
# ~ -> Bitwise NOT
# << -> Bitwise left shift
# >> -> Bitwise right shift
print("\nBitwise Operators:")
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print("a & b:", a & b)  # Returns 1 (Binary: 0001)
print("a | b:", a | b)  # Returns 7 (Binary: 0111)
print("a ^ b:", a ^ b)  # Returns 6 (Binary: 0110)
print("~a:", ~a)  # Returns -6 (Binary: 1010 in two's complement)
print("a << 1:", a << 1)  # Returns 10 (Binary: 1010)
print("a >> 1:", a >> 1)  # Returns 2 (Binary: 0010)
# Special Operators 
# Special operators are used for specific purposes in Python
# The "is" operator is used to check if two variables point to the same object
# The "is not" operator is used to check if two variables do not point to the same object
print("\nSpecial Operators:")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)  # Returns True, as both point to the same object
print("a is c:", a is c)  # Returns False, as they are different objects
print("a is not c:", a is not c)  # Returns True, as they are different objects
# The "in" operator is used to check if a value is present in a sequence
# The "not in" operator is used to check if a value is not present in a sequence
my_string = "Hello, World!"
print("\nMembership Operators:")
print("'Hello' in my_string:", 'Hello' in my_string)  # Returns True
print("'Python' not in my_string:", 'Python' not in my_string)  # Returns True      
# The "lambda" operator is used to create anonymous functions
# It is a small, unnamed function that can take any number of arguments but can only have one expression
print("\nLambda Operator:")
square = lambda x: x ** 2  # Creates a lambda function to square a number
print("Square of 5:", square(5))  # Returns 25
# The "yield" operator is used in generator functions to yield a value and pause the function's execution   
def count_up_to(n):
    count = 1   
    while count <= n:
        yield count
        count += 1

print("\nYield Operator:")
for number in count_up_to(5):
    print(number)
# This prints numbers from 1 to 5 using a generator function
# The "del" operator is used to delete variables or objects
# It can be used to remove items from a list, delete a variable, or delete an entire object 
print("\nDel Operator:")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
del my_list[2]  # Deletes the item at index 2
print("List after deletion:", my_list)      
# The "pass" operator is used as a placeholder for future code
# It does nothing and is used when a statement is required syntactically but no action is needed
print("\nPass Operator:")
def my_function():
    pass  # This function does nothing
print("Function defined with pass operator:", my_function)      