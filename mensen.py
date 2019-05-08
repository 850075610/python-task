def monday():
    print("Montag\n" + "Herzhafte Kohlroulade mit Schmorkraut und Petersilienkartoffeln" +
          "\nKräuterrührei, dazu Rahmspinat und Salzkartoffeln")


def tuesday():
    print("Dienstag\n" + "Hähnchenschnitzel mit Tomaten-Gnocchi und Rucola" +
          "\nRotes Linsen Dal mit Kräuter-Paprika-Bulgur und marinierten Pflücksalaten")


def wednesday():
    print("Mittwoch\n" + "Coq au vin-Hähnchenkeule in Rotwein geschmort, dazu Buttererbsen und Herzoginkartoffeln" +
          "\nVegetarische Paprikaschote mit Gemüse, Reis und Hirtenkäse gefüllt, dazu Tomatensoße und Kressekartoffeln")


def thursday():
    print("Donnerstag\n" + "Kleine Backfischnuggets (Kibbelinge) mit Remouladensoße, dazu gebackene Kartoffelecken und Salat" +
          "\nScharfes Kürbisgemüse mit Linsen und Rucola auf Penne Rigate")


def friday():
    print("Freitag\n" + "Hausgemachte Kartoffelsuppe mit 1 Paar Wiener Würstchen und Brötchen" +
          "\nVegetarische Gemüselasagne mit Tomatensoße und marinierten Salaten")


def saturday():
    print("Samstag\n" + "Die Mensa ist geschlossen!")


def sunday():
    print("Sonntag\n" + "Die Mensa ist geschlossen!")


def main():
    print("Lieber mensen gehen")
    print("Angebot Mensa WUeins")
    print("********************")
    while True:
        try:
            wochentag = input(
                "Gib deinen gewünschten Wochentag (1 bis 7) ein: \n ")
            switch = {"1": monday, "2": tuesday,
                      "3": wednesday, "4": thursday, "5": friday, "6": saturday, "7": sunday}

            print("Menüplan für ", end='')
            switch[wochentag]()
            break
        except KeyError:
            print("gültigen Wochentag soll nur von 1 bis 7 sein!")

if __name__ == '__main__':
    main()
