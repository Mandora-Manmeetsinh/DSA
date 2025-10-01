class emp:
    company = "Google"

    def showdetail(self):
        print("yes")

class programmer(emp):
    lang = "Python"

    def getname(self):
        print(f"The lang is {self.lang}")

    e = emp()
    e.showdetail()

    # p = programmer()
    # p.showdetail()