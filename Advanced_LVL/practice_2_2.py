# 8.4 Передача изменяемых и неизменяемых данных в функцию

# def try_to_change(some_list, num):
#     for i_index, i_val in enumerate(some_list):
#         some_list[i_index] += 10
#     num += 10
#
#
# my_list = [1, 2, 4, 3, 5]
# number = 75
#
# try_to_change(my_list, number)
# print(my_list, number)

# +++++++++++++++++++++++++++++++++++++++++++#

# int
# float
# str  # Неизменяемые(immutable) типы данных
# tuple
# bool
#
# list
# dict  # Изменяемые(mutable) типы данных
# set

# 8.6 Именованные аргументы и значения по умолчанию

# def ask_user(question,
#              complaint="Incorrect input",
#              retries=3):
#
#     while True:
#         answer = input(question).lower()
#         if answer == 'yes':
#             return 1
#         elif answer == 'no':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print("No retries left.")
#             break
#         print(complaint)
#         print("Retries left:", retries)
#
# ask_user("Are you sure? ", "Incorrect input, choice Yes or No")
# ask_user("Are you sure? ", retries=2)

# 8.7 Аргументы args и kwargs

# def print_tax_document(tax, *args, **kwargs):
#     price_sum = 0
#     for i_price in args:
#         price_sum += i_price * tax / 100
#     print('Total sum and tax:', price_sum)
#
#     for i_info, i_value in kwargs.items():
#         print(f'{i_info}: {i_value}')
#
# my_tax = int(input('Tax percent: '))
#
# print_tax_document(my_tax, 100, 200, 300, 400, 500, yer=1999, doc_type='report', id=147001)

# 9.1 Модуль os генерация путей и метод listdir

import os

# folder_name = 'project'
# file_name = 'file.txt'
#
# path = 'docs/{folder}/{file}'.format(
#     folder=folder_name,
#     file=file_name
# )
#
# print(path)

# +++++++++++++++++++++++++++++++++++++++++++#

# real_path = os.path.join('docs', folder_name, file_name)
# print(real_path)

# +++++++++++++++++++++++++++++++++++++++++++#

# abs_path = os.path.abspath(file_name)
# print(abs_path)

# +++++++++++++++++++++++++++++++++++++++++++#

# import os
#
# def print_dirs(project):
#     print('Содержимое директории:', project)
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print('  ', path)
#
#
# project_list = ['PythonBasic', 'Practice']
#
# for i_project in project_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     print_dirs(path_to_project)

# 9.2 Модуль os проверки

# import os
#
# def print_dirs(project):
#     print('Содержимое директории:', project)
#     if os.path.exist(project):
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print('  ', path)
#     else:
#         print('Каталог проекта отсутствует')
# project_list = ['PythonBasic'], ['Prod'], ['Practice']
#
# for i_project in project_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     print_dirs(path_to_project)

# +++++++++++++++++++++++++++++++++++++++++++#

# import os
#
# def find_file(cur_path, file_name):
#     print('Переходим', cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('   смотрим', path)
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):  # исправлено
#             print('Это директория')
#             result = find_file(path, file_name)
#             if result:  # если нашли, сразу возвращаем
#                 return result
#
#     return None  # если не нашли
#
#
# file_path = find_file(os.path.abspath(os.path.join('..', '..', 'System32')), "cmd.exe")
# if file_path:
#     print('Абсолютный путь к файлу:', file_path)
# else:
#     print("Файл не найден")
#
#     print('Файл не найден')

# 9.3 Базовые операции с файлами open, close, read

# speaker_file = open('speaker_file.txt', 'r', encoding='utf-8')

# +++++++++++++++++++++++++++++++++++++++++++#

# data = speaker_file.read()
# print(data)

# +++++++++++++++++++++++++++++++++++++++++++#
# for i_line in speaker_file:
#     print(i_line, end='')
#
# speaker_file.close()

# 9.4 Метод write. Режимы записи

# speaker_file = open('speaker_file.txt', 'r', encoding='utf-8')
#
# sym_count = []
#
# for i_line in speaker_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
#
# sym_count_str = '\n'.join(sym_count)
# speaker_file.close()
#
# counts_file = open('sym_count.txt', 'w')
# counts_file.write(sym_count_str)
# counts_file.close()

# +++++++++++++++++++++++++++++++++++++++++++#

# import os
#
# def find_file(cur_path, file_name):
#     print('Переходим в', cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('   смотрим', path)
#
#         if file_name == i_elem:
#             return path
#         elif os.path.isdir(path):
#             print('Это директория')
#             result = find_file(path, file_name)
#             if result:
#                 return result
#     return None
#
# start_path = os.path.abspath(os.path.join('.', 'Skillbox'))
# file_name = 'homework_1.py'
#
# file_path = find_file(start_path, file_name)
#
# # сохраняем результат в историю
# with open('search_history.txt', 'a', encoding='utf-8') as history_file:
#     if file_path:
#         print('Абсолютный путь к файлу:', file_path)
#         history_file.write(file_path + '\n')
#     else:
#         print('Файл не найден.')
#         history_file.write('Файл не найден.\n')

