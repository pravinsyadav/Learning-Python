#FUNCTION -> 'function' is group of statements performing a specific task


#Function Definition
def avg():                
    a = int(input("enter 1st no: "))        #This is a user-defined function that takes input from the user, 
    b = int(input("enter 2nd no: "))        #calculates the average of three numbers, and prints the result when the function is called
    c = int(input("enter 3rd no: "))

    average = (a + b + c)/3
    print(average)

#Function Call
avg()


# there are two types of functions in python
#         1. built in function
#                Ex. len(), print(), range()
#         2. user defined function
#                Ex. avg(), func()


