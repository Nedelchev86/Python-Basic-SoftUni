widht, lenght = int(input()), int(input())

total_pices = widht * lenght
pices_eaten = 0

while total_pices >= pices_eaten:
  pieces = input()

  if pieces == "STOP":
    print(F"{total_pices - pices_eaten} pieces are left.")
    break
  else:
    pices_eaten += int(pieces)
else:
  print(F"No more cake left! You need {pices_eaten - total_pices} pieces more.")