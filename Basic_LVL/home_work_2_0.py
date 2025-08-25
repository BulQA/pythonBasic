# `````````````````Дз / gpt```````````````````````#
# N = 9  # Задайте значение N
# number = 1
# while number <= N:
#     cube = number ** 3
#     print(cube)
#     number += 1

# `````````````````Дз```````````````````````#
# number = 0
# while number >= 0 :
#     number += 1
#     cube = number ** 3
#     if number >= 9 :
#         break
#     print(cube)

# `````````````````Дз```````````````````````#
# name = input("Введите ваше имя :")
# debt = 13250
#
# print("Здравствуйте" , name , "Ваш долг составляет : " , debt)
#
#
# while debt > 0 :
#     deposit = int(input("Какую сумму желаете внести? :"))
#     debt -= deposit
#     if debt > 0 :
#         print("Оставшийся долг :", debt)
#     else :
#         print("Поздравляем" , name , "Ваш долг погашен , хорошего дня ! ")

# ````````````Дз на пополам с gpt````````````#
# number = int(input("Введите ваше число :"))
# ttl_digit = 0
#
# if number == 0:
#     ttl_digit = 1
# else:
#     while number > 0:
#         number //= 10
#         ttl_digit += 1
#
# print(ttl_digit)

# ````````````Дз на пополам с gpt````````````#
# number = int(input("Введите число: "))
#
# positive_numbers = 0
# negative_numbers = 0
#
# while number != 0:
#     if number > 0:
#         positive_numbers += 1
#     elif number < 0:
#         negative_numbers += 1
#
#     number = int(input("Введите число: "))
#
# print("Кол-во положительных чисел:", positive_numbers)
# print("Кол-во отрицательных чисел:", negative_numbers)

# ````````````Дз на пополам с gpt````````````#
# print("Начался восьмичасовой рабочий день.")
#
# work_hour = 1
# total_tasks = 0
# calls = 0
#
# while work_hour <= 8:
#     print(f"{work_hour}-й час")
#
#     tasks = int(input("Сколько задач решит Максим? "))
#     total_tasks += tasks
#
#     while True:
#         call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#         if call == 0 or call == 1:
#             break
#         else:
#             print("Ошибка ввода! Введите только 1 — да, 0 — нет.")
#
#     if call == 1:
#         calls += 1
#
#     work_hour += 1
#
# print("Рабочий день закончился. Всего выполнено задач:", total_tasks)
#
# if calls > 0:
#     print("Нужно зайти в магазин.")

# ````````````Дз на пополам с gpt````````````#
# deposit = 100000
# percent = 17
# expectations = 500000
#
# years = 0
#
# while deposit < expectations:
#     deposit += int(deposit * (percent / 100))
#     years += 1
#
# print("Вы накопите желаемую сумму через :", years, "лет")

# ````````````Дз на пополам с gpt````````````#
# attempt = 0
# digit = 6
#
# while True:
#     number = int(input("Введите ваше число :"))
#     attempt += 1
#
#     if number < digit:
#         print("Число меньше, чем нужно. Попробуйте ещё раз!")
#     elif number > digit:
#         print("Число больше, чем нужно. Попробуйте ещё раз!")
#     else:
#         print("Вы угадали! Число попыток:", attempt)
#         break

# `````````````````Дз```````````````````````#
# min = 1
# max = 100
#
# while True:
#     mid = (min + max) // 2
#
#     print("Твоё число равно, меньше или больше, чем число:", mid, "?")
#     answer = int(input("Введите одно из трёх чисел : 1 — равно, 2 — больше, 3 — меньше"))
#     if answer == 1:
#         print("Весёлая игра , давай ещё раз ?")
#         break
#     elif answer == 2:
#         min = mid + 1
#         print("Текущее число :", min)
#     else:
#         max = mid - 1
#         print("Текущее число :", max)

# `````````````````Дз```````````````````````#
# for meters in (100,90,95,87,102):
#  if meters % 3 == 0:
#    print(meters, 'Подходит')
#  else:
#    print(meters, 'Не подходит')

# `````````````````Дз```````````````````````#
# for number in (15, 258, 547, 220, 647, 330, 907, 256, 86, 23) :
#     if 99 < number < 1000 and number % 5 == 0 :
#         print(number , "выигрышный билет")

# `````````````````Дз```````````````````````#
# for square in range( 0 , 11) :
#     print(square ** 2)

# `````````````````Дз```````````````````````#
# time = int(input("Который час? "))
#
# for time in range( 0 , time) :
#     print("Ку-ку!")

# `````````````````Дз```````````````````````#
# for square in range (0 , 20) :
#     print(2 ** square)

# `````````````````Дз```````````````````````#
# for cube in range (1 , 11) :
#     print(cube ** 3)

