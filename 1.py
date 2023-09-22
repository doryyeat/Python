while True:
    try:
        num = int(input("Введите натуральное число: "))
        if num <= 0:
            print("Число должно быть больше нуля.")
            continue
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите натуральное число.")

sum_of_odd_digits = 0
odd_digits = []

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        sum_of_odd_digits += digit
        odd_digits.append(str(digit))
    num = num // 10
    odd_digits_str = ",".join(odd_digits)

print("Нечётные цифры числа:", odd_digits_str)
print("Сумма нечетных цифр введенного числа:", sum_of_odd_digits)

