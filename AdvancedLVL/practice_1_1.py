#2.1 Списки и их инициализация

# number_list = [1, 2, 3, 5, -1]
#
# for _ in range(5):
# 	new_num = int(input('Insert number:'))
# 	number_list.append(new_num)
#
# for number in number_list:
# 	print(number, '**2=', number ** 2)

# +++++++++++++++++++++++++++++++++++++++++++#

# book_id = [50, 34, -1, -1, 2, 23, -1]
# new_books_id = []
# returned = 0
#
# for _ in range(10):
# 	id = int(input('Insert book id:'))
# 	book_id.append(id)
#
# for id in book_id:
# 	if id == -1:
# 		returned += 1
# 	else:
# 		new_books_id.append(id)
#
# print('New list of books:', new_books_id)
# print('Returned books:', returned)

#2.2 Индексы. Работа с элементами списка

# scores = [8, 5, 10, 7, 6]
# print(scores)

# +++++++++++++++++++++++++++++++++++++++++++#

# new_scores = []
# for score in new_scores:
# 	if score == 5:
# 		score *= 3
# 	new_scores.append(score)
#
# print(new_scores)

#2.2 Индексы. Работа с элементами списка

# scores = [8, 5, 10, 7, 6]
# scores[1] *= 3
#
# print(scores)

# +++++++++++++++++++++++++++++++++++++++++++#

# x = scores[4]
# x += 10
#
# print(scores)

# +++++++++++++++++++++++++++++++++++++++++++#

# monsters_count = int(input('Total monsters:'))
# mage_index = int(input('Caster top:'))
#
# monsters_dmg = []
#
# for monster in range(monsters_count):
# 	print('DMG of', monster + 1 , 'monster:', end = ' ')
# 	dmg = int(input())
# 	monsters_dmg.append(dmg)
#
# for i in range(monsters_count):
# 	if monsters_dmg[i] < 100 and i != mage_index - 1:
# 		monsters_dmg[i] += monsters_dmg[mage_index - 1]
#
# print('Total DMG of monsters:', monsters_dmg)

#2.3 Списки работа со строками

# word = input("Insert you'r word:")
# replace_num = int(input("Number of change:"))
# replace_sym = input('Value:')
#
# new_word = ''
#
# count = 0
# for sym in word:
# 	count += 1
# 	if replace_num != count:
# 		new_word += sym
# 	else:
# 		new_word += replace_sym
#
# print(new_word)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = input("Insert you'r word:")
# replace_num = int(input("Number of change:"))
# replace_sym = input('Value:')
#
# sym_list = [word]
#
# for sym in word:
# 	sym_list.append(sym)
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#
# 	print(i, end = '')

# +++++++++++++++++++++++++++++++++++++++++++#

# word = input("Insert you'r word:")
# replace_num = int(input("Number of change:"))
# replace_sym = input('Value:')
#
# sym_list = list(word)
#
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#     print(i, end = '')

# +++++++++++++++++++++++++++++++++++++++++++#

# words_list = []
# counts = [0, 0, 0]
#
# for i in range(3):
# 	print('Insert', i + 1, 'words:', end = ' ')
# 	word = input()
# 	words_list.append(word)
#
# text = input('Word in text:')
# while text != "end":
# 	for index in range(3):
# 		if words_list[index] == text:
# 			counts[index] += 1
# 	text = input('Word in text:')
#
# print('\n Count words in text')
#
# for i in range(3):
# 	print(words_list[i], ':', counts[i])

# +++++++++++++++++++++++++++++++++++++++++++#

#2.4 Базовые возможности при работе со списками

# def length(player_list):
# 	players_count = 0
# 	for _ in player_list:
# 		players_count += 1
# 	return players_count
#
# scores = [8, 5, 10, 7, 6]
# scores[1] += length(scores)
# scores.append(0)
# scores[2] += length(scores)
#
# print(scores)

# +++++++++++++++++++++++++++++++++++++++++++#

# scores = [8, 5, 10, 7, 6]
# scores[1] += len(scores)
# scores.append(0)
# scores[2] += len(scores)
#
# print(scores)

#3.2 Работа со списками методы insert, remove, index

# langs = ['Python', 'Java', 'JS', 'SQL']
# new_langs = []
#
# for i_lang in range(2):
#     new_langs.append(langs[i_lang])
# new_langs.append('C++')
#
# for i_lang in range(2, len(langs)):
#     new_langs.append(langs[i_lang])
# print(new_langs)

