#!/usr/bin/python

import proxy
import pyexcel as pe
from pyexcel._compact import OrderedDict

proxy.setup()

book = pe.get_book(file_name='dict.xlsx')
print(isinstance(book, OrderedDict))

sheets = book.to_dict()
for name in sheets.keys():
    print(name)
