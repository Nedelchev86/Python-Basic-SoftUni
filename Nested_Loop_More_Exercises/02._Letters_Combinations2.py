first = ord(input())
second = ord(input())
third = ord(input())
counter = 0

for i in range(first, second+ 1):
    for k in range(first, second+ 1):
        for j in range(first, second+ 1):
            if i != third and k != third and j != third:
                counter += 1
                print(F"{chr(i)}{chr(k)}{chr(j)}", end=" ")
print(counter)
