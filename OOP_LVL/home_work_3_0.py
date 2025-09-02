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
