days = int(input())
days_win = 0
days_loose = 0
money = 0
days_money = 0

for i in range(days):
    game_Win = 0
    game_loose = 0
    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            money += 20
            game_Win += 1
        else:
            game_loose += 1
    if game_Win > game_loose:
        money = money * 1.1
        days_win += 1
    else:
        days_loose += 1
    days_money += money
    money = 0
if days_win > days_loose:
    days_money = days_money * 1.2
    print(F"You won the tournament! Total raised money: {days_money:.2F}")
else:
    print(F"You lost the tournament! Total raised money: {days_money:.2F}")
