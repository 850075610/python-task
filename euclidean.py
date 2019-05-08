def euclidean(one, other):
    if one == other:
        return one
    elif one > other:
        one -= other
        # print("Current one = " + str(one))
        return euclidean(one, other)
    elif one < other:
        other -= one
        # print("Current other = " + str(other))
        return euclidean(one, other)
    elif one == 0:
        return other
    elif other == 0:
        return one


def main():
    print("**************")
    print("* GREEK GEEK *")
    print("**************")

    while True:
        try:
            one = int(input("Bitte geben sie eine ganze, positive Zahl ein.\n "))
            other = int(
                input("Bitte geben sie eine ganze, positive Zahl ein.\n "))
            result = euclidean(one, other)
        # print(result)
            print("Ergebnis: " + str(result))
            break
        except ValueError:
            print("Positive Nummer soll gegeben werden!")

if __name__ == '__main__':
    main()
