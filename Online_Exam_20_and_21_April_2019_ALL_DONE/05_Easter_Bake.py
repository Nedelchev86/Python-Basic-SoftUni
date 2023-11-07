import math

total_flour = 0
total_sugar = 0
max_sugar = 0
max_flour = 0

cake = int(input())
for i in range(cake):
    spent_sugar = int(input())
    spent_flour = int(input())
    if spent_flour > max_flour:
        max_flour = spent_flour
    if spent_sugar > max_sugar:
        max_sugar = spent_sugar
    total_flour += spent_flour
    total_sugar += spent_sugar

print(F"Sugar: {math.ceil(total_sugar / 950)}")
print(F"Flour: {math.ceil(total_flour / 750)}")
print(F"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
