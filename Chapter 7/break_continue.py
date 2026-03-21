# BREAK ->  it instruct program to exit the loop


for i in range(25):
    if(i == 12):
        break            # it will break the loop and stop the iteration when the if condition become true
    print(i)           # this will print from 0 to 11




# CONTINUE ->   it instruct program to skip the particular iteration


for i in range(25):
    if(i == 12):
        continue         # it will skip 12th iteration
    print(i)        # this will print from 0 to 24 but it does not print 12 


for i in range(25):
    print(i,end=" ")       # end means don't go to next line ... print space instead 

# whenever we use end = " " then use one empty print() for moving to next line 

print()               # this will print empty line or it moves cursor to next line 
print(*range(25))            # this will print range from 0 to 24 