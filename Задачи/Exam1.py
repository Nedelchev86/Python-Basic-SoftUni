# tax = float(input())
#
# cake = tax - (tax * 0.8)
# drinks = cake - ( cake * 0.45)
# animator = tax / 3
# print(tax + cake + drinks + animator)

# tax = float(input())
# cake = tax / 5
# drinks = cake - (cake * 0.45)
# animator = tax / 3
# print(tax + cake + drinks + animator)

bitcoin = 1168
yoan = 0.15
usd1 = 1.76
euro = 1.95

bitcoin_num = int(input())
yoan_num = float(input())
commision = float(input())

bitcoin_sum = bitcoin * bitcoin_num
yoan_sum = yoan * yoan_num
yoan_in_leva = yoan_sum * usd1

total =((bitcoin_sum) + (yoan_in_leva)) / euro
commision2 = ( total * commision) / 100
grad_total = total - commision2
print (F"{grad_total:.2F}")