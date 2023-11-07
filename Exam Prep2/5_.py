# kids = 0
# adults = 0
# toys = 5
# sweater = 15
# command = input()
# while command != "Christmas":
#     years = int(command)
#     if years <= 16:
#         kids += 1
#     else:
#         adults += 1
#     command = input()
#
# print(F"Number of adults: {adults}")
# print(F"Number of kids: {kids}")
# print(F"Money for toys: {kids * toys}")
# print(F"Money for sweaters: {adults * sweater}")

command_nc = input()
price_for_toys_nc = 5
price_for_sweater_nc = 15

age_nc = 0
count_sixteen_nc = 0
more_than_count_nc = 0
money_for_toys_nc = 0
money_for_sweater = 0

while command_nc != "Christmas":
    age_nc = int(command_nc)

    if age_nc <= 16:
        count_sixteen_nc += 1
        money_for_toys_nc += price_for_toys_nc

    else:
        more_than_count_nc +=1
        money_for_sweater += price_for_sweater_nc

    command_nc = input()


print(f"Number of adults: {more_than_count_nc}")
print(f"Number of kids: {count_sixteen_nc}")
print(f"Money for toys: {money_for_toys_nc}")
print(f"Money for sweaters: {money_for_sweater}")