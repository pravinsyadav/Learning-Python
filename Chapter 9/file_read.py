
f = open("Learning-Python/Chapter 9/file.txt")             # here the file is by default on read mode if you want to write you need to add "w" in it
data = f.readlines()
print(data)
f.close()

