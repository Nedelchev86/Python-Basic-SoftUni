# 1. Първи ред – брой на хората. Цяло число в интервала [1…100]
# 2. Втори ред – такса вход. Реално число в интервала [0.00…50.00]
# 3. Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
# 4. Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00]
import math

people = int(input())
tax = float(input())
price_for_lounge = float(input())
price_for_sunshade = float(input())

tax_for_all = tax * people
all_for_lounge =  price_for_lounge * (math.ceil( 0.75 * people))
all_for_sunshade = math.ceil(people / 2)  * price_for_sunshade

total = tax_for_all + all_for_sunshade + all_for_lounge

print(F"{total:.2F} lv.")