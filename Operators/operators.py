num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
choice = input("Enter Choice : Add-1, Sub-2, Mul-3, Div-4")
if choice == '1':
    print("Addition is:", num1 + num2)
elif choice == '2':
    print("Substraction is:", num1 - num2)
elif choice == '3':
    print("Multiplication is:", num1 * num2)
elif choice == '4':
    print("Division is:", num1 / num2)
else :
    print("Invalid Choice....!!")