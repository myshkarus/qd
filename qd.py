#!/usr/bin/python

from enum import Enum, auto



class Language(Enum):
    English = auto()
    German = auto()





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
