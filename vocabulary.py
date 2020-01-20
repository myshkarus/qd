#!/usr/bin/python

from abc import ABC, abstractmethod
import constants as c
from crawler import Crawler


class Publisher(ABC):
    @abstractmethod
    def __init__(self, url=None, pattern=None):
        self._entry_url = None
        self.url = url
        self.pattern = pattern
        self.worker = Crawler()

    @property
    def entry_url(self):
        return self._entry_url

    @entry_url.setter
    def entry_url(self, some_url):
        self.worker.entry_url = some_url
        self._entry_url = self.worker.entry_url

    @property
    def url(self): pass

    @url.setter
    @abstractmethod
    def url(self, url): pass

    @property
    def pattern(self): pass

    @pattern.setter
    @abstractmethod
    def pattern(self, pattern): pass

    def get_transcription(self, entry):
        self.entry_url = (self.url, entry)
        transcript = self.worker.do_work(self.pattern['transcription'])
        if len(transcript) > 0:
            return [tr.replace(
                '/', '') for tr in transcript]


class Oxford(Publisher):
    def __init__(self, url=c.ENTRY_URL_OXFORD, pattern=c.PATTERNS_OXFORD):
        super(Oxford, self).__init__()
        self._url = None
        self._pattern = None
        self.pattern = pattern
        self.url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        self._pattern = pattern


class Cambridge(Publisher):
    def __init__(self, url=c.ENTRY_URL_CAMBRIDGE, pattern=c.PATTERNS_CAMBRIDGE):
        super(Cambridge, self).__init__()
        self._url = None
        self._pattern = None
        self.pattern = pattern
        self.url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        self._pattern = pattern


if __name__ == '__main__':
    ox = Oxford()
    print(
        '{0} entry: \'was\' --> transcription {1}'.format(Oxford().__class__.__name__, ox.get_transcription('was')))
    print('entry url: {0}'.format(ox.entry_url))

    print('-' * 50)
    cb = Cambridge()
    print(
        '{0} entry: \'was\' --> transcription {1}'.format(Cambridge().__class__.__name__, cb.get_transcription('was')))
    print('entry url: {0}'.format(cb.entry_url))
