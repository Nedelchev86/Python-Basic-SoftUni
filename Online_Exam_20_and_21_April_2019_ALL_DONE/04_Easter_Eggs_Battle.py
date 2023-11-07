eggs_first = int(input())
eggs_second = int(input())

command = input()
while command != "End":
    if command =="one":
        eggs_second -=1
        if eggs_second == 0:
            print(F"Player two is out of eggs. Player one has {eggs_first} eggs left.")
            break
    else:
        eggs_first -=1
        if eggs_first == 0:
            print(F"Player one is out of eggs. Player two has {eggs_second} eggs left.")
            break
    command = input()
else:
    print(F"Player one has {eggs_first} eggs left.")
    print(F"Player two has {eggs_second} eggs left.")
