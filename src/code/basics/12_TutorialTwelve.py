# To run the "TutorialTwelve.py" file use command :  python src/code/basics/12_TutorialTwelve.py
# Functions in python
# Write a function to calculate the Average of Three Numbers
# Functions are just like methods in Java, it is nothing but a block of reusable code
# To create any kind of function in Python we use 'def' keyword
# Below is function decleration 
def average(a, b, c):
    d = (a + b + c)/3
    print(d)
    
# Note: your function will not show any output if it is not called
# Calling the average() function and passing the arguments
average(5, 7, 33) # Output: 15.0
# In above function a = 5, b = 7 and c = 33
average(4, 2, 1) # Output: 2.3333333333333335
# Assigning the result of a function to a variable
o1 = average(4, 2, 1) # Here we cannot assign a function output to a variable because it will treat it as object.
print(o1) # Output: null
# If we have to assign the output of any function to a specific variable then we have to return some data from the function
def newAverage(a, b, c):
    d = (a + b + c)/3
    return d
o2 = newAverage(1, 2, 3)
print(o2) # Output: 2.0
# return is a reserved keyword in Python we cannot take it as a variable