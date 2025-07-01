# 9.2 Сравнение строк

# password = (input("Введите пароль :"))
#
# while password != "bsae124531" :
#     print("Не верный пароль!")
#     password = (input("Повторите попытку"))
# print("Добро пожаловать!")

# +++++++++++++++++++++++++++++++++++++++++++#

# author = ("Имя автора произведения?"))
# bad_answer = 0

# while author != "Пушкин" :
#     author = ("Имя автора произведения?"))
#     bad_answer += 1
# print("Молодец , пятёрка")
# print("У нас в классе" , bad_answer , "учиников")

# +++++++++++++++++++++++++++++++++++++++++++#

# bad_answer = 0
# for student in range (5):
#     answer = (input("Имя автора произведения?"))
#     if (answer == "Пушкин") or (answer == "пукшкин"):
#         print("Молодец , пятёрка")
#         break
#     print("Не правильно 2 !")
#     bad_answer += 1
# print("Кол-во двоек :" , bad_answer)

# 9.3 Цикл for итерирование по строке

# +++++++++++++++++++++++++++++++++++++++++++#

# for symbol in "Python":
#     print(symbol)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = input("Введите слово :")
# for symbol in word:
#     print(symbol)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = input("Введите слово :")
# for symbol in word:
#     print(symbol * 3)
#     print("_" * 4)

# +++++++++++++++++++++++++++++++++++++++++++#

# 9.4 Дополнительные возможности функции print

# text = input("Введите текст:")
# new_sym = ""
#
# for symbol in text:
#     new_sym += symbol + ""
# print(new_sym)

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input("Введите текст:")
#
# for symbol in text:
#     print(symbol , end = " ")

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input("Введите текст:")
#
# for symbol in text:
#     print(symbol , end = "@ , \n")

# +++++++++++++++++++++++++++++++++++++++++++#

# number = int(input("Введите число:"))
# step = int(input("Введите шаг:"))
# summ = 0
#
# print("IP-адерес:", end = " ")
# for count in range(3):
#     print(number , end = '.')
#     summ += number
#     number += step
# print(summ)

# 9.5 Типовые алгоритмы работы со строками

# text = input("Введите текст")
# summ = 0
#
# print("\nОтфильтрованный текст" , end = " ")
# for symbol in text:
#     if symbol == "1" or symbol == "9":
#         summ += int(symbol)
#     else :
#         print(symbol , end = " ")
# print("\nСумма :" , summ)

# +++++++++++++++++++++++++++++++++++++++++++#

# string = input("Введите строку :")
# prevSym = ""
# equalSym = False
#
# for letter in string:
#     if prevSym == letter:
#         equalSym == True
#         break
#     else:
#         prevSym == letter
#
# if equalSym:
#     print("Есть две одиноковые буквы подряд")
# else:
#     print("Нет двух одиноковые букв подряд")

# +++++++++++++++++++++++++++++++++++++++++++#

# 10.1 Работа со вложенными циклами

# for a in range(1, 10):
#     for b in range(1, 10):
#         print(a, "*" , b, "=", a * b)
#     print()

# for row in range(6):
#     for col in range(6):
#         print(row + col , end = "")
#     print()

# 10.2 Использование if во вложенных циклах

# size = int(input("Введите размер таблицы:"))
#
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if row %2 == 0:
#             print(row , end = " ")
#         else:
#             print(col, end = " ")
#     print()

# +++++++++++++++++++++++++++++++++++++++++++#

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end=" ")
#         elif col == 24:
#             print("|", end=" ")
#         else:
#             print("?", end=" ")
#
#     print()

# 10.3 Работа с двумя счётчиками в условном операторе

# size = int(input("Введите число :"))
#
# for row in range(size):
#     for col in range(size):
#         if row < col:
#             print(0, end = "")
#         elif row > col:
#             print(2, end = "")
#         else:
#             print(1, end = "")
#     print()

# +++++++++++++++++++++++++++++++++++++++++++#

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end=" ")
#         elif col == row + 29:
#             print("\\", end=" ")
#         elif col == -row + 19:
#             print("/", end=" ")
#         elif col == 24:
#             print("|", end=" ")
#         else:
#             print(" ", end=" ")
#
#     print()

# 10.4 Решение задач с помощью вложенных циклов

