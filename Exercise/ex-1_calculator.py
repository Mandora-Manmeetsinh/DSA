num1 = int(input("Enter value of num1 :- "))
num2 = int(input("Enter value of num2 :- "))

print("Choose 1 : Adittion , 2 : Substraction , 3 : Multiplication , 4 : Division , 5 : Modulo")

choice = int(input("Enter your choice :- "))

if choice == 1 :
    print(num1 + num2)
elif choice == 2 :
    print(num1 - num2)
elif choice == 3 :
    print(num1 * num2)
elif choice == 4 :
    print(num1 / num2)
elif choice == 5 :
    print(num1 % num2)
else : 
    print("Invalid Choice")


# ====================================================================================================================================

# Type - 2 code

Exp = input("Enter The Expression :- ")
print(eval(Exp))                                    # Using eval function