# Вход
# • Име на актьора – текст
# • Точки от академията - реално число в интервала [2.0... 450.5]
# • Брой оценяващи n – цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# o Име на оценяващия – текст
# o Точки от оценяващия – реално число в интервала [1.0... 50.0]

name = input()
academy_Score = float(input())
n = int(input())

for i in range(n):
    judge_name = input()
    score = float(input())
    academy_Score +=  (len(judge_name) * score) / 2
    if academy_Score >= 1250.5:
        print(F"Congratulations, {name} got a nominee for leading role with {academy_Score:.1F}!")
        break
else:
    print(F"Sorry, {name} you need {1250.5 - academy_Score:.1F} more!")