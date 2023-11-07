
time = int(input())
scane_number = int(input())
time_one_scane = int(input())

preparation = 0.15 * time
total_scane = scane_number * time_one_scane

if time >= total_scane + preparation:
    print(F"You managed to finish the movie on time! You have {round(time -(total_scane + preparation))} minutes left!")
else:
    print(F"Time is up! To complete the movie you need {round((total_scane + preparation) - time)} minutes.")