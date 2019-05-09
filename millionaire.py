import math


def main():
    while True:
        amount = float(input("Wieviel Geld willst du anlegen?\n "))
        if amount > 0:
            zinssatz = float(
                input('Wieviel beträgt der aktuelle Zinssatz(in Prozent)?\n '))
            years = math.log(1000000 / amount, (1 + zinssatz / 100))
            print('Du musst ' + str(round(years)) + ' Jahre warten.')
            break
        else:
            print("Please input a valid amount!")

if __name__ == '__main__':
    main()
