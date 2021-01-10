# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random
from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super (Application,self).__init__(master)
        self.create_widgets()
        self.grid()
        self.random_number()

    def create_widgets(self):
        Label(self, text="Witaj w grze 'Jaka to liczba'!").grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,text="Mam na myśli pewną liczbę z zakresu od 1 do 100.").grid(row=1, column=0, columnspan=2, sticky=W)
        Label(self, text="Spróbuj ją odgadnąć w jak najmniejszej liczbie prób").grid(row=2, column=0, columnspan=2, sticky=W)

        Label(self, text="Ta liczba to: ").grid(row=3, column=0, sticky=W)
        self.guess_txt=Entry(self)
        self.guess_txt.grid(row=3, column=1, sticky=W)

        Button(self,
               text="Zgaduję!",
               command=self.check
               ).grid(row=4, column=0, sticky=W)

        self.comp_answer=Text(self, width=50, height=5, wrap=WORD)
        self.comp_answer.grid(row=5, column=0, columnspan=2, sticky=W)

    def random_number(self):

        self.the_number = random.randint(1, 100)
        self.tries=0

    def check(self):

        self.tries += 1
        guess_int=int(self.guess_txt.get())

        if guess_int > int(self.the_number):
            answer= "Podałeś zbyt dużą liczbę..."
        if guess_int< self.the_number:
            answer="Podałeś zbym małą liczbą..."
        if guess_int==self.the_number:
            answer="Brawo! Chodziło właśnie o "+str(self.the_number)+"."
            answer+="\nDo odgadnięcia potrzebowałeś "+str(self.tries)+" prób."

        self.comp_answer.delete(0.0, END)
        self.comp_answer.insert(0.0, answer)

root= Tk()
root.title("Zgadnij, jaka to liczba.")
app=Application(root)
root.mainloop()


