a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))
distance_AB = abs(a-b)
distance_AC = abs(a-c)
if distance_AB < distance_AC:
    print(distance_AB)
else:
    print(distance_AC)
