class Boot:
    """docstring for Boot"""

    def __init__(self, Bootsnummer, Bootsnamen, Leistung, type):
        self.Bootsnummer = Bootsnummer
        self.Bootsnamen = Bootsnamen
        self.Leistung = Leistung
        self.type = type

    def __str__(self):
        return f"\n\nBootszulassung\n******************\nName = {self.type}{self.Bootsnamen}\nNummer = {self.Bootsnummer}\nMotorleistung = {self.Leistung}"


if __name__ == '__main__':
    # eintrag_M = [346, 'Monika', 48]
    # eintrag_S = [123, 'Jimmy', 60]
    eintrag = []
    data = input(
        "Welche Daten moechten Sie erfassen?\nGeben Sie (M/m) fuer Motorboot bzw.\nGeben Sie (S/s) fuer Segelboot ein!\n")
    # if data.lower() == 'm':
    #     boot = Boot(eintrag_M[0], eintrag_M[1], eintrag_M[2], data.upper())
    # elif data.lower() == 's':
    #     boot = Boot(eintrag_S[0], eintrag_S[1], eintrag_S[2], data.upper())
    print("------------------Erfassen der Daten-----------------")
    bootsnummer = int(input("Welche Bootsnummer erhaelt das Boot?\t"))
    eintrag.append(bootsnummer)
    bootsname = input("Welchen Bootsnamen erhaelt das Boot?\t")
    eintrag.append(bootsname)
    leistung = int(input("Welche Leistung hat das Motorboot?\t"))
    eintrag.append(leistung)
    boot = Boot(eintrag[0], eintrag[1], eintrag[2], data.upper())
    print(str(boot))
