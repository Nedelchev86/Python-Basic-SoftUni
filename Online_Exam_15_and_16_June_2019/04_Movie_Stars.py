# От конзолата първо се чете един ред:
# • Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
# След това се четат многократно по един или два реда до команда "ACTION" или до изчерпване на бюджета:
# • Име на актьор - текст
# Ако името на актьора съдържа по-малко или равно на 15 брой символи:
# o Възнаграждение - реално число в интервала [250.0… 1 000 000.0

budget = float(input())
money = 0

while budget > money:
    actior = input()
    if actior == "ACTION":
        print(F"We are left with {budget -money:.2F} leva.")
        break
    if len(actior) <= 15:
        money_for_actioer = float(input())
    else:
        money_for_actioer = (budget - money) * 0.20
    money += money_for_actioer
else:
    print(F"We need {money - budget:.2F} leva for our actors.")