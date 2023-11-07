day_off = int(input())

working_day = 365 - day_off
must_play = 30000
play_witt_tom = (working_day * 63) + (day_off * 127)
difference= abs(play_witt_tom - must_play)

hours= difference // 60
minute = difference % 60

if play_witt_tom > must_play:
    print("Tom will run away")
    print(F"{hours} hours and {minute} minutes more for play")
else:
    print("Tom sleeps well")
    print(F"{hours} hours and {minute} minutes less for play")

