try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
    print("Результат деления:", result)
except ArithmeticError:
    print("Невозможно деление на нуль.")
except ValueError:
    print("Введите целое число.")
finally:
    print("Выполнение завершено.")
