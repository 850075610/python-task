import datetime


class Student(object):
    """docstring for Student"""

    def __init__(self, name, Vorname, Geburtsdatum, Studiengang, Matrikelnummer):
        super(Student, self).__init__()
        self.name = name
        self.Vorname = Vorname
        self.Geburtsdatum = Geburtsdatum
        self.Studiengang = Studiengang
        self.Matrikelnummer = Matrikelnummer


if __name__ == '__main__':
    print("Welcome to the student management system and we need to enter information for 2 students.")
    students = []
    ordinal = ['1st.', '2nd.', '3rd.']
    for i in range(2):
        if i < 3:
            print("\nInformation for the " + ordinal[i] + " student: ")
        else:
            print("\nInformation for the " + str(i + 1) + "th" + " student: ")
        name = input("Please enter the surname: ")
        vorname = input("Please enter the first name: ")
        year, month, day = input(
            "Please enter the date of birth in the order of year, month and day separated by a space: ").split(" ")
        geburtsdatum = datetime.datetime((int)(year), (int)(month), (int)(day))
        studiengang = input("Please enter the course of studies: ")
        matrikelnummer = input("Please enter the matriculation number: ")
        students.append(Student(name, vorname, geburtsdatum, studiengang, matrikelnummer))
    print("\nBasic information of students: \n")
    print("Vorname" + "\tName" + "\tGeburtsdatum" + "\tStudiengang" + "\tMatrikelnummer")
    for s in students:
        print(
            s.Vorname + "\t" + s.name + "\t" + str(s.Geburtsdatum)[
                                               :11] + "\t" + s.Studiengang + "\t" + s.Matrikelnummer)
