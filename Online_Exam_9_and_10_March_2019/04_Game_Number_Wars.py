
name_first = input()
name_second = input()
point_first = 0
point_second = 0
command = input()

while command != "End of game":
    card_first = int(command)
    card_second = int(input())
    if card_first > card_second:
        point_first += (card_first - card_second)
    elif card_second > card_first:
        point_second += (card_second - card_first)
    if card_first == card_second:
        card_first = int(input())
        card_second = int(input())
        if card_first > card_second:
            print("Number wars!")
            print(F"{name_first} is winner with {point_first} points")
            break
        else:
            print("Number wars!")
            print(F"{name_second} is winner with {point_second} points")
            break
    command = input()
else:
    print(F"{name_first} has {point_first} points")
    print(F"{name_second} has {point_second} points")
