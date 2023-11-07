n = input()
max = -2147483647

while n != "Stop":
    number = int(n)
    if number > max:
        max = number
    n = input()
print(max)


# bigger = int(input())
#
# while True:
#     user_input = input()
#     if user_input == "Stop":
#         break
#     num = int(user_input)
#     if num > bigger:
#         bigger = num
# print(bigger)