# Calculate how long it will take to save for a
# down payment given the following assumptions:

# User inputs
annual_salary = int(input("Enter your annual salary: ")) # Annual salary
total_cost =  1000000 # Cost of your dream home
semi_annual_raise = 0.07 # Raise every 6 months (e.g 0.03 = 3%)

# Given assumptions
portion_down_payment = 0.25 # Down payment (e.g. 0.25 = 25%)
current_savings = 0 # Current savings
r = 0.04 # 4% rate of return on the current savings

# Calculations
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved


for i in range(36) current_savings < total_cost*portion_down_payment:
    current_savings += current_savings*r/12 + monthly_savings
    if months % 6 == 0 and months != 0:
        monthly_salary *= 1+semi_annual_raise
        monthly_savings = monthly_salary*portion_saved
    months += 1

print("Number of months:", months)