# `````````````````Дз```````````````````````#
# num_1 = int(input("Введите первое число :"))
# num_2 = int(input("Введите второе число :"))
# sum = 0
#
# for nums in range (num_1 , num_2+1) :
#     sum += nums
#     print(sum)

# `````````````````Дз```````````````````````#
# result = 0
#
# for number in (-407, -312, -229, -201, 30, 253, 410, 483, 573, 943):
#     if number >= 0 and number % 2 == 0:
#         result += 1
# print("Результат :", result, "числа")

# `````````````````Дз```````````````````````#
# ttl_sum = 0
#
# for month in range(1, 13):
#     salary = int(input("Ваша заплата в этом месяце?: "))
#
#     ttl_sum += salary
#
# mid_salary = ttl_sum / 12
#
# print("Ваша средняя ЗП в этом году :", mid_salary)

# `````````````````Дз```````````````````````#
# n = int(input("Введите число для расчёта факториала: "))
#
# fctrl = 1
# for i in range(1, n + 1):
#     fctrl *= i
#
# print("Факториал числа", n, "равен:", fctrl)

# `````````````````Дз```````````````````````#
# exсellent = 0
# good = 0
# mid = 0
#
# for numbers in (3, 3, 4, 4, 4, 5, 5 , 5, 5, 5, 5) :
#     if numbers == 5 :
#         exсellent += 1 #Отличники
#     elif numbers == 4 :
#         good += 1 #Хорошисты
#     else :
#         mid += 1 #Троечники
#
# if   mid < exсellent > good :
#     print("Отличников больше")
# elif exсellent < good > mid :
#     print("Хорошистов больше")
# else :
#     print("Троечников больше")

# `````````````````Дз```````````````````````#
# first_num =  int(input("Введите первое число :"))
# second_num = int(input("Введите второе число :"))
# digit = 0
# mid = 0
#
# for nums in range (first_num , second_num + 1) :
#     if nums % 3 == 0 :
#         digit += nums
#         mid += 1
#
# if mid > 0:
#     result = digit / mid
#     print("Cреднее арифметическое всех чисел из диапазона равно :" , result)
# else:
#     print("В указанном диапазоне нет чисел, кратных 3.")

# `````````````````полностью от gpt ```````````````````````#
# for digit in range(10, 100):
#     x = digit // 10
#     y = digit % 10
#
#     if digit == 3 * (x * y):
#         print(digit)

# `````````````````полностью от gpt ```````````````````````#
# nums = int(input("Введите количество карточек: "))
#
# total_sum = nums * (nums + 1) // 2
# entered_sum = 0
#
# for card in range(nums - 1):
#     number = int(input("Введите номер оставшейся карточки: "))
#     entered_sum += number
#
# missing_card = total_sum - entered_sum
# print("Номер пропавшей карточки:", missing_card)

# `````````````````Дз```````````````````````#
# digit = int(input("Введите число :"))
#
# for cube in range(0, digit + 1, 2):
#     print(cube ** 2)

# `````````````````Дз```````````````````````#

# hour = int(input("Введите число часов :"))
# cells = 1
#
# for division in range(3, hour + 1, 3):
#     cells *= 2
#     print("Прошло часов:", division)
#     print("Количество клеток:", cells)
#     print("Осталось часов:", hour - division)
#     print()

# `````````````````Дз```````````````````````#

# n = digit = int(input("Введите число :"))
#
# for cube in range(1, n // 2 + n % 2 + 1):
#     result = cube * 2 - 1
#     print(result, "** 2 =", result ** 2)

# `````````````````Дз```````````````````````#

# nums = int(input("До какого числа вычеслить куб? :"))
#
# for cube in range(1, nums + 1, 2):
#     result = cube ** 3
#     print(cube, " ** 3 = ", result)

# `````````````````Дз```````````````````````#

# n = int(input("Введите число"))
# sum = 0
#
# for chair in range(1, n + 1, 5):
#     sum += chair
#     print("Номер стула:", chair)
#
# print("Сумма:", sum)

# `````````````````Дз```````````````````````#

# n = int(input("Введите кол-во секунд:"))
#
# for second in range(n, -1, -1):
#     print(second)
# print("Я иду искать!")

# `````````````````Дз```````````````````````#

# n = int(input("Введите кол-во секунд: "))
#
# start = n - n % 2
#
# for second in range(start, 0, -2):
#     print(second)

# `````````````````Дз```````````````````````#

# bag = 100
# monthly_consumption = 4
# months = bag // monthly_consumption
#
# for month in range(1, months + 1):
#     remaining = bag - monthly_consumption * month
#     print("Через", month, "мес.:", remaining, "кг гречки осталось")

# `````````````````Дз```````````````````````#

