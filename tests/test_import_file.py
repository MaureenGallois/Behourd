from app.import_file import *

from pytest import *

def test_fileExtentionIsGood():
    assert CheckFileExtention() == 'xlsx'

def test_fileExtentionIsBad():
    assert CheckFileExtention() == 'doc'