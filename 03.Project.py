x = float(input("Enter First Number: "))
y = (input("Enter Operator(+,-,*,/): "))
z = float(input("Enter Second Number: "))

if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/':
    print(x/z)
else:
    print("Invalid Operator")

