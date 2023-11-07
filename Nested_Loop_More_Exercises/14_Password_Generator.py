first_input = int(input())
second_input = int(input())

for a in range(1, first_input):
    for b in range(1, first_input):
        for c in range(97, (97 + second_input)):
            for d in range(97, (97 + second_input)):
                for e in range(1, first_input + 1):
                    if e > a and e > b:
                        print(F"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")
