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

    try:
        for work_sheet in sheet_can_include:
            [sheets.append(sheet) for sheet in xlsheets if re.search(
                work_sheet.lower(), sheet.lower())]
        return sheets[0]
    except:
        raise NotImplementedError('Sheet is not exist')


def to_transcript(words):
    my_vocabulary = dict()
    for entry in words:
        # TODO: change re pattern
        word = re.sub(r"(-\w+)", "",
                      entry[c.ENTRY_PART['word']])
        transcript = re.sub(
            r"\[*?\]*?", "", entry[c.ENTRY_PART['transcription']])

        word_to_array = word.split()
        transcript_to_array = transcript.split()

        for i, j in enumerate(word_to_array):
            if len(word_to_array) > 0 and len(word_to_array) <= len(transcript_to_array):
                my_vocabulary[j] = transcript_to_array[i]
            else:
                if j not in my_vocabulary and re.findall('[a-zA-Z]', j):
                    my_vocabulary[j] = ''

    pprint.pprint(my_vocabulary)


def get_words_dictionary(lang: Language):
    sheet_to_use = get_sheet_name(lang)
    words_dictionary = pe.get_records(file_name=c.XL_FILE, sheet_name=sheet_to_use,
                                      name_columns_by_row=1)
    return words_dictionary


def get_words_list(lang: Language):
    sheet_to_use = get_sheet_name(lang)
    entry_list = pe.get_array(file_name=c.XL_FILE,
                              sheet_name=sheet_to_use,
                              start_column=c.XL_TABLE_START_POSITION['column'],
                              start_row=c.XL_TABLE_START_POSITION['row'])
    # print(entry_list)
    return entry_list


if __name__ == '__main__':
    r = get_words_list(Language.English)
    to_transcript(r)