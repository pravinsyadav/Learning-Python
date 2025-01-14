name = "harry"           #this is string    and it is 'immutable'.....'immutable' means we cannot change existing string
b = 'pravin'             # we can declare string in single , double , triple quote
c = '''pravin'''


nameshort = name[0:3]       #start from index 0 all the way till 3 (excluding 3)   that means it will print (0,1,2)
print(nameshort)

print(name[-4:-1])        # this is neagative slicing 
print(name[1:4])         # here we converted negative number to its corresponding positive number



# SKIP VALUE

word = "0123456789"
print(word[1:7:2])       #here skip value works first it reserve 1 to 6 then print 1,3,5 that means 
                             #start character then whatever the the number is given it exlude that amount of character and print selected character

#steps for skip value
print(word[1:7])    # it gives 1,2,3,4,5,6 then we have 2 so it starts from 1 then it exlude 1,2 and print 3 similarly it exludes 3,4 and print 5
