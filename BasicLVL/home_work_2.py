# `````````````````Дз```````````````````````#

# number = int(input("Введите число:"))
#
# print("-=-" , end = "")
# for digit in range(0, number + 10, 10):
#     print(digit , end = "-=-")

# `````````````````Дз```````````````````````#

# karamba_count = 0
# secret_word = "Карамба"
#
# for team in range(1, 10 + 1):
#     print(f"Кандидат номер {team} ", end=' ')
#     salut = input("введите слово:")
#     if salut == secret_word or salut == "карамба":
#         karamba_count += 1
#
# print(f"В команду попало {karamba_count}, человек(а) ")

# `````````````````Дз```````````````````````#

# text = input("Введите сообщение:")
# top = 0
#
# for symbol in text:
#     top += 1
#     if symbol == "*":
#         break
#
# print(f"Символ «*» стоит на позиции {top}")

# `````````````````Дз```````````````````````#

# row = int(input("Введите кол-во рядов: "))
# armchair = int(input("Введите кол-во кресел в ряду: "))
# empty_size = int(input("Введите расстояние между рядами (в сантиметрах): "))
#
# for i in range(row):
#     print("O " * armchair)
#     print(" " * empty_size)

# `````````````````Дз```````````````````````#

# width = 15
# height = 20
#
# x = width // 2
# y = height // 2
#
# steps = 10
#
# for Charley in range(steps):
#     print(f"Марсоход находится на позиции {x}, {y}, введите команду:")
#     command = input("W (север), S (юг), A (запад), D (восток)")
#
#     if command == "W":
#         if y < height:
#             y += 1
#     elif command == "S":
#         if y > 0:
#             y -= 1
#     elif command == "A":
#         if x > 0:
#             x -= 1
#     elif command == "D":
#         if x < width:
#             x += 1
#     else:
#         print("Неверная команда! Используйте W (север), S (юг), A (запад), D (восток).")

# `````````````````Дз```````````````````````#

# boys = int(input("Кол-во мальчиков:"))
# girls = int(input("Кол-во девочек:"))
# answer = ""
#
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print("Нет решения")
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range(k):
#         answer += "BGB"
#     for bg in range(girls - k):
#         answer += "BG"
# else:
#     k = girls - boys
# for gbg in range(k):
#     answer += "GBG"
# for gb in range(boys - k):
#     answer += "GB"
#
# print(answer)

# `````````````````Дз```````````````````````#

# ttlmilk = 0
#
# for cow in range(1, 11):
#     print(f"Стойло {cow}" )
#     asnwer =  input("Выберете вариант : a — свободное стойло, b — занятое")
#     if asnwer == "a":
#         cow += 1
#     else :
#         ttlmilk += cow * 2
#     print(f"получено молока: {ttlmilk}")
# print(f"всего получено молока сегодня:,{ttlmilk}")

# `````````````````Дз```````````````````````#

# message = input("Введите зашифрованное сообщение:")
# numm = 0
# first = ""
# last = ""
#
# for symbol in message:
#     numm += 1
#     if numm % 2 == 1:
#         first = first + symbol
#     else:
#         last = symbol + last
#
# resul = first + last
# print("Расшифрованное сообщение:", resul)

# `````````````````Дз```````````````````````#

# for a in range(1, 10):
#     for b in range(1, 10):
#          print(a * b , end = "\t")
#     print()

# `````````````````Дз```````````````````````#

# digit = int(input("Ввведите число:"))
#
# for row in range(digit + 1):
#     for col in range(digit + 1):
#         print(row + col, end = "\t")
#     print()

# `````````````````Дз```````````````````````#

# for row in range (10):
#     for col in range (0, -10, -1):
#         print(row + col, end = "\t")
#     print()

# `````````````````Дз```````````````````````#

# numm = int(input("Ввведите число:"))
#
# for row in range(1, numm + 1):
#     for col in range(1, numm + 1):
#         if row %2 == 0:
#             print(row , end = " ")
#         else:
#             print(col, end = " ")
#     print()

# `````````````````Дз```````````````````````#

# numm = int(input("Ввведите размер матрицы:"))

