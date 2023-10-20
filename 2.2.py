def process_data(data):
    try:
        if isinstance(data, tuple):
            length_of_words = sum([len(word) for word in data if isinstance(word, str)])
            return length_of_words

        elif isinstance(data, list):
            negative = False
            total_sum = 0
            for num in data:
                if negative:
                    total_sum += num
                elif num < 0:
                    negative = True
            return total_sum

        elif isinstance(data, int):
            count_even_digits = len([int(digit) for digit in str(data) if int(digit) % 2 == 0])
            return count_even_digits

        elif isinstance(data, str):
            total_sum = sum([int(word) for word in data if word.isdigit()])
            return total_sum

    except Exception:
        print("Произошла ошибка.")
    except ValueError: # ошибка преобразования

        print("Некорректное значение.")

print(process_data(("язык", 5, "программирования", 2, "питон", "кортеж")))  # длина слов в кортеже
print(process_data([1, -2, 14, 11, 0]))  # сумма чисел после первого отриц элемента
print(process_data(1234567897))  # кол-во четных цифр
print(process_data("у меня 3 яблока и 4 банана"))  # сумма всех чисел в строке


