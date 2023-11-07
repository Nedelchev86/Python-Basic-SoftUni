# •	Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# •	Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# •	Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# •	Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]

capacity =int(input())
debit_p1 =int(input())
debit_p2 =int(input())
time =float(input())

pipe1 = debit_p1 * time
pipe2 = debit_p2 * time
water_in_pool=  pipe1 + pipe2
percent_water = (water_in_pool / capacity) * 100
pipe1_percent = (pipe1 / water_in_pool) * 100
pipe2_percent = (pipe2 / water_in_pool) * 100

if capacity >= water_in_pool:
    print(F"(The pool is {percent_water:.2F}% full. Pipe 1: {pipe1_percent:.2F}%. Pipe 2: {pipe2_percent:.2F}%.")
else:
    too_much = water_in_pool - capacity
    print(F"For {time} hours the pool overflows with {water_in_pool-capacity} liters.")

# •	До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# o	"The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# o	"For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."
