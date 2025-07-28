#5.2 Форматирование строк format и f-strings

# user_name = input('Input user name:')
# file_name = input('Input file name:')
#
# path = 'C:/{user}/docs/folder/{new file}.txt'.format(
#         user=user_name,
#         new_file=file_name
# )
#
# path_1 = 'C:/{0}/docs/folder/{1}.txt'.format(
#         user_name,
#             file_name
# )
#
# print('File path:', path, path_1)

# +++++++++++++++++++++++++++++++++++++++++++#

# while True:
#     gartes_template = input('Input your template like "Hello {name}": ')
#
#     if "{name}" in gartes_template:
#         break
#     print('Error: you must include "{name}" in the template.')
#
# print('Input names, list ends with "end"')
# names_list = []
#
# while True:
#     name = input('Name: ')
#     if name.lower() == 'end':
#         break
#     names_list.append(name)
#
# for i_name in names_list:
#     print(gartes_template.format(name=i_name))
