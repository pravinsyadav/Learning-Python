# sets is collection of non-repeatitive elements.... sets are unorderd and unindexed and mutable

s = {1, 3,3,3,3, 4}    # this is set .... set cannot print repetitive elements
print(s)
print(len(s))

e = set()        # this is empty set ......if we declare e = {} then it is empty dict not empty set
print(type(e))


# METHODS OF SET

s.add(8)
print(s)
s.remove(3)
print(s)



# union and intersection of set

s1 = {1,2,3,4,5}
s2 = {2,3,4}

print(s1.union(s2))           # it will print all elements from s1 and s2 set without repetating values
print(s1.intersection(s2))         # it will print elements present in both s1 and s2 set