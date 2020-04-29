import csv
import random
import sys

import pandas as pd


def zufall():
    f = open('Europawahlzettel.csv', 'rt')
    reader = csv.reader(f)

    # Im Zufallsmodus sollen einfach 3 Kandidierende inkl. deren hinterlegten Informationen zufällig
    # ausgegeben werden.

    row_list = []

    for row in reader:
        row_list.append(row)
        # print(row)
    # print(len(row_list))
    # print(row_list)

    for i in range(3):
        print(row_list[random.randint(1, len(row_list) - 1)])
    f.close()


def spezifisch():
    # valid_input = ['Ja', 'Nein']

    print('Spezifische Auswahl')
    partei_wichtig = True if input(
        'Ist dir die Partei wichtig? [Ja/Nein, alle Nicht \'Ja\' Eingaben werden als \'Nein\' gewertet.]\n') == 'Ja' else False
    # print(partei_wichtig)

    # If pass sys.argv[1] as parameter, then have to check if this parameter
    # is given
    df = pd.read_csv('Europawahlzettel.csv')
    partei_list = df['Partei'].drop_duplicates(
    ).values.tolist()  # can also use df.column_name
    if partei_wichtig:
        print("Partei " + str(partei_list))
        partei = input("")
    listenplatz_wichtig = True if input(
        'Ist dir der Listenplatz wichtig? [Ja/Nein, alle Nicht \'Ja\' Eingaben werden als \'Nein\' gewertet.]\n') == 'Ja' else False
    if listenplatz_wichtig:
        listenplatz = int(input("Listenplatz\n"))
    weiterer_listenplatz = True if input(
        'Soll ein weiterer Listenplatz einbezogen werden? [Ja/Nein, alle Nicht \'Ja\' Eingaben werden als \'Nein\' gewertet.]\n') == 'Ja' else False
    if weiterer_listenplatz:
        # print(df[(df.Listenplatz == listenplatz) & (df.Bundesland.isin(['SN', 'BE']))])
        pass
    print("Ausgabe der Kandidaten\n")
    # multiple filter criteria: df[df.columnname.isin([])]
    if listenplatz_wichtig and partei_wichtig:
        print(df[(df.Partei.isin([partei, ])) &
                 (df.Listenplatz == listenplatz)])
    elif partei_wichtig:
        print(df[df.Partei.isin([partei, ])])
    elif listenplatz_wichtig:
        print(df[df.Listenplatz == listenplatz])
    else:
        zufall()


def main():
    modus = int(input('Wähle eine Modus (1) Zufall oder (2) Spezifisch\n'))
    if modus == 1:
        zufall()
    elif modus == 2:
        spezifisch()


if __name__ == '__main__':
    main()
