# replace word donkey with ###### in a particular file

# here we see fistly we need to read the file and then write in a file
# when there is no need of modify, replace condition in a previous file the we directly write in a file without using read

word = "donkey"

with open("Learning-Python/Chapter 9/ps.txt", "r") as f:
    content = f.read()

#we can write above code without 'with' also but we need to close that code or file 
#with 'with' python automatically closes file 

# f = open("Learning-Python/Chapter 9/ps.txt", "r")
# content = f.read()
# f.close()

contentnew = content.replace(word, "######")

with open("Learning-Python/Chapter 9/ps.txt", "w") as f:
    f.write(contentnew)