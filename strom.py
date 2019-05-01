# define the function blocks Tarife
def radio_lightning():
    global Arbeitspreis_in_Netto, Arbeitspreis_in_Brutto, Grundpreis_in_Netto, Grundpreis_in_Brutto
    Arbeitspreis_in_Netto = 24.12
    rbeitspreis_in_Brutto = 28.70
    Grundpreis_in_Netto = 142.68
    Grundpreis_in_Brutto = 169.79


def easy_green():
    global Arbeitspreis_in_Netto, Arbeitspreis_in_Brutto, Grundpreis_in_Netto, Grundpreis_in_Brutto
    Arbeitspreis_in_Netto = 22.92
    Arbeitspreis_in_Brutto = 27.27
    Grundpreis_in_Netto = 69.48
    Grundpreis_in_Brutto = 82.68


def electrical_short():
    global Arbeitspreis_in_Netto, Arbeitspreis_in_Brutto, Grundpreis_in_Netto, Grundpreis_in_Brutto
    Arbeitspreis_in_Netto = 22.35
    Arbeitspreis_in_Brutto = 26.60
    Grundpreis_in_Netto = 80.40
    Grundpreis_in_Brutto = 95.68


# If there's more Tarife:


def more_tarife():
    pass

def main():
    MwSt = 0.19
    print("Stromtarifrechner")
    verbrauch = int(input("Dein Jahresstromverbrauch (in kWh)\n "))
    print("\nIhr passender Stromtarif lautet:")
    print("--------------------------------")
    if verbrauch < 1500:
        tarif = "radio-lightning"
        radio_lightning()
    elif verbrauch >= 1500 and verbrauch <= 3500:
        tarif = "easy-green"
        easy_green()

    elif verbrauch >= 3501:
        tarif = "electrical-short"
        electrical_short()
    print(tarif)
    print("--------------------------------")
    print("\nTarifdaten")
    print("********************************")
    print("Grundpreis/Jahr in Netto: " + str(Grundpreis_in_Netto) + " Euro.")
    Grundpreis_in_Brutto = Grundpreis_in_Netto * (1 + MwSt)
    print("Grundpreis/Jahr in Brutto: " +
          str(Grundpreis_in_Brutto) + " Euro.")
    print("\nArbeitspreis/kWh in Netto: " +
          str(Arbeitspreis_in_Netto) + " Cent.")
    Arbeitspreis_in_Brutto = Arbeitspreis_in_Netto * (1 + MwSt)
    print("Arbeitspreis/kWh in Brutto: " +
          str(Arbeitspreis_in_Brutto) + " Cent.")
    print("\nIhre jährlichen Kosten")
    print("**************************")
    print("Ihr Jahresverbrauch: " + '{0:.1f}'.format(verbrauch) + " kWh")
    print("Gesamtpreis (Netto): " + '{0:.13f}'.format(
        Grundpreis_in_Netto + Arbeitspreis_in_Netto * verbrauch / 100) + " Euro")
    print("Gesamtpreis (zzgl. 19% MwSt): " + '{0:.13f}'.format(
        Grundpreis_in_Brutto + Arbeitspreis_in_Brutto * verbrauch / 100) + " Euro")
if __name__ == '__main__':
    main()
