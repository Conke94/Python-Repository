import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox

class PlayerRegister:
    def __init__(self):
    # SETTING SCREEN
        self.screen = tk.Tk()
        self.screen.geometry("400x400")
        self.screen.title('Cadastro de Jogador')

    # DIVIDING SCREEN
        self.topFrame = tk.Frame(self.screen, width = 400, height=50, relief='flat')
        self.topFrame.grid(row=0, column=0, pady=1, padx=0, sticky='NSEW')

        self.bottomFrame = tk.Frame(self.screen, width = 400, height=350, relief='flat')
        self.bottomFrame.grid(row=1, column=0, pady=1, padx=0, sticky='nswe')

    # SETTING TOP FRAME
        labelCadastro = tk.Label(self.topFrame, text='CADASTRO DE JOGADOR', anchor='ne', font=('Ivy 20'), fg="#000000")
        labelCadastro.place(x=25, y=10)
        labelCadastro = tk.Label(self.topFrame, text='', anchor='nw', font=('Ivy 1'), fg="#000000", bg="#483D8B", width=340)
        labelCadastro.place(x=25, y=45)

    # SETTING BOTTOM FRAME
        labelName = tk.Label(self.bottomFrame, text='Nome:', anchor='nw', font=('Ivy 12'), fg="#000000")
        labelName.place(x=25, y=12)
        entryName = tk.Entry(self.bottomFrame, width=22, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        entryName.place(x=100, y=12)

        labelPosition = tk.Label(self.bottomFrame, text='Posição:', anchor='nw', font=('Ivy 12'), fg="#000000")
        labelPosition.place(x=25, y=50)
        entryPosition = tk.Entry(self.bottomFrame, width=22, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        entryPosition.place(x=100, y=50)

        buttonRegister = tk.Button(self.bottomFrame, text='CADASTRAR', width=30, height=1, font=('Ivy 10 bold'), fg="#FFFFFF", bg="#483D8B", relief='raised', overrelief='ridge')
        buttonRegister.place(x=70, y=164)

        labelAge = tk.Label(self.bottomFrame, text='Idade:', anchor='nw', font=('Ivy 12'), fg="#000000")
        labelAge.place(x=25, y=88)
        ageData=("07 anos", "08 anos", "09 anos", "10 anos", "11 anos", "12 anos", "13 anos", "14 anos", "15 anos", "16 anos", "17 anos", "18 anos", "19 anos", "20 anos", "21 anos")
        ageBox = Combobox(self.screen, values=ageData)
        ageBox.place(x=100, y=144)

        labelGender = tk.Label(self.bottomFrame, text='Gênero:', anchor='nw', font=('Ivy 12'), fg="#000000")
        labelGender.place(x=25, y=126)
        genderData=("Masculino", "Feminino")
        genderBox = Combobox(self.screen, values=genderData)
        genderBox.place(x=100, y=180)

        self.screen.mainloop()

    def create_player (self, nome, pos):
        pass

