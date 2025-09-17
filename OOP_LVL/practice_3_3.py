# 17.6 Специальная переменная __name__

#import new_python
#
# if __name__ == '__main__':
#     print('Инициализация исполняемого файла')
#     new_python.func()
#
# '''
# Если функция достаточно простая то вместо отдельного
# обьявления можно использовать lambda, главное помнить
# про читаемость кода и пайтоник вэй.
#
# Если мы хотим применить какую нибудь функцию к каждому
# итерируемому объекту, то для этого используется map.
#
# Для филтрации какого либо значения функции используется
# функция filter.
#
# Для чистоты кода используется if __name__ == '__main__' .
# '''

#18.2 Регулярные выражения модуль re и его методы
import re #Регулярные выражения

text = 'Тут лежит ваш текст'

result = re.match(r'Тут', text) #Поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону', result)
print(result.group(0))
print(result.start())
print(result.end())

#+++++++++++++++++++++++++++++++++++++++++++#

print('=' * 40)
result = re.search(r'ваш', text) #Поиск в строке по шаблону
print('Поиск в строке по шаблону', result)
print(result.group(0))

#+++++++++++++++++++++++++++++++++++++++++++#

print('=' * 40)
result = re.findall(r'ваш', text) #Все совпадения по шаблону
print('Все совпадения по шаблону', result)

#+++++++++++++++++++++++++++++++++++++++++++#

print('=' * 40)
result = re.sub(r'ваш','наш', text) #Замена всех найденных шаблонов
print('Все совпадения по шаблону', result)

#18.3 Регулярные выражения шаблоны
import re

text = 'AV is largest Analytics community of India'

result = re.findall(r'\b[aeiouAEIOU]\w+', text) #спец символы '.', '\W'...

"""
Зачем нужны регулярные выражения:

1. Проверка формата данных (телефонный номер, e-mail)
2. Разбиение строки на подстроки, поиск, извлечение и 
замена символов
3. Высокая скорость выполнения сложных операций по
поиску и замене подстрок.
"""

import re

deep_ocean = """oCeAn Marlin OcEaN oceAN OCEAN OCEAN OCEAN OCEAN OCEan Ocean Ocean ocean oCeAn 
OcEaN oceAN OCEAN OCEAN OCEAN OCEan Ocean Ocean ocean oCeAn OcEaN oceAN OCEAN OCEAN OCEAN OCEAN 
OCEan Ocean Ocean OCEan Ocean Ocean ocean Ocean ocean oCeAn OcEaN oceAN OCEAN OCEAN OCEAN OCEAN 
ocean oCeAn OcEaN nemaa OCEAN OCEAN OCEAN OCEAN OCEan Ocean nemo0 ocean oCeAn OcEaN oceAN OCEAN
OCEAN OCEAN OCEAN OCEan Ocean Ocean ocean oNeMa OcEaN oceAN OCEAN OCEAN OCEAN OCEAN OCEan Ocean
Ocean ocean oCeAn OcEaN oceAN nenemo OCEAN OCEAN OCEAN OCEan Ocean Ocean Nemo ocean oCeAn OcEaN 
oceAN OCEAN OCEAN OCEAN OCEAN OCEan Ocean"""

nemo_pattern = r'[Nn]em\w{0,2}'
full_search = re.findall(nemo_pattern, deep_ocean)
print(full_search)

#+++++++++++++++++++++++++++++++++++++++++++#

transparent = re.sub(r'[Oo]\w{4}\s+', '', deep_ocean)
print('Всё что совпало с паттерном было заменено, осталось лишь это:')
print(transparent)