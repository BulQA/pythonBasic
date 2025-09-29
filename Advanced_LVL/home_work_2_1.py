# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня'
# ]
#
# favorite = []
#
# while True:
#     film = input('Введите название фильма (или "exit" для выхода): ')
#     if film.lower() == 'exit':
#         break
#
#     if film in films:
#         favorite.append(film)
#         print(f'Фильм "{film}" добавлен в избранное!')
#     else:
#         print(f'Ошибка: фильма "{film}" у нас нет :(')
#
# print('Ваш список избранного:', favorite)

# `````````````````Дз```````````````````````#

# n = int(input('Количество контейнеров: '))
#
# weights = []
# for i in range(n):
#     w = int(input('Введите вес контейнера: '))
#     # Контроль ввода: натуральные числа ≤ 200
#     while w <= 0 or w > 200:
#         w = int(input('Вес должен быть от 1 до 200. Повторите ввод: '))
#     weights.append(w)
#
# new_w = int(input('Введите вес нового контейнера: '))
# while new_w <= 0 or new_w > 200:
#     new_w = int(input('Вес должен быть от 1 до 200. Повторите ввод: '))
#
# pos = 0
# while pos < len(weights) and new_w <= weights[pos]:
#     pos += 1
#
# print('Номер, который получит новый контейнер:', pos + 1)

# `````````````````Дз```````````````````````#

# k = int(input('Сдвиг: '))
# n = int(input('Количество элементов: '))
# nums = []
# for i in range(n):
#     nums.append(int(input(f'Элемент {i + 1}: ')))
#
# if n > 0:
#     k %= n
#     nums[:] = nums[-k:] + nums[:-k]
#
# print('Сдвинутый список:', nums)

# `````````````````Дз```````````````````````#

# word = input('Введите слово: ')
#
# if word == word[::-1]:
#     print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом')

# `````````````````Дз```````````````````````#

# n = int(input('Количество чисел: '))
# nums = []
# for k in range(n):
#     nums.append(int(input(f'Число {k + 1}: ')))
#
# print('Изначальный список:', nums)
#
# for i in range(len(nums)):
#     min_index = i
#     for j in range(i + 1, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#
#     nums[i], nums[min_index] = nums[min_index], nums[i]
#
# print('Отсортированный список:', nums)

