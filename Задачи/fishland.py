
mackerel_price = float(input())
sprat_price = float(input())
bonito_amount = float(input())
safrid_amount = float(input())
mussels_amount = float(input())

bonito_price = mackerel_price + (mackerel_price * 0.6)
safrid_price = sprat_price + (sprat_price * 0.8)
mussels_price = 7.5

total = (bonito_price * bonito_amount) + (safrid_price * safrid_amount) + (mussels_price * mussels_amount)
print(f"{total:.2F}")
