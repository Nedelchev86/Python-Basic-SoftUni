
studenets = int(input())
bad = 0
good = 0
very_good = 0
top = 0
sum_grades = 0

for i in range(1, studenets +1):
    grades = float(input())
    sum_grades += grades
    if grades <= 2.99:
        bad += 1
    elif grades <= 3.99:
        good += 1
    elif grades <= 4.99:
        very_good += 1
    else:
        top +=1
total_students = bad + good + very_good + top

print(F"Top students: {top / total_students * 100:.2F}%")
print(F"Between 4.00 and 4.99: {very_good / total_students * 100:.2F}%")
print(F"Between 3.00 and 3.99: {good / total_students * 100:.2F}%")
print(F"Fail: {bad / total_students * 100:.2F}%")
print(F"Average: {sum_grades / studenets:.2F} ")

