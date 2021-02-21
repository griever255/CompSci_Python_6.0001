## Calculate how long it will take to save for a
# down payment given the following assumptions:

## User input
annual_salary = int(input("Enter your annual salary: ")) # Annual salary

## Given assumptions
total_cost =  1000000 # Cost of your dream home
semi_annual_raise = 0.07 # Raise every 6 months (e.g 0.03 = 3%)
portion_down_payment = 0.25 # Down payment (e.g. 0.25 = 25%)
r = 0.04 # 4% rate of return on the current savings
current_savings = 0

## Bisection Search
epsilon = 100 # Within $100 of required down payment
low = 0
high = 10000
portion_saved = (high+low)/2.0
numSteps = 0
notPossible = False
while abs(current_savings - total_cost*portion_down_payment) >= epsilon:
    current_savings = 0
    monthly_salary = annual_salary/12
    monthly_savings = monthly_salary*portion_saved/10000
    for month in range(36):
        if month % 6 == 0 and month != 0:
            monthly_salary *= 1+semi_annual_raise
            monthly_savings = monthly_salary*portion_saved/10000
        current_savings += current_savings*r/12 + monthly_savings
    if current_savings > total_cost*portion_down_payment:
        high = portion_saved
    else:
        low = portion_saved
    portion_saved = int(high+low)/2.0
    if portion_saved == 9999:
        notPossible = True
        break
    numSteps += 1

if notPossible:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved/10000)
    print("Steps in bisection search:", numSteps)

