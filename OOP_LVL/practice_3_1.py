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

#14.3 Декораторы

# import time
# from typing import Callable, Any
#
# def timer(func: Callable) -> Callable:
#     '''
#     Декоратор, выводит время, которое заняло
#     выполнение декорируемой функции
#     '''
#     def wrapped_func(*args, **kwargs) -> Any:
#         started_at = time.time()
#         result = func(*args, **kwargs)
#         ended_at = time.time()
#
#         run_time = round(ended_at - started_at, 4)
#
#         print('Функция работала {} секунд(ы)'.format(run_time))
#         return result
#     return wrapped_func
#
#
# @timer
# def squares_sum() -> int:
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 2 for i_num in range(1000)])
#     return result
#
#
# @timer
# def cubes_sum(number: int) -> int:
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 3 for i_num in range(1000)])
#     return result
#
#
# new_sum = squares_sum()
# print(new_sum)
#
# my_cubes_sum = cubes_sum(100)
# print(my_cubes_sum)

#+++++++++++++++++++++++++++++++++++++++++++#

# def decorator(func):    # Функция, которая ожидает другую функцию в качестве аргумента
#     def wrapped_func(*args, **kwargs):
#         # Код до вызова функции
#         value = func(*args, **kwargs)
#         # Код после вызова функции
#         return value
#     return wrapped_func

#14.4 Некоторые особенности использования декораторов

# import time
# from typing import Callable, Any
#
# def timer(func: Callable) -> Callable:
#     '''
#     Декоратор, выводит время, которое заняло
#     выполнение декорируемой функции
#     '''
#     def wrapped_func(*args, **kwargs) -> Any:
#         started_at = time.time()
#         result = func(*args, **kwargs)
#         ended_at = time.time()
#
#         run_time = round(ended_at - started_at, 4)
#
#         print('Функция работала {} секунд(ы)'.format(run_time))
#         return result
#     return wrapped_func
#
#
# def logging(func: Callable) -> Callable:
#     '''
#     Декоратор, логирующий работу кода
#     '''
#     def wrapped_func(*args, **kwargs) -> Any:
#         print(
#             '\nВызывается функция {func}\t'
#             'Позиционные аргументы: {args}\t'
#             'Именованные аргументы: {kwargs}'.format(
#                 func=func.__name__, args=args, kwargs=kwargs
#             )
#         )
#         result = func(*args, **kwargs)
#         print('Функция успешно завершила работу')
#         return result
#     return wrapped_func
#
#
# @logging
# @timer
# def squares_sum() -> int:
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 2 for i_num in range(1000)])
#     return result
#
#
# @logging
# @timer
# def cubes_sum(number: int) -> int:
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 3 for i_num in range(1000)])
#     return result

#+++++++++++++++++++++++++++++++++++++++++++#

# from typing import Callable
#
# plugins = dict()
#
# def register(func: Callable) -> Callable:
#     '''
#     Декоратор регистрирующий функцию как плагин
#     '''
#     plugins[func.__name__] = func
#     return func
#
# @register
# def hello(name: str) -> str:
#     return 'Hello {name}'.format(name=name)
#
# @register
# def goodbye(name: str) -> str:
#     return 'Goodbye {name}'.format(name=name)
#
# print(plugins)
# print(hello('Mask'))


#14.5 Модуль functools. Декоратор functools.wraps()

# import time
# from typing import Callable, Any
# import functools
#
# def timer(func: Callable) -> Callable:
#     '''
#     Функция нахождения суммы квадратов
#     для каждого N от 0 до 1000,
#     где 0 <= N <= 100
#
#     :return: сумма квадратов
#     '''
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         started_at = time.time()
#         result = func(*args, **kwargs)
#         ended_at = time.time()
#
#         run_time = round(ended_at - started_at, 4)
#
#         print('Функция работала {} секунд(ы)'.format(run_time))
#         return result
#     return wrapped_func
#
#
# @timer
# def squares_sum() -> int:
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 2 for i_num in range(1000)])
#     return result
#
#
# @timer
# def cubes_sum(number: int) -> int:
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 3 for i_num in range(1000)])
#     return result
#
#
# print(squares_sum.__doc__)
# print(squares_sum.__name__)
