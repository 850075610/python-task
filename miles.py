def main():
    print("*****************************")
    print("Kraftstoffverbrauch eines Kfz")
    print("*****************************")
    distance = int(
        input('Bitte die gewünschte Kilometer-Entfernung eingeben:\n '))
    liter = int(input('Bitte den Liter-Betrag des Verbrauches eingeben:\n '))
    print("Der Kraftstoffverbrauch beträgt durchschnittlich: " +
          '{0:.15f}'.format(liter / distance * 100))
if __name__ == '__main__':
    main()
