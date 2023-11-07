
days = int(input())
foood = float(input())

eaten_by_dog = 0
eaten_by_cat = 0
biscuit = 0

for i in range (1, days +1):
    dog_eat = int(input())
    cat_eat = int(input())
    if i % 3 == 0:
        biscuit += (dog_eat + cat_eat) * 0.1
    eaten_by_dog += dog_eat
    eaten_by_cat += cat_eat

print(F"Total eaten biscuits: {round(biscuit)}gr.")
print(F"{(eaten_by_cat + eaten_by_dog) / foood * 100:.2F}% of the food has been eaten.")
print(F"{eaten_by_dog / (eaten_by_cat + eaten_by_dog) * 100:.2F}% eaten from the dog.")
print(F"{eaten_by_cat / (eaten_by_cat + eaten_by_dog) * 100:.2F}% eaten from the cat.")

