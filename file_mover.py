# Das Programm ist hauptsächlich für mich selbst, um meine Dateien schneller einzuordnen,
# ohne selbst in die Ordner navigieren zu müssen oder Verknüpfungen der Ordner zu erstellen

# Die jeweiligen Pfade können natürlich je nach Belieben angepasst werden, wenn jemand dieses Programm für sich
# selbst nutzen will :-).

import shutil
import os
import sys
import getpass

username = getpass.getuser()

# Semesterangabe, falls Ordner in Semester unterteilt.
semester = input("Gib das Semester (als Zahl) an, zu der die Datei gehört: ") + ". Semester"

startpfad = os.path.join('/Users', username, 'OneDrive', 'Uni', 'FU', semester)

def check_datei(dateiname):
    module = ["ALP3", "ALP4", "TI2", "TI3", "Statistik", "Statistik_II"]
    uebungen = reversed([f"U{i}" for i in range(1, 15)])

    # Wenn Modulname und Uebungsnummer im Dateinamen vorhanden sind, suche Datei
    matches = [(mod, ueb) for mod in module for ueb in uebungen if mod in dateiname and ueb in dateiname]
    if matches:
        modul = matches[0][0]
        uebung = matches[0][1]
        zielpfad = os.path.join(startpfad, modul, uebung)
        if os.path.exists(zielpfad):
            verschiebe_datei(dateiname, zielpfad)
        else:
            check_pfad(dateiname, zielpfad)
    else:
        print("Datei nicht gefunden.")


def check_pfad(datei, pfad):
    ordner_teile = pfad.split(os.path.sep)
    for i in range(1, len(ordner_teile) + 1):
        teilpfad = os.path.join(*ordner_teile[:i])
        if not os.path.exists(teilpfad):
            ordner_erstellen = input(f"Der Ordner '{teilpfad}' existiert nicht.\nSoll dieser Ordner erstellt werden? (Y/N): ")
            if ordner_erstellen.lower() == ('y'):
                os.makedirs(teilpfad)
                check_datei(datei)
            else:
                print("Vorgang abgebrochen, Ordner wird nicht erstellt.")
                break

def verschiebe_datei(dateiname, zielort):
    verzeichnis_pfad = os.getcwd()
    dateien = os.listdir(verzeichnis_pfad)
    # verschiebe alle Dateien die den richtigen Dateinamen haben (Übungsname + Nummer)
    gefunden = [datei for datei in dateien if dateiname in datei]
    if gefunden:
        print(f"gefundene Dateien: {gefunden}")
        for datei in gefunden:
            print(f"Datei {datei} wird nach {zielort} verschoben")
            source = os.path.join(verzeichnis_pfad, datei)
            shutil.move(source, zielort)
    else:
        print(f"Keine Datei/en mit diesem Namen in Verzeichnis {verzeichnis_pfad} gefunden")

if len(sys.argv) != 2:
    print("Bitte gebe genau einen Dateinamen an")
else:
    argument = sys.argv[1]
    check_datei(argument)