# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
import math
vineyard = int(input())
grape_for_1= float(input())
need_for_wine = int(input())
workers = int(input())

land_for_grape = vineyard * 0.4
grape_for_wine = land_for_grape * grape_for_1
wine = grape_for_wine / 2.5
not_enought= abs(math.floor(need_for_wine - wine))
not_enought2= abs(math.ceil(need_for_wine - wine))
for_worker= math.ceil(not_enought/workers)
if need_for_wine > wine:
    print(F"It will be a tough winter! More {not_enought:.0F} liters wine needed.")
else:
    print(F"Good harvest this year! Total wine: {wine:.0f} liters.")
    print("%1f" % math.ceil(not_enought2), "liters left ->", math.ceil(for_worker), "liters per person.")
 #   print(F"{not_enought2:.0F} liters left -> {for_worker:.0F} liters per person.")

# На конзолата трябва да се отпечата следното:
# •	Ако произведеното вино е по-малко от нужното:
# o	“It will be a tough winter! More {недостигащо вино} liters wine needed.”
# 	Резултатът трябва да е закръглен към по-ниско цяло число
# •	Ако произведеното вино е колкото или повече от нужното:
# o	“Good harvest this year! Total wine: {общо вино} liters.”
# 	Резултатът трябва да е закръглен към по-ниско цяло число
# o	“{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# 	И двата резултата трябва да са закръглени към по-високото цяло число



# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.