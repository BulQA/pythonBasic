#11.2 Классы

# user_tuple = ('Admin', 'qwerty', False)
# user_list = ['Admin', 'qwerty', False]
#
# user_dict = {
# 	'user_name':'Admin',
# 	'password':'qwerty',
# 	'is_banned': False

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

#+++++++++++++++++++++++++++++++++++++++++++#

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

# 11.4 Конструктор __init__ и работа с несколькими классами

# class Employer:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def print_info(self):
#         print(
#             'Name: {}\nSalary: {}'.format(self.name, self.salary)
#         )
#
#
# emp_1 = Employer('Bob', 900)
# emp_2 = Employer('Shel', 1000)
#
# emp_1.print_info()
# emp_2.print_info()

#+++++++++++++++++++++++++++++++++++++++++++#

# class Potato:
#     state = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print('Картошка {} сейчас {}'.format(
#             self.index, Potato.state[self.state]
#         ))
#
#
# class PotatoGarden:
#
#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('Картошка прорастает.')
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         for i_potato in self.potatoes:
#             if not i_potato.is_ripe():
#                 print('Картошка ещё не созрела.\n')
#                 break
#         else:
#             print('Картошка готова к сбору.\n')
#
#
# my_garden = PotatoGarden(5)
# my_garden.are_all_ripe()
#
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()

#11.5 Определение классов в модулях и их подключение

# from garden import PotateGarden
#
#
# my_garden = PotateGarden(5)
# my_garden.are_all_ripe()
#
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()


#12.1 Разбор домашнего задания

# class Water:
#     def __str__(self):
#         return 'Вода'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Vapor()
#         elif isinstance(other, Earth):
#             return Dirt()
#         else:
#             return None
#
#
# class Air:
#     def __str__(self):
#         return 'Воздух'
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         else:
#             return None
#
#
# class Fire:
#     def __str__(self):
#         return 'Огонь'
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Vapor()
#         elif isinstance(other, Air):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Lava()
#         else:
#             return None
#
#
# class Earth:
#     def __str__(self):
#         return 'Земля'
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Dirt()
#         elif isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#         else:
#             return None
#
# class Storm:
#     def __str__(self):
#         return 'Шторм'
#
#
# class Vapor:
#     def __str__(self):
#         return 'Пар'
#
#
# class Dirt:
#     def __str__(self):
#         return 'Грязь'
#
#
# class Lightning:
#     def __str__(self):
#         return 'Молния'
#
#
# class Lava:
#     def __str__(self):
#         return 'Лава'
#
#
# class Dust:
#     def __str__(self):
#         return 'Пыль'
#
#
# water = Water()
# air = Air()
# fire = Fire()
# earth = Earth()
#
# print(water + air)    # Вода + Воздух = Шторм
# print(water + fire)   # Вода + Огонь = Пар
# print(water + earth)  # Вода + Земля = Грязь
# print(air + fire)     # Воздух + Огонь = Молния
# print(fire + earth)   # Огонь + Земля = Лава
# print(air + earth)    # Воздух + Земля = Пыль

#12.2 Инкапсуляция и сокрытие данных. Геттеры и сеттеры

# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         Person.__count += 1
#
#     def __init__(self):
#         return 'Имя: {}\tВозраст: {}'.format(self.__name, self.__age)
#
#     def get_count(self): #геттер
#         return self.__count
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age): #сеттер
#         if age in range(1, 99):
#             self.__age = age
#         else:
#             raise Exception('Недопустимое значение')
#
# masha = Person('Masha', 20)
# petya = Person('Petya', 23)
# print(masha.get_count())
#
# new_age = 40
# petya.set_age(new_age)
# print(petya.get_age)

# __count  сокрытие данных

# Инкапсуляция - объеденение данных и методов в
#единый объект и сокрытие реализации от пользователя

# Приватными могут быть не только методы, но и классы

#12.3 Наследование

# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'Да' if self.has_tail else 'Нет'
#         return 'Количество ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail=tail
#         )
#
#
# class Cat(Pet):
#     def sound(self):
#         print('Мяу')
#
#
# class Dog(Pet):
#     def sound(self):
#         print('Гав')
#
#
# class Frog(Pet):
#     has_tail = False  # у лягушки нет хвоста
#
#     def sound(self):
#         print('Ква')
#
# cat = Cat()
# print(cat)
# cat.soud()
#
# dog = Dog()
# dog.soud()
# print(dog)
#
# frog = Frog()
# frog.soud()
# print(frog)

#+++++++++++++++++++++++++++++++++++++++++++#

# class Ship:
#     def __init__(self, model):
#         self.__model = model
#
#     def __str__(self):
#         return '\nМодель корабля: {model}'.format(
#             model=self.__model
#         )
#
#     def sail(self):
#         print('\nКорабль покинул гавань.')
#
#
# class WarShip(Ship):
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def attack(self):
#         print("На корабле установлено оружие:", self.gun)
#
#
# class CargoShip(Ship):
#     def __init__(self, model):
#         super().__init__(model)
#         self.tonnage_load = 0
#
#     def load(self):
#         print('Загружаем корабль')
#         self.tonnage_load += 1
#         print('Текущая загруженность:', self.tonnage_load)
#
#     def unload(self):
#         print('Разгружаем корабль')
#         if self.tonnage_load > 0:
#             self.tonnage_load -= 1
#         else:
#             print('Корабль уже разгружен!')
#         print('Текущая загруженность:', self.tonnage_load)
#
# warship = WarShip('Abc', 'Торпеды')
# print(warship)
# warship.attack()
#
# cargoship = CargoShip('Titanic')
# print(cargoship)
# cargoship.load()
# cargoship.unload()
# cargoship.unload()
