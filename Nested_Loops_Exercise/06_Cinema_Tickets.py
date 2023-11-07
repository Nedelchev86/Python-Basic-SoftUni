
total_students = 0
total_standart = 0
total_kids = 0
sold_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break
    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        type_of_Tickets = input()

        if type_of_Tickets == "End":
            break

        if type_of_Tickets == "student":
            total_students += 1
        elif type_of_Tickets == "standart":
            total_standart +=1
        else:
            total_kids += 1

        sold_tickets += 1

    print(F"{movie_name} - {sold_tickets / capacity * 100:.2F}% full.")
total_tickets = total_kids + total_students + total_standart
print(F"Total tickets: {total_tickets}")