# 9.5 Перемещение курсора в файле. Метод seek

# spkr_file = open('spkr_file.txt', 'r'б encoding='utf-8')
# data = spkr_file.raed(10)
# spkr_file.seek(0)
# data_2 = spkr_file.raed(15)
# print(data)
# print(data_2)
# spkr_file.close()

# 10.2 Обработка исключений операторы try, except

# num_sum = 0
# num_count = 0
#
# try:
#     numbers_file = open('numbers_file.txt', 'r')
#     for i_line in numbers_file:
#         num_sum += 1
#         num_count += 1
#     numbers_file.close()
#     print('Среднее арифм.', num_sum / num_count)
# except FileNotFoundError:
#     print('Такого файла не существует.')
# except ValueError:
#     print('Нельзя преобразовать в целое число.')

# +++++++++++++++++++++++++++++++++++++++++++#

# def divide(number):
#     return 10 / number
#
#
# def sum_of_divided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print('Нельзя делить на ноль!')
#     return div_sum
#
#
# total = 0
#
# try:
#     numbers_file = open('numbers_file.txt', 'r')
#     for i_line in numbers_file:
#         nums_list = i_line.split()
#         first_num = int(nums_list[0])
#         second_num = int(nums_list[1])
#
#         total += sum_of_divided(first_num, second_num)
#     print('Общая сумма:', total)
#
# except ZeroDivisionError:
#     print('Нельзя делить на ноль!')

#10.3 Обработка исключений операторы else, finally

# def divide(number):
#     return 10 / number
#
#
# def sum_of_divided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print('На ноль делить нельзя!')
#     return div_sum
#
# total = 0
#
# try:
#     numbers_file = open('numbers.txt', 'r')
#     for i_line in numbers_file:
#         nums_list = i_line.split()
#         first_num = int(nums_list[0])
#         second_num = int(nums_list[1])
#         total += sum_of_divided(first_num, second_num)
#     print('Общая сумма:', total)
#
# except FileNotFoundError:
#     print('Файл numbers.txt не найден.')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#
#
# answer_file = open('answer.txt', 'w')
# try:
#     answer_file.write('The answer is: ')
#     answer_file.write(str(total))
# except TypeError:
#     print('Ошибка записи в файл: тип данных не строка.')
# else:
#     print('Программа выполнилась без ошибок.')
# finally:
#     answer_file.close()
#     print(answer_file.closed)

#10.4 Вызов исключений оператор raise

# sym_sum = 0
# line_count = 0
#
# try:
#     people_file = open('people_file.txt', 'r')
#     for i_line in people_file:
#         lenght = len(i_line)
#         line_count += 1
#         if i_line.endswith('\n'):
#             lenght -= 1
#         if lenght < 5:
#             raise BaseException('Длина {} строки меньше 5 символов.'.format(line_count))
#         sym_sum += lenght
#     people_file.close()
#
# except FileNotFoundError:
#     print('Файл не найден.')
# finally:
#     print('Найденная сумма символов:', sym_sum)

# +++++++++++++++++++++++++++++++++++++++++++#

# names_list = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if name.lower() == 'error':
#             raise BaseException('Ты сломал программу!')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print('Место закончилось')
#             break
#     except TypeError:
#         print('Ты чего ввёл?')
#     except BaseException:
#         names_list = []
#         print('Введено стоп-слово.')
#         raise ValueError('Пожалуйста, не вводите error')
#
# names_file = open('names.txt', 'w')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print('Программа закончена, запись завершена')

#10.5 Context manager оператор with

# line_count = 0
# sym_sum = 0
#
# try:
# 	with open('people.txt', 'r') as people_file:
# 	    for i_line in people_file:
# 	        line_count += 1
# 	        length = len(i_line)
# 	        if i_line.endswith('\n'):
# 	            length -= 1
# 	        if length < 3:
# 	            raise BaseException(f'Длина {line_count} строки меньше 3 символов.')
# 	        sym_sum += len(i_line)
# 	    people_file.close()
#
# except FileNotFoundError:
#     print('Файл не найден.')
# finally:
# 	print('Найденная сумма символов:', sym_sum)
# 	print(people_file.closed)
#
# try:
# 	num = int(input())
# except TypeError:
# 	print('Это не число.')
#
# else: # оператор запускает в случае успешной работы кода
# 	print('Код успешно отработал.')
# finally: # выполняет код в любом случае, а так же выполняет подчистку данных
# 	file.close()
#
# # если нужно вызвать исключение в ручную или для проброса исключений
# raise TypeError('Неверный тип данных.')
#
# # контекстный менеджер, автоматически закрывает файлы даже при сбое
# with open('text.txt', 'r') as text_file

