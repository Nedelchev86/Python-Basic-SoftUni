# От конзолата се чете:
#  На първи ред - Началното количество яйца в магазина - цяло число в интервала [1… 10000]
#  След това поредица от два реда (до получаване на команда "Close" или при заявка за
# купуване на повече от наличните в магазина яйца) :
# o Команда за купуване или допълване на яйца в магазина – текст ("Buy" или "Fill")
# o Брой на яйца, които да бъдат купени или допълнени в магазина – цяло число в интервала
# [1… 1000]

eggs_in_shop = int(input())
sell_eggs = 0

while eggs_in_shop >= 0:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(F"{sell_eggs} eggs sold.")
        break
    number = int(input())
    if command == "Buy":
        eggs_in_shop -= number
        if eggs_in_shop < 0:
            print(F"Not enough eggs in store!")
            print(F"You can buy only {eggs_in_shop + number}.")
            break
        sell_eggs += number

    else:
        eggs_in_shop += number

else:
    print(F"Not enough eggs in store!")
    print(F"You can buy only {eggs_in_shop}.")
