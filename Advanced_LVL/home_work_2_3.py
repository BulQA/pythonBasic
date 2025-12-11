#6.2 Методы словарей

# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# combined = [small_storage, big_storage]
# big_storage = {}
#
# for d in combined :
#     big_storage.update(d)
#
# order = input('Введите название товара:')
#
# if order in big_storage:
#     print('На складе:',big_storage.get(order), order)
# else:
#     print('Такого товара нет на складе')

# +++++++++++++++++++++++++++++++++++++++++++#

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# total = sum(incomes.values())
# min_key = min(incomes, key=incomes.get)
# min_price = incomes[min_key]
#
# print('Общий доход за год составил:', total, 'рублей')
# print(f'Самый маленький доход у {min_key} — он составляет {min_price} рублей')
#
# incomes.pop(min_key)
#
# print('Итоговый словарь:', incomes)

#6.3 Методы словарей

# text = input("Введите текст: ")
#
# histogram = {}
#
# for ch in text:
#     histogram[ch] = histogram.get(ch, 0) + 1
#
# for ch in sorted(histogram.keys()):
#     print(f"{ch} : {histogram[ch]}")
#
# print("Максимальная частота:", max(histogram.values()))

#6.3 Вложенные словари и значения по умолчанию в get

# order = {
#     'apple': 2,
#     'banana': 3,
#     'pear': 1,
#     'watermelon': 10,
#     'chocolate': 5
# }
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# profit = 0
#
# for item, amount in order.items():
#     price = incomes.get(item, 0)
#     profit += price * amount
#
# print("Итоговая сумма:", profit)
