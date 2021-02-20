# Calculate how long it will take to save for a
# down payment given the following assumptions:

# User inputs
annual_salary = int(input("Enter your annual salary: ")) # Annual salary
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) # Money saved each month (e.g. 0.10 = 10% of annual salary)
total_cost =  int(input("Enter the cost of your dream home: ")) # Cost of your dream home

# Given assumptions
portion_down_payment = 0.25 # Down payment (e.g. 0.25 = 25%)
current_savings = 0 # Current savings
r = 0.04 # 4% rate of return on the current savings

# Calculations
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved

months = 0
while current_savings < total_cost*portion_down_payment:
    current_savings += current_savings*r/12 + monthly_savings
    months += 1

print("Number of months:", months)

