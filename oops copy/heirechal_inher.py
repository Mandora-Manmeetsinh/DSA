class person:
    country = "India"

    def takeBreak(self):
        print("I am here")

class emp(person):
    company = "Honda" 

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am a person so i am breathing also!")
        
class programmer(person):
    company = "Fiverr"

    def getSalary(self):
        print("No salary")

e = emp()
e.takeBreak()
print(e.company)
print(e.country)

pr = programmer()
pr.takeBreak()
print(pr.company)
print(pr.country)