# import math
#
# size = int(input('Укажите размер файла для скачивания: '))
# speed = int(input('Какова скорость вашего соединения в МБ/с: '))
#
# downloaded = 0
# sec = 0
#
# while downloaded < size:
#     sec += 1
#     downloaded += speed
#     if downloaded > size:
#         downloaded = size
#     percent = math.ceil((downloaded / size) * 100)
#     print(f'Прошло {sec} сек. Скачано {downloaded} из {size} МБ ({percent}%)')
#
# print(f'Скачивание завершено за {sec} сек.')

# `````````````````Дз```````````````````````#

# import math
#
# size = int(input('Укажите размер файла для скачивания: '))
# speed = int(input('Какова скорость вашего соединения в МБ/с: '))
#
# total_seconds = math.ceil(size / speed)
#
# for sec in range(1, total_seconds + 1):
#     downloaded = speed * sec
#     if downloaded > size:
#         downloaded = size
#     percent = math.ceil((downloaded / size) * 100)
#     print(f'Прошло {sec} сек. Скачано {downloaded} из {size} МБ ({percent}%)')

# `````````````````Дз```````````````````````#

# x = float(input("Введите положительное действительное число X: "))
#
# fractional_part = x % 1
#
# first_decimal_digit = int(fractional_part * 10)
#
# print("Первая цифра после десятичной точки:", first_decimal_digit)

# `````````````````Дз```````````````````````#

# import math
#
# r = float(input("Введите радиус случайной планеты: "))
# v = (4 / 3) * math.pi * (r ** 3)
# earth_volume = 1.08321 * 10 ** 12
#
# ratio = earth_volume / v
#
# if ratio > 1:
#     print(f"Объём планеты Земля больше в {round(ratio, 3)} раз")
# else:
#     print(f"Объём планеты Земля меньше в {round(1 / ratio, 3)} раз")

# `````````````````Дз```````````````````````#

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# maximum = (a + b + abs(a - b)) // 2
#
# print("Наибольшее число:", maximum)

# `````````````````Дз```````````````````````#

# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#
#
# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting
#     print('Следующий.\n')

# `````````````````Дз```````````````````````#

# def que_sum():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
#
# print("Сколько мешков рыбы и мяса?")
# que_sum()
#
# print("Сколько буханок белого и чёрного хлеба?")
# que_sum()
#
# print("Сколько вёдер воды и молока?")
# que_sum()

# `````````````````Дз```````````````````````#

# def person():
#     print("Фамилия: Иванов")
#     print("Имя: Василий")
#     print("Улица: Пушкина")
#     print("Дом: 32")
#     print()
#
# person()
# person()
# person()
# person()

# `````````````````Дз```````````````````````#

# def wather(price):
# 	print('КлирВотер')
# 	print('ВодЗавод')
# 	print(price)
# 	print()
#
# wather('25')
# wather('30')
# wather('40')

# `````````````````Дз```````````````````````#

# import math
#
# radius = float(input("Введите радиус планеты: "))
#
# def sphereArea():
#     s = 4 * math.pi * (radius ** 2)
#     print(f"Площадь поверхности планеты: {s} км²")
#
# def sphereVolume():
#     v = (4 / 3) * math.pi * (radius ** 3)
#     print(f"Объём планеты: {v} км³")
#
# sphereArea()
# sphereVolume()

# `````````````````Дз```````````````````````#

# def isPrime(num):
#     if num < 2:
#         print(f"{num} — не простое число")
#     else:
#         i = 2
#         while i * i <= num:
#             if num % i == 0:
#                 print(f"{num} — не простое число")
#                 break
#             i += 1
#         else:
#             print(f"{num} — простое число")
#
# N = int(input("Сколько чисел вы хотите проверить? "))
#
# for _ in range(N):
#     number = int(input("Введите число: "))
#     isPrime(number)

# `````````````````Дз```````````````````````#

# def mid_num():
#     first_num = int(input('Введите левую границу: '))
#     second_num = int(input('Введите правую границу: '))
#
#     if first_num < second_num:
#         count = second_num - first_num + 1
#         total = (first_num + second_num) * count / 2
#         average = total / count
#         print('Среднее:', average)
#     else:
#         print('Ошибка: первое число должно быть меньше второго.')
#
# mid_num()

