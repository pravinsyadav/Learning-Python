# PRINT TABLE OF ANY NUMBER

n = int(input("enter the number: "))

for i in range(1, 11):
    # print(i * n)
    print(f"{i} * {n} = {n*i}")        # here we used f string
    i += 1


# VERY IMP ->
     # we know python by default print new line when using print function 
     # to avoid new line we use (end = "") in print statement in one line
     # example->  print(i, end = "")

