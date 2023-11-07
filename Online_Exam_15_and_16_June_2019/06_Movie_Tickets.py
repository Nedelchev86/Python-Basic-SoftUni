
a1 = int(input())
a2 = int(input())
n = int(input())

for first in range(a1, a2):
    for secont in range(1, n):
        for third in range(1, int(n/2)):
            fourth = first
            sum = secont + third + fourth
            if first % 2 != 0 and sum % 2 != 0:
                print(f"{chr(first)}-{secont}{third}{fourth}")