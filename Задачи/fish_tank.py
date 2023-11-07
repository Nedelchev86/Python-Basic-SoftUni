# length = int(input())
# width = int(input())
# height = int(input())
# percent = float(input()) / 100
#
# capacity = ((length * width * height) / 1000)
# capacity_only_water = capacity - (capacity * percent)
#
# print(capacity_only_water)

length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

capacity = ((length * width * height) / 1000)
capacity -= capacity * percent

print(capacity)
