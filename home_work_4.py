# `````````````````Дз```````````````````````#

# def count_additions():
#     print("Введите число в эксп. форме: ", end='')
#     s = input()
#
#     e_pos = -1
#     i = 0
#     for ch in s:
#         if ch == 'e':
#             e_pos = i
#         i += 1
#
#     valid = 0
#     if e_pos != -1:
#         i = 0
#         for ch in s:
#             if i == e_pos + 1 and ch == '-':
#                 valid = 1
#             i += 1
#
#     while valid == 0:
#         print("Неверный ввод. Пример: 1e-3")
#         print("Введите число в эксп. форме: ", end='')
#         s = input()
#
#         e_pos = -1
#         i = 0
#         for ch in s:
#             if ch == 'e':
#                 e_pos = i
#             i += 1
#
#         valid = 0
#         i = 0
#         for ch in s:
#             if i == e_pos + 1 and ch == '-':
#                 valid = 1
#             i += 1
#
#
#     mantissa_str = ""
#     i = 0
#     for ch in s:
#         if i == e_pos:
#             break
#         mantissa_str = mantissa_str + ch
#         i += 1
#
#
#     exponent_str = ""
#     i = 0
#     for ch in s:
#         if i > e_pos + 1:
#             exponent_str = exponent_str + ch
#         i += 1
#
#
#     mantissa = float(mantissa_str)
#     exponent = int(exponent_str)
#
#
#     power = 1.0
#     i = 0
#     while i < exponent:
#         power = power * 0.1
#         i = i + 1
#     N = mantissa * power
#
#
#     X = 1.0
#     additions = 0
#     while X <= 2.0:
#         X = X + N
#         additions = additions + 1
#
#     print("Кол-во прибавлений:", additions)
#
# count_additions()

# `````````````````Дз```````````````````````#

# def float_format():
#     x = float(input("Введите число: "))
#
#     if x <= 10:
#         print("Число должно быть больше 10")
#         return
#
#     b = 0
#     a = x
#
#     while a >= 10:
#         a /= 10
#         b += 1
#
#     print(f"Формат плавающей точки: x = {a} * 10 ** {b}")
#
# float_format()

# `````````````````Дз```````````````````````#

# def tax_count():
#     tax = float(input("Введите бюджет страны: "))
#     new_tax = float(input("Новые поступления (налог): "))
#
#     total = tax + new_tax
#
#     if total == tax:
#         print("Результат: Бюджет не изменится")
#     else:
#         print("Результат: Бюджет увеличится")
#
# tax_count()

# `````````````````Дз```````````````````````#

# from decimal import Decimal, getcontext
#
# def eqv():
#     getcontext().prec = 30
#
#     frst_numm = Decimal(input('Введите первое число: '))
#     sec_numm = Decimal(input('Введите второе число: '))
#     thrd_numm = Decimal(input('Введите третье число: '))
#
#     if frst_numm + sec_numm == thrd_numm:
#         print('True')
#     else:
#         print('False')
#
# eqv()

# `````````````````Дз```````````````````````#

# def to_float_point():
#     x = float(input("Введите число: "))
#
#     while x <= 0:
#         print("Число должно быть больше 0.")
#         x = float(input("Введите число: "))
#
#     a = x
#     b = 0
#
#     if x >= 10:
#         while a >= 10:
#             a = a / 10
#             b = b + 1
#     elif x < 1:
#         while a < 1:
#             a = a * 10
#             b = b - 1
#
#     print(f"Формат плавающей точки: x = {a} * 10 ** {b}")
#
# to_float_point()

# `````````````````Дз```````````````````````#

# def maximum_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# def maximum_of_three(a, b, c):
#     max_ab = maximum_of_two(a, b)
#     max_abc = maximum_of_two(max_ab, c)
#     return max_abc
#
# x = float(input("Введите первое число: "))
# y = float(input("Введите второе число: "))
# z = float(input("Введите третье число: "))
#
# max_value = maximum_of_three(x, y, z)
# print("Максимум из трёх чисел:", max_value)

# `````````````````Дз```````````````````````#

# def reverse_number(n):
#     reversed_n = 0
#     while n > 0:
#         digit = n % 10
#         reversed_n = reversed_n * 10 + digit
#         n //= 10
#     return reversed_n
#
# def main():
#     n = int(input("Введите первое число: "))
#     k = int(input("Введите второе число: "))
#
#     rev_n = reverse_number(n)
#     rev_k = reverse_number(k)
#
#     print("Первое число наоборот:", rev_n)
#     print("Второе число наоборот:", rev_k)
#
#     total = rev_n + rev_k
#     rev_total = reverse_number(total)
#
#     print("Сумма:", total)
#     print("Сумма наоборот:", rev_total)
#
# main()
