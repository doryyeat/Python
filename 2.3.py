try:
    n, m = map(int, input("Введите размеры массива n и m через пробел: ").split())

    array = []
    for a in range(n):
        row = list(map(int, input("Введите строку элементов массива через пробел: ").split()))
        if len(row) != m:
            raise ValueError("Количество элементов в строке не соответствует m")
        array.append(row)

    i, j = map(int, input("Введите числа i и j через пробел: ").split())

    if i < 0 or i >= m or j < 0 or j >= m:
        raise ValueError("Некорректные значения i и j") # явное генерирование исключений

    for k in range(n):
        array[k][i], array[k][j] = array[k][j], array[k][i]

    print("Результат:")
    for row in array:
        print(row)

except ValueError: # отлавливает и обрабатывает исключения
    print("Ошибка: некорректный ввод.")
except Exception:
    print("Произошла ошибка.")