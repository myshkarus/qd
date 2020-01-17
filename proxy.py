#!/usr/bin/python

from configparser import ConfigParser
import os
import sys

sys.path.append(os.path.abspath('./'))


def setup():
    try:
        config = ConfigParser()
        with open('./config/config.ini') as f:
            config.read_file(f)
            config.read(f, encoding='utf-8')
    except IOError as err:
        print('config.ini is not exist: ', err)

    proxy = config.get('proxy', 'url')
    print('proxy: ', proxy)

    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy


if __name__ == '__main__':
    setup()
