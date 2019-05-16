def romanum(zahl):
    result = 0
    if zahl.islower():
        print("Please check the validity of input, it should be in uppercase!")
    else:
        for x in zahl:
            if x == 'I':
                result += 1
            elif x == 'V':
                result += 5
            elif x == "X":
                result += 10
            elif x == "L":
                result += 50
            elif x == "C":
                result += 100
            elif x == 'D':
                result += 500
            elif x == 'M':
                result += 1000
    print("\nDeine Zahl lautet: " + str(result))


def main():
    print("Imperium Romanum\n")
    zahl = input("Bitte eine römische Zahl eingeben: ")
    romanum(zahl)


if __name__ == '__main__':
    main()
