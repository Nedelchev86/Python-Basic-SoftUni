# От конзолата се четат 4 реда:
# Име на сериал - текст
# Брой сезони – цяло число в диапазона [1… 10]
# Брой епизоди  – цяло число в диапазона [10… 80]
# Времетраене на обикновен епизод без рекламите – реално число в диапазона [40.0… 65.0]
# Изход

name = input()
season = int(input())
episodes = int(input())
time_for_episode = float(input()) * 1.20

needed_time = (episodes * time_for_episode * season) + (season *10)
print(F"Total time needed to watch the {name} series is {needed_time:.0F} minutes.")


