# От конзолата се четат 3 реда:
# 1. Време за снимки – цяло число в диапазона [0… 1440]
# 2. Брой сцени – цяло число в диапазона [5… 25]
# 3. Времетраене на сцена – цяло число в диапазона [20… 90

time_for_pic = int(input()) *  0.85
scene = int(input())
time_for_scene = int(input())

time_needed = (time_for_scene * scene)

if time_for_pic > time_needed:
    print(F"You managed to finish the movie on time! You have {time_for_pic - time_needed:.0F} minutes left!")
else:
    print(F"Time is up! To complete the movie you need {time_needed - time_for_pic:.0F} minutes.")