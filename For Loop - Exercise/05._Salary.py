# ⦁	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# ⦁	Заплата - число в интервала [500...1500]

open_tabs = int(input())
salary = int(input())

Facebook = 150
Instagram = 100
Reddit = 50
penalty = 0

for i in range (0, open_tabs):
    site = input()
    if site == "Facebook":
        penalty += Facebook
    elif site == "Instagram":
        penalty += Instagram
    elif site == "Reddit":
        penalty += Reddit
    if salary <= penalty:
        print("You have lost your salary.")
        break
if salary > penalty:
    print(int(salary - penalty))

