balance = 0

while True:
  user_input = input()
  if user_input == "NoMoreMoney":
    break
  money = float(user_input)
  if money < 0:
    print("Invalid operation!")
    break
  print(F"Increase: {money:.2F}")
  balance += money

print(F"Total: {balance:.2F} ")
