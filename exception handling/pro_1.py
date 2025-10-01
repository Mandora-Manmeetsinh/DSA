# 1st type :-
# Try to find the squere root of given number but nagative number is not supported using exception handling using sqrt function .

import math

try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number is not supported")
    else:
        print("Square root of the number is: ", math.sqrt(num))
except ValueError as e:
    print("Error: ", str(e))

finally :
    print("Program ended")

# 2nd type :- 
# Try to find the squere root of given number but nagative number is not supported using exception handling .

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number is not supported")
    else:
        print("Square root of the number is: ", num ** 0.5)

except ValueError as e:
    print("Error: ", str(e))

finally :
    print("Program is completed") 


# print(0.1 + 0.2 == 0.3)