# if numm <= 0:
#     print("Число должно быть больше 0!")
# else:
#      for row in range(1, numm + 1):
#         for col in range(1, numm + 1):
#             if row == numm:
#                 print(row, end=" ")
#             elif col % 3 == 0:
#                 print(col, end=" ")
#             else:
#                 print(row, end=" ")
#
#         print()

# `````````````````Дз```````````````````````#

# for row in range(5):
#     for col in range(10):
#         if row == 0:
#             print("-", end="")
#         elif col == 0 or col == col - 1:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()

# `````````````````Дз```````````````````````#

# numm = int(input("Введите размер матрицы: "))
#
# for row in range(numm):
#     for col in range(numm):
#         if row + col == numm - 1:
#             print(1, end=" ")
#         elif row + col < numm - 1:
#             print(0, end=" ")
#         else:
#             print(2, end=" ")
#     print()

# `````````````````Дз```````````````````````#
# msg = int(input("Введите число :"))
#
# resolt = 0
#
# while resolt < 5:
#     numm = int(input("Введите число :"))
#     if numm >= 5:
#         resolt += 1
#
#     print(f"всего чисел 5 : {resolt}")

# `````````````````Дз```````````````````````#
# numm = int(input("Введите число: "))
#
# for row in range(numm + 1):
#     for col in range(row, numm + 1):
#         print(col, end=' ')
#     print()

# `````````````````Дз```````````````````````#

# for row in range(6):
#     for col in range(0, 11, 2):
#         print(row + col, end = '\t')
#     print()

# `````````````````Дз```````````````````````#

# digit = int(input("Введите число: "))
#
# for row in range(1, digit + 1):
#     for col in range(row):
#         print(row, end=" ")
#     print()

# `````````````````Дз```````````````````````#

# for row in range(10):
#     for col in range(10):
#         if row == 0 or row == 9:
#             print("_", end = " ")
#         elif col == 0 or col == 9:
#             print("|", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# `````````````````Дз```````````````````````#

# nummTtl = int(input("Введите количество чисел: "))
#
# numCount = 0
# entered = 0
#
# while entered < nummTtl:
#     digit = int(input("Введите число: "))
#     entered += 1
#
#     if digit >= 2:
#         dividerCount = 0
#         for divider in range(1, digit + 1):
#             if digit % divider == 0:
#                 dividerCount += 1
#
#         if dividerCount == 2:
#             numCount += 1
#
# print(f"Количество простых чисел в последовательности: {numCount}")

# `````````````````Дз```````````````````````#

# n = int(input("Введите высоту пирамиды: "))
#
# for row in range(1, n+1, 2):
#     print(" " * ((7 - row) // 2) + "#" * row)

# `````````````````Дз```````````````````````#

# n = int(input("Сколько чисел вы хотите ввести? "))
# max_digit_sum = 0
# number_with_max_sum = 0
#
# for digit in range(n):
#     num = int(input("Введите число: "))
#     sum_of_digits = 0
#     temp = num
#
#     while temp > 0:
#         sum_of_digits += temp % 10
#         temp //= 10
#
#     if sum_of_digits > max_digit_sum:
#         max_digit_sum = sum_of_digits
#         number_with_max_sum = num
#
# print(f"Число с наибольшей суммой цифр: {number_with_max_sum}")
# print(f"Сумма его цифр: {max_digit_sum}")

# `````````````````Дз```````````````````````#

# n = int(input("Введите высоту пирамиды: "))
# current = 1
#
# for row in range(1, n + 1):
#     print(" " * (n - row), end="")
#     for i in range(row):
#         print(current, end=" ")
#         current += 2
#     print()

# `````````````````Дз```````````````````````#

# n = int(input("Введите глубину ямы:"))
#
# for row in range(1, n + 1):
#     for col in range(n, n - row, -1):
#         print(col, end="")
#     print("." * (2 * (n - row)), end="")
#
#     for col in range(n - row + 1, n + 1):
#         print(col, end="")
#     print()

# `````````````````Дз```````````````````````#

# rows = int(input("Кол-во уровней?:"))
# new_num = 1
#
# for line in range(rows):
#
#     for space in range(rows - line - 1, 0, -1):
#         print(end=' ')
#
#     for number in range(line + 1):
#         print(new_num, end=' ')
#         new_num += 2
#     print()

