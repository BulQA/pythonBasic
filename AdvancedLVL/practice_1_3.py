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
