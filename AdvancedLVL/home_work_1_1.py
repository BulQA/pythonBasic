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
#
# nums = [4, 9, 7, 6, 3, 2]
#
# selection_sort(nums)
#
# print(nums)
