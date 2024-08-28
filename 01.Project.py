input_days = int(input("Enter Number of Days: "))

days_per_year = 365
days_per_week = 7

years = input_days // days_per_year
remaining_days_after = input_days - (years * days_per_week)
weeks = remaining_days_after // days_per_week
remaining_days = remaining_days_after - (weeks * days_per_week)

print("Years: ", years)
print("Weeks: ", weeks)
print("Days: ", remaining_days)