# От конзолата се прочитат 3 реда, въведени от потребителя:
# •	N1 - цяло число;
# •	N2 - цяло число;
# •	Оператор - един символ измежду: "+", "-", "*", "/", "%".

N1 = int(input())
N2 = int(input())
operation = input()
after_operation = 0

if operation == "+":
    if (N1 +N2) % 2 == 0:
        print(f"{N1} {operation} {N2} = {N1+N2} - even")
    else:
        print(f"{N1} {operation} {N2} = {N1 + N2} - odd")
elif operation == "-":
    if (N1 - N2) % 2 == 0:
        print(f"{N1} {operation} {N2} = {N1 - N2} - even")
    else:
        print(f"{N1} {operation} {N2} = {N1 - N2} - odd")
elif operation == "*":
    if (N1 * N2) % 2 == 0:
        print(f"{N1} {operation} {N2} = {N1 * N2} - even")
    else:
        print(f"{N1} {operation} {N2} = {N1 * N2} - odd")
elif operation == "/":
    if N2 == 0:
        print(F"Cannot divide {N1} by zero")
    else:
        print(F"{N1} / {N2} = {N1 / N2:.2F}")
elif operation == "%":
    if  N2 == 0:
        print(F"Cannot divide {N1} by zero")
    else:
      print(F"{N1} % {N2} = {N1 % N2}")

