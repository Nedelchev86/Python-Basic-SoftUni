naylon = int(input()) + 2
paint = int(input())
dilvent = int(input())
hours = int(input())

nylon_price = 1.5
paint_price = 14.5
diluent_price = 5
bags = 0.4
paint = paint + paint * 0.1

total= (naylon * nylon_price) + (paint_price * paint) + (diluent_price * dilvent) + bags

work_per_hour = total * 0.3
all = total + (work_per_hour * hours)
print(all)

