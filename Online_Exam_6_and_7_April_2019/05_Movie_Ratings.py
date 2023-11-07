
import sys

movies_number = int(input())
max_rataing = 0
best_movie = ""
worst_movie = ""
worst_rating =  sys.maxsize
total = 0

for i in range (movies_number):
    movie = input()
    rating = float(input())
    total += rating
    if rating > max_rataing:
        max_rataing = rating
        best_movie = movie
    elif rating < worst_rating:
        worst_rating = rating
        worst_movie = movie
print(F"{best_movie} is with highest rating: {max_rataing:.1F}")
print(F"{worst_movie} is with lowest rating: {worst_rating:.1F}")
print(F"Average rating: {total / movies_number:.1F}")