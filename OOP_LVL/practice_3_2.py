#15.4 Множественное наследование примеси и абстрактные классы
# from abc import ABC, abstractmethod
#
#
# class Figure(ABC):
#     """Абстрактный базовый класс Фигура
#
#     Args and Attrs:
#         pos_x(int): Координата Х
#         pos_y(int): Координата У
#         length(int): Длина фигуры
#         width(int): Ширина фигуры
#     """
#     def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.length = length
#         self.width = width
#
#     @abstractmethod
#     def move(self, pos_x: int, pos_y: int) -> None:
#         """Перемещает фигуру"""
#         pass
#
#
# class ResizableMixin:
#     def resize(self, length: int, width: int) -> None:
#         self.length = length
#         self.width = width
#
#
# class Rectangle(Figure, ResizableMixin):
#     """Прямоугольник, Родительский класс: Figure"""
#
#     def move(self, pos_x: int, pos_y: int) -> None:
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#
#
# class Square(Figure, ResizableMixin):
#     """Квадрат, Родительский класс: Figure"""
#
#     def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
#         super().__init__(pos_x, pos_y, size, size)
#
#     def move(self, pos_x: int, pos_y: int) -> None:
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#
#
# rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
# rect_2 = Rectangle(pos_x=30, pos_y=39, length=11, width=10)
# square_1 = Square(pos_x=50, pos_y=70, size=8)
#
# for figure in [rect_1, rect_2, square_1]:
#     new_size_x = figure.length * 2
#     new_size_y = figure.width * 2
#     figure.resize(new_size_x, new_size_y)
#     figure.move(100, 200)   # проверка move
#     print(f"{figure.__class__.__name__}: x={figure.pos_x}, y={figure.pos_y}, "
#           f"length={figure.length}, width={figure.width}")


#15.5 Класс как контекст-менеджер. Методы enter и exit

#Контекст-менеджер - Это объект Python, который следит за инициализацией и финализацией
#данного контекста, в частности определяет действия, которые должны происходить до и после
#выполнения блока кода.

# import time
#
# class Timer:
#     def __init__(self) -> None:
#         print('Время работы кода')
#         self.start = None
#
#     def __enter__(self) -> 'Timer':
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         print(time.time() - self.start)
#         if exc_type is TypeError:
#             return True
#
# with Timer as t1:
#     print('Первая часть')
#     val_1 = 100 * 100 ** 10000
#
# with Timer as t2:
#     print('Вторая часть')
#     val_2 = 200 * 200 ** 20000

# #15.6 Методы класса декораторы setter и property

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age  # вызовет setter
#
#     def __str__(self):
#         return 'Имя: {name}\tВозраст: {age}'.format(
#             name=self.__name,
#             age=self.__age
#         )
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception("Недопустимый возраст")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name: str):
#         if isinstance(new_name, str) and new_name.strip():
#             self.__name = new_name
#         else:
#             raise Exception("Недопустимое имя")
#
#
# tom = Person('Tom', 24)
# print(tom)
# print(tom.age)
#
# tom.age = 27
# print(tom.age)
# print(tom)
#
# tom.name = "Tommy"
# print(tom)

#15.7 Методы класса декоратор classmethod

# class Pet:
#     ttl_sound = 0
#
#     def __init__(self) -> None:
#         self.__legs = 4
#         self.__has_tail = True
#
#     def __str__(self) -> str:
#         tail = 'Yes' if self.__has_tail else 'No'
#         return 'Всего ног: {legs}\nХвост присутствует: {has_tail}'.format(
#             legs=self.__legs,
#             has_tail=self.__has_tail
#         )
#
#
# class Cat(Pet):
#     @classmethod
#     def sound(cls) -> None:
#         cls.ttl_sound += 1
#         print(cls.ttl_sound)
#         print('Мяу!')
#
# class Dog(Pet):
#     @classmethod
#     def sound(cls) -> None:
#         print('Гав!')
#
# cat = Cat()
#
# Cat.sound()
# Cat.sound()









