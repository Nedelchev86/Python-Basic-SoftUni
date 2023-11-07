
months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

for i in range(months):
    electricity = float(input())
    water = 20
    internet = 15
    other = (electricity + water + internet) * 1.2
    total_electricity += electricity
    total_water +=water
    total_internet += internet
    total_other += other

print(F"Electricity: {total_electricity:.2F} lv")
print(F"Water: {total_water:.2F} lv")
print(F"Internet: {total_internet:.2F} lv")
print(F"Other: {total_other:.2F} lv")
print(F"Average: {(total_other + total_electricity + total_internet + total_water)/months:.2F} lv")

