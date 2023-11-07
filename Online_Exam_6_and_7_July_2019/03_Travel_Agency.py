# От конзолата се четат 4 реда:
# 1. Име на града - текст с възможности ("Bansko", "Borovets", "Varna" или "Burgas")
# 2. Вид на пакета - текст с възможности ("noEquipment", "withEquipment", "noBreakfast" или
# "withBreakfast")
# 3. Притежание на VIP отстъпка - текст с възможности "yes" или "no"
# 4. Дни за престой - цяло число в интервала [1 … 10000]

destination = input()
type = input()
vip_card = input()
days = int(input())

price = 0


if days > 7:
    days -= 1

if not destination in ("Bansko", "Borovets", "Varna", "Burgas") or type not in ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast"):
    print(f'Invalid input!')
elif days <= 0:
    print("Days must be positive number!")
else:
    if vip_card == "no":
        if destination == "Bansko" or destination == "Borovets":
            if type == "noEquipment":
                price = 80
            else:
                price = 100
        elif destination == "Varna" or destination == "Burgas":
            if type == "noBreakfast":
                price = 100
            else:
                price = 130

    else:
        if destination == "Bansko" or destination == "Borovets":
            if type == "noEquipment":
                price = 80 * 0.95
            else:
                price = 100 * 0.90
        elif destination == "Varna" or destination == "Burgas":
            if type == "noBreakfast":
                price = 100 * 0.93
            else:
                price = 130 * 0.88

    total = price * days

    print(F"The price is {total:.2F}lv! Have a nice time!")


