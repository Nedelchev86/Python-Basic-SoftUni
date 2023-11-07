n = input()
min = 2147483647

while n != "Stop":
  number = int(n)
  if number < min:
    min = number
  n = input()
print(min)
