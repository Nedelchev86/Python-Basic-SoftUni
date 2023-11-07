# конзолата се четат 4 реда:
# Ред 1. Минути на контролата – цяло число в интервала [0…59]
# Ред 2. Секунди на контролата – цяло число в интервала [0…59]
# Ред 3. Дължината на улея в метри – реално число в интервала [0.00…50000]
# Ред 4. Секунди за изминаване на 100 метра – цяло число в интервала [0…1000

target_min = int(input())
target_sec = int(input())

distance = float(input())
seconds_for_100_m = int(input())
targer_in_sec = target_min * 60 + target_sec
slow_for_all = (distance / 120) * 2.5

marti_time = (distance / 100 ) * seconds_for_100_m - slow_for_all

if marti_time <= targer_in_sec:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marti_time:.3F}.")
else:
    print(F"No, Marin failed! He was {marti_time - targer_in_sec:.3F} second slower.")