
stongest_word_score = 0
strongest_word = ""
list_of_vowels = ['a','e','i','o','u','y','A','E','O','Y','I','U']

while True:
    word = input()
    sum1 = 0
    if word == "End of words":
        break
    for i in word:
        sum1 += ord(i)
    if word[0] in list_of_vowels:
        sum1 = sum1 * len(word)
    else:
        sum1 = round(sum1 / len(word))
    if sum1 > stongest_word_score:
        stongest_word_score = sum1
        strongest_word = word
print(F"The most powerful word is {strongest_word} - {stongest_word_score}")
