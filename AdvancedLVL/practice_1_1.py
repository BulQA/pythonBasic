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