
cake = 3.20
eggs = 4.35
cookies = 5.4
eggs_paint = 1.8

num_Cake = int(input())
num_Eggs = int(input())
num_cookies = int(input())

total_cake = cake * num_Cake
total_cookies = num_cookies * cookies
total_eggs = (num_Eggs * eggs) + num_Eggs * eggs_paint

print(F"{total_eggs +total_cookies + total_cake:.2F}")