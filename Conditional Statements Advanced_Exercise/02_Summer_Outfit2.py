degreese = int(input())
time_of_day = input()
outfit = None
shoes = None

if 10 <= degreese <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degreese <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
else:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"


print(F"It's {degreese} degrees, get your {outfit} and {shoes}.")
