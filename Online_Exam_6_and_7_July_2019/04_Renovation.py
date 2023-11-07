wall_height = int(input())
wall_length = int(input())
windows_doors = int(input())
tired = True

total_for_paint = ((wall_length * wall_height) * 4) - (((wall_length * wall_height) * 4) * windows_doors / 100)

command = input()
while command != "Tired!":
    painted = int(command)
    total_for_paint -= painted
    if total_for_paint < 0:
        print(F"All walls are painted and you have {abs(total_for_paint):.0f} l paint left!")
        tired = False
        break
    elif total_for_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        tired = False
        break
    command = input()
if tired:
    print(F"{total_for_paint:.0f} quadratic m left.")