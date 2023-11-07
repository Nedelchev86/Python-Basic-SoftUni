# Входът се чете от конзолата и се състои от два реда:
#  Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
#  Втори ред – уред - текст ("ribbon", "hoop" или "rope"

country = input()
gear = input()

difficulty = 0
performance = 0

if country == "Russia":
    if gear == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif gear == "hoop":
        difficulty = 9.300
        performance = 9.800
    else:
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if gear == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif gear == "hoop":
        difficulty = 9.550
        performance = 9.750
    else:
        difficulty = 9.500
        performance = 9.400
else:
    if gear == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif gear == "hoop":
        difficulty = 9.450
        performance = 9.350
    else:
        difficulty = 9.700
        performance = 9.150
total = difficulty + performance

print(F"The team of {country} get {total:.3F} on {gear}.")
print(F"{(100 - (total / 20 *100)):.2F}%")