# +++++++++++++++++++++++++++++++++++++++++++#

# lang = ['Python', 'Java', 'JS', 'SQL']
# lang.insert(2, 'C++')
#
# print(langs)

# +++++++++++++++++++++++++++++++++++++++++++#

# langs = ['Python', 'Java', 'JS', 'SQL']
# user_lang = input("Number a new Language:")
# i_lang = langs.index(user_lang)
#
# lang = ['Python', 'Java', 'JS', 'SQL']
# langs.insert(i_lang + 1, 'C++')
#
# print(langs)

# +++++++++++++++++++++++++++++++++++++++++++#

# def is_film_exist(movie, films_list):
#     for i_movie in films_list:
#         if i_movie == movie:
#             return True
#     return False
#
#
# films = [
#  'Титаник', 'Трансформеры', 'В поисках Немо'
# ]
#
# my_list = []
#
# while True:
#     print('\nYour TOP movies list:', my_list)
#     new_movie = input('Movie name: ')
#
#     if is_film_exist(new_movie, films):
#         print('Commands: add, delete, insert')
#         command = input('Choose a command: ')
#
#         if command == 'add':
#             my_list.append(new_movie)
#
#         if command == 'delete':
#             if is_film_exist(new_movie, my_list):
#                 my_list.remove(new_movie)
#             else:
#                 print('This movie is not in your TOP.')
#
#         if command == 'insert':
#             index = int(input('What position in TOP?: '))
#             my_list.insert(index - 1, new_movie)
#     else:
#         print('This movie does not exist on the site :(')

#3.3 Работа с несколькими списками. Методы extend и count

# my_list = ['a', 'b', 'c']
# your_list = ['d', 'e', 'f']
#
# #my_list.append(your_list)
#
# #for i_elem in your_list:
# #	my_list.append(i_elem)
#
# my_list.extend(your_list)
#
# my_list.extend('g')
#
# for i_elem in my_list:
# 	print(my_list)

# +++++++++++++++++++++++++++++++++++++++++++#

# pack = []
# decode = []
# bad_pacs = 0
#
# packs = int(input('Pack count:'))
#
# for i_pack_num in range(packs):
# 	print('\nNumber of pack', i_pack_num + 1)
# 	for i_bit in range(4):
# 		print(i_bit + 1, 'bit:', end = ' ')
# 		num = int(input())
# 		pack.append(num)
# 	if pack.count(-1) <= 1:
# 		decode.extend(pack)
# 	else:
# 		print('To much error in pack.')
# 		bad_pacs += 1
# 	pack = []
#
# 	print('\nMessage:', decode)
# 	print('Error count in messaage:', decode.count(-1))
# 	print('Loss pack count:', bad_pacs)

#3.4 Вложенные списки

# members = []
#
# n = int(input('Players count:'))
#
# for i_num in range(1, n + 1):
#   members.append(i_num)
#
# members = list(range(1, n + 1))

# +++++++++++++++++++++++++++++++++++++++++++#
# n = int(input('Players count:'))
# members = []
# num = 1
#
# for _ in range(n //3):
# 	members.append(list(range(num, num + 3)))
# 	num + 3
#
# print(members)

# +++++++++++++++++++++++++++++++++++++++++++#

# words_list = [[' ', 0], [ ' ', 0], [' ', 0]]
#
# for i_num in range(3):
# 	print('Input', i_num + 1, 'word:', end = ' ')
# 	word = input()
# 	words_list[i_num][0] = word
#
# text = input('Word in text:')
# while text != 'end':
# 	for index in range(3):
# 		if words_list[index][0] == text:
# 		    words_list[index][1] += 1
# 	text = input('Word of text:')
#
# print('\n Calculate wonrs in text...')
# for index in range(3):
# 	print(words_list[index][0], ':', words_list[index][1])

#4.2 List comprehensions

# squares = []
#
# for x in range(10):
# 	squares.append(x ** 2)
#
# print(squares)

# +++++++++++++++++++++++++++++++++++++++++++#

# squares = [x ** 2 for x in range(10)]
#
# print(squares)

# +++++++++++++++++++++++++++++++++++++++++++#

