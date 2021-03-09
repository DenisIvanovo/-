"""
Скрипт генерирует надежные пароли.
Пароль состоит из Символов нижнего и верхнего регистра,десятичных символов и спецсимволов.
Пароли можно использовать повседневно,для различных нужд.
"""

from random import *
import string

letters = string.ascii_letters  # Содержит символы нижнего и верхнего регистра.
numbers = string.digits  # Содержит десятичные числа.
special_symbol = string.punctuation  # Содежит спецсимволы.
generation = letters + numbers + special_symbol

min_length = input("Введите минумальную длину пароля:")
while True:
    if not min_length.isdecimal():
        print("Ошибка")
        print("Используйте только целые числа.")
        min_length = input("Введите минумальную длину пароля:")
        continue
    else:
        min_length = int(min_length)
        if 0 == min_length < 8:
            print("Минимальная длина надежного пароля ДОЛЖНА состоять из 8 символов!")
            min_length = input("Введите минумальную длину пароля:")
            continue
        else:
            break

max_length = input("Введите максимальную длину пароля:")
while True:
    if not max_length.isdecimal():
        print("Ошибка")
        print("Используйте только целые числа.")
        max_length = input("Введите максимальную длину пароля:")
        continue
    else:
        max_length = int(max_length)
        if max_length < 8:
            print("Минимальная длина надежного пароля ДОЛЖНА состоять из 8 символов!")
            max_length = input("Введите максимальную длину пароля:")
            continue
        else:
            break

new_password = "".join(choice(generation) for x in range(min_length, max_length))

print(new_password)
