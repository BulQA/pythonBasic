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
