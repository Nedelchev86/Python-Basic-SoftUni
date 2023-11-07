start = int(input())
end = int(input())
magic = int(input())
counter = 0
is_found = False

for first_digit in range(start, end + 1):
    if is_found:
        break
    for secont_digit in range(start, end +1):
        counter +=1
        if first_digit + secont_digit == magic:
            print(F"Combination N:{counter} ({first_digit} + {secont_digit} = {magic})")
            is_found = True
            break
if not is_found:
    print(F"{counter} combinations - neither equals {magic}")