# debt = int(input("Введите количество должников: "))
# ttlDebt = 0
# for sum in range(0, debt + 1, 5):
#     print("Должник с номером", sum)
#     answer = int(input("Сколько должны?"))
#     ttlDebt += answer
# print("Общая сумма долга:", ttlDebt)

# `````````````````Дз```````````````````````#

# reverse_timer = int(input("Введите количество секунд: "))
#
# for timer in range(reverse_timer, -1, -1):
#     print("Осталось", timer, "секунд.")
#     answer = int(input("Прервать режим разогрева? 1 = Да, еда готова / 0 = Нет: "))
#
#     if answer == 1:
#         print("Ваша еда готова, можете забрать. Таймер был прерван на", timer, "секунде.")
#         break
#     elif timer == 0:
#         print("Ваша еда готова, осторожно горячo!")

# `````````````````Дз```````````````````````#

# num_1 = int(input("Введите первое число:"))
# num_2 = int(input("Введите второе число:"))
# num_3 = int(input("Введите делитель:"))
# ttlsum = 0
# ttldigit = 0
#
# for digit in range(num_1 , num_2 + 1):
#     if digit % num_3 == 0 :
#         ttlsum += digit
#         ttldigit += 1
#
# if ttldigit != 0:
#     resul = ttlsum / ttldigit
#     print("Среднее арифметическое:", resul)
# else:
#     print("Нет чисел, кратных", num_3, "в этом диапазоне.")

# `````````````````Дз```````````````````````#

# start = int(input("Введите начало отрезка: "))
# end = int(input("Введите конец отрезка: "))
# step = int(input("Введите шаг: "))
#
# if step >= 0:
#     print("Шаг должен быть отрицательным!")
# else:
#     for x in range(end, start - 1, step):
#         y = (x - 1) ** 2
#         print(f"В точке {x} функция равна {y}")

# `````````````````Дз```````````````````````#

# educational_grant = int(input("Введите стипендию: "))
# expenses = int(input("Введите расходы на проживание: "))
#
# total_money_needed = 0
#
# for month in range(1, 11):
#     if month > 1:
#         expenses *= 1.03,
#
#     shortage = expenses - educational_grant
#
#     total_money_needed += shortage
#
#     print(f"{month} месяц: расходы = {expenses:.2f}, нехватка = {shortage:.2f}")
#
# print(f"Итого нужно попросить у родителей: {total_money_needed:.2f} рублей")

# `````````````````Дз```````````````````````#

# N = int(input("Введите число N: "))
#
# total_sum = 0
#
# for n in range(N):
#     elem = (-1) ** n * (1 / 2) ** n
#     total_sum += elem
#     print(f"n = {n}, elem = {elem}")
#
# print(f"\nСумма {N} элементов последовательности: {total_sum}")

# `````````````````Дз```````````````````````#

# x = int(input("Введите количество мальчиков: "))
# y = int(input("Введите количество девочек: "))
#
# if (x - y > 1) or (y - x > 1):
#     print("Нет решения")
# else:
#     result = ""
#
#     if x >= y:
#         first = "B"
#         second = "G"
#     else:
#         first = "G"
#         second = "B"
#
#     for i in range(x + y):
#         if i % 2 == 0:
#             result += first
#         else:
#             result += second
#
#     print(result)

# `````````````````Дз```````````````````````#

# answer = 'Да, конечно, сделал'
# for i in range(10):
#     question = input("Выполнил ли задание, которое выдавал вчера ?")
#     if question == answer:
#         break

# `````````````````Дз```````````````````````#

# username = input("Как тебя звать?")
# print(f"{username} , купи слона!")
#
# for i in range(1000):
#     argument = input()
#     print(f"Все говорят, {argument} , а ты купи слона!")

# `````````````````Дз```````````````````````#

# text = input("введите текст :")
# frsSym = input("Введите первый искомый символ :")
# secSym = input("Введите второй искомый символ :")
# fscoun = 0
# sscount = 0
#
# for symbol in text:
#     if symbol == frsSym:
#         fscoun += 1
#     if symbol == secSym:
#         sscount += 1
#
# print(f"кол-во {frsSym} равно : {fscoun}")
# print(f"кол-во {secSym} равно : {sscount}")

# `````````````````Дз```````````````````````#

# text = input("Введите текст:")
#
# for symbol in text :
#     print(symbol * 3)

# `````````````````Дз```````````````````````#

# text = input("Введите текст:")
# litl_sym = 0
# hight_sym = 0
#
# for sym in text:
#     if sym == "Ы":
#         hight_sym += 1
#     if sym == "ы":
#         litl_sym += 1
#
# print(f"Больших букв Ы: {hight_sym}")
# print(f"Маленьких букв ы: {litl_sym}")