# `````````````````Дз```````````````````````#

# rows = int(input("Кол-во уровней?:"))
# new_num = 1
#
# for line in range(rows):
#     space_count = rows - line - 1
#     print(' ' * space_count, end='')
#     for number in range(line + 1):
#         print(new_num, end=' ')
#         new_num += 2
#     print()

# `````````````````Дз```````````````````````#

#age = int(input("Введите возраст :"))
# temperature = float(input("Введите температуру :"))
#
# mny_gift = round(age * temperature, 2)
#
# print(mny_gift)

# `````````````````Дз```````````````````````#

# chatle = int(input("Сколько чатлов?: "))
#
# CR = float(chatle) / 2200
# ships = int(CR / 0.5)
#
# print(f"Это {CR} CR")
# print(f"Можно купить кораблей: {ships}")

# `````````````````Дз```````````````````````#

# while True:
#     print("Введите местоположение фигуры")
#     x = float(input("По горизонтали: "))
#     y = float(input("По вертикали: "))
#
#     if x < 0 or x >= 0.8 or y < 0 or y >= 0.8:
#         print("Клетки с такой координатой не существует")
#     else:
#         xValue = int(x * 10)
#         yValue = int(y * 10)
#         print(f"Фигура находится в клетке ({xValue}, {yValue})")

# `````````````````Дз```````````````````````#

# import math
#
# a = int(input("Введите длину стороный 'А': "))
# b = int(input("Введите длину стороный 'В': "))
# c = int(input("Введите длину стороный 'С': "))
#
# if a + b > c and a + c > b and b + c > a:
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь треугольника равна:", int(s))
# else:
#     print("Треугольник с такими сторонами не существует")

# `````````````````Дз```````````````````````#

# import math
#
# x = 0
# y = 0
#
# distance = float(input("Введите расстояние: "))
# angle_deg = float(input("Введите угол (в градусах): "))
#
# angle_rad = math.radians(angle_deg)
#
# x += distance * math.cos(angle_rad)
# y += distance * math.sin(angle_rad)
#
# print(f"Новые координаты персонажа: ({x}, {y})")

# `````````````````Дз```````````````````````#

# import math
#
# numm = float(input("Введите ваше число: "))
#
# print("Округляем вниз:")
# print(math.floor(numm))
#
# print("Округляем вверх:")
# print(math.ceil(numm))
#
# print("Модуль числа:")
# print(abs(numm))
#
# if numm < 0:
#     print("Корень из отрицательного числа невозможен")
# else:
#     print("Квадратный корень:")
#     print(math.sqrt(numm))
#
# print("Считаем экспоненту:")
# print(math.exp(numm))
#
# if numm <= 0:
#     print("Логарифм не определён для нуля и отрицательных чисел")
# else:
#     print("Вычисляем логарифм:")
#     print(math.log(numm))
#
#     print("Вычисляем логарифм по основанию 2:")
#     print(math.log2(numm))
#
#     print("Вычисляем логарифм по основанию 10:")
#     print(math.log10(numm))
#
# print("Вычисляем sin числа:")
# print(math.sin(numm))
#
# print("Вычисляем cos числа:")
# print(math.cos(numm))
#
# if numm < 0 or not numm.is_integer():
#     print("Факториал можно считать только от неотрицательного целого числа")
# else:
#     print("Вычисляем факториал:")
#     print(math.factorial(int(numm)))

# `````````````````Дз```````````````````````#

# price = float(input('Введите сумму покупки в Евро: '))
#
# euro_to_usd = 1.25
# usd_to_rub = 60.87
#
# rub = price * euro_to_usd * usd_to_rub
#
# print('Общая стоимость составляет:', round(rub, 2), 'рублей')

# `````````````````Дз```````````````````````#

# import math
#
# attemp = int(input('Введите кол-во чисел:'))
# attempCount = 0
#
# while attempCount < attemp:
#     numm = float(input('Введите число:'))
#
#     if numm >= 0:
#         maxNumm = math.ceil(numm)
#         print(math.log(maxNumm))
#     else:
#         minNumm = math.floor(numm)
#         print(math.exp(minNumm))
#
#     attempCount += 1

