num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Second Number: "))

if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num2 == num3 or num3 == num1:
    print(0)