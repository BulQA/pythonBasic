# 2.1 Переменные

# t = "Hello world!"
# print(t)

# `````````````````ДЗ````````````````````````#
# first = "Моя первая переменная!"
# second = "И не последняя !"
# print(first)
# print(second)
# +++++++++++++++++++++++++++++++++++++++++++#

# 2.2 Оператор ввода input

# name = input("Введите имя ")
# print("Привет")
# print(name)
# name2 = input("Введите второе имя ")
# print("Привет, ")
# print(name2)

# `````````````````ДЗ````````````````````````#
# name = input("Введите ваше имя :")
# color = input("Ваш любимый цвет : ")
# sport = input("Каким спортом вы занимаетесь ? :")
# print("Привет",name)
# print("Твой любимый цвет это" ,color , "?")
# print("А занимаешься ты " , sport)
# `````````````````ДЗ2```````````````````````#
# name_1 = input("Введите первое имя :")
# name_2 = input("Введите второе имя :")
# print("Привет ,")
# print(name_1)
# print("Привет ,")
# print(name_2)
# `````````````````ДЗ3```````````````````````#
# sur_name = input('Введите фамилию: ')
# print('Ваша фамилия - ')
# print(sur_name)

# +++++++++++++++++++++++++++++++++++++++++++#

# 2.3 Строки и конкатенация

# name = input("Введите имя ")
# print("Привет", name, "I'm - computer")

# Конкатинация#

# print("Торговая "+" Площадь")

# a = input("Введите первое слово: ")
# b = input("Введите второе слово: ")
# c = a + " середина " + b
# print(c)
# `````````````````ДЗ1```````````````````````#
# surname = input("Ваша фамилия ? :")
# print("HI", surname )
# `````````````````ДЗ2```````````````````````#
# wirbs_1 = input("Введите первое слово :")
# wirbs_2 = input("Введите второе слово :")
# print(wirbs_1  +  wirbs_2)
# `````````````````ДЗ3```````````````````````#
# animal_1 = "заяц"
# animal_2 = "черепаха"
# print(animal_1 +  " спит, " +animal_2 + " идёт")
# `````````````````ДЗ4```````````````````````#
# first_name = input('Введите имя пользователя: ')
# greeting = 'Утро доброе!'
# print(greeting, first_name)
# intro = "К сожалению, у Вас нет доступа к системе."
# info = "Пожалуйста, обратитесь к системному администратору."
# print(intro , info)
# `````````````````ДЗ5```````````````````````#
# where_from = input("Откуда вылетаете ?:")
# where_for = input("Куда летите ?:")
# print(where_from + " - " + where_for)
# `````````````````ДЗ6```````````````````````#
# user = input("Введите имя пользователя :")
# new_file = input("Введите имя файла :")
# print("Путь к файлу " +"C/:"+user+"/docs/folder/"+new_file+".txt" )
# +++++++++++++++++++++++++++++++++++++++++++#

# 2.4 Особенности работы с переменными

# name1, naem2, name3 = "Саша","Маша","Паша"
# print(name1,naem2,name3)
# `````````````````Д1```````````````````````#
# a = input('Введите первое слово: ')
# b = input('Введите второе слово: ')
# print(a, b)
# a , b = b , a
# print(a, b)

# +++++++++++++++++++++++++++++++++++++++++++#

# 3.2 Числа и арифметические операции с ними

# print(10+20)
# print(30/15)
# print(99-72)
# print(4**7)

# a = 12
# b = 13
# c = a + b
# print(c)
# or
# print(a + b)
# print("HI", c)

# +++++++++++++++++++++++++++++++++++++++++++#

# 3.3 Приоритет арифметических операций

# +++++++++++++++++++++++++++++++++++++++++++#

# 3.4 Ввод числа с клавиатуры

# a = int(input("Введите первое число :"))
# b = int(input("Введите второе число :"))
# c = a + b
# print(c)

# a = "123"
# b = "432"
# c = a + b
# d = int(c)*2
# print(d)

