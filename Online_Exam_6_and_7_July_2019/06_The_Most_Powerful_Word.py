# За Лора думите притежават голяма сила. Тя те моли да измислиш алгоритъм, с който да откриеш коя е "найсилната" дума. До получаване на команда "End of words"
# ще се четат от конзолата думи. За да се открие
# силата на всяка една, трябва да се намери сборът от ASCII стойностите на символите, от които се състои
# думата. Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви),
# полученият сбор трябва да се умножи по дължината на думата, в противен случай, да се раздели на
# дължината и да се закръгли до най-близкото цяло число надолу

stongest_word_score = 0
strongest_word = ""
while True:
    word = input()
    sum1 = 0
    if word == "End of words":
        break
    for i in range(len(word)):
        sum1 += ord(word[i])
    if ord(word[0]) == 97 or ord(word[0]) ==  101 or ord(word[0]) == 105 or ord(word[0]) == 111 or ord(word[0]) ==  117 \
            or ord(word[0]) ==  121 or ord(word[0]) == 65 or ord(word[0]) ==  69 or ord(word[0]) ==  73 \
            or ord(word[0]) ==  79 or ord(word[0]) == 85 or ord(word[0]) ==  89:
        sum1 = sum1 * len(word)
    else:
        sum1 = round(sum1 / len(word))
    if sum1 > stongest_word_score:
        stongest_word_score = sum1
        strongest_word = word
print(F"The most powerful word is {strongest_word} - {stongest_word_score}")
