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

# +++++++++++++++++++++++++++++++++++++++++++#

# scores = [8, 5, 10, 7, 6]
# scores[1] *= 3

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