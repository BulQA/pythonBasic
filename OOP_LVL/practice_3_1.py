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
