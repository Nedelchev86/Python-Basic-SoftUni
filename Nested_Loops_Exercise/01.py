num = int(input())
counter = 0

for i in range(1, num + 1):
    for j in range(1, i +1 ):
        counter += 1
        print(F"{counter}", end =" ")
        if counter == num:
            exit()
    print()