def main():
    print("Pick dig")
    print("*************\n")
    inner = int(input("Anzahl der inneren Gitterpukten: "))
    out = int(input("Anzahl der äußeren Gitterpukten "))

    pick(inner, out)


def pick(inner, out):
    result = out + inner / 2 - 1
    print("Pick sagt " + str(result) + " Gitterquadrateeinheiten.")

if __name__ == '__main__':
    main()
