#!/usr/bin/python

from os import path
import pyexcel as pe
from enum import Enum, auto
import constants as c
import re
import pprint


class Language(Enum):
    English = auto()
    German = auto()


def get_sheet_name(lang: Language):
    if lang == Language.English:
        sheet_can_include = c.XL_SHEET_NAME_INCLUDE_ENGLISH
    else:
        sheet_can_include = c.XL_SHEET_NAME_INCLUDE_GERMAN

    sheets = list()
    xlsheets = pe.get_book(file_name=c.XL_FILE).sheet_names()

    for work_sheet in sheet_can_include:
        [sheets.append(sheet) for sheet in xlsheets if re.search(
            work_sheet.lower(), sheet.lower())]
    return sheets[0]


def to_transcript(words):
    # try find solution to non alpabetic symbols
    my_vocabulary = dict()
    for entry in words:
        word = entry[c.ENTRY_PART['word']]
        if re.findall('[a-zA-Z]', word):
            transcript = re.sub(
                r"\[{0,}\]{0,}", "", entry[c.ENTRY_PART['transcription']])
            d = word.split()
            if len(d) > 1:
                t = transcript.split()
                for i, j in enumerate(d):
                    my_vocabulary[j] = t[i]
            else:
                my_vocabulary[word] = transcript
    return my_vocabulary

    # entries = set()
    # for entry in entry_list:
    #     [entries.add(word) for word in entry[0].split() if
    #         re.findall('[a-zA-Z]', word)]
    # return entries
    # pprint.pprint(entry_list)


def get_words_dictionary(lang: Language):
    use_sheet = get_sheet_name(lang)
    words_dictionary = pe.get_records(file_name=c.XL_FILE, sheet_name=use_sheet,
                                      name_columns_by_row=1)
    return words_dictionary


def get_words_list(lang: Language):
    use_sheet = get_sheet_name(lang)
    entry_list = pe.get_array(file_name=c.XL_FILE,
                              sheet_name=use_sheet,
                              start_column=c.XL_TABLE_START_POSITION['column'],
                              start_row=c.XL_TABLE_START_POSITION['row'])
    return entry_list


if __name__ == '__main__':
    r = get_words_list(Language.English)
    print(to_transcript(r))
