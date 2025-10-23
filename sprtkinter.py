#import biblioteki "tkinter" i odwolywanie sie do niej skrotem 'tk', przez to ze aliasem jest tk, nie musimy importowac kazdej klasy/metody z tej biblioteki, tylko piszemy "tk.nazwa_klasy/metody"
import random
import tkinter as tk
from tkinter import ttk

class Aplikacja:
    def __init__(self, okno):
        self.okno = okno

        self.label1 = tk.Label(okno, text="label1")
        self.label1.grid(row=0, column=0)
        
        self.tekst1 = tk.StringVar()
        self.entry1 = tk.Entry(okno, textvariable=self.tekst1)
        self.entry1.grid(row=0, column=1)
        
        self.button1 = tk.Button(okno, text="przycisk1")
        self.button1.grid(row=0, column=2)
        
        


        
        self.wyborrb = tk.StringVar()
        self.wyborrb.set("brak")

        self.labelrb = tk.Label(okno, text="wybierz opcje:")
        self.labelrb.grid(row=1, column=0)

        self.rb1 = tk.Radiobutton(okno, text="111", variable=self.wyborrb ,value="opcja1", command=self.wynik_radiobutton)
        self.rb1.grid(row=2, column=0)

        self.rb2 = tk.Radiobutton(okno, text="222", variable=self.wyborrb ,value="opcja2", command=self.wynik_radiobutton)
        self.rb2.grid(row=3, column=0)

        self.rb3 = tk.Radiobutton(okno, text="333", variable=self.wyborrb ,value="opcja3", command=self.wynik_radiobutton)
        self.rb3.grid(row=4, column=0)

        self.wynikrb = tk.Label(okno, text=f"twoj wybor: ")
        self.wynikrb.grid(row=5, column=0)





        self.wartoscsb = tk.StringVar(value="1")
    

        self.labelsb = tk.Label(okno, text="wybierz liczbe:")
        self.labelsb.grid(row=6, column=0)

        self.spinbox = tk.Spinbox(okno, from_=1, to=10, textvariable=self.wartoscsb, command=self.wartosc_spinbox)
        self.spinbox.grid(row=6, column=1)

        self.wyniksb = tk.Label(okno, text="aktualna wartosc: ")
        self.wyniksb.grid(row=7, column=0)





        self.labelchb = tk.Label(okno, text="opcje checkbutton")
        self.labelchb.grid(row=8, column=0)

        self.opcjachb1 = tk.BooleanVar(value=False)
        self.opcjachb2 = tk.BooleanVar(value=False)
        self.opcjachb3 = tk.BooleanVar(value=True)

        self.chb1 = tk.Checkbutton(okno, text="opcja1", variable=self.opcjachb1, command=self.pokazywanie_checkbutton)
        self.chb1.grid(row=9, column=0)

        self.chb2 = tk.Checkbutton(okno, text="opcja2", variable=self.opcjachb2, command=self.pokazywanie_checkbutton)
        self.chb2.grid(row=10, column=0)

        self.chb3 = tk.Checkbutton(okno, text="opcja3", variable=self.opcjachb3, command=self.pokazywanie_checkbutton)
        self.chb3.grid(row=11, column=0)

        self.wynikchb = tk.Label(okno, text="")
        self.wynikchb.grid(row=12, column=0)
  




        self.wyborlr = tk.StringVar(value="wybierz opcje")

        self.labellr = tk.Label(okno, text="wybierz cos z listy")
        self.labellr.grid(row=13, column=0)

        self.combo = ttk.Combobox(okno,
            textvariable=self.wyborlr,
            values=["1", "2", "3", "4", "5"])
        self.combo.grid(row=14, column=0)
        self.combo.bind("<<ComboboxSelected>>", self.pokazywanie_wartosci_z_lr)

        self.wyniklr = tk.Label(okno, text="")
        self.wyniklr.grid(row=15, column=0)





        self.kolor_domyslny = self.okno.cget("bg")

        self.labelb1 = tk.Label(okno, text="przyciski")
        self.labelb1.grid(row=16, column=0)

        self.labelb2 = tk.Label(okno, text="zmien kolor tla")
        self.labelb2.grid(row=17, column=0)

        self.button2 = tk.Button(okno, text="zielony", command=self.zielone_tlo)
        self.button2.grid(row=17, column=1)

        self.button3 = tk.Button(okno, text="domyslne", command=self.domyslne_tlo)
        self.button3.grid(row=17, column=2)





        self.labelb3 = tk.Label(okno, text="zmien kolor przycisku")
        self.labelb3.grid(row=18, column=0)    

        self.button4 = tk.Button(okno, text="czerwony", command=self.czerwone_tlo)
        self.button4.grid(row=18, column=1)





        self.labelb4 = tk.Label(okno, text="zmiana koloru, rozmiaru i typu czcionki")
        self.labelb4.grid(row=19, column=0)

        self.button5 = tk.Button(okno, text="rozowa czcionka", command=self.rozowa_czcionka)
        self.button5.grid(row=20, column=0)

        self.button6 = tk.Button(okno, text="italic 12px", command=self.rozmiar_typ)
        self.button6.grid(row=20, column=1)





        self.labelb5 = tk.Label(okno, text="zmien rozmiar okna")
        self.labelb5.grid(row=21, column=0)

        self.button7 = tk.Button(okno, text="500x500", command=self.rozmiar_okna_500x500)
        self.button7.grid(row=22, column=0)

        self.button8 = tk.Button(okno, text="1000x500", command=self.rozmiar_okna_1000x500)
        self.button8.grid(row=22, column=1)

        self.button9 = tk.Button(okno, text="500x1000", command=self.rozmiar_okna_500x1000)
        self.button9.grid(row=22, column=2)




    def wynik_radiobutton(self):
        self.wynikrb.config(text="twoj wybor: " + self.wyborrb.get())  

    def wartosc_spinbox(self):
        self.wyniksb.config(text="aktualna wartosc: " + self.wartoscsb.get())

    def pokazywanie_checkbutton(self):
        zaznaczone = []
        if self.opcjachb1.get():
            zaznaczone.append("opcja1")
        if self.opcjachb2.get():
            zaznaczone.append("opcja2")
        if self.opcjachb3.get():
            zaznaczone.append("opcja3")

        if zaznaczone:
            self.wynikchb.config(text="zaznaczone: " + ", ".join(zaznaczone))
        else:
            self.wynikchb.config(text="nic nie zaznaczono")

    def pokazywanie_wartosci_z_lr(self, event):
        self.wyniklr.config(text=f"wybrales: {self.wyborlr.get()}")

    def zielone_tlo(self):
        self.okno.config(bg="lightgreen")

    def domyslne_tlo(self):
        self.okno.config(bg=self.kolor_domyslny)

    def czerwone_tlo(self):
        self.button4.config(bg="red")

    def rozowa_czcionka(self):
        self.labelb4.config(fg="pink")

    def rozmiar_typ(self):
        self.labelb4.config(font="none 12 italic")

    def rozmiar_okna_500x500(self):
        self.okno.geometry("500x500")
    
    def rozmiar_okna_1000x500(self):
        self.okno.geometry("1000x500")

    def rozmiar_okna_500x1000(self):
        self.okno.geometry("500x1000")

