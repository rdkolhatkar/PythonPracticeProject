# To run the "TutorialEight.py" file use command: python src/code/basics/08_TutorialEight.py
# Loops in Python
# There are different types of loops in Python, such as "for" and "while" loops.

# For loop example
for i in range(1, 11):  # Looping from 1 to 10
    print(f"Number: {i}")   
    
# For loop for printig tabel of 5
print("\nTable of 5:") 
for i in range(1, 11):  # Looping from 1 to 10
    print(f"5 x {i} = {5 * i}") 
    
# For loop for writing the table of a user-defined number
number = int(input("\nEnter a number to print its table: "))
print(f"\nTable of {number}:")  
for i in range(1, 11):  # Looping from 1 to 10
    print(f"{number} x {i} = {number * i}")
    
# While loop example
count = 1
print("\nCounting from 1 to 5 using while loop:")   
while count <= 5:  # Loop until count is less than or equal to 5
    print(f"Count: {count}")
    count += 1  
    
i = 1
print("\nCounting from 1 to 5 using while loop:")   
while i < 11:  # Loop until count is less than or equal to 5
    print(f"Count: {i}")
    i = i + 1 
    
    