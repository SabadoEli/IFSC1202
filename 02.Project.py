import math

side_1 = float(input("Enter Side 1: "))
side_2 = float(input("Enter Side 2: "))
side_3 = float(input("Enter Side 3: "))
s = (side_1 + side_2 + side_3) / 2
area = (math.sqrt(s*(s-side_1)*(s-side_2)*(s-side_3)))
print(area)