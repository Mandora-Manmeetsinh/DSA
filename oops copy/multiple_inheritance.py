class emp:
    company = "Visa"

class freelancer :
    company1 = "Fiverr"
    level = 2

    def upgrade(self):
        self.level += self.level
        
class user(emp , freelancer):
    name = "Manmeet"

U = user()
print(U.company)
print(U.company1)
U.upgrade()
print(U.level) 