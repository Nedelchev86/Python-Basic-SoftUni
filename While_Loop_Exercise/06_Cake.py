cake_w = int(input())
cake_h =  int(input())
cake = cake_w * cake_h
total = 0
piece_size = input()
while piece_size != "STOP":
  piece = int(piece_size)
  cake = cake - piece
  total +=piece
  if cake <= 0:
    print(F"No more cake left! You need {abs(cake)} pieces more.")
    break
  piece_size = input()
else:
  print(F"{(cake_w * cake_h) - total} pieces are left.")