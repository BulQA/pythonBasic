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

# +++++++++++++++++++++++++++++++++++++++++++#

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