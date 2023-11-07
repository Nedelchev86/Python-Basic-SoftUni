start = str(input())
end = str(input())

srart_1 = int(start[0])
srart_2 = int(start[1])
srart_3 = int(start[2])
srart_4 = int(start[3])
end_1 = int(end[0])
end_2 = int(end[1])
end_3 = int(end[2])
end_4 = int(end[3])


for num_1 in range(srart_1, end_1 +1):
    for num_2 in range(srart_2, end_2 +1):
        for num_3 in range(srart_3, end_3 +1):
            for num_4 in range(srart_4, end_4 +1):
                if num_1 % 2 !=0 and num_2 % 2 !=0 and num_3 % 2 !=0 and num_4 % 2 !=0:
                    print(F"{num_1}{num_2}{num_3}{num_4}", end=" ")
