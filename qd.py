#!/usr/bin/python

from enum import Enum, auto


from os import path


import pyexcel as pe


class Language(Enum):
    English = auto()
    German = auto()


class Words:
    def __init__(self, filename: str, lang: Language, position: dict):
        self._filename = None
        self._lang = None
        self.filename = filename
        self.lang = lang
        self._start_row = position.get('row', 0)
        self._start_column = position.get('column', 0)

    @property
    def start_row(self):
        return self._start_row

    @start_row.setter
    def start_row(self, row: int):
        self._start_row = row

    @property
    def start_column(self):
        return self._start_column

    @start_column.setter
    def start_column(self, column: int):
        self._start_column = column

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang: Language):
        self._lang = lang

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, file: str):
        if path.exists(file):
            self._filename = file

    @property
    def sheet(self):
        return self._get_sheet()

    def _get_sheet(self):
        sheets = list()
        xlsheets = pe.get_book(file_name=self.filename)
        if self.lang == Language.English:
            vocabulary = english_vocabulary
        elif self.lang == Language.German:
            vocabulary = german_vocabulary
        else:
            raise NotImplementedError
        for i in vocabulary:
            [sheets.append(sheet)
             for sheet in xlsheets.sheet_names() if re.search(i.lower(), sheet.lower())]
        return sheets[0]

    def get_vocabulary(self):
        entries = set()
        entry_list = pe.get_array(file_name=self.filename,
                                  sheet_name=self.sheet,
                                  start_column=self.start_column,
                                  start_row=self.start_row)
        for entry in entry_list:
            [entries.add(word) for word in entry[0].split() if
             re.findall('[a-zA-Z]', word)]
        return entries

    def __str__(self):
        return 'Words class(filename:=\'{0}\', sheet:=\'{1}\', ' \
               'lang:=\'{2}\')'.format(self.filename, self.sheet, self.lang)

    def __repr__(self):
        return 'Words(\'{0}\', \'{1}\', \'{2}\')'.format(self.filename,
                                                         self.sheet, self.lang)


class Vocabulary_Worker:
    def __init__(self, words: Words = None):
        self._words = words

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, filename: str, lang: Language, position: dict):
        self._words = Words(filename, lang, position)

    @property
    def vocabulary(self):
        return self.get_vocabulary()

    def get_vocabulary(self):
        return self.words.get_vocabulary()



    def run():
        pass


if __name__ == '__main__':
    wd = Words(file, Language.English, start_position)
    worker = Vocabulary_Worker(wd)
    worker.get_transcript()

    # proxy.setup()
    # get_transcript(Language.English)

    # prepare('https://www.lexico.com/robots.txt')
    # print('definition: ', is_allowed('https://www.lexico.com/definition/'))

    # target_url = 'https://www.lexico.com/'
    # https://www.lexico.com/definition/<>
    #
    # lexico = download_page(target_url)
    # links = extract_links(lexico)

    # for link in links:
    #     print(urljoin(target_url, link))