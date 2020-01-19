#!/usr/bin/python

import proxy
from urllib.request import urlopen, urljoin
import re


class Crawler:
    def __init(self):
        self._entry_url = None

    @property
    @classmethod
    def entry_url(self):
        return self._entry_url

    @entry_url.setter
    @classmethod
    def entry_url(self, some_url):
        print(some_url)
        try:
            base_url, entry = some_url
            self._entry_url = urljoin(base_url, entry)
            print(self._entry_url)
        except:
            raise NotImplementedError
        return self._entry_url

    @classmethod
    def do_work(self, pattern):
        pass
        # page = self._download_page()
        # return self._extract_data(page, pattern)

    @classmethod
    def _download_page(self):
        return urlopen(self.entry_url).read().decode('utf-8')

    @classmethod
    def _extract_data(self, page, pattern):
        data_pattern = re.compile(pattern, re.IGNORECASE | re.DOTALL)
        data = data_pattern.findall(page)
        return data


if __name__ == '__main__':
    c = Crawler()
