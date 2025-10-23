import tkinter as tk
from tkinter import ttk

class Aplikacja:
    def __init__(self, root):
        self.label1 = tk.Label(root, text="przykladowy sprawdzian")
        self.label1.grid(row=0, column=0)

        self.entry = tk.Entry(root)
        self.entry.grid(row=1, column=0)



        self.opcjarb = tk.StringVar()
        self.opcjarb.set("brak")

        self.rb1 = tk.Radiobutton(root, text="111", variable=self.opcjarb, value="111")
        self.rb1.grid(row=2, column=0)

        self.rb2 = tk.Radiobutton(root, text="222", variable=self.opcjarb, value="222")
        self.rb2.grid(row=3, column=0)

        self.rb3 = tk.Radiobutton(root, text="333", variable=self.opcjarb, value="333")
        self.rb3.grid(row=4, column=0)



        self.wartoscsb = tk.StringVar()

        self.spinbox = tk.Spinbox(root, from_=1, to=10, textvariable=self.wartoscsb)
        self.spinbox.grid(row=5, column=0)



        self.opcja1 = tk.BooleanVar(root, value=False)
        self.opcja2 = tk.BooleanVar(root, value=False)
        self.opcja3 = tk.BooleanVar(root, value=True)

        self.cb1 = tk.Checkbutton(root, text="opcja1", variable=self.opcja1)
        self.cb1.grid(row=6, column=0)

        self.cb2 = tk.Checkbutton(root, text="opcja2", variable=self.opcja2)
        self.cb2.grid(row=7, column=0)

        self.cb3 = tk.Checkbutton(root, text="opcja3", variable=self.opcja3)
        self.cb3.grid(row=8, column=0)



        self.wartoslr = tk.StringVar()
        self.wartoslr.set("wybierz opcje")

        self.combo = ttk.Combobox(root, textvariable=self.wartoslr ,values=["1", "2", "3"])
        self.combo.grid(row=9, column=0)



        self.button = tk.Button(root, text="zatwierdz", command=self.pobierz_wartosci)
        self.button.grid(row=10, column=0)

        self.label2 = tk.Label(root, text="")
        self.label2.grid(row=11, column=0)

    def pobierz_wartosci(self):
        self.get_entry = self.entry.get()



        self.get_rb = self.opcjarb.get()



        self.get_sb = self.wartoscsb.get()



        zaznaczone = []

        if self.opcja1.get():
            zaznaczone.append("opcja1")
        if self.opcja2.get():
            zaznaczone.append("opcja2")
        if self.opcja3.get():
            zaznaczone.append("opcja3")



        self.get_lr = self.wartoslr.get()

        self.lista = ", ".join(zaznaczone)

        self.label2.config(text=f"w entry wpisales: {self.get_entry}\n wybrany radiobutton: {self.get_rb} \n wartosc wybrana na spinboxie: {self.get_sb} \n zaznaczone chechbuttony: {self.lista} \n wartosc wybrana z listy: {self.get_lr}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplikacja")
    root.geometry("500x500")
    app = Aplikacja(root)
    root.mainloop()