import re

while True:
    word = input("Введите слово: ")
    if word.isalpha() and re.match("^[а-яА-Я]+$", word):
        break
    else:
        print("Ошибка ввода. Пожалуйста, русские буквы.")

print("Введенное слово:", word)

lower_pairs = 0
upper_pairs = 0
count_consonants = 0

for i in range(len(word)-1):
    if word[i].isupper() and word[i+1].isupper():
        upper_pairs += 1
    elif word[i].islower() and word[i+1].islower():
        lower_pairs += 1

consonants = "бвгджзйклмнпрстфхцчшщ"
for letter in word:
    if letter.lower() in consonants:
        count_consonants += 1

print("Количество пар верхнего регистра:", upper_pairs)
print("Количество пар нижнего регистра:", lower_pairs)
print("Количество согласных букв: ", count_consonants)
