import  math
movie = input()
movie_time = int(input())
break_time = int(input())

time_for_luch = break_time / 8
pochivka = break_time / 4
total = time_for_luch + pochivka + movie_time

if total <= break_time:
    print(F"You have enough time to watch {movie} and left with {math.ceil(break_time - total)} minutes free time.")
else:
    print(F"You don't have enough time to watch {movie}, you need {math.ceil(total - break_time)} more minutes.")