# +++++++++++++++++++++++++++++++++++++++++++#

# 3.5 Деление нацело и с остатком

# mango = 98
# boxes = 11
# full_boxes = mango // boxes
# print("Полных ящиков :" ,full_boxes)
# rest_mango = mango % boxes
# print("Неполных ящиков :" , rest_mango)

# "//" - деление нацело (Показывает только целое число при делении)
# "%" - деление с остатком (Показывает только остаток от числа при делении)

# +++++++++++++++++++++++++++++++++++++++++++#

# 3.6 Сокращённые операторы

# product = 0
# product = product + 200
# print("Итоговая сумма :" , product)
# product = product + 327
# print("Итоговая сумма :" , product)
# product += 450
# print("Итоговая сумма :" , product)

# +++++++++++++++++++++++++++++++++++++++++++#

# 4.2 Условный оператор

# count = int(input("Загадай число от 1 до 10 :"))
# my_number = 8
# if count == my_number:
#      print("Ты молодец!")
# else:
#     print("В следующий раз повезёт :)")

# +++++++++++++++++++++++++++++++++++++++++++#

# 5.2 Вложенные условия

# bank = int(input("К оплате :"))
# if bank > 40000:
# 	bank -= 40000
# 	print("Покупка успешно совершена")
# 	if bank < 2000:
# 		bank+=500
# 		print("Применена скидка")
# else:
# 	print("Недостаточно средств :(")
# print("На счету осталось " , bank)
# print("Хорошего дня!")


# product = int(input("Сумма чека :"))
# delivery = int(input("Сумма доставки :"))
# discout = 0
# if product > 7500:
# 	print("Поздравляем , доставка вдвое дешевле")
# 	delivery /=2
# 	if product %2 == 0:
# 		print("Вам положен подарок")
# 		discout = 500
# price = product + delivery - discout
# print("Всего к оплате:", price)

# +++++++++++++++++++++++++++++++++++++++++++#

# 5.3 Цепочки условий if-elif-else

# profit = int(input("Размер взноса :"))
# if profit < 9700:
# 	tax = profit * 13 / 100
# 	print("Сумма налога 13% ", tax)
# elif profit < 63000:
# 	tax = profit * 20 / 100
# 	print("Сумма налога 20% ", tax)
# else:
# 	tax = profit * 30 / 100
# 	print("Сумма налога 30% ", tax)

# +++++++++++++++++++++++++++++++++++++++++++#

# 5.5 Использование нескольких логических операторов

# year =  int(input("Дата выпуска :"))
# speed_count = int(input("Колличество скоростей :"))
# if year >= 2018:
# 	if speed_count >=12:
# 		print("OK")
# 	else:
# 		print("Не подходит")
# else:
# 	print("Не подходит")
#
#
# year = int(input("Введите год :"))
# if (year %4 == 0) and not (year %100 != 0) or (year %400 == 0):
# 	print("Год високосный")
# else:
# 	print("Год не високосный")

# +++++++++++++++++++++++++++++++++++++++++++#

# 6.1 Знакомство с циклом while

# ttl_weight = 0
# car = 900
# while ttl_weight < car :
#     if ttl_weight == 0 :
#         print( "В машине есть свободное место ")
#     else:
#         print(ttl_weight)
#     weight = int(input("Вес мешка :"))
#     ttl_weight += weight
#     car_weight = car - ttl_weight
# print("В машине закончилось свободного место :" , car_weight)

# +++++++++++++++++++++++++++++++++++++++++++#

# counter = 0
# total = 0
#
# while counter <5:
#     counter += 1
#     total += counter
# print("Total", total)
# print("counter", counter)

# +++++++++++++++++++++++++++++++++++++++++++#

# balance = 10000
# limit = 130
#
# while balance > limit:
#  	print("Баланс:", balance)
#  	expense = int(input("Сумма траты?:"))
#  	balance -= expense
# print("Ваш лимит исчерпан , на счету осталось", balance )

# +++++++++++++++++++++++++++++++++++++++++++#

