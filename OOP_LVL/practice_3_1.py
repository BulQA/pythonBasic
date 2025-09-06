#12.5 Документация. Описание классов и методов
#
# class Person:
#     """
#     Базовый класс, описывающий человека
#
#     __count: кол-во человек
#
#     args:
#         name(str): передаётся имя человека
#         age(int): передаётся возраст человека
#
#     attributes:
#         max_count(int): максимальное кол-во инстансов
#     """
#     __count = 0
#     max_count = 5
#
#     def __init__(self, name, age):
#         self._name = name
#         self.set_age(age)
#         self.__location = 'Moscow'
#
#         if Person.__count >= Person.max_count:
#             raise Exception('Слишком много людей')
#         Person.__count += 1
#
#     def get_age(self):
#         """
#         Геттер для получения возраста
#
#         :return: _age
#         """
#         return self._age
#
#     def set_age(self, age):
#         """
#         Сеттер для установления возраста
#
#         :param age: возраст
#         :type age: int
#         :raise Exception: если возраст не в границе от 1 до 90, то вызывается исключение
#         """
#         if age in range(1, 90):
#             self._age = age
#         else:
#             raise Exception("Недопустимый возраст")
#
#
# class Employee(Person):
#     """
#     Класс Работник. Родитель: Person
#
#     args:
#         name(str): передаётся имя человека
#         age(int): передаётся возраст человека
#
#     attributes:
#         job(str): должность работника
#     """
#     def __init__(self, name, age, job='Sales manager'):
#         super().__init__(name, age)
#         self.job = job
#
#     def get_job(self):
#         return self.job
#
#     def employ(self, value):
#         self.job = value
#
#
# print(Person.__doc__)

#13.2 Итераторы

# items = [10, 20, 30]
#
# iterator = iter(items)
#
# print(next(iterator))  # 10
# print(next(iterator))  # 20
# print(next(iterator))  # 30
#
# # следующий вызов вызовет ошибку StopIteration
# # print(next(iterator))

#+++++++++++++++++++++++++++++++++++++++++++#

# items = ['a', 'b', 'c']
#
# iterator = iter(items)
#
# for elem in iterator:
#     print(elem)

#+++++++++++++++++++++++++++++++++++++++++++#

# class Countdown:
#     def __init__(self, start):
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration
#         value = self.current
#         self.current -= 1
#         return value
#
#
# for num in Countdown(5):
#     print(num)   # 5, 4, 3, 2, 1

#13.4 Реализация итераторов

# import random
#
# class RandomNumbers:
#     def __init__(self, limit):
#         self.__limit = limit
#         self.__counter = 0
#
#     def __iter__(self):
#         return iter
#
#     def __next__(self):
#         if self.__counter < self.__limit:
#             self.__counter += 1
#             return random.randint(0, 10)
#         else:
#             raise StopIteration
#
# new_iter = RandomNumbers(limit=3)
#
# print(next(new_iter))
#
# for num in new_iter:
#     print(num)

#+++++++++++++++++++++++++++++++++++++++++++#

# class Fibonacci:
#
#     def __init__(self, number):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         self.number = number
#
#     def __iter__(self):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.number:
#                 raise StopIteration()
#             self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
#         return self.cur_val
#
#
# fibo = Fibonacci(10)
# for i_value in fibo:
#     print(i_value)
#
#
# print(7 in Fibonacci(10))

# 13.5 Генераторы и их реализация

# def Fibonacci(number):
#     cur_val = 0
#     next_val = 1
#
#     for _ in range(number):
#         yield cur_val
#         cur_val, next_val = next_val, cur_val + next_val
#         if cur_val > 10**6:
#             return
#
#
# def square(nums):
#     for num in nums:
#         yield num ** 2
#
#
# fibo = Fibonacci(number=1000000)
#
# for i in fibo:
#     print(i, end=' ')
# print('\n')
#
# # Генератор от генератора
# print(sum(square(Fibonacci(number=1470))))
#
# # Генераторные выражения
# print()
# cubes_gen = (num ** 3 for num in range(10))
#
# for i_num in cubes_gen:
#     print(i_num, end=' ')

#13.6 Аннотации типов

# from collections.abc import Iterable
#
# class Person:
#     def __init__(self, name: str, age: int, friends: list) -> None:
#         self.__name = name
#         self.__age = age
#         self.__friends = friends
#
#     def __str__(self) -> str:
#         return 'Имя: {}\tВозраст: {}\tДрузья: {}'.format(
#             self.__name, self.__age, self.__friends
#         )
#
#     def set_age(self, age: int) -> None:
#         self.__age = age
#
#     def get_age(self) -> int:
#         return self.__age
#
#
# def Fibonacci(number: int) -> Iterable[int]:
#     cur_val = 0
#     next_val = 1
#
#     for _ in range(number):
#         yield cur_val
#         cur_val, next_val = next_val, cur_val + next_val
#         if cur_val > 10 ** 6:
#             return

#14.2 Функция как объект. Функции высшего порядка

# import time
# from typing import Callable, Any
#
# def timer(func: Callable, *args, **kwargs) -> Any:
#     '''Функция таймер'''
#
#     started_at = time.time()
#     result = func(*args, **kwargs)
#     ended_at = time.time()
#
#     run_time = round(ended_at - started_at, 4)
#
#     print('Функция работала {} секунд(ы)'.format(run_time))
#     return result
#
# def squares_sum() -> int:
#     number = 100
#     result = 0
#
#     for _ in range(number + 1):
#         result += sum([i_num ** 2 for i_num in range(1000)])
#     return result
#
# def cubes_sum(number: int) -> int:
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 3 for i_num in range(1000)])
#     return result
#
#
# new_result = timer(squares_sum)
# print(new_result)
#
# new_cubes = timer(cubes_sum, 200)
# print(new_cubes)
