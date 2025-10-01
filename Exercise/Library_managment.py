class Main_Library :
    def __init__(self, name, library_card_number, books):
        self.name = name
        self.library_card_number = library_card_number
        self.books = books

    def info(self):
        print(f"The name of Customer is {self.name}")
        print(f"The library card number of Customer is {self.library_card_number}")
        print(f"The number of books available in Library is {self.books}")

    def book_issue(self):
        print("Thank you for book purchase")
        self.books -= 1


Obj = Main_Library("Manmeet" , "A01" , 100)
Obj.info()
print()
Obj.book_issue()
print()
Obj.info()
