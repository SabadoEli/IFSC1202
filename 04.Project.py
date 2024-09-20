first_number = int(input("Enter Start of Range: "))
second_number = int(input("Enter End of Range: "))

start = min(first_number, second_number)
end = max(first_number, second_number)

primes = []

for num in range(start, end +1):
    if num < 2: 
        continue
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break 
        
    if is_prime:
            if num not in primes:
                primes.append(num)
    
print(f"Prime Numbers between {first_number} and {second_number}: {primes}")
