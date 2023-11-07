target = int(input())
success_jump = 0
needed = target - 30
count = 0
unsuccess = 0
while target >= needed:
    for i in range(3):
        jump = int(input())
        count += 1
        if jump > needed:
            needed += 5
            success_jump = jump
            unsuccess = 0
            break
        else:
            unsuccess += 1
        if unsuccess == 3:
            print(F"Tihomir failed at {needed}cm after {count} jumps.")
            exit()
print(F"Tihomir succeeded, he jumped over {target}cm after {count} jumps.")
