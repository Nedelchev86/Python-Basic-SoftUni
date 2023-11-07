height = float(input())
length = float(input())
height_roof = float(input())

front_back_wall = height * height
door = 1.2 * 2
side_wall = height * length
windows = 1.5 * 1.5

total_green_paint_fron = ((2 * front_back_wall) - door)
total_green_paint_side = ((2 *side_wall) - (2 * windows))
total_green =(total_green_paint_side + total_green_paint_fron) / 3.4

front_roof = (height * height_roof) / 2
side_roof = length * height
total_roof = (2 * front_roof) + (2 * side_roof)
total_red_paint = total_roof / 4.3

print(f"{total_green:.2f}")
print(f"{total_red_paint:.2f}")

