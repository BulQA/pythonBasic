# 13.1 Разбор домашнего задания

# class Stack:
#     def __init__(self):
#         self.__st = []
#
#     def __str__(self):
#         return '; '.join(map(str, self.__st))
#
#     def push(self, elem):
#         self.__st.append(elem)
#
#     def pop(self):
#         if len(self.__st) == 0:
#             return None
#         return self.__st.pop()
#
#
# new_st = Stack()
#
# for i in range(5):
#     new_st.push(i)
# print(new_st)
#
# for _ in range(3):
#     new_st.pop()
# print(new_st)
#
#
# class TaskManager:
#     def __init__(self):
#         self.task = dict()
#
#     def __str__(self):
#         display = []
#         if self.task:
#             for i_priority in sorted(self.task.keys()):
#                 display.append(
#                     '{prio} {task}\n'.format(
#                         prio=str(i_priority),
#                         task=self.task[i_priority]
#                     )
#                 )
#         return ''.join(display)
#
#     def new_task(self, task, priority):
#         if priority not in self.task:
#             self.task[priority] = Stack()
#         self.task[priority].push(task)
#
#
# manager = TaskManager()
#
# manager.new_task("Написать эссэ", 2)
# manager.new_task("Завести жену", 3)
# manager.new_task("Построить дом", 1)
#
# print(manager)

#14.1 Разбор домашнего задания

# from typing import Any, Optional
#
#
# class Node:
#     def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
#         self.value = value
#         self.next = next
#
#     def __str__(self) -> str:
#         return 'Node [{value}]'.format(
#             value=str(self.value)
#         )
#
#
# class LinkedList:
#     def __init__(self) -> None:
#         self.head: Optional[Node] = None
#         self.length = 0
#
#     def __str__(self) -> str:
#         if self.head is not None:
#             current = self.head
#             values = [str(current.value)]
#             while current.next is not None:
#                 current = current.next
#                 values.append(str(current.value))
#             return '[{values}]'.format(values=' '.join(values))
#         return 'LinkedList []'
#
#     def append(self, elem: Any) -> None:
#         new_node = Node(elem)
#         if self.head is None:
#             self.head = new_node
#             self.length += 1
#             return
#
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#         self.length += 1
#
#     def remove(self, index: int) -> None:
#         if self.length == 0 or index >= self.length or index < 0:
#             raise IndexError("Index out of range")
#
#         cur_node = self.head
#
#         if index == 0:  # удаляем первый элемент
#             self.head = cur_node.next
#             self.length -= 1
#             return
#
#         prev = None
#         cur_index = 0
#
#         while cur_node is not None:
#             if cur_index == index:
#                 prev.next = cur_node.next
#                 self.length -= 1
#                 return
#             prev = cur_node
#             cur_node = cur_node.next
#             cur_index += 1
#
#
# new_list = LinkedList()
#
# new_list.append(10)
# new_list.append(20)
# new_list.append(30)
#
# print(new_list)
# print()
#
# new_list.remove(1)
# print(new_list)

#15.1 Разбор домашнего задания

# from collections.abc import Callable
# import functools
#
#
# def counter(func: Callable) -> Callable:
#     '''
#     Декоратор, считывающий и выводящий кол-во
#     вызовов декорируемой функции
#     '''
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print('Функция {func} была вызвана: {count} раз'.format(
#             func=func.__name__, count=wrapper.count))
#         return res
#
#     wrapper.count = 0
#     return wrapper
#
#
# @counter
# def test():
#     print("Тест кейс 1")
#
# test()

#16.1 Разбор домашнего задания

# class Date:
#
#     def __init__(self, day: int=0, month: int=0, year: int=0) -> None:
#         self.day = day
#         self.month =month
#         self.year = year
#
#     def __str__(self) -> str:
#         return 'День: {}\tМесяц: {}\tГод: {}'.format(
#             self.day, self.month, self.year
#         )
#
#     @classmethod
#     def is_date_valid(cls, date: str) ->bool:
#         day, month, year = map(int, date.split('-'))
#         date_obj = cls(day, month, year)
#         return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999
#
#     @classmethod
#     def from_string(cls, date: str) -> 'Date':
#         #dmy_list = date.split('-')
#         #day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
#         day, month, year = map(int, date.split('-'))
#         date_obj = cls(day, month, year)
#         return date_obj
#
# new_date = Date.from_string('11-11-2010')
# print(new_date)
#
# print(Date.is_date_valid('11-11-2010'))
#
# print(Date.is_date_valid('40-11-4099'))