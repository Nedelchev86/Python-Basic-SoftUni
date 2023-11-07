best_player = None
best_Score = -1

while best_Score < 10:
    player_name = input()
    if player_name == "END":
        break

    player_Score = int(input())

    if player_Score > best_Score:
        best_player = player_name
        best_Score = player_Score

print(F"{best_player} is the best player!")
print(F"He has scored {best_Score} goals {'and made a hat-trick !!!' if best_Score >= 3 else '.'}")