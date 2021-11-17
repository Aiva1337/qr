from tkinter import *
import os
import pyqrcode

langas = Tk()
langas.title("QR kodo generatorius")
langas.iconbitmap('qr.ico')

def sukurti():
    if len(objektas.get()) != 0:
        global qr, nuotrauka
        qr = pyqrcode.create(objektas.get())
        nuotrauka = BitmapImage(data=qr.xbm(scale=8))
    else:
        print("Iveskite eilute, kuri bus paversta QR kodu")
    try:
        rodyti()
    except:
        pass


def rodyti():
    paveikslop.config(image=nuotrauka)
    pavadinimas.config(text="QR kodas " + objektas.get())



langas1 = langas
pavadinimas1 = Label(langas1, text="Iveskite norima teksta")
pavadinimas1.grid(row=0, column=0, sticky=N + S + W + E)
objektas = StringVar()
objektoi = Entry(langas1, textvariable=objektas)
objektoi.grid(row=0, column=1, sticky=N + S + W + E)
sukurimom = Button(langas1, text="Sukurti", width=15, command=sukurti)
sukurimom.grid(row=0, column=3, sticky=N + S + W + E)
paveikslop = Label(langas1)
paveikslop.grid(row=2, column=1, sticky=N + S + W + E)
pavadinimas = Label(langas1, text="")
pavadinimas.grid(row=3, column=1, sticky=N + S + W + E)



Rows = 2
Columns = 3

for row in range(Rows + 1):
    langas1.grid_rowconfigure(row, weight=1)

for col in range(Columns + 1):
    langas1.grid_columnconfigure(col, weight=1)

langas1.mainloop()
