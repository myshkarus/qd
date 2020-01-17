#!/usr/bin/python

import proxy
import pyexcel as pe
from pyexcel import Book, Sheet
from pyexcel._compact import OrderedDict
import re

list_or_words = []
dict_of_entries = set()
# proxy.setup()

# xlbook = pe.Book(filename='dict.xlsx', path='./')
# print(xlbook.number_of_sheets())
# print(xlbook.sheet_names())

book = pe.get_book(file_name='dict.xlsx')
# print(book.number_of_sheets())
# print(book.sheet_names())
# print(type(book['Eng_dict']))

sheet = book['Eng_dict']
# print(sheet.number_of_rows())


sh = Sheet(book['Eng_dict'])
# print(sh.number_of_rows())

# sheets = book.to_dict()
# for name in sheets.keys():
#     print(name)

# my_dict = pe.get_dict(file_name='dict.xlsx',
#                       name_columns_by_row=-1, name_rows_by_column=2)
# # print(isinstance(my_dict, OrderedDict))
# # print(my_dict['word'])
# print(len(my_dict))

# for key, values in my_dict.items():
#     #     # print(key, ','.join([str(item) for item in values]))
#     print('key: {0}; value[0]: {1}'.format(key, values[0]))

ar = pe.get_array(file_name='dict.xlsx', sheet_name='Eng_dict',
                  start_column=2, start_row=3)
print('total entries: {0}'.format(len(ar)))
print('=' * 50)
for i in ar:
    for j in i[0].split():
        if re.findall('[a-zA-Z]', j):
            dict_of_entries.add(j)


print(dict_of_entries)
print('=' * 50)
print(len(dict_of_entries))
