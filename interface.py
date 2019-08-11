# towerofhanoi
# Construction a game of Tower of Hanoi with 5 levels and a mode when the computer solves the game. #

from tkinter import *


class Application:
    def __init__(self, master=None):
        self.pularbutton = None
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Bem-vindo ao jogo da Torre de Hanoi")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.titulo = Label(self.segundoContainer, text="Deseja utilizar o modo inteligente?")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.butsim = Button(self.terceiroContainer)
        self.butsim["text"] = "SIM"
        self.butsim["font"] = ("Calibri", "10")
        self.butsim["width"] = 12
        self.butsim["command"] = self.continuarbutton
        self.butsim.pack()

        self.butnao = Button(self.terceiroContainer)
        self.butnao["text"] = "NAO"
        self.butnao["font"] = ("Calibri", "10")
        self.butnao["width"] = 12
        self.butnao["command"] = self.pularbutton
        self.butnao.pack()

    def continuarbutton(self):
        botao = self.autenticar.get()
        if botao == 'SIM':
            print('teste')
        else:
            print()
root = Tk()
Application(root)
root.mainloop()
