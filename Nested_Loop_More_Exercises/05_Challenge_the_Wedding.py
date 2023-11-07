men = int(input())
woman = int(input())
table = int(input())
counter = 0
for i in range(1, men +1):
    for j in range(1, woman +1):
        counter += 1
        if counter > table:
            exit()
        print(F"({i} <-> {j})", end =" ")
