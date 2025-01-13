a = "33.3"       # this is str
print(type(a))

b = float(a)       # here we converted str to float 
print(type(b))


x = int(float(a))        # we cannot directly convert to interger fist convert to float and then to int 
print(type(x))