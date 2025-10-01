class Employee :
    name = "Manmeet"

    def __len__(self) :
        i = 0
        for item in self.name :
            i = i + 1
        return i

    

E1 = Employee()
# print(E1.name)
# print(len(E1))