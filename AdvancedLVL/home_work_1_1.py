# main_list = ['True', 'False', 'pop', 'remove', 'del']
# print(main_list)

# `````````````````Дз```````````````````````#

# prog_languages = ['JavaScript', 'Java', 'Python', 'C#', 'PHP', 'C++']
#
# for werbs in (prog_languages):
#     print(werbs)

# `````````````````Дз```````````````````````#

# digits = [7, -2, '13', '1', '-5', 4]
#
# count = 0
# for _ in digits: count += 1
#
# pairs = []
# for i in range(count): pairs.append([int(digits[i]), digits[i]])
#
# i = 0
# while i < count:
#     j = 0
#     while j < count - 1:
#         if pairs[j][0] < pairs[j + 1][0]: pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
#         j += 1
#     i += 1
#
# result = []
# for i in range(count): result.append(pairs[i][1])
#
# print(result)

# `````````````````Дз```````````````````````#

# test_string = 'the best and good'
# new_str = test_string.split(' and ')
# print(new_str)

# `````````````````Дз```````````````````````#

# simple = 'promo'
# add_lis = 'tion'
# new_str = []
#
# for letters in simple, add_lis:
#     new_str += letters
#
# print(new_str)

# `````````````````Дз```````````````````````#

# slice_string = ['pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwawmbbiiigevfrualbsgijbvskfskwczlbervxkmsgtxrfxswmxsibffvaqrabgwxwcqzcrjiedsizjauufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujgbisagzswdaeebwerdcluoqvgajabbelaadswzdebwgxvdfaugqjazlwvzejdgleszsrlqxnsrkbkqcvgwekwsqezll']
#
# print(slice_string[0][::87])

# `````````````````Дз```````````````````````#

# def selection_sort(my_list):
#     for i_mn in range(len(my_list)):
#         for curr in range(i_mn, len(my_list)):
#             if my_list[curr] < my_list[i_mn]:
#                 my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]
#
#nums = [4, 9, 7, 6, 3, 2]
#
# selection_sort(nums)
#
# print(nums)

# `````````````````Дз```````````````````````#

# nums = []
# reverse_list = []
# for i in range((len*(nums))-2, -1, -1):
# 	    reverse_list.append(nums[i])

# `````````````````Дз```````````````````````#

# def is_palendrom(num_list):
# 	reverse_list = []
# 	for i_num in range(len(num_list)- 1, -1, -1):
# 		reverse_list.append(num_list[i_num])
# 	if num_list == reverse_list:
# 		return True
# 	else:
# 		return False
#
# nums = [1, 2, 3, 4, 5]
# new_nums = []
# answer = []
#
# for i_nums in range(0, len(nums)):
# 	for j_elem in range(i_nums, len(nums)):
# 		new_nums.append(nums[j_elem])
# 	if is_palendrom(new_nums):
# 		for i_answer in range(0, i_nums):
# 			answer.append(nums[i_answer])
# 		answer.reverse()
# 		break
# 	new_nums = []
#
# print("Yo'r list:", nums)
# print("Exist number's of polendrom:", len(answer))
# print("List of exist digits:", answer)

# `````````````````Дз```````````````````````#

# my_lsit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output = [digit for digit in my_lsit]
#
# print(output)

# `````````````````Дз```````````````````````#

# my_lsit = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# output = [digit for each_list in my_lsit for digit in each_list]
#
# print(output)

# `````````````````Дз```````````````````````#

# def caesar_cipher(string, user_shift):
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     new_str = ''
#     for sym in string:
#         if sym == ' ':
#             new_str += ' '
#         elif sym in alphabet:
#             index = (alphabet.index(sym) + user_shift) % len(alphabet)
#             new_str += alphabet[index]
#         else:
#             new_str += sym  # чтобы сохранить знаки препинания и т.п.
#     return new_str
#
# input_str = input('Input string: ')
# shift = int(input('Input shift: '))
#
# output_str = caesar_cipher(input_str.lower(), shift)
# print('Your new string is:', output_str)
