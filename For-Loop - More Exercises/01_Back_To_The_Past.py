
money = float(input())
years = int(input())
year_cost = 12000

ivan_years = 18 - 1
total_cost = 0

for i in range(1800, years +1):
    ivan_years += 1
    if i % 2 == 0:
        total_cost += year_cost
    else:
        total_cost += year_cost + ( 50 * ivan_years)
if money >= total_cost:
    print(F"Yes! He will live a carefree life and will have {money-total_cost:.2F} dollars left.")
else:
    print(F"He will need {total_cost-money:.2F} dollars to survive.")

