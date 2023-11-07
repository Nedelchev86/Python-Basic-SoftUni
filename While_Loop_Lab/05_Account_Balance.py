amount = input()
balance = 0
while amount != "NoMoreMoney":
  increase = float(amount)
  if increase < 0:
    print("Invalid operation!")
    break
  balance += increase
  print(F"Increase: {increase:.2F}")
  amount = input()
print(F"Total: {balance:.2F}")