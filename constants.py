#!/usr/bin/python

ENTRY_URL_OXFORD = 'https://www.lexico.com/definition/'
ENTRY_URL_CAMBRIDGE = 'https://dictionary.cambridge.org/dictionary/english/'

PATTERNS_OXFORD = {
    'transcription': '<span class="phoneticspelling">(.*?)\</span>'
}

PATTERNS_CAMBRIDGE = {
    'transcription': '<span class="ipa dipa lpr-2 lpl-1">(.*?)\</span>'
}

XL_FILE = '_dict.xlsx'
XL_TABLE_START_POSITION = {'row': 3, 'column': 2}
XL_SHEET_NAME_INCLUDE_ENGLISH = ['eng', 'english']
XL_SHEET_NAME_INCLUDE_GERMAN = ['ger', 'germ', 'german', 'deutsch']

ENTRY_PART = {
    'word': 0,
    'translation (ua)': 1,
    'type': 2,
    'transcription': 3,
    'form': 4,
    'clone': 5,
    'page': 6,
    'examples / explanation': 7,
    'flag': 8
}
