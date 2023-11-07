budget = float(input())

graphic_card_count = int(input())
processors_count = int(input())
ram_count = int(input())

graphics_card_price = graphic_card_count * 250
processors_price = processors_count * (graphics_card_price * 0.35)
ram_price = ram_count * ( graphics_card_price * 0.1)

total_price = graphics_card_price + processors_price + ram_price

if graphic_card_count > processors_count:
    total_price *= 0.85
if total_price <= budget:
    print(F"You have {budget - total_price:.2F} leva left!")
else:
    print(F"Not enough money! You need {total_price - budget:.2F} leva more!")