siza_a, siza_b, siza_c = int(input()), int(input()), int(input())

total_space = siza_a * siza_b * siza_c
total = 0
while total_space > total:
  command = input()
  if command == "Done":
    print(F"{total_space - total} Cubic meters left.")
    break
  total += int(command)
else:
  print(F"No more free space! You need {total - total_space} Cubic meters more.")