from app.import_file import *

from pytest import *

def test_fileExtentionIsGood():
    assert import_file.CheckFileExtention("Exemple1.xslx") == True

def test_fileExtentionIsBad():
    assert CheckFileExtention("Truc.pdf") == False