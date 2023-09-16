# In your Python projects folder, create a new file called functions_practice.py. Open your file in VSCode, and create the following functions:

# 1. A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
    print("Hello and welcome to this python class!")

# 2. A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(jelly, peanutbutter, bread):
    return [jelly, peanutbutter, bread]
            
# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")

# Test that your file works by running it in your terminal. Remember, you need to call your functions in order for them to run. Make sure that all three functions run (please print the output of pack()) before submitting the file.When your file is completed, follow your normal process to add, commit, and push the changes to your local directory up to your GitHub repository. Don't forget to also submit the assignment on Canvas!

hello()
print(pack("jelly", "peanutbutter", "bread"))
eat_lunch(["chips", "sandwich", "dessert"])
eat_lunch([])
eat_lunch(["sandwich"])