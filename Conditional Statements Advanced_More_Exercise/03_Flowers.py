number_chrysanthemum = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday = input()
total_flowers_count = number_chrysanthemum + number_roses + number_tulips

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
else:
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if holiday == "Y":
    chrysanthemum_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15
if season == "Spring" and number_tulips > 7:
    chrysanthemum_price *= 0.95
    roses_price *= 0.95
    tulips_price *= 0.95
if season == "Winter" and number_roses >= 10:
    chrysanthemum_price *= 0.90
    roses_price *= 0.90
    tulips_price *= 0.90
if total_flowers_count > 20:
    chrysanthemum_price *= 0.80
    roses_price *= 0.80
    tulips_price *= 0.80
print(F"{(number_tulips * tulips_price) + (number_roses * roses_price) + (number_chrysanthemum * chrysanthemum_price) + 2:.2F}")