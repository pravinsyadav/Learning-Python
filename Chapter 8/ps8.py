# find greatest number using function

def find(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = 11
b = 2
c = 3

print(find(a, b ,c))