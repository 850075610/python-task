def romanum(zahl):
    result = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if zahl.islower():
        print("Please check the validity of input, it should be in uppercase!")
    else:
        for x in range(0, len(zahl) - 1):
            # print(zahl[x])
            if d[zahl[x]] < d[zahl[x + 1]]:
                result -= d[zahl[x]]
            else:
                result += d[zahl[x]]
        result += d[zahl[len(zahl) - 1]]

    print("\nDeine Zahl lautet: " + str(result))


def main():
    print("Imperium Romanum\n")
    zahl = input("Bitte eine römische Zahl eingeben: ")
    # show attribute of string
    # print(dir(zahl))
    romanum(zahl)


if __name__ == '__main__':
    main()
