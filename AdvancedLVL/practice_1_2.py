#5.2 Форматирование строк format и f-strings

# user_name = input('Input user name:')
# file_name = input('Input file name:')
#
# path = 'C:/{user}/docs/folder/{new file}.txt'.format(
#         user=user_name,
#         new_file=file_name
# )
#
# path_1 = 'C:/{0}/docs/folder/{1}.txt'.format(
#         user_name,
#             file_name
# )
#
# print('File path:', path, path_1)

# +++++++++++++++++++++++++++++++++++++++++++#

# while True:
#     gartes_template = input('Input your template like "Hello {name}": ')
#
#     if "{name}" in gartes_template:
#         break
#     print('Error: you must include "{name}" in the template.')
#
# print('Input names, list ends with "end"')
# names_list = []
#
# while True:
#     name = input('Name: ')
#     if name.lower() == 'end':
#         break
#     names_list.append(name)
#
# for i_name in names_list:
#     print(gartes_template.format(name=i_name))


#5.3 Методы строк split и join

# words_list = []
#
# while True:
#     word = input('Input word:')
#     if word != 'end':
#         words_list.append(word)
#     else:
#         break
#
# print(words_list)

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input('Input yor text:')
# word_list = text.split()
#
# print(word_list)
#
# new_text = ''
#
# for word in word_list:
#     new_text += '---' + word
#
# print(new_text[3:])

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input('Input yor text:')
# word_list = text.split()
#
# print(word_list)
#
# new_text = '---'.join(word_list)
#
# print(new_text)

# +++++++++++++++++++++++++++++++++++++++++++#

# while True:
#     grats_template = input('Input your template like "Hello {name} and {age}": ')
#     if "{name}" in grats_template and "{age}" in grats_template:
#         break
#     print('Error: you must include "{name}" and "{age}" in the template.')
#
# names_list = input('Names list separated by ", ": ').split(', ')
# ages_str = input("Ages list separated by spaces: ")
# ages = [int(i_number) for i_number in ages_str.split()]
#
# if len(names_list) != len(ages):
#     print("Error: count of names and ages must match!")
#     exit()
#
# people = [
#     grats_template.format(name=names_list[i], age=ages[i])
#     for i in range(len(names_list))
# ]
#
# people_str = '\n'.join(people)
# print('\nGrats:\n', people_str)

#5.4 Методы строк startswith, endswith, upper, lower

# user_name = input('')
# file_name = input('')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user = user_name,
#     new_file = file_name
# )
#
# if path[-4:] == '.txt':
#         print('Path:', path)
# else:
#     print('Ivalid file format')
#
# if not path.endswit('.txt'):
#     print('Ivalid file format')
# elif not path.startswith('C:/'):
#     print('Disc path error')
# else:
#     print('Path:', path)

# +++++++++++++++++++++++++++++++++++++++++++#

# word_list = []
#
# for i_num in range(3):
#     print('input', i_num+1, 'word', end = ' ')
#     word = input().lower()
#     word = input().upper()
#     word_list.append(word)
#
# text = input('Input text:').lower().split()
#
# print('\nWords Count in text')
# for index in range(3):
#     print(word_list[index]), ':', text.count(word_list[index])

#5.5 Форматирование строк подстановки

# details_num = 500000000
# price = 23.8589578
# increase = 0.045678
#
# print('На складе {:,d} деталей'.format(details_num))
# print('Каждая деталь стоит {:.2f} рублей').format(price)
# print('Цена увеличилась на {:.1%}').format(increase)
# print('На складе {:.0e} деталей'.format(details_num))

#6.1 Словарь основы

# phonebook_lsit = [
# ['Саша', +905103722715],
# ['Маша', +905103722715],
# ['Ваня', +905103722715]
# ]
#
# name = input('Input name:')
#
# is_exist = False
#
# for i_person in phonebook_lsit:
#     if i_person[0] == name:
#         is_exist = True
#         print(i_person[1])
#         break
# if not is_exist:
#     print('Error: {} not found').format(name)

# +++++++++++++++++++++++++++++++++++++++++++#

# phonebook_dict = {
#     'Саша' : +905103722715,
#     'Маша' : +905103722716,
#     'Ваня' : +905103722717
# }
#
# name = input('Input name:')
#
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#      print('Error: {} not found').format(name)

# +++++++++++++++++++++++++++++++++++++++++++#

# student_str = input('Введите информацию (имя, фамилия, город, оценки через запятую):\n')
#
# student_info = [item.strip() for item in student_str.split(',')]
#
# student = dict()
# student['имя'] = student_info[0]
# student['фамилия'] = student_info[1]
# student['город'] = student_info[2]
# student['оценки'] = [int(grade) for grade in student_info[3:]]
#
# for key, value in student.items():
#     print(f'{key} - {value}')


#6.2 Методы словарей

# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] += 1
#     return sym_dict
#
# text = input('input text:').lower()
# hist = histogram(text)
#
# for i_sym in sorted(hist.keys()):
#     print(i_sym, ':', hist[i_sym])
#
# print('Maximum freq:', max(hist.value()))

#+++++++++++++++++++++++++++++++++++++++++++#

# phonebook = {
#     'Даша' : 123,
#     'Ваня' : 456,
#     'Миша' : 789
# }
#
# other_phonebook = {
#     'Лера' : 987 ,
#     'Миша' : 654,
#     'Сергей' : 321
# }
#
# phonebook.update(other_phonebook)
# phonebook.pop('Сергей')
# phonebook['Саша'] = phonebook.pop('Лера')
# print(phonebook)
#
# hist = {'a' : 1, 'b' : 2}
# hist.keys() # Выводит ключи
# hist.values # Выводит значение
# hist.update(other_hist) # Обновляет словарь из другого словаря
# hist['c'] = hist.pop('b') # Заменяет один ключ на дуказанный
# hist.get() #Возвращает None при отсутствуещем значении

#6.3 Вложенные словари и значения по умолчанию в get

# data = dict()
# data['server'] = {
# 	'host' : '127.0.0.1',
# 	'port' : '89'
# }
#
# data['cfg'] = {
# 	'ssh' : {
# 		'acecess' : 'true',
# 		'login' : 'Vasiliy',
# 		'password' : 12345
# 	}
# }
#
# print(data['server']['port'])
# data['cfg']['ssh']['login'] = 'Vladimir'
#
# for i_values in data.values():
# 	for j_key in i_values:
# 		print(j_key, i_values[j_key])

#+++++++++++++++++++++++++++++++++++++++++++#

# players_dict = {
# 	1:{'name' : 'Masha', 'team' : 'C', 'status' : 'rest'},
# 	2:{'name' : 'Alina', 'team' : 'B', 'status' : 'training'},
# 	3:{'name' : 'Sasha', 'team' : 'A', 'status' : 'travel'},
# 	4:{'name' : 'Andrei', 'team' : 'A', 'status' : 'rest'},
# 	5:{'name' : 'Egor', 'team' : 'C', 'status' : 'training'},
# 	6:{'name' : 'Max', 'team' : 'C', 'status' : 'rest'},
# 	7:{'name' : 'Lena', 'team' : 'B', 'status' : 'rest'},
# 	8:{'name' : 'Petya', 'team' : 'A', 'status' : 'travel'}
# }
#
# team_a_members = [
# 	player['name']
# 	for player in players_dict.value
# 		if player['team'] == 'A' and player['status'] == 'rest'
# ]
# print(teaam_a_members)

#6.4 Множества. Функция set

# import random
#
# numer_list = [random.randint(1, 4) for _ in range(10)]
# new_list = []
#
# for i_num in numer_list:
# 	if i_num not in new_list:
# 		new_list.append(i_num)
#
# print(numer_list)
# print(new_list)
#
# unique = set(numer_list)
# print(unique)

#+++++++++++++++++++++++++++++++++++++++++++#

# nums_1 = {1, 2, 3, 4, 5}
# nums_2 = {6, 7, 8, 3, 1}
#
# nums_1.intersection(nums_2) #'&' пересечение
#
# nums_1.union(nums_2) #'|' объеденение
#
# nums_1.difference(nums_2) #'-' разность

#6.5 Генерация словарей

# data = [
# {'id' :1, 'user' : 'Эля'},
# {'id' :2, 'user' : 'Миша'},
# {'id' :3, 'user' : 'Эля'},
# {'id' :3, 'user' : 'Саша'}
# ]
#
# unique_data = []
#
# for i_dict in data:
# 	data_exist = False
# 	for uniq_dict in unique_data:
# 		if uniq_dict['id'] == i_dict['id']:
# 			data_exist = True
# 			break
# 	if not data_exist:
# 		unique_data.append(i_dict)
#
# print(unique_data, '\n')
#
# unique_data_dict = {i_dict['id']: i_dict for i_dict in data}
# print(unique_data_dict.values())

#+++++++++++++++++++++++++++++++++++++++++++#

# hist = dict
# hist =['a'] = 10
# hist.keys()
# hist.values()
# hist.update(new_hist)
# hist.pop('a')
# hist.get('a')
# hist.get('a', 0)
#
# nums = [1, 2, 4, 3, 3, 5]
# new_nums = set(nums)
#
# {i_dict['id']: for i_dict in data}

#7.2 Кортежи

# def add_num(seq, number):
# 	seq = list(seq)
# 	for i_num in range(len(seq)):
# 		seq[i_num] += number
# 	return seq
#
# origin_tuple = (1, 2, 3, 3, 5)
# changed_list = add_num(origin_tuple, 5)
#
# print(origin_tuple)
# print(changed_list)

#+++++++++++++++++++++++++++++++++++++++++++#

# user = 'Vova', 'Petrov', 25
# name, surname, age = user
#
# print(user)
# print(name, surname, age)






