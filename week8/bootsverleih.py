class Boot:
    """docstring for Boot"""

    def __init__(self, Bootsnummer, Bootsnamen, Leisung, type):
        self.Bootsnummer = Bootsnummer
        self.Bootsnamen = Bootsnamen
        self.Leisung = Leisung
        self.type = type

    def __str__(self):
        return f"\n------------------Erfassen der Daten-----------------\nWelche Bootsnummer erhaelt das Boot?\t{self.Bootsnummer}\nWelchen Bootsnamen erhaelt das Boot?\t{self.Bootsnamen}\nWelche Leisung hat das Motorboot?\t\t{self.Leisung}\n\nBootszulassung\n******************\nName = {self.type}{self.Bootsnamen}\nNummer = {self.Bootsnummer}\nMotorleistung = {self.Leisung}"


if __name__ == '__main__':
    eintrag_M = [346, 'Monika', 48]
    eintrag_S = [123, 'Jimmy', 60]
    data = input(
        "Welche Daten moechten Sie erfassen?\nGeben Sie (M/m) fuer Motorboot bzw.\nGeben Sie (S/s) fuer Segelboot ein!\n")
    if data.lower() == 'm':
        boot = Boot(eintrag_M[0], eintrag_M[1], eintrag_M[2], data.upper())
    elif data.lower() == 's':
        boot = Boot(eintrag_S[0], eintrag_S[1], eintrag_S[2], data.upper())
    print(str(boot))
