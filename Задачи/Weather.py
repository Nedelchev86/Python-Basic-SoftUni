# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold

num = float(input())

if num >= 26 and num <= 35.00:
    print("Hot")
elif num >= 20.1 and num <= 25.9:
    print("Warm")
elif num >= 15 and num <= 20:
    print("Mild")
elif num >= 12 and num <= 14.9:
    print("Cool")
elif num >= 5 and num <= 11.9:
    print("Cold")
else:
    print("unknown")
