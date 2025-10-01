a = 10
b = 0

try :
    c = a / b 
    print(c)

except ZeroDivisionError as e :
    print("Error: Division by zero is not allowed")

except TypeError as t :
    print("Error: Invalid data type")

finally :
    print("Division operation is completed")
    print("Always Executed")