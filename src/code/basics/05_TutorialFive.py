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
# // -> Floor Division (Quotient)ø
a = 10
b = 3
print("Arithmetic Operators:") # Output: Arithmetic Operators:
print("Addition:", a + b) # Output: Addition: 13
print("Subtraction:", a - b)# Output: Subtraction: 7
print("Multiplication:", a * b) # Output: Multiplication: 30
print("Division:", a / b)# Output: Division: 3.3333333333333335
print("Modulus:", a % b)# Output: Modulus: 1
print("Exponentiation:", a ** b)# Output: Exponentiation: 1000
print("Floor Division:", a // b)# Output: Floor Division: 3
# Example of Arithmetic Operators
a = 34
b = 2 
# Arithmetic Operator 
print("a + b = ", a + b) # Output: a + b =  36
print("a - b = ", a - b) # Output: a - b =  32
print("a * b = ", a * b) # Output: a * b =  68
print("a / b = ", a / b) # Output: a / b =  17.0
print("a % b = ", a % b) # Output: a % b =  0
print("a // b = ", a // b) # Output: a // b =  17
print("a ** b = ", a ** b) # Output: a ** b =  1156
 
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
print("\nAssignment Operators:") # Output: Assignment Operators:
a = 10
print("Initial value of a:", a) # Output: Initial value of a: 10
a += 5
print("After += 5, a =", a) # Output: After += 5, a = 15
a -= 3
print("After -= 3, a =", a) # Output: After -= 3, a = 12
a *= 2
print("After *= 2, a =", a) # Output: After *= 2, a = 24
a /= 4
print("After /= 4, a =", a) # Output: After /= 4, a = 6.0
a %= 3
print("After %= 3, a =", a) # Output: After %= 3, a = 0.0
a **= 2
print("After **= 2, a =", a) # Output: After **= 2, a = 0.0
a //= 3
print("After //= 3, a =", a) # Output: After //= 3, a = 0.0
# Example of Assignment Operators
a = 32
print(a) # Output: 32
a*=3
print(a) # Output: 96
    
# Comparison Operators
# Comparison operators are used to compare two values and return a boolean result (True or False)
# == -> Equal to        
# != -> Not equal to
# > -> Greater than
# < -> Less than
# >= -> Greater than or equal to
# <= -> Less than or equal to
print("\nComparison Operators:") # Output: Comparison Operators:
# Example of Comparison Operators
x = 5   
y = 10
print("x == y:", x == y) # Output: x == y: False
print("x != y:", x != y) # Output: x != y: True
print("x > y:", x > y) # Output: x > y: False
print("x < y:", x < y) # Output: x < y: True
print("x >= y:", x >= y) # Output: x >= y: False
print("x <= y:", x <= y) # Output: x <= y: True
# Conditional Operators 
a = 34
b = 2
print(a>4) # Output: True
print(a<4) # Output: False
print(a<=4) # Output: False
print(a>=4) # Output: True
print(a==4) # Is a equal to 4? Output: False
print(a==34) # Is a equal to 34? Output: True
print(a!=34) # Is a not equal to 34?

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
print("a or b:", a or b) # Returns True
print("not a:", not a)  # Returns False
# Example of Logical Operators
c = True 
d = False

print(True and True) # Output: True
print(True and False) # Output: False
print(False and True) # Output: False
print(False and False) # Output: False

print("For Or Operator...") # Output: For Or Operator...
print(True or True) # Output: True
print(True or False) # Output: True 
print(False or True) # Output: True
print(False or False) # Output: False

print("Not Operator") # Output: Not Operator
print(not(True) ) # Output: False
print(not(False) ) # Output: True

# Identity Operators
# Identity operators are used to compare the memory locations of two objects
# is -> Returns True if both variables point to the same object     
# is not -> Returns True if both variables do not point to the same object
print("\nIdentity Operators:") # Output: Identity Operators:
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y) # Output: x is y: True, as both x and y point to the same object
print("x is not y:", x is not y) # Output: x is not y: False, as both x and y point to the same object
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
    print(number) # Output: 1 2 3 4 5, as the generator yields numbers from 1 to 5
# This prints numbers from 1 to 5 using a generator function
# The "del" operator is used to delete variables or objects
# It can be used to remove items from a list, delete a variable, or delete an entire object 
print("\nDel Operator:")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list) # Output: Original list: [1, 2, 3, 4, 5]
del my_list[2]  # Deletes the item at index 2
print("List after deletion:", my_list) # Output: List after deletion: [1, 2, 4, 5]
del my_list  # Deletes the entire list    
# The "pass" operator is used as a placeholder for future code
# It does nothing and is used when a statement is required syntactically but no action is needed
print("\nPass Operator:")
def my_function():
    pass  # This function does nothing
print("Function defined with pass operator:", my_function) # Output: Function defined with pass operator: <function my_function at 0x...>
# This script demonstrates various types of operators in Python, including arithmetic, assignment, comparison, logical, identity, membership, bitwise, and special operators. Each operator is explained with examples to illustrate its usage and output. You can experiment with these operators further to understand their behavior in different scenarios.    