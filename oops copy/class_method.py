class emp:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self , sel):
    #     self.__class__salary = sel

    def changeSalary(cls , sal):
        cls.salary = sal

e = emp()
print(e.salary)
e.changeSalary(456)
print(e.salary)
print(e.salary)

