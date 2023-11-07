deposit_Sum = int(input())
period = int(input())
annual_interest_rate = float(input()) / 100

# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
total_sum = deposit_Sum + period * (( deposit_Sum * annual_interest_rate) / 12 )
print(total_sum)