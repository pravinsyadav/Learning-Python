st = "pravin is studying in ycce"


f = open("Learning-Python/Chapter 9/myFile.txt", "w")  
data = f.write(st)             #it will overwrite old data 
data = f.write("\nhello")     #it will add new line without overwriting old data 
f.close()