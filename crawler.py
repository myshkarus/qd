#!/usr/bin/python

import proxy
from urllib.request import urlopen, urljoin
import re

if proxy.use_proxy():
    proxy.setup()


class Crawler:
    def __init(self):
        self._entry_url = None

    @property
    def entry_url(self):
        return self._entry_url

    @entry_url.setter
    def entry_url(self, some_url):
        try:
            base_url, entry = some_url
            self._entry_url = urljoin(base_url, entry)
        except:
            raise NotImplementedError

    def do_work(self, pattern):
        page = self._download_page()
        return self._extract_data(page, pattern)

    def _download_page(self):
        try:
            page = urlopen(self.entry_url).read().decode('utf-8')
            return page
        except:
            pass

    def _extract_data(self, page, pattern):
        # print(type(page))
        if page is not None:
            data_pattern = re.compile(pattern, re.IGNORECASE | re.DOTALL)
            data = data_pattern.findall(page)
            # print('===> crawling')
            return data


if __name__ == '__main__':
    c = Crawler()
