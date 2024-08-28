hundreds = (number // 100)
tens = (number // 10)
ones = (number % 10)
if hundreds < tens < ones:
    print("Yes")
else:
    print("No")