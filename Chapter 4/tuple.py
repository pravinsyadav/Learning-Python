a = (1,2,3,4,5)             # this is tuple ..... and this is immutable
print(type(a))

a = ()         # this is empty tuple
print(type(a))             # class <tuple>

a = (1)         # this is not tuple it will return int as a type 
print(type(a))           # class <int>

a = (1,)            # this will represent tuple
print(type(a))          # class <tuple>



# METHODS OF TUPLE

a = (33, 4 ,4 , 49, 495,29)
no = a.count(4)           # .count will count the no present in tuple 
print(no)

i = a.index(49)          # it will return the index of that number
print(i)

print(len(a))