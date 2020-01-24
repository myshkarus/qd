#!/usr/bin/python

import vocabulary as strategy
from words import Language as l
import words
import constants
import pprint


class Worker:
    def __init__(self, lang: l = l.English):
        self._lang = None
        self.lang = lang

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang: l = l.English):
        self._lang = lang

    def run(self, strategy: strategy.Publisher = strategy.Oxford):
        words_from_file = words.get_words_list(self.lang)
        words_dict = words.to_transcript(words_from_file)
        pprint.pprint(words_dict)
        i = 0
        for key, value in words_dict.items():
            if not value.strip():
                print('+' * i)
                words_dict[key] = strategy().get_transcription(key)
                i += 1
        pprint.pprint(words_dict)


if __name__ == '__main__':
    w = Worker()
    w.run()
