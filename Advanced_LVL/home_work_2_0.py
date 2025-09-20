# main_list = ['True', 'False', 'pop', 'remove', 'del']
# print(main_list)

# `````````````````Дз```````````````````````#

# prog_languages = ['JavaScript', 'Java', 'Python', 'C#', 'PHP', 'C++']
#
# for werbs in (prog_languages):
#     print(werbs)

# `````````````````Дз```````````````````````#

# digits = [7, -2, '13', '1', '-5', 4]
#
# count = 0
# for _ in digits: count += 1
#
# pairs = []
# for i in range(count): pairs.append([int(digits[i]), digits[i]])
#
# i = 0
# while i < count:
#     j = 0
#     while j < count - 1:
#         if pairs[j][0] < pairs[j + 1][0]: pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
#         j += 1
#     i += 1
#
# result = []
# for i in range(count): result.append(pairs[i][1])
#
# print(result)

# `````````````````Дз```````````````````````#

# test_string = 'the best and good'
# new_str = test_string.split(' and ')
# print(new_str)

# `````````````````Дз```````````````````````#

# simple = 'promo'
# add_lis = 'tion'
# new_str = []
#
# for letters in simple, add_lis:
#     new_str += letters
#
# print(new_str)

# `````````````````Дз```````````````````````#

# slice_string = ['pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwawmbbiiigevfrualbsgijbvskfskwczlbervxkmsgtxrfxswmxsibffvaqrabgwxwcqzcrjiedsizjauufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujgbisagzswdaeebwerdcluoqvgajabbelaadswzdebwgxvdfaugqjazlwvzejdgleszsrlqxnsrkbkqcvgwekwsqezll']
#
# print(slice_string[0][::87])

# `````````````````Дз```````````````````````#

# def selection_sort(my_list):
#     for i_mn in range(len(my_list)):
#         for curr in range(i_mn, len(my_list)):
#             if my_list[curr] < my_list[i_mn]:
#                 my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]
#
#nums = [4, 9, 7, 6, 3, 2]
#
# selection_sort(nums)
#
# print(nums)

# `````````````````Дз```````````````````````#

# nums = []
# reverse_list = []
# for i in range((len*(nums))-2, -1, -1):
# 	    reverse_list.append(nums[i])

# `````````````````Дз```````````````````````#

# def is_palendrom(num_list):
# 	reverse_list = []
# 	for i_num in range(len(num_list)- 1, -1, -1):
# 		reverse_list.append(num_list[i_num])
# 	if num_list == reverse_list:
# 		return True
# 	else:
# 		return False
#
# nums = [1, 2, 3, 4, 5]
# new_nums = []
# answer = []
#
# for i_nums in range(0, len(nums)):
# 	for j_elem in range(i_nums, len(nums)):
# 		new_nums.append(nums[j_elem])
# 	if is_palendrom(new_nums):
# 		for i_answer in range(0, i_nums):
# 			answer.append(nums[i_answer])
# 		answer.reverse()
# 		break
# 	new_nums = []
#
# print("Yo'r list:", nums)
# print("Exist number's of polendrom:", len(answer))
# print("List of exist digits:", answer)

# `````````````````Дз```````````````````````#

# my_lsit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output = [digit for digit in my_lsit]
#
# print(output)

# `````````````````Дз```````````````````````#

# my_lsit = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# output = [digit for each_list in my_lsit for digit in each_list]
#
# print(output)

# `````````````````Дз```````````````````````#

# def caesar_cipher(string, user_shift):
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     new_str = ''
#     for sym in string:
#         if sym == ' ':
#             new_str += ' '
#         elif sym in alphabet:
#             index = (alphabet.index(sym) + user_shift) % len(alphabet)
#             new_str += alphabet[index]
#         else:
#             new_str += sym  # чтобы сохранить знаки препинания и т.п.
#     return new_str
#
# input_str = input('Input string: ')
# shift = int(input('Input shift: '))
#
# output_str = caesar_cipher(input_str.lower(), shift)
# print('Your new string is:', output_str)

# `````````````````Дз```````````````````````#

# def is_poly(string):
# 	char_dict = {}
# 	for i_sym in string:
# 		char_dict[i_sym] = char_dict.get(i_sym, 0 + 1)
#
# 	count = 0
#
# 	for i_value in char_dict.values():
# 		if i_value % 2 != 0:
# 			count += 1
#
# 	return count <= 1
#
# my_string = input('Input yuor string:')
# if is_poly(my_string):
# 	print('Can make poly')
# else:
# 	print("Can't do a poly")

