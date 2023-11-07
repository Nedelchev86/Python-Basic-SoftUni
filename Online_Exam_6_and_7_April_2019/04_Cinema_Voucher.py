# Стойността на ваучера – цяло число в интервала [1…100000]
# След това до получаване на команда "End" или до изчерпването на ваучера, се чете по един ред:
# Покупката, която Любо е избрал – текст

vaucher = int(input())
buy = input()
price = 0
ticket = 0
other = 0

while buy != "End":
    if len(buy) > 8:
        price = ord(buy[0]) + ord(buy[1])
        vaucher -= price
        if vaucher <0:
            break
        ticket +=1
    else:
        price = ord((buy[0]))
        vaucher -= price
        if vaucher <0:
            break
        other +=1
    buy = input()

print(ticket)
print(other)
