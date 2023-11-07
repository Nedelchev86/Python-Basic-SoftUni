# От конзолата се прочитат 3 реда, въведени от потребителя:
# •	N1 - цяло число;
# •	N2 - цяло число;
# •	Оператор - един символ измежду: "+", "-", "*", "/", "%".

N1 = int(input())
N2 = int(input())
operation = input()
after_operation = 0
result = None

if operation == "+":
    result = F"{N1} + {N2} = {N1 + N2}" + (" - even" if  (N1 + N2) % 2 == 0 else " - odd")

elif operation == "-":
    result = F"{N1} - {N2} = {N1 - N2}" + (" - even" if (N1 - N2) % 2 == 0 else " - odd")

elif operation == "*":
    result = F"{N1} * {N2} = {N1 * N2}" + (" - even" if (N1 * N2) % 2 == 0 else " - odd")
elif N2 == 0:
    result = F"Cannot divide {N1} by zero"
elif operation == "/":
        result = f"{N1} / {N2} = {N1 / N2:.2F}"
elif operation == "%":
        result= f"{N1} % {N2} = {N1 % N2:}"

print(result)
