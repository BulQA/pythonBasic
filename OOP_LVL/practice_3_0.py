#11.2 Классы

# user_tuple = ('Admin', 'qwerty', False)
# user_list = ['Admin', 'qwerty', False]
#
# user_dict = {
# 	'user_name':'Admin',
# 	'password':'qwerty',
# 	'is_banned': False
}

# +++++++++++++++++++++++++++++++++++++++++++#

# class User:
# 	user_name = 'Admin'
# 	password = 'qwerty'
# 	is_banned = False
#
# user_1 = User() #Экземпляр класса user
#
# user_1.user_name = 'Bob'
# print(user_1.user_name)
#
# user_2 = User()
# print(user_2.user_name)

#11.3 Методы класса, аргумент self

# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print('name: {}\npassword: {}\nBan status: {}'.format(
#             self.user_name, self.password, self.is_banned)
#         )
#
#     def add_friend(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'Masha'
#
# user_1.print_info()
# user_1.add_friend('Bob')
# user_1.add_friend(user_2)
#
# print(user_1.friends)

# +++++++++++++++++++++++++++++++++++++++++++#

# class Family:
#     surname = 'Common Family'
#     money = 100000
#     house = False
#
#     def info(self):
#         print(
#             'Famile name: {}\nFamily founds: {}\nHaving a house: {}'.format(
#                 self.surname, self.money, self.house
#             )
#         )
#
#     def earn_money(self, amount):
#         self.money += amount
#         print('Earned {} money! Current value: {}'.format(amount, self.money))
#
#     def buy_house(self, house_price, discount=0):
#         house_price -= house_price * discount / 100
#         if self.money >= house_price:
#             self.money -= house_price
#             self.house = True
#             print('House purchased! Current money: {}\n'.format(self.money))
#         else:
#             print('Not enough money\n')
#
#
# my_family = Family()
# my_family.info()
#
# print('Try to buy a house')
# my_family.buy_house(10 ** 5)
#
# if not my_family.house:
#     my_family.earn_money(900000)
#     print('Try to buy a house again')
#     my_family.buy_house(10 ** 5, 10)
#
# my_family.info()
