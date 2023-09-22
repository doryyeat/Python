# МЕНЮ
menu = {'Торт': [['бисквитное тесто', 'крем', 'лесные ягоды'], 30, 500],
        'Пирожное': [['тиррамису', 'карамель'], 7, 400],
        'Маффин': [['шоколадный бисквит', 'шоколадная стружка'], 5, 150]}

# ОПИСАНИЕ
def show_description(product):
    if product in menu:
        description = ", ".join(menu[product][0])
        print(f"Описание {product}а: {description}")

# ЦЕНА
def show_price(product):
    if product in menu:
        price = menu[product][1]
        print(f"Цена {product}а: {price} рублей за 100 гр.")

# КОЛИЧЕСТВО
def show_quantity(product):
    if product in menu:
        quantity = menu[product][2]
        print(f"Количество {product}а: {quantity} гр.")

# ВСЯ ИНФА
def show_all():
    print("--- Вся информация о продукции ---")
    for product, data in menu.items():
        description = ", ".join(data[0])
        price = data[1]
        quantity = data[2]
        print(f"{product}:")
        print(f"  Описание: {description}")
        print(f"  Цена: {price} рублей за 100 гр.")
        print(f"  Количество: {quantity} гр.")
        print()

# ПОКУПКА
def make_purchase():
    total_price = 0
    remaining_items = menu.copy()

    while True:
        product = input("Введите название продукции (или 'n' для выхода): ")
        if product.lower() == 'n':
           break
        quantity = int(input("Введите количество продукции: "))

        if product in menu:
            price = menu[product][1]
            remaining_quantity = menu[product][2]

            if quantity <= remaining_quantity:
                total_price += (price * quantity)
                remaining_items[product][2] -= quantity
                print("Покупка успешно совершена!")
            else:
                print("Не хватает доступного количества продукции.")



    print(f"Суммарная стоимость покупки: {total_price} рублей")
    print("Остатки продукции:")
    for product, data in remaining_items.items():
        print(f"{product}: {data[2]} гр.")

# ГЛАВНОЕ МЕНЮ
while True:
    print("\n     Кондитерская ")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        product = input("Введите название продукции: ")
        show_description(product)
    elif choice == '2':
        product = input("Введите название продукции: ")
        show_price(product)
    elif choice == '3':
        product = input("Введите название продукции: ")
        show_quantity(product)
    elif choice == '4':
        show_all()
    elif choice == '5':
        make_purchase()
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Некорректный ввод. Попробуйте ещё раз.")