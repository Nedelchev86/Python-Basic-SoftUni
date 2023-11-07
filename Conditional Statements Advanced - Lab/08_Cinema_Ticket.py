# day = input()
#
# if day == "Monday":
#     print("12")
# elif day == "Tuesday":
#     print("12")
# elif day == "Wednesday":
#     print("14")
# elif day == "Thursday":
#     print("14")
# elif day == "Friday":
#     print("12")
# elif day == "Saturday":
#     print("16")
# elif day == "Sunday":
#     print("16")

day = input()
if day == "Monday" or day == "Tuesday" or day == "Friday":
    print("12")
elif day == "Wednesday" or day == "Thursday":
    print("14")
else:
    print("16")
