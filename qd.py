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
        for key, value in words_dict.items():
            if not value.strip():
                print('key: {0}; value: {1}; len: {2}'.format(
                    key, value, len(value)))
                words_dict[key] = strategy().get_transcription(key)
        pprint.pprint(words_dict)


if __name__ == '__main__':
    w = Worker()
    w.run()
