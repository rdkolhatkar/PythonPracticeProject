# Typecasting in Python
# This script demonstrates typecasting in Python.
# To run the "TutorialTwo.py" file use command: python src/code/basics/02_TutorialTwo.py

a = 34
print("The value of variable a is:", a) # Output: The value of variable a is: 34
print("The type of a is:", type(a)) # Output: The type of a is: <class 'int'>
b = "34"
print("The value of b is:", b) # Output: The value of b is: 34
print("The type of b is:", type(b)) # Output: The type of b is: <class 'str'>
# Typecasting from string to integer
c = int(b)
print("The value of c is:", c) # Output: The value of c is: 34
print("The type of c is:", type(c)) # Output: The type of c is: <class 'int'>
d = 23
e = str(d) # Typecasting from integer to string
print("The value of d is ", d) # Output: The value of d is 23
print("The type of variable d is ", type(d)) # Output: The type of variable d is <class 'int'>
print("The value of e is ", e)# Output: The value of e is 23
print("The type of variable e is ", type(e))# Output: The type of variable e is <class 'str'>
# Typecasting from integer to float
f = float(d)
print("The value of f is ", f) # Output: The value of f is 23.0
print("The type of variable f is ", type(f)) # Output: The type of variable f is <class 'float'>
# Typecasting from float to integer
g = int(f)
print("The value of g is ", g) # Output: The value of g is 23
print("The type of variable g is ", type(g)) # Output: The type of variable g is <class 'int'>  
# Typecasting from string to float
h = float(b)        
print("The value of h is ", h) # Output: The value of h is 34.0
print("The type of variable h is ", type(h)) # Output: The type of variable h is <class 'float'>
# Typecasting from float to string
i = str(f)
print("The value of i is ", i) # Output: The value of i is 23.0
print("The type of variable i is ", type(i)) # Output: The type of variable i is <class 'str'>
# This script demonstrates various typecasting operations in Python.
# You can add more examples of typecasting as needed.
