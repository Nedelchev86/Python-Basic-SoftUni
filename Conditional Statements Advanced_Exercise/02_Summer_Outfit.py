degreese = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= degreese <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degreese <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degreese >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= degreese <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degreese <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degreese >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(F"It's {degreese} degrees, get your {outfit} and {shoes}.")
