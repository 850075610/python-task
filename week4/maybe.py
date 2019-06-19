def search():
    eintrag = {'Ludwig-Müller, Jutta': ['Fakultät Biologie', '(0351) 463-33939'], 'Müller, Anja': ['Fakultät Maschinenwesen', '(0351) 463-42096'], 'Müller, Bernhard': ['Fakultät Umweltwissenschaften', '(0351) 463-37890'], 'Müller, Christian': [
        'Fakultät Erziehungswissenschaften', '(0351) 463-39943'], 'Müller, Claudia': ['Philosophische Fakultät', '(0351) 463-35806'], 'Müller, Egbert': ['Fakultät Bauingenieurwesen', '(0351) 463-37305']}
    while True:

        print("Telefonverzeichnis")
        print("******************")
        print("\nAktuelle Einträge:")
        for x in eintrag.keys():
            print(x)
        person = input("Für welche Person brauchst du mehr Infos?\n ")
        for key, detail in eintrag.items():
            if person == key:
                print("\n", detail[0])
                print(detail[1])
                return
        if person not in eintrag.keys():
            print('Given name doesn\'t exist, please check your input!\n')


def main():
    search()

if __name__ == '__main__':
    main()