# `````````````````Дз```````````````````````#

# def mail(surname, name, country, town, street, home, door):
#     print('Фамилия:', surname)
#     print('Имя:', name)
#     print('Страна:', country)
#     print('Город:', town)
#     print('Улица:', street)
#     print('Дом:', home)
#     print('Квартира:', door)
#     print()
#
# mail('Пупкин', 'Вася', 'Бангладеш', 'Где-то', 'Ж', 10, 15)
# mail('Иванов', 'Пётр', 'Россия', 'Москва', 'Ленина', 5, 8)
# mail('Смирнова', 'Анна', 'Казахстан', 'Алматы', 'Абая', 21, 3)

# `````````````````Дз```````````````````````#

# import math
#
# def myDistance(x, y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print("Расстояние до точки от начала координат:", distance)
#
# def betweenDistance(x1, y1, x2, y2):
#     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     print("Расстояние между двумя точками:", distance)
#
# choice = int(input('Выберите действие:\n1 - расстояние до точки\n2 - расстояние между двумя точками\nВаш выбор: '))
#
# if choice == 1:
#     x = float(input('Введите координату x: '))
#     y = float(input('Введите координату y: '))
#     myDistance(x, y)
#
# elif choice == 2:
#     x1 = float(input('Введите координату x1: '))
#     y1 = float(input('Введите координату y1: '))
#     x2 = float(input('Введите координату x2: '))
#     y2 = float(input('Введите координату y2: '))
#     betweenDistance(x1, y1, x2, y2)
# else:
#     print('Ошибка ввода: выберите 1 или 2')

# `````````````````Дз```````````````````````#

# def summa_n():
#     result = 0
#     n = int(input('Введите число:'))
#     for digit in range(1, 5 + 1):
#         result += digit
#     print(f'Я знаю, что сумма чисел от 1 до {n} равна {result}')
#
# summa_n()

# `````````````````Дз```````````````````````#

# def positive():
#     print('Положительное')
#
# def negative():
#     print('Отприцательное')
#
# def test():
#     numm = int(input('Введите ваше число:'))
#     if numm > 0:
#         positive()
#     elif numm < 0:
#         negative()
#     else:
#         print('Ошибка повторите ввод')
#
# test()

# `````````````````Дз```````````````````````#

# def digit_sum(n):
#     if n < 0:
#         n = -n
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     print("Сумма цифр:", result)
#
#
# def digit_min(n):
#     if n < 0:
#         n = -n
#     min_digit = 9
#     while n > 0:
#         d = n % 10
#         if d < min_digit:
#             min_digit = d
#         n //= 10
#     print("Минимальная цифра:", min_digit)
#
#
# def digit_max(n):
#     if n < 0:
#         n = -n
#     max_digit = 0
#     while n > 0:
#         d = n % 10
#         if d > max_digit:
#             max_digit = d
#         n //= 10
#     print("Максимальная цифра:", max_digit)
#
# while True:
#     n = int(input('Введите ваше число: '))
#     move = input('Выберите действие: "sum", "min", "max": ')
#
#     if move == "sum":
#         digit_sum(n)
#     elif move == "min":
#         digit_min(n)
#     elif move == "max":
#         digit_max(n)
#     else:
#         print("Неизвестная команда. Попробуйте ещё раз.")

# `````````````````Дз```````````````````````#

# def reverse_number(n):
#     found_digit = 0  # 0 — ещё не было значимой цифры
#
#     print("Число наоборот:", end=" ")
#
#     while n > 0:
#         digit = n % 10
#         if digit != 0:
#             found_digit = 1  # теперь можно печатать всё
#             print(digit, end="")
#         else:
#             if found_digit == 1:
#                 print(0, end="")
#         n = n // 10
#
#     if found_digit == 0:
#         print(0, end="")
#
#     print()
#
# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         print("Программа завершена!")
#         break
#     reverse_number(num)

# `````````````````Дз```````````````````````#