# info = ("Вы вошли в систему")
# pswrd = "1470"
#
# user_input = ""
#
# while user_input != pswrd :
#     user_input = input("Введите пароль: ")
# print(info)

# +++++++++++++++++++++++++++++++++++++++++++#

#6.2 Прерывание цикла, оператор break

# n=6
# total = 0
#
# while n :
# 	print("process n" , n)
# 	total += n
# 	n -= 1
#
# print("total: " , total)



# n=6
# total = 0
#
# while n :
# 	print("process n" , n)
# 	if n < 4 :
# 		break
# 	total += n
# 	n -= 1



# number = 123456
# nums_total = 0
#
# while number :
# 	remaider = number % 10
# 	nums_total += remaider
# 	number //= 10
# print("nums_total:", nums_total)
#
# print("total: " , total)



# number = 123456
# nums_total = 0
#
# while number :
# 	remaider = number % 10
# 	if remaider < 4 :
# 		break
# 	nums_total += remaider
# 	number //= 10
# print("Всего чисел:", nums_total)
# print("Сумма всех чисел: " , number)



# memory = None
#
# while True :
# 	command = input("Command:")
# 	if command == "r" :
# 		print("Memory:", memory)
# 	elif command == "w" :
# 		memory = input("Remember:")
# 	elif command == "q" :
# 		print("Bye!")
# 		break
# 	else:
# 		print("Know commands : r , w , q")

# +++++++++++++++++++++++++++++++++++++++++++#

#6.5 Практическая работа

# counter = 0
#
# while counter < 10 :
# 	counter += 1
# 	if counter %3 != 0 :
# 		squared = counter * counter
# 		print(counter , squared)
#
#
#
# counter = 0
#
# while counter < 10 :
# 	counter += 1
# 	if counter %3 == 0 :
# 		print("skip" , counter)
# 		continue
# 	squared = counter * counter
# 	print(counter , squared)
#
#
#
# counter = 0
#
# while True < 10 :
# 	counter += 1
# 	if counter > 10 :
# 		break
# 	if counter %3 == 0 :
# 		print("skip" , counter)
# 		continue
# 	squared = counter * counter
# 	print(counter , squared)

# +++++++++++++++++++++++++++++++++++++++++++#

#7.2 Цикл for. Работа со списком чисел
# number = 0
#
# while number <= 10 :
#     print(number ** 2)
#     number += 1

# for number in  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 :
#     print(number**2)

# winners = 0
#
# for ticket in 345, 19, 87, 1020, 431 :
#     if ticket %5 == 0 :
#         print(ticket, "- Lucky ticket!")
#         winners += 1
# print("Total winners:", winners)

# +++++++++++++++++++++++++++++++++++++++++++#

#7.3 Функция range

# text = "hello"
# for word_count in range(5) :
# 	print(text)

# for number in range(10) :
# 	print(number ** 2)



# ttl_mounts = int(input("Период накопления?: "))
# summ = 0
#
# for month in range(ttl_mounts):
# 	print("Месяц", month)
# 	money = int(input("Какой взнос? "))
# 	summ += money
# print("За" , ttl_mounts , "месяцев накопленно" , summ , "долларов")

# +++++++++++++++++++++++++++++++++++++++++++#

#7.4 Функция range с началом отсчёта

# begin_number = int(input("Первое число :"))
# end_number = int(input("Второе число"))
#
# for number in range(begin_number , end_number + 1) :
# 	print(number ** 2)


# wake_up = int(input("Время пробуждения? :"))
# awake_hours = 0
# calories_sum = 0
#
# for hour in range(wake_up , 23) :
# 	print("Сейчас", hour , "часов")
# 	calories = int(input("Колличество съеденных каллорий?:"))
# 	calories_sum += calories
# 	if calories_sum > 2000 :
# 		print("Хорошо поел , можно и  поспать.")
# 		break
# 	awake_hours += 1
# print("Съеденно каллорий за день:" , calories_sum)
# print("Часов не спал:", awake_hours)
