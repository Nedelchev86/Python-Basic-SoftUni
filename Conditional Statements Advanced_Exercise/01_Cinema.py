# Напишете програма, която въвежда тип прожекция (стринг),
# брой редове и брой колони в залата (цели числа) и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат като в примерите по-долу - с 2 цифри след десетичния знак.
screening_type = input()
screening_type = screening_type.lower()
rows = int(input())
columbs = int(input())
price = 0
total_places = rows * columbs

if screening_type == "premiere":
    price = 12
elif screening_type == "normal":
    price = 7.5
else:
    price = 5
print(F"{total_places * price:.2F} leva")
