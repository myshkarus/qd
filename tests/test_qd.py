import sys
sys.path.append('../')

import qd
import pytest


@pytest.fixture
def word_object():
    file = 'dict.xlsx'
    language = qd.Language.English
    wd = qd.Words(file, language)
    return wd


def test_filename():
    assert word_object.filename == 'dict.xlsx'


def test_language(word_object):
    assert word_object.lang == qd.Language.English


def test_setup_file(word_object):
    word_object.source_file = 'somefile.xlsx'
    assert word_object.source_file == 'somefile.xlsx'
