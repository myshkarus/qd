#!/usr/bin/python

from configparser import ConfigParser
import os
import sys

sys.path.append(os.path.abspath('./'))


def _retrieve_config():
    try:
        config = ConfigParser()
        with open('./config/config.ini') as f:
            config.read_file(f)
            config.read(f, encoding='utf-8')
    except IOError as err:
        print('config.ini is not exist: ', err)
    return config


def setup():
    proxy = config.get('proxy', 'url')
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy


def use_proxy():
    if bool(config.getboolean('Default', 'use_proxy')):
        return True


config = _retrieve_config()

if __name__ == '__main__':
    setup()
