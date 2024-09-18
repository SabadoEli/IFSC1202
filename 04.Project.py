start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print(f"Prime Numbers between {start} and {end}:")

full_list=[]
prime_list = []

for num in range(start, end +1):
    full_list.append(num)
    if 