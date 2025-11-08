#4.7 Практическая работа

# text = input('Введите текст: ')
# vowels = 'аоуэиыеёюяАОУЭИЫЕЁЮЯ'
#
# letters = [char.lower() for char in text if char.lower() in vowels]
#
# print('Список гласных букв:', letters)
# print('Длина списка:', len(letters))

# +++++++++++++++++++++++++++++++++++++++++++#

# N = int(input('Введите длину списка: '))
#
# result = [1 if i % 2 == 0 else i % 5 for i in range(N)]
#
# print('Результат:', result)

# +++++++++++++++++++++++++++++++++++++++++++#

# import random
#
# team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
# team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
#
# winners = []
#
# for i in range(20):
#     if team_1[i] > team_2[i]:
#         winners.append(team_1[i])
#     else:
#         winners.append(team_2[i])
#
# print("Первая команда:", team_1)
# print("Вторая команда:", team_2)
# print("Победители тура:", winners)

# +++++++++++++++++++++++++++++++++++++++++++#

# alphabet = 'abcdefg'
#
# print("1:", alphabet[:])       # копия строки
# print("2:", alphabet[::-1])    # в обратном порядке
# print("3:", alphabet[::2])     # каждый второй, начиная с первого
# print("4:", alphabet[1::2])    # каждый второй после первого
# print("5:", alphabet[:1])      # до второго элемента (не включая второй)
# print("6:", alphabet[-1:])     # последний элемент
# print("7:", alphabet[3:4])     # элементы с индексом 3 до 4 (не включая 4)
# print("8:", alphabet[-3:])     # последние три элемента
# print("9:", alphabet[3:5])     # индексы 3 и 4
# print("10:", alphabet[4:2:-1]) # предыдущий пункт, но наоборот

# +++++++++++++++++++++++++++++++++++++++++++#

# s = input("Введите строку: ")
#
# first = s.index('h')        # индекс первого h
# last = s.rindex('h')        # индекс последнего h
#
# middle_reversed = s[first+1:last][::-1]
# print("Развёрнутая последовательность между первым и последним h:", middle_reversed)

# +++++++++++++++++++++++++++++++++++++++++++#

# new_list = [[i + 1 + j * 4 for j in range(3)] for i in range(4)]
#
# print(new_list)

# +++++++++++++++++++++++++++++++++++++++++++#

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# answer = []
#
# for i in nice_list:
#     for j in i:
#         for k in j:
# 	        answer.append(k)
#
# print('Ответ:',answer )

# +++++++++++++++++++++++++++++++++++++++++++#

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# answer = [k for i in nice_list for j in i for k in j]
#
# print('Ответ:',answer)

# +++++++++++++++++++++++++++++++++++++++++++#

# alphabet = [
#     'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
#     'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
# ]
#
# message = input('Введите сообщение: ')
# shift = int(input('Введите сдвиг: '))
#
# result = ''
#
# for letters in message:
#     if letters in alphabet:
#         old_index = alphabet.index(letters)
#         new_index = (old_index + shift) % len(alphabet)
#         result += alphabet[new_index]
#     else:
#         result += letters  # пробелы, цифры и прочее оставляем как есть
#
# print('Зашифрованное сообщение:', result)

#5.2 Форматирование строк: format и f-strings

# name = input('Введите имя:')
# order_code = int(input('Введите код заказа:'))
#
# print('Здравствуйте, {n}! Ваш номер заказа: {o}. Приятного дня!'.format(
#         n = name,
#         o = order_code
#         ))

# +++++++++++++++++++++++++++++++++++++++++++#

# name = input('Введите имя: ')
# debt = input('Введите долг: ')
#
# print(f'{name}! {name}, привет! Как дела, {name}? Где мои {debt} рублей? {name}!')

#5.3 Методы строк: split и join

# user_words = []
#
# for i in range(3):
#     word = input(f'Введите слово №{i+1}: ').lower()
#     user_words.append(word)
#
# text = input('Введите строку из произведения: ').lower()
#
# words_in_text = text.split()
#
# for w in user_words:
#     count = words_in_text.count(w)
#     print(f'Слово "{w}" встречается {count} раз(а).')

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input('Введите текст: ')
#
# fixed_text = ' '.join(text.split())
#
# print('Исправленный текст:', fixed_text)

# +++++++++++++++++++++++++++++++++++++++++++#

# template = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
# people = input('Список людей через запятую: ').split(', ')
# ages_input = input('Возраст людей через пробел: ').split()
#
# ages = []
# for a in ages_input:
#     ages.append(int(a))
#
# # Индекс вручную
# i = 0
# for person in people:
#     age = ages[i]
#     print(template.format(name=person, age=age))
#     i += 1
#
# # Собираем итоговую строку
# result = []
# i = 0
# for person in people:
#     result.append(f'{person} {ages[i]}')
#     i += 1
#
# print('\nИменинники:', ', '.join(result))

#5.4 Методы строк: startswith, endswith, upper, lower

# alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
#
# text = input('Введите текст для шифрования: ').lower()
# k = int(input('Введите сдвиг (K): '))
#
# encrypted = []
#
# for ch in text:
#     if ch in alphabet:
#         i = alphabet.index(ch)
#         new_char = alphabet[(i + k) % len(alphabet)]
#         encrypted.append(new_char)
#     else:
#         encrypted.append(ch)
#
# print('Зашифрованный текст:', ''.join(encrypted))

# +++++++++++++++++++++++++++++++++++++++++++#

# path = input('Путь к файлу: ')
# disc = input('На каком диске должен лежать файл: ')
# ext = input('Требуемое расширение файла: ')
#
# if path.startswith(disc) and path.endswith(ext):
#     print('Путь корректен!')
# else:
#     print('Путь некорректен!')

# +++++++++++++++++++++++++++++++++++++++++++#

# up_ch = 0
# low_ch = 0
#
# text = input('Введите строку: ')
#
# for ch in text:
#     if ch.isalpha():
#         if ch.isupper():
#             up_ch += 1
#         else:
#             low_ch += 1
#
# if up_ch >= low_ch:
#     print(text.upper())
# else:
#     print(text.lower())

#5.7 Практическая работа

# menu = input('Доступное меню:')
#
# new_menu = ', '.join(menu.split(';'))
#
# print(new_menu)

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input('Введите строку: ')
#
# words = text.split()
#
# longest = ''
# for word in words:
#     clean_word = ''
#     for ch in word:
#         if ch.isalpha():
#             clean_word += ch
#     if len(clean_word) > len(longest):
#         longest = clean_word
#
# print(f'Самое длинное слово: «{longest}».')
# print(f'Длина этого слова: {len(longest)} символов.')

# +++++++++++++++++++++++++++++++++++++++++++#

# ban_list = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
#
# file_name = input('Название файла: ')
#
# if file_name[0] in ban_list:
#     print('Ошибка: название начинается с недопустимого символа.')
# elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
#     print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
# else:
#     print('Файл назван верно.')

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input('Введите строку: ')
#
# result = text.title()
#
# print('Результат:', result)

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input('Введите строку: ')
#
# words = text.split()
# capitalized_words = [word.capitalize() for word in words]
# result = ' '.join(capitalized_words)
#
# print('Результат:', result)
