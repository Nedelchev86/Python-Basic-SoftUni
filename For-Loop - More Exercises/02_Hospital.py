period = int(input())
pacient = 0
been_reviewed = 0
not_been_reviewed = 0
total_pacient = 0
doctors = 7

for i in range(1, period +1):
    pacient = int(input())
    if i % 3 == 0 and not_been_reviewed > been_reviewed:
        doctors += 1
    if pacient > doctors:
        been_reviewed += doctors
        not_been_reviewed += pacient - doctors
    else:
        been_reviewed += pacient
print(F"Treated patients: {been_reviewed}.")
print(F"Untreated patients: {not_been_reviewed}.")
