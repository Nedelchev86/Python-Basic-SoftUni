count_junior = int(input())
count_senior = int(input())
trace_type = input()
price_junior = 0
price_senior = 0

if trace_type == "trail":
  price_junior = 5.50
  price_senior = 7
elif trace_type == "cross-country":
  if (count_junior + count_senior) >= 50:
    price_junior = 8 * 0.75
    price_senior = 9.50 * 0.75
  elif  (count_junior + count_senior) < 50:
    price_junior = 8
    price_senior = 9.50
elif trace_type == "downhill":
  price_junior = 12.25
  price_senior = 13.75
elif trace_type == "road":
  price_junior = 20
  price_senior = 21.50

total = ((price_junior * count_junior) + (count_senior * price_senior)) * 0.95
print(F"{total:.2F}")
