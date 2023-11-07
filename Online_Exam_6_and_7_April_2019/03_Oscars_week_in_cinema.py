# Входът се чете от конзолата и се състои от три реда:
# Първи ред – име на филм – текст ("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite")
# Втори ред– вид на залата – текст ("normal", "luxury" или "ultra luxury")
# Трети ред – брой на закупените билети – цяло число в интервала [1…100]

movie = input()
hall = input()
tickets = int(input())
price = 0

if movie == "A Star Is Born":
    if hall == "normal":
        price = 7.50
    elif hall == "luxury":
        price = 10.50
    else:
        price = 13.50
elif movie == "Bohemian Rhapsody":
    if hall == "normal":
        price = 7.35
    elif hall == "luxury":
        price = 9.45
    else:
        price = 12.75
elif movie == "Green Book":
    if hall == "normal":
        price = 8.15
    elif hall == "luxury":
        price = 10.25
    else:
        price =  13.25
else:
    if hall == "normal":
        price = 8.75
    elif hall == "luxury":
        price = 11.55
    else:
        price = 13.95
print(F"{movie} -> {tickets * price:.2F} lv.")