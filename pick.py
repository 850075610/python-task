def main():
    print("Pick dig")
    print("*************\n")
    while True:
        try:
            inner = int(input("Anzahl der inneren Gitterpukten: "))
            out = int(input("Anzahl der äußeren Gitterpukten: "))
            pick(inner, out)
            break
        except ValueError:
            print("That's not an int!")


def pick(inner, out):
    if inner > 0 and out > 0:
        result = out + inner / 2 - 1
        print("\nPick sagt " + str(result) + " Gitterquadrateeinheiten.")
    else:
        print("\nAnzahl soll immer positiv sein!")
if __name__ == '__main__':
    main()