#przypisanie okna do jednej zmiennej, bo trzeba sie do tego okna odwolywac potem przy kazdym widgecie zeby python kumal ze ma wrzucic ten widget do okna
okno = tk.Tk()

#ustawienie tytulu aplikacji
okno.title("Tytul okna")

#ustawienie wymiarow aplikacji w pixelach, trzeba to dac w cudzyslowie bo inaczej nie zadziala
okno.geometry("1000x1000")

#ustawienie tego czy mozna poszerzac okno czy nie, pierwszy argument to szerokosc, a drugi wysokosc(jak chcemy zeby sie rozszerzalo dajemy "True" jak nie to "False")
okno.resizable(False, False)

#przypisanie obrazku do zmiennej, dawajcie png zawsze bo zadziala, nwm jak z innymi rozszerzeniami, fota musi byc w tym samym folderze, zeby python wykminil ze to ten konkretny obrazek
icon = tk.PhotoImage(file="elektron.png")

#ustawienie obrazku jako ikonke aplikacji, "True" jest po to, zeby python skumal ze ikonka jest aktywna i mial ja zmienic na obrazek przypisany do zmiennej "icon"
okno.iconphoto(True, icon)

#prosze mnie nie pytac po co to bo nie mam pojecia co i dlaczego, bez tego nic sie nie wyswietli jezeli robicie do obiektowo, po prostu macie to kurwa dac i chuj, dla ambitnych wpisac w google ps. chyba chodzi o przypisanie wartosci ale nw
app = Aplikacja(okno)

#wyswietlenie okna
okno.mainloop()