# people = int(input("Введите кол-во людей:"))
#
# for hour in range(people + 1):
#     print("Идёт час :", hour)
#     for num in range(hour, people):
#         print("Номер в очереди:", num)
#     print()
# print("Очередь обслужена!")

# +++++++++++++++++++++++++++++++++++++++++++#

# seqNum = int(input("Сколько будет чисел :"))
# digit = int(input("Какую цифру считать? :"))
#
# while digit < 0 or digit > 9:
#     digit = int(input("Ввведите цифру от 0 до 9!"))
# digitCount = 0
#
# for num in range(seqNum):
#     print(f"Введите, {num} ,число :", end = "")
#     number = int(input())
#     while number > 0:
#         if number %10 == digit:
#             digitCount += 1
#         number //= 10
# print(f"Цифр {digit}, в последовательности {digitCount} " )

# 10.5 Блок else для цикла. Бесконечный внешний цикл

# attpcoun = 3
#
# for attemp in range(1, 4):
#     pswrd = int(input("Введите пинкод:"))
#     if pswrd == 4321:
#         print("Верный пинкод.")
#         break
#     attpcoun -= 1
#     print(f"Неверный пинкод, осталось попыток: {attemp} ")
# if attpcoun == 0:
#     print("Ваша карта заблокированна.")

# +++++++++++++++++++++++++++++++++++++++++++#

# while True:
#     for attemp in range(1, 4):
#         pswrd = int(input("Введите пинкод:"))
#         if pswrd == 4321:
#             print("\nВерный пинкод.")
#             break
#         attpcoun -= 1
#         print(f"Неверный пинкод, осталось попыток:,3 - {attemp} ")
#     if attpcoun == 0:
#         print("\nВаша карта заблокированна.")

# 11.2 Ввод вещественного числа. Функции float и round

# bet = int(input("Ваша ставка?:"))
# coefficient = int(input("Коэффициент:"))
#
# win = bet * coefficient
#
# print("Выигрыш :", win)

# +++++++++++++++++++++++++++++++++++++++++++#

# bet = int(input("Ваша ставка?:"))
# coefficient = float(input("Коэффициент:"))
#
# win = bet * coefficient
#
# print("Выигрыш :", round(win, 2))

# +++++++++++++++++++++++++++++++++++++++++++#

# height = float(input("Ваш рост?:"))
# weight = float(input("Ваш вес?:"))
#
# bmi = round(weight / height ** 2, 2)
# print("Идекс массы тела:", bmi)
#
# if bmi < 18.5:
#     print("У вас недостаточная масса тела")
# elif bmi < 25:
#     print("У вас нормальная масса тела")
# elif bmi < 30:
#     print("У вас избыточная масса тела")
# else:
#     print("У вас ожирение!")

# 11.3 Приведение типов между int и float

# while True:
#     force = float(input("Сила удара :"))
#     force *= 10
#     print("Балл :", int(force))

# +++++++++++++++++++++++++++++++++++++++++++#

# x = float(input("Расположение по горизонтали:"))
# y = float(input("Расположение по вертикали:"))
#
# xSquare = int(x * 10)
# ySquare = int(y * 10)
#
# print("Фигура на координатах :", xSquare,",", ySquare)

# 11.4 Математические функции. Работа с модулем math

# import math
#
# x = int(input("Введите координату х :"))
# y = int(input("Введите координату у:"))
#
# distance = math.sqrt(x ** 2 + y ** 2)
#
# print("Расстояние:", distance)

# +++++++++++++++++++++++++++++++++++++++++++#

# import math
#
# distance = float(input("Введите расстояние до танка:"))
# angle = float(input("Введите угол в градусах:"))
#
# angle /= 57.2958
# x = math.cos(angle) * distance
# y = math.sin(angle) * distance
#
# print("Координаты танка :", x, ",", y)

# 12.2 Функции и их вызов

# for food in range(3):
#  fruit = int(input('Сколько фруктов?'))
#  vegetables = int(input('Сколько овощей?'))
#  summ = fruit + vegetables
#  print('Всего :', summ)

# +++++++++++++++++++++++++++++++++++++++++++#

