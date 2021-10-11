import app.import_file as file

from pytest import *

def test_fileExtentionIsGood():
    assert file.CheckFileExtension("Exemple1.xlsx") == True

def test_fileExtentionIsBad():
    assert file.CheckFileExtension("Truc.pdf") == False