# day 19_100 days - tax loan

print("""
  *******************
  * LOAN CALCULATOR *
  *******************
""")

loan_value = 1000
apr = (5/100)

print(f"${loan_value} over 10 years at {apr}% APR")

for year_calc in range(10):
  loan_value += (loan_value * apr)
  print(f"Year {year_calc+1} is {round(loan_value,2)}")

print(f"You paid {round((loan_value-1000),2)} in interessstttt")