# print('Обезьяны')
# fruit = int(input('Введите кол-во фруктов:'))
# vegetables = int(input('Сколько овощей?'))
# print('Всего :', fruit + vegetables)
#
# print('\nЖирафы')
# fruit = int(input('Введите кол-во фруктов:'))
# vegetables = int(input('Сколько овощей?'))
# print('Всего :', fruit + vegetables)
#
# print('\nСлоны')
# fruit = int(input('Введите кол-во фруктов:'))
# vegetables = int(input('Сколько овощей?'))
# print('Всего :', fruit + vegetables)

# +++++++++++++++++++++++++++++++++++++++++++#

# def countFood():
#     fruit = int(input('Введите кол-во фруктов:'))
#     vegetables = int(input('Сколько овощей?'))
#     print('Всего :', fruit + vegetables)
#
# print('Обезьяны')
# countFood()
# print('\nЖирафы')
# countFood()
# print('\nСлоны')
# countFood()

# +++++++++++++++++++++++++++++++++++++++++++#

# def triangle():
#     stars = 1
#     for line in range(5):
#         print(" " * (5 - line - 1), end = '')
#         print('*' * stars)
#         stars += 2
#
# def rectagle():
#     for line in range(5):
#         if line == 0 or line == 4:
#             print('*' * 5)
#         else:
#             print('*' + '' * 3 + '*')
#
# choice = int(input('1 - треугольник, 2 - прямоугольник'))
#
# if choice == 1:
#     triangle()
# elif choice == 2:
#     rectagle()
# else:
#     print('Выберете один из доступных вариантов')

# 12.3 Функции с одним параметром

# def person(name):
# 	print('Фамилия : Иванов')
# 	print('Имя :', name)
# 	print('Улица : Есенина')
# 	print('Дом : 89')
#
# person('Саша')
# person('Маша')
# person('Ваня')

# +++++++++++++++++++++++++++++++++++++++++++#

# import math
#
# def func(x):
# 	if -5 <= x <= 5:
# 		print('x =', x, 'y = ', math.exp(x))
# 	elif x < -5:
# 		print('x =', x, 'y = ', 2 * abs(x)-1)
# 	else:
# 		print('x =', x, 'y = ', 2 * x)
#
# for x in range(-10, 11):
# 	func(x)

# 12.4 Функции с несколькими параметрами

# def myAdress(name, house_number):
#     print('Имя:', name)
#     print('Фамилия: Пупкин')
#     print('Улица: Байрона')
#     print('Дом:', house_number)
#     print()  # правильный отступ
#
# myAdress('Вася', 3)
# myAdress('Даня', 34)
# myAdress('Женя', 12)
# myAdress('Маша', 31)


# +++++++++++++++++++++++++++++++++++++++++++#

# import math

# def myDistance(x, y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print("Расстояние до точки от начала координат:", distance)
#
# def betweenDistance(x_1, y_1, x_2, y_2):
#     distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
#     print("Расстояние между двумя точками:", distance)
#
# choice = int(input('1 - расстояние до точки, 2 - расстояние между двух точек: '))
#
# if choice == 1:
#     x = float(input('Введите координату x: '))
#     y = float(input('Введите координату y: '))
#     myDistance(x, y)
# elif choice == 2:
#     x_1 = float(input('Введите координату x1: '))
#     y_1 = float(input('Введите координату y1: '))
#     x_2 = float(input('Введите координату x2: '))
#     y_2 = float(input('Введите координату y2: '))
#     betweenDistance(x_1, y_1, x_2, y_2)
# else:
#     print('Ошибка ввода')

#12.5 Вложенный вызов функции

# def mainMenu():
#     print('1. Сделать что - то хоррошее')
#     print('2. Сделать что - то плохое')
#     choice = int(input('Введите номер действия:'))
#     if choice == 1:
#         good()
#     elif choice == 2:
#         bad()
#     else:
#         print('Выберете между 1 и 2')
#         mainMenu()
#
# def good():
#     print('Всё хорошо.')
#     input('Введите любой символ')
#     mainMenu()
#
# def bad():
#     print('Всё плохо.')
#
# mainMenu()

# 13.2 Несколько результатов одной функции

# def sqr(numm):
#     result = numm * numm
#     print(result)

# +++++++++++++++++++++++++++++++++++++++++++#

# def sqr(numm):
#     return numm * numm

# 13.3 Вещественные числа в Python

# def div_n_time(value, divider, times):
#     for i in range(times):
#         value /= divider
#     return value
#
# div_n_time(28, 4, 2)