# `````````````````Дз```````````````````````#

# goods = {
# 	'Лaмпa': '12345',
# 	'Стол': '23456',
# 	'Диван': '34567',
# 	'Стул': '45678',
# }
#
# store = {
# 	'12345': [
#
# 		{'quantity': 27, 'price': 42},
# 	],
#
# 	'23456': [
#
# 		{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520},
# 	],
# 	'34567': [
#
# 		{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150},
# 	],
# 	'45678': [
#
# 	{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97},
# 	],
# }
#
# for i_title, i_code in goods.items():
# 	total_quantity = 0
# 	total_cost = 0
#
# 	for j_good in store[i_code]:
# 		total_quantity += j_good['quantity']
# 		total_cost += j_good['price'] * j_good['quantity']
# 	print('{title} - {quantity}, стоимость{cost}'.format(
# 		title = i_title,
# 		quantity = total_quantity,
# 		cost = total_cost
# 		))

# Результат работы программы.
#Лампа - 27т, стоимость 1134 руб
# Стол
# Диван
#54 шт, стоимость 27860 руб
#3 шт, стоимость 3550 руб
# Стул 105 шт, стоимость 10311 руб

#8.1 Разбор домашнего задания

# def shortest_seq_range(string, tuple_):
#     return min(len(string), len(tuple_))
#
# sym_str = 'abc'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = ((sym_str[i_elem], nums_tpl[i_elem])
#          for i_elem in range(shortest_seq_range(sym_str, nums_tpl)))
#
# pairs_list = list(pairs)
#
# for i_elem in pairs_list:
#     print(i_elem)
#
# print(pairs_list)

#10.1 Разбор домашнего задания

# import collections
# import zipfile
#
# def unzip(archive):
#     zfile = zipfile.ZipFile(archive, 'r')
#     zfile.extractall()  # распаковываем всё
#     zfile.close()
#
#
# def collect_stats(file_name):
#     result = {}
#
#     # если на входе .zip → распаковываем
#     if file_name.endswith('.zip'):
#         unzip(file_name)
#         file_name = file_name[:-3] + 'txt'   # заменяем расширение
#
#     with open(file_name, 'r', encoding='utf-8') as text_file:
#         for line in text_file:
#             for char in line:
#                 if char.isalpha():
#                     char = char.lower()  # нормализуем буквы
#                     result[char] = result.get(char, 0) + 1
#
#     return result
#
#
# def print_stats(stats):
#     print('+{:-^19}+'.format('+'))
#     print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
#     print('+{:-^19}+'.format('+'))
#     for char, count in stats.items():
#         print('|{: ^9}|{: ^9}|'.format(char, count))
#     print('+{:-^19}+'.format('+'))
#
#
# def sort_by_frequency(stats_dict):
#     # OrderedDict в порядке убывания
#     sorted_dict = collections.OrderedDict(
#         sorted(stats_dict.items(), key=lambda item: item[1], reverse=True)
#     )
#     return sorted_dict
#
#
# file_name = 'file_name.zip'   # или сразу .txt
# stats = collect_stats(file_name)
# stats = sort_by_frequency(stats)
# print_stats(stats)

#11.1 Разбор домашнего задания

# user_name = input('Ваше имя?: ')
# while True:
#     print('1 - для вступления в чат, 2 - для вступления в беседу')
#     response = input('Выберите 1 или 2: ')
#     if response == '1':
#         try:
#             with open('chat.txt', 'r') as file:
#                 messages = file.readlines()
#                 print(''.join(messages))
#         except FileNotFoundError:
#             print('Служебное сообщение: пока ничего нет')
#     elif response == '2':
#         new_message = input('Введите сообщение: ')
#         with open('chat.txt', 'a') as file:
#             file.write('{name}: {message}\n'.format(name=user_name, message=new_message))
#     else:
#         print('Неизвестная команда')

#2.1 Списки и из инициализация

# numbers = [3,7,5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#         print()

# `````````````````Дз```````````````````````#

# numbers = []
# for i in range(101):
#     numbers.append(i)
# print(numbers)

# `````````````````Дз```````````````````````#

# employees = []
#
# count = int(input('Кол-во сотрудников в офисе: '))
#
# for i in range(count):
#     emp_id = int(input('ID сотрудника: '))
#     employees.append(emp_id)
#
# search_id = int(input('Какой ID ищем? '))
#
# if search_id in employees:
#     print('Сотрудник на месте')
# else:
#     print('Сотрудник не работает!')
