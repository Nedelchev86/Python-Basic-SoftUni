#     • Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
#     • Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23",
# "24-27" или "28-31"
#     • Трети ред - брой нощувки - цяло число в интервала [1… 100]

destination = input()
date = input()
nights = int(input())
price = 0

if destination == "France":
    if date == "21-23":
        price = 30
    elif date == "24-27":
        price = 35
    else:
        price = 40
elif destination == "Italy":
    if date == "21-23":
        price = 28
    elif date == "24-27":
        price = 32
    else:
        price = 39
else:
    if date == "21-23":
        price =  32
    elif date == "24-27":
        price = 37
    else:
        price = 43
print(F"Easter trip to {destination} : {price * nights:.2F} leva.")
