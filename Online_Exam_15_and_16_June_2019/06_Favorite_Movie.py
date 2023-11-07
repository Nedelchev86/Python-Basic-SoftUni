
count = 0
best_score = 0
best_movie = ""

while True:
    movie_name = input()
    count += 1
    ascii = 0
    if movie_name == "STOP":
        break
    if count == 7:
        print("The limit is reached.")
        break
    for i in movie_name:
        if ord(i) in range(ord("A"), ord("Z") + 1):
            ascii += ord(i) - len(movie_name)
        elif ord(i) in range(ord("a"), ord("z") + 1):
            ascii += ord(i) - ( 2 *len(movie_name))
        else:
            ascii += ord(i)
    if ascii > best_score:
        best_score = ascii
        best_movie = movie_name
print(F"The best movie for you is {best_movie} with {best_score} ASCII sum.")


