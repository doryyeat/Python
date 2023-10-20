def is_password_good(password):
    if len(password) >= 10:
        upperLetters = False
        lowerLetters = False

        for letter in password:
            if letter.isupper():
                upperLetters = True
            elif letter.islower():
                lowerLetters = True
        if upperLetters and lowerLetters:
            return True
        else:
            return False
    else:
        return False

password = input("Введите пароль: ")
while not is_password_good(password): # пока ф-ия принимает значение False
    print("Пароль недостаточно надежный.")
    password = input("Введите пароль: ")
print("Пароль надежный :)")