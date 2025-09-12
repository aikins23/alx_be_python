monthly_income = float(input("Enter your monthly income: "))
total_monthly = float(input("Enter your total monthly income: "))
monthly_savings = monthly_income - total_monthly
Projected_Savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Your monthly savings are: ${monthly_savings}" )
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}" )
