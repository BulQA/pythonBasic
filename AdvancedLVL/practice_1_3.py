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

#+++++++++++++++++++++++++++++++++++++++++++#

# int
# float
# str  # Неизменяемые(immutable) типы данных
# tuple
# bool
#
# list
# dict  # Изменяемые(mutable) типы данных
# set

#8.6 Именованные аргументы и значения по умолчанию

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

#8.7 Аргументы args и kwargs

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

#+++++++++++++++++++++++++++++++++++++++++++#

# real_path = os.path.join('docs', folder_name, file_name)
# print(real_path)

#+++++++++++++++++++++++++++++++++++++++++++#

# abs_path = os.path.abspath(file_name)
# print(abs_path)

#+++++++++++++++++++++++++++++++++++++++++++#

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

#9.2 Модуль os проверки

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

#+++++++++++++++++++++++++++++++++++++++++++#

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

#9.3 Базовые операции с файлами open, close, read

# speaker_file = open('speaker_file.txt', 'r', encoding='utf-8')

#+++++++++++++++++++++++++++++++++++++++++++#

# data = speaker_file.read()
# print(data)

#+++++++++++++++++++++++++++++++++++++++++++#
# for i_line in speaker_file:
#     print(i_line, end='')
#
# speaker_file.close()

#9.4 Метод write. Режимы записи

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

#+++++++++++++++++++++++++++++++++++++++++++#

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

#9.5 Перемещение курсора в файле. Метод seek

# spkr_file = open('spkr_file.txt', 'r'б encoding='utf-8')
# data = spkr_file.raed(10)
# spkr_file.seek(0)
# data_2 = spkr_file.raed(15)
# print(data)
# print(data_2)
# spkr_file.close()









