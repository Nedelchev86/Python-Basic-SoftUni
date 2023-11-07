first = input()
second = input()
third = input()
counter = 0

for i in range(ord(first), ord(second) + 1):
    for k in range(ord(first), ord(second) + 1):
        for j in range(ord(first), ord(second) + 1):
            if i != ord(third) and k != ord(third) and j != ord(third):
                counter += 1
                print(F"{chr(i)}{chr(k)}{chr(j)}", end=" ")
print(counter)
