chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50

total_chicken_menu = int(input())
total_fish_menu = int(input())
total_vegan_menu = int(input())

total= (chicken_menu * total_chicken_menu) + (fish_menu * total_fish_menu) + (vegan_menu * total_vegan_menu)
desert = total * 0.2

grand_total =total + delivery + desert
print(grand_total)