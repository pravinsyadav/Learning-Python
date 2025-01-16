# 'dectionary' in python is a collection of key-value pair..... dict are mutable, unordered and indexed

d = {}     # empty dictionary
marks = {
    "pravin": 98,
    "vivek" :95           # here we can see dict can store key-value pair
}


print(marks)
print(type(marks))            # class = dict
print(len(marks))

# print(marks[0])               # it does not work in dict it work in list,tuple,string
print(marks["pravin"])           # it will print corrspondig pair of pravin 


# METHODS OF DICT

print(marks.items())       # it gives key-value pair present in dict
print(marks.keys())        # it gives only keys present in dict
print(marks.values())      # it gives only values present in dict


# here both gives same output but there is slight difference in both
print(marks.get("pravin"))         # it checks key in dict if present then returs its value if key is not present then it returns none       
print(marks["pravin"])             # it checks key in dict if present then returs its value if key is not present then it returns key error