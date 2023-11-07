# 1. Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# 2. Вид на билета – текст - “Standard”, “Premium” или “VIP”
# 3. Брой билети – цяло число в интервала [1 … 30]
# 4. Снимка с трофея – символ – 'Y' (да) или 'N' (не)

tournir = input()
ticket_type = input()
tickets = int(input())
picture = input()

total = 0

if tournir == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    else:
        price = 118.90
elif tournir == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    else:
        price = 300.40
else:
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    else:
        price = 400


total = price * tickets

if total > 4000 and picture == "Y":
    total = total  * 0.75
elif total > 4000 and picture == "N":
    total = total * 0.75
elif total > 2500 and picture == "Y":
    total = total * 0.90 + ( tickets * 40)
elif total > 2500 and picture == "N":
    total = total * 0.90
elif total >0 and picture == "Y":
    total = total + (tickets * 40)

print(F"{total:.2F}")
