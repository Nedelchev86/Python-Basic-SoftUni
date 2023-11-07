pens_packages = int(input())
markers_packeges = int(input())
detergent = int(input())
discount = int(input()) / 100

pens_price = 5.8
markers_price = 7.20
detergent_price = 1.20

total = (pens_price * pens_packages) + (markers_price * markers_packeges) + (detergent_price * detergent)
total_after_discount = total - (total * discount)
print(total_after_discount)