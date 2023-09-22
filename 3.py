lst = [1612, 49, 'hello', 6, 19, 'world']
print('Изначальный список: ',lst)

vowels = ['a', 'e', 'i', 'o', 'u', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

print('Конечный список: ')
for i in range(len(lst)):
   # элемент - число
    if isinstance(lst[i], int):
        if lst[i] % 2 == 0:
            digit_sum = 0
            for digit in str(lst[i]):
                digit_sum += int(digit)
            lst[i] = digit_sum
        else:
            lst[i] = 1
            # нечетное число - строка
    elif isinstance(lst[i], str):
        vowel_count = 0
        consonant_count = 0
        word = lst[i].lower()
        for char in word:
            # символ - буква
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        lst[i] = {'word': lst[i], 'vowels': vowel_count, 'consonants': consonant_count}  # Заменяем строку на словарь

for item in lst:
    # элементы конечного списка
    print(item)