# find greatest number using function

def find(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("enter no 1: "))
b = int(input("enter no 2: "))
c = int(input("enter no 3: "))

print("largest no is: ", find(a, b ,c))