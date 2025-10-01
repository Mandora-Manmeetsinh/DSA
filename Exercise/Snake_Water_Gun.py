import random

print(" ========== Welcome to Snake Water Gun Game ========== ")
print("-1 :- Snake , 0 : Water , 1 : Gun")

Computer_turn  = random.randrange(-1,1)
user_choice = int(input("Enter your choice :- "))
print("The computer's choice :- " , Computer_turn)

if Computer_turn == user_choice :
    print("Tie")
elif Computer_turn == -1 and user_choice == 1 :
    print("User Wins")
elif Computer_turn == -1 and user_choice == 0 :
    print("Computer Wins")
elif Computer_turn == 0 and user_choice == -1 :
    print("User Wins")
elif Computer_turn == 0 and user_choice == 1 :
    print("Computer Wins")
elif Computer_turn == 1 and user_choice == -1 :
    print("Computer Wins")
elif Computer_turn == 1 and user_choice == 0 :
    print("User Wins")
else :
    print("Invalid Input")