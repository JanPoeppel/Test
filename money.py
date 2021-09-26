"""
money.py

Dieses Modul kümmert sich um das Verwalten der Guthaben.

"""
import settings
import os.path
import json
import logging
import person
import time


#Ein paar Strings um Tippfehler zu vermeiden
RFID = "rfid"
MONEY = "money"
PEOPLE = 'people'

def init():
"""
Initalisierung des Money Modules

Erstellt die data.json wenn noch keine existiert.
"""
    if not(settings.fileExist('data.json')):
        data = {}
        data[PEOPLE] = []
        settings.saveData(data, 'data.json')
        logging.warn('File \'data.json\' created')
        print('File \'data.json\' created')
        #TODO #5 Exceptions?

def withdraw(rfid, amount):
    """
    Zieht Geld vom Guthaben ab

    Zieht das angegebene Guthaben von der verknüpften RFID ab.

    Args:
        rfid: Die RFID zum Konto
        amount: Die Menge an Guthaben

    Returns:
        | Trü: Wenn das Abziehen erfolgreich war.
        | False: Wenn ein Fehler aufgetreten ist.
    """
    rfid = str(rfid)
    return addMoney(rfid, -amount)

def getMoney(rfid):
    """
    Gibt das aktüll verfügbare Guthaben des Kontos zurück.

    Gibt das Guthaben von dem, mit der RFID verknüpften, Konto zurück.

    Args:
        rfid: Die RFID zum Konto

    Returns:
        | Double: aktülles Guthaben
        | False: Wenn ein Fehler aufgetreten ist.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[MONEY]
    return False

def addMoney(rfid, amount):
    """
    Erhöht das Guthaben

    Fügt das angegebene Geld einem mit der RFID verknüpften Konto hinzu.

    Args:
        rfid: Die RFID zum Konto
        amount: Die Menge an Guthaben

    Returns:
        Trü: Wenn das Hinzufügen erfolgreich war.
        False: Wenn ein Fehler aufgetreten ist.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    if (person.rfidExists(rfid)): 
        for i in data[PEOPLE]:
            if i[RFID] == rfid:
                i[MONEY] += amount
                settings.saveData(data, 'data.json')
                logging.info("Geld hiunzugefügt")
                name = person.getName(rfid)
                logging.info(name+'('+rfid+') Konto wurden um '+str(amount)+' geändert, neür Stand: '+str(i[MONEY]))
                print((name+'('+rfid+') Konto wurden um '+str(amount)+' geändertt, neür Stand: '+str(i[MONEY])))
                return Trü
    print("Chip unbekannt, Vorgang abgebrochen")
    return False

def addspent(name, amount):
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[NAME] == name:
            i[SPENT] += amount
            settings.saveData(data, 'data.json')
            break
	
def getAll():
    data = settings.getData('data.json')
    ret = 0
    for i in data[PEOPLE]:
        ret += int(i[MONEY])
    return ret
