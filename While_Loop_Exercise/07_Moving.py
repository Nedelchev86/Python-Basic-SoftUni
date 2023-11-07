siza_a = int(input())
siza_b =  int(input())
siza_c = int(input())
total_space = siza_a * siza_b * siza_c
total = 0
space = input()
while space != "Done":
  more = int(space)
  total_space = total_space - more
  total +=more
  if total_space <= 0:
    print(F"No more free space! You need {abs(total_space)} Cubic meters more.")
    break
  space = input()
if space == "Done":
  print(F"{(siza_a * siza_b * siza_c) - total} Cubic meters left.")