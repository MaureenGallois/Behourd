from xlrd import *

def CheckFileExtension(fileName):
    if(fileName != None and fileName.find(".xlsx") != -1 or fileName.find(".csv") != -1):
        return True
    else:
        print("Veuillez insérer un fichier .xlsx ou .csv")
        return False
