h = float(input()) * 100
w = float(input()) * 100
w_without_coridor = w - 100
desk_w = w_without_coridor // 70
desk_h = h // 120
total_desk = int(desk_h * desk_w - 3)
print(total_desk)