size = int(input())
counter = 0
for i in range (1, size +1):
    for j in range(1, i+1):
        counter += 1

        print(F"{counter}", end=" ") if i !=j else print(F"{counter}")
        if counter == size:
            raise SystemExit