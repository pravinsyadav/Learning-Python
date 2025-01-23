class employee:
    company = "ITC"
    salary = 10000
    def show(self):
       print(f"The name of the employee is {self.company} and the salary is {self.salary}")


class coder:
    language = "python"
    def printlanguage(self):
        print(f"the language is {self.language}")



class programmer(employee, coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")
    

a = employee()
b = programmer()



# a.company will print ITC and b.company will print ITC Infotech 
print(a.company, b.company)
b.show()
b.printlanguage()