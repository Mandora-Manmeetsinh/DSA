class person:
    country = "India"

    def takeBreak(self):
        print("I am here")

class emp(person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("I am a person so i am breathing also!")

class programmer(emp):
    company = "Fiverr"

    def grtSalary(self):
        print("No salary")

    def takeBreak(self):
        super().takeBreak()
        print("I am here and i am sitting")

P = person()
P.takeBreak()

e = emp()
e.takeBreak()

pr = programmer()
pr.takeBreak()
