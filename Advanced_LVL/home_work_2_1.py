# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня'
# ]
#
# favorite = []
#
# while True:
#     film = input('Введите название фильма (или "exit" для выхода): ')
#     if film.lower() == 'exit':
#         break
#
#     if film in films:
#         favorite.append(film)
#         print(f'Фильм "{film}" добавлен в избранное!')
#     else:
#         print(f'Ошибка: фильма "{film}" у нас нет :(')
#
# print('Ваш список избранного:', favorite)

# `````````````````Дз```````````````````````#

# n = int(input('Количество контейнеров: '))
#
# weights = []
# for i in range(n):
#     w = int(input('Введите вес контейнера: '))
#     # Контроль ввода: натуральные числа ≤ 200
#     while w <= 0 or w > 200:
#         w = int(input('Вес должен быть от 1 до 200. Повторите ввод: '))
#     weights.append(w)
#
# new_w = int(input('Введите вес нового контейнера: '))
# while new_w <= 0 or new_w > 200:
#     new_w = int(input('Вес должен быть от 1 до 200. Повторите ввод: '))
#
# pos = 0
# while pos < len(weights) and new_w <= weights[pos]:
#     pos += 1
#
# print('Номер, который получит новый контейнер:', pos + 1)

# `````````````````Дз```````````````````````#

# k = int(input('Сдвиг: '))
# n = int(input('Количество элементов: '))
# nums = []
# for i in range(n):
#     nums.append(int(input(f'Элемент {i + 1}: ')))
#
# if n > 0:
#     k %= n
#     nums[:] = nums[-k:] + nums[:-k]
#
# print('Сдвинутый список:', nums)

# `````````````````Дз```````````````````````#

# word = input('Введите слово: ')
#
# if word == word[::-1]:
#     print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом')

# `````````````````Дз```````````````````````#

# n = int(input('Количество чисел: '))
# nums = []
# for k in range(n):
#     nums.append(int(input(f'Число {k + 1}: ')))
#
# print('Изначальный список:', nums)
#
# for i in range(len(nums)):
#     min_index = i
#     for j in range(i + 1, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#
#     nums[i], nums[min_index] = nums[min_index], nums[i]
#
# print('Отсортированный список:', nums)

# `````````````````Дз```````````````````````#

# numbers = []
# for x in input('Введите число:').split():
#     numbers.append(int(x))
#
# for digit in range(len(numbers) - 1, -1, -1):
#     if numbers[digit] % 2 == 0:
#         print(numbers[digit], end=" ")

#2.6 Практическая работа (автотесты)

# digits = []
# n = int(input("Введите число N: "))
#
# for digit in range(1, n + 1):
#         digits.append(digit)
#
# print("Список из нечётных чисел от 1 до N:", digits)

#3.3 Работа с несколькими списками. Методы extend и count

# first = input("Первое сообщение: ")
# second = input("Второе сообщение: ")
#
# count_first = first.count("!") + first.count("?")
# count_second = second.count("!") + second.count("?")
#
# # Логика вывода
# if count_first > count_second:
#     print("Третье сообщение:", first + second)
# elif count_second > count_first:
#     print("Третье сообщение:", second + first)
# else:
#     print("Ой")

# `````````````````Дз```````````````````````#

# decoded_message = []
# total_errors = 0
# dropped_packets = 0
#
# count = int(input("Кол-во пакетов: "))
#
# for i in range(1, count + 1):
#     print(f"\nПакет номер {i}")
#     packet = []
#     errors_in_packet = 0
#
#
#     for j in range(1, 5):
#         bit = int(input(f"{j} бит: "))
#         packet.append(bit)
#         if bit == -1:
#             errors_in_packet += 1
#
#     if errors_in_packet <= 1:
#         decoded_message.extend(packet)
#         total_errors += errors_in_packet
#     else:
#         print("Много ошибок в пакете.")
#         dropped_packets += 1
#
# print("\nИтоговое сообщение для декодирования:", decoded_message)
# print("Количество ошибок:", total_errors)
# print("Необработанных пакетов:", dropped_packets)

#3.4 Вложенные списки

# matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
#
# for row in matrix:
#     for item in row:
#         print(item, end=' ')
#     print()

# `````````````````Дз```````````````````````#

# teams = []
#
# n = int(input('Кол-во участников:'))
# k = int(input('Кол-во человек в команде:'))
#
# if n % k == 0:
#     print('Кол-во человек в команде: ', n / k)
# else:
#     teams = []
#     for i in range(0, n, k):
#         team = []
#         for j in range(k):
#             team.append(i + j + 1)
#         teams.append(team)
#
#     print("Общий список команд:", teams)

# `````````````````Дз```````````````````````#

# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# fruit_name = input("Новый фрукт: ")
# price = float(input("Цена: "))
#
# goods.append([fruit_name, price])
# print("Новый ассортимент:", goods)
#
# for item in goods:
#     item[1] *= 1.08
#
# print("Новый ассортимент с увел. ценой:", goods)

#3.5 Практическая работа

# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
#
# for i_elem in b:
#     a.append(i_elem)
#
# count_5 = a.count(5)
#
# while 5 in a:
#     a.remove(5)
#
# for j_elem in c:
#     a.append(j_elem)
#
# count_3 = a.count(3)
#
# print(f'Количество цифр 5 при первом объединении: {count_5}')
# print(f'Количество цифр 3 при втором объединении: {count_3}')
# print('Итоговый список:', a)

# `````````````````Дз```````````````````````#

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
#
# def merge_sorted_lists(list1, list2):
#     merged = sorted(set(list1 + list2))
#     return merged
#
# merged = merge_sorted_lists(list1, list2)
# print(merged)

# `````````````````Дз```````````````````````#

# shop = [
#     ['каретка', 1200], ['шатун', 1000], ['седло', 300],
#     ['педаль', 100], ['седло', 1500], ['рама', 12000],
#     ['обод', 2000], ['шатун', 200], ['седло', 2700]
# ]
#
# detail = input('Название детали: ')
# quantity = int(input('Количество деталей: '))
#
# total_price = 0
#
# for item, price in shop:
#     if item == detail:
#         total_price += price * quantity
#
#     print(f'Общая стоимость: {total_price}')
# else:
#     print('Такой детали нет в магазине.')

# `````````````````Дз```````````````````````#

# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
#
# while True:
#     print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
#     action = input('Гость пришёл или ушёл? ')
#
#     if action == 'Пора спать':
#         print('Вечеринка закончилась, все легли спать.')
#         break
#
#     elif action == 'пришёл':
#         name = input('Имя гостя: ')
#         if len(guests) < 6:
#             guests.append(name)
#             print(f'Привет, {name}!')
#         else:
#             print(f'Прости, {name}, но мест нет.')
#
#     elif action == 'ушёл':
#         name = input('Имя гостя: ')
#         if name in guests:
#             guests.remove(name)
#             print(f'Пока, {name}!')
#         else:
#             print(f'{name} не был на вечеринке.')
#
#     else:
#         print('Некорректный ввод. Введите "пришёл", "ушёл" или "Пора спать".')