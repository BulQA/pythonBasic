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