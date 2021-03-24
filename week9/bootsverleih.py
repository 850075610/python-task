import tkinter as tk
from tkinter import *
from tkinter import messagebox


class Boot:
    """docstring for Boot"""

    def __init__(self, Bootsnummer, Bootsnamen, Leistung, type):
        self.Bootsnummer = Bootsnummer
        self.Bootsnamen = Bootsnamen
        self.Leistung = Leistung
        self.type = type

    def __str__(self):
        return f"\n\nBootszulassung\n******************\nName = {self.type}{self.Bootsnamen}\nNummer = {self.Bootsnummer}\nMotorleistung = {self.Leistung}"


class MyApp(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fLabel = Label(
            master,
            text="Welche Daten moechten Sie erfassen?\nGeben Sie (M/m) fuer Motorboot bzw.\nGeben Sie (S/s) fuer Segelboot ein!")
        self.fLabel.grid()
        self.fEntry = Entry(master)
        self.fEntry.grid()
        self.submitButton = Button(self.OnButtonClickEvent(), text='submit')
        self.submitButton.grid()
        # self.close_button = Button(...)

    def OnButtonClickEvent(self, event):
        """ handle button click event and get text from entry area"""
        # if:
        #     self.open_button.configure(state="disabled")
        # else:
        #     self.open_button.configure(state="normal")
        pass


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label


if __name__ == '__main__':
    # eintrag_M = [346, 'Monika', 48]
    # eintrag_S = [123, 'Jimmy', 60]
    eintrag = []
    app = MyApp()
    # window = Tk()
    # window.title("Bootsverleih")
    # window.geometry("800x600")

    # lbl = Label(window, text='Welche Daten moechten Sie erfassen?\nGeben Sie (M/m) fuer Motorboot bzw.\nGeben Sie (S/s) fuer Segelboot ein!')
    # make_label(window, 10, 10, 80, 780,
    #            text='Welche Daten moechten Sie erfassen?\nGeben Sie (M/m) fuer Motorboot bzw.\nGeben Sie (S/s) fuer Segelboot ein!',
    #            background='white')


    def button2clicked():
        # eintrag.append()
        pass


    def generate_new_window():
        window2 = Tk()
        window2.title("------------------Erfassen der Daten-----------------")
        window2.geometry("800x600")
        texts = ['Welche Bootsnummer erhaelt das Boot?', 'Welchen Bootsnamen erhaelt das Boot?',
                 'Welche Leistung hat das Motorboot?']
        for i in range(3):
            make_label(window2, 10, 10 + i * 100, 30, 780,
                       text=texts[i], background='white')
            txt2 = Text(window2, height=2, width=300)
            window2.update()
            txt2.place(x=window2.winfo_width() / 2.5,
                       y=40 + i * 100, width=120, height=25)
        btn2 = Button(window2, text='submit', command=button2clicked)
        # window2.update()
        btn2.place(x=window2.winfo_width() / 2.5,
                   y=window2.winfo_height() / 2, width=120, height=25)


    def clicked():
        """ handle button click event and get text from entry area"""
        ret = txt.get("1.0", 'end-1c')
        # ret = "Hallo " + ret
        # return ret
        # msg = messagebox.showinfo("Hello Python", "Hello World")
        generate_new_window()


    # btn1 = Button(window, text='submit', command=clicked)
    # window.update()
    # btn1.place(x=window.winfo_width() / 2.5, y=200, width=120, height=25)
    # txt = Text(window, height=2, width=300)
    # txt.place(x=window.winfo_width() / 2.5, y=100, width=120, height=25)
    # lbl.grid(column=0, row=0)
    # btn1.grid(column=0, row=2)
    # txt.grid(column=0, row=1)

    # window.mainloop()
    # data = messagebox.showinfo(
    #     "Welche Daten moechten Sie erfassen?\nGeben Sie (M/m) fuer Motorboot bzw.\nGeben Sie (S/s) fuer Segelboot ein!\n")
    # if data.lower() == 'm':
    #     boot = Boot(eintrag_M[0], eintrag_M[1], eintrag_M[2], data.upper())
    # elif data.lower() == 's':
    #     boot = Boot(eintrag_S[0], eintrag_S[1], eintrag_S[2], data.upper())
    # print("------------------Erfassen der Daten-----------------")
    # lbl.configure(text='------------------Erfassen der Daten-----------------')
    # messagebox_bootsnummer = messagebox.showinfo(
    #     "Welche Bootsnummer erhaelt das Boot?\t")
    # bootsnummer
    # eintrag.append(bootsnummer)
    # bootsname = input("Welchen Bootsnamen erhaelt das Boot?\t")
    # eintrag.append(bootsname)
    # leistung = int(input("Welche Leistung hat das Motorboot?\t"))
    # eintrag.append(leistung)
    # boot = Boot(eintrag[0], eintrag[1], eintrag[2], data.upper())
    # print(str(boot))
