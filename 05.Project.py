start_of_ran = int(input("Enter Start of Range: "))
end_of_ran = int(input("Enter End of Range: "))

def special_number(num):
    original_num = num
    num_digits = 0
    while original_num > 0:
        original_num //= 10
        num_digits +=1
        
    sum_of_powers = 0
    original_num = num
    while original_num > 0:
        digit = original_num % 10
        sum_of_powers += digit ** num_digits
        original_num //= 10
        
    return sum_of_powers == num

def find_special_numbers(start,end):
    special_numbers=[]
    for num in range(start,end + 1):
        if special_number(num) :
            special_numbers.append(num)
    return special_numbers
    
special_numbers = find_special_numbers (start_of_ran, end_of_ran)
print(f"Special Numbers between {start_of_ran} and {end_of_ran}:")
for number in special_numbers:
        print(number)
    