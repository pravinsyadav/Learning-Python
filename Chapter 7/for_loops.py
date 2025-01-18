#FOR LOOP ->

# range(n) ----> [0 to n-1]      
#ex. range(4) --> output: 0,1,2,3
#ex. range(1,4)  --> output: 1,2,3
#ex. range(1, n+1)   --> output: 1,2,3,4,n       .. ex. range(1,4+1) --> output: 1,2,3,4

for i in range(4):           # range(4) means 0-3   that means it will print "0,1,2,3"
    print(i)

# we can iterate tuple, list, string 

s = "pravin"
for i in s:
    print(i)


# we can also use for loop with else statement

l = (1,3,4,5)
for item in l:
    print(item)
else:
    print("done")          # this is printed when the loop exhaust!
