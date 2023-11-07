tshirt = float(input())
shorts = tshirt * 0.75
socks = shorts * 0.20
shoes = 2 * (tshirt + shorts)

target = float(input())

total = (tshirt + shorts + socks + shoes) * 0.85

if total >= target:
    print(F"Yes, he will earn the world-cup replica ball!")
    print(F"His sum is {total:.2F} lv.")
else:
    print(F"No, he will not earn the world-cup replica ball.")
    print(F"He needs {target - total:.2F} lv. more.")