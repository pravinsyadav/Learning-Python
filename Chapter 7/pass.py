# PASS -> pass is the null statement in python ... it instruct to do nothing

for i in range(6):
    pass           # here if we were not used pass then it could be thorow error


for i in range(10):
    print(i,end=" ")
    i += 1

print()

for i in range(10):
    print(i,end=" ")

#In both codes, the output is the same because the for loop takes values from range() and assigns them to i in each iteration. 
#Even if we write i += 1, it doesn’t affect the loop, because Python overwrites i with the next value from range().
# So both codes behave the same.