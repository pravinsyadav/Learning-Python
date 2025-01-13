x = 'pravin'
x = "pravin"    #this both are same 
y = 5
print(x)
print(y)
print(type(x))      #this print type of variable
print(type(y))

a = 4
A = "Sally"        #Remember that variable names are case-sensitive

x, y, z = "Orange", "Banana", "Cherry"        #this is used to assign muliple values to multiple variables
print(x)
print(y)
print(z)


#  Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# Global variable
x = 10
def print_global():
    print(x)  # Accessing global variable inside a function

print_global()  # Output: 10

