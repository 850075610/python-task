def main():
    print("*****************************")
    print("Kraftstoffverbrauch eines Kfz")
    print("*****************************")
    distance = int(
        input('\nBitte die gewünschte Kilometer-Entfernung eingeben:\n '))
    liter = int(input('Bitte den Liter-Betrag des Verbrauches eingeben:\n '))
    if distance > 0:
        print("\nDer Kraftstoffverbrauch beträgt durchschnittlich: " +
              '{0:.15f}'.format(liter / distance * 100))
    else:
        print("\nDie gewünschte Kilometer-Entfernung soll immer positiv sein!")
if __name__ == '__main__':
    main()