# def get_higher_price(percent, price):
#     return round(price * (1 + percent / 100), 2)
#
# price = [1.01, 92.43, 54.66, 2.55, 9.99]
#
# first_percent = int(input('First year tax (%): '))
# second_percent = int(input('Second year tax (%): '))
#
# prices_first = [get_higher_price(first_percent, i_price) for i_price in price]
# prices_second = [get_higher_price(second_percent, i_price) for i_price in prices_first]
#
# print('Original total:', round(sum(price), 2))
# print('After first year:', round(sum(prices_first), 2))
# print('After second year:', round(sum(prices_second), 2))


#4.3 List comprehensions с условиями. Модуль random

# squares = []
#
# for x in range(10):
# 	if x % 2 != 0:
# 		squares.append(x ** 2)
#
# print(squares)

# +++++++++++++++++++++++++++++++++++++++++++#

# squares_odds = [x ** 2 for x in range(10) if x %2 != 0]
#
# squares_cubes = [(x ** 2 if x %2 != 0 else x ** 3) for x in range(10) ]
#
# print(squares_odds)
# print(squares_cubes)

# +++++++++++++++++++++++++++++++++++++++++++#

# import random
#
# fst_squad = [random.randint(50, 80) for _ in range(10)]
# sec_squad = [random.randint(30, 60) for _ in range(10)]
# trd_squad = [('Die' if fst_squad[i_damage] + sec_squad[i_damage] > 100 else 'Alive') for i_damage in range(10)]
#
# print('First squad DMG:', fst_squad)
# print('First squad DMG:', sec_squad)
# print('Therd squad status:', trd_squad)

#4.4 Срезы списков

# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] == 0
#
# for i_elem in range(2, 8):
# 	print(new_nums[i_elem], end = ' ')
#
# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] == 0
#
# print(new_nums [2:8])
# print(new_nums [2:8:2])
# print(new_nums [::-1])

# +++++++++++++++++++++++++++++++++++++++++++#

# nums = [x for x in range(1, 101) if x % 10 == 0]
# nums[:3] = [1, 1, 1]

# +++++++++++++++++++++++++++++++++++++++++++#

# def is_palendrom(num_list):
# 	reverse_list = num_list[::-1]
# 	if num_list == reverse_list:
# 		return True
# 	else:
# 		return False
#
# nums = [1, 2, 3, 4, 5]
# answer = []
#
# for i_nums in range(0, len(nums)):
# 	if is_palendrom(nums[i_nums : len(nums)]):
# 		answer = nums[:i_nums]
# 		answer.reverse()
# 		break
#
# print("Yo'r list:", nums)
# print("Exist number's of polendrom:", len(answer))
# print("List of exist digits:", answer)

#4.5 Строки индексы и срезы

# word = 'Привет'
# result = []
#
# sym_lit = list(word)
#
# first_part = sym_lit[:len(sym_lit) // 2]
# first_part = first_part[::-1]
# print(first_part)
#
# sec_part = sym_lit[len(sym_lit) // 2:]
# sec_part = sec_part[::-1]
# print(sec_part)
#
# result.extended(first_part)
# result.extended(sec_part)
#
# print(result)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = 'Привет'
# result = []
#
# sym_lit = list(word)
#
# first_part = word[:len(sym_lit) // 2]
# first_part = first_part[::-1]
# print(first_part)
#
# sec_part = word[len(sym_lit) // 2:]
# sec_part = sec_part[::-1]
# print(sec_part)
#
# print(first_part + sec_part)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = 'Привет'
#
# first_part = word[:len(word) // 2]
# print(first_part[::-1])
#
# sec_part = word[len(word) // 2:]
# print(sec_part[::-1])
#
# print(first_part[::-1] + sec_part[::-1])

# +++++++++++++++++++++++++++++++++++++++++++#

# sqr = [x ** 2 for x in range(10)]
#
# sqr = [x ** 2 for x in range(10) if x % 2 == 0]
#
# sqr = [x ** 2 x % 2 == 0 else x ** 3
#                   for x in range(10)]

# +++++++++++++++++++++++++++++++++++++++++++#

# nums[:6]
# nums[6:]
# nums[::6]
# nums[::-1]

# +++++++++++++++++++++++++++++++++++++++++++#

# word = 'World'
#
# word[2] = '#' - ошибка
# sym = word[2]
# sym = word[1:5]