# def count_letters():
#     txt = input('Введите ваш текст: ')
#     dig = input('Какую цифру ищем? ')
#     letter = input('Какую букву ищем? ')
#
#     dig_count = 0
#     letter_count = 0
#
#     for symb in txt:
#         if symb == dig:
#             dig_count += 1
#         elif symb == letter:
#             letter_count += 1
#
#     if dig_count == 0 and letter_count == 0:
#         print('Совпадений не найдено.')
#     else:
#         print(f'Кол-во цифр {dig}: {dig_count}')
#         print(f'Кол-во букв {letter}: {letter_count}')
#
# count_letters()

# `````````````````Дз```````````````````````#

# def gcd(a, b):
#     while b != 0:
#         temp = b
#         b = a % b
#         a = temp
#     print("Наибольший общий делитель:", a)
#
# x = int(input("Введите первое число: "))
# y = int(input("Введите второе число: "))

# `````````````````Дз```````````````````````#

# import random
#
# def rock_paper_scissors():
#     print("Игра 'Камень, ножницы, бумага'!")
#     choices = ['камень', 'ножницы', 'бумага']
#     player = input("Ваш выбор (камень, ножницы, бумага): ").lower()
#     computer = random.choice(choices)
#
#     print("Компьютер выбрал:", computer)
#
#     if player == computer:
#         print("Ничья!")
#     elif (player == 'камень' and computer == 'ножницы') or \
#          (player == 'ножницы' and computer == 'бумага') or \
#          (player == 'бумага' and computer == 'камень'):
#         print("Вы выиграли!")
#     elif player in choices:
#         print("Вы проиграли!")
#     else:
#         print("Неверный ввод. Попробуйте снова.")
#
# def guess_the_number():
#     number = 72
#     response = -1
#
#     while response != number:
#         response = int(input('Угадай какое было загадано число: '))
#         if response < number:
#             print("Слишком маленькое число.")
#         elif response > number:
#             print("Слишком большое число.")
#         else:
#             print('Поздравляем, вы выиграли!')
#
# def mainMenu():
#     while True:
#         print("\nГлавное меню:")
#         print("1 - Угадай число")
#         print("2 - Камень, ножницы, бумага")
#         print("0 - Выход")
#
#         answer = input("Выберите игру: ")
#
#         if answer == '1':
#             guess_the_number()
#         elif answer == '2':
#             rock_paper_scissors()
#         elif answer == '0':
#             print("До свидания!")
#             break
#         else:
#             print("Ошибка: выберите 1, 2 или 0.")
#
# mainMenu()

# `````````````````Дз```````````````````````#

# def summa_n(n):
#     ttl = 0
#     for dig in range(1, n + 1):
#         ttl += dig
#     return ttl
#
# n = int(input("Введите число: "))
# if n <= 0:
#     print("Число должно быть больше нуля!")
# else:
#     result1 = summa_n(n)
#     print(f"Сумма от 1 до {n} = {result1}")
#     result2 = summa_n(result1)
#     print(f"Сумма от 1 до {result1} = {result2}")

# `````````````````Дз```````````````````````#

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
#
# result = gcd(num1, num2)
# print("НОД =", result)

# `````````````````Дз```````````````````````#

# def numeral_count(number):
#     if number < 0:
#         return 0
#     if number == 0:
#         return 1  # У числа 0 одна цифра
#     count = 0
#     while number > 0:
#         count += 1
#         number //= 10
#     return count
#
# n = int(input("Введите кол-во задач: "))
#
# max_digits = 0
# priority_task = 0
#
# for i in range(n):
#     num = int(input("Введите число: "))
#     digits = numeral_count(num)
#
#     if digits > max_digits:
#         max_digits = digits
#         priority_task = num
#
# print("Первая задача на обработку:", priority_task)

# `````````````````Дз```````````````````````#

# def divider():
#     result = 1.0
#     divide = 0
#
#     while result > 0:
#         result /= 2
#         divide += 1
#         print(f'Кол-во делений = {divide}, минимальное число = {result}')
#
#     print("\nДальше делить нельзя — результат стал равен 0.")
#     return divide, result
#
# divider()