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
