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
