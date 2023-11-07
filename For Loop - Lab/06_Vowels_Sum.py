#   буква	a	e	i	o	u
# стойност	1	2	3	4	5
a = 1
e = 2
i = 3
o = 4
u = 5
word = input()
sum = 0

for letter in word:
    if letter == "a":
        sum += a
    elif letter == "e":
        sum += e
    elif letter == "i":
        sum += i
    elif letter == "o":
        sum += o
    elif letter == "u":
        sum += u

print(sum)