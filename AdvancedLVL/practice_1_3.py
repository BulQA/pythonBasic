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