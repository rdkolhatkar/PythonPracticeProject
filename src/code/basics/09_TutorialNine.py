# To run this "TutorialNine.py" file use command: python src/code/basics/09_TutorialNine.py
# Break and Continue statements in Python
# This script demonstrates the use of break and continue statements in Python.
for i in range(0,10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("Current value of i is:", i)
    
# Now using continue statement
for j in range(0,10):
    if j == 5:          
        print("Skipping the value 5")
        continue
        print("This line will be skipped when j is 5") # continue skips the rest of the loop for this iteration
    print("Current value of j is:", j)

# Pass statement in Python
# The pass statement is a null operation; it does nothing when executed.
# It is used when a statement is required syntactically but you do not want any command or code to execute. 
for k in range(0, 5):
    if k == 2:
        print("Pass statement encountered at k =", k)
        pass # This will do nothing, just a placeholder
    print("Current value of k is:", k)
# The pass statement allows you to write empty loops or functions.
# It can be useful as a placeholder for future code.
# The script ends here.
