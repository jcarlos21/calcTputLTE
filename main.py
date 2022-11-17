
from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("LTE Throughput Calculator")
        self.root.configure(background="blue")
        self.root.geometry("550x350")
        self.root.iconbitmap("img/venda1.ico")
        # self.root.resizable(False, False)
        
        self.backGroundImage = PhotoImage(file="img/background.png")
        self.label = Label(self.root, image=self.backGroundImage)
        self.label.place(x=0, y=0)
        self.label.image = self.backGroundImage

        # Barra de Menu

        menubar = Menu(root)
        file1 = Menu(root, tearoff=False)
        file1.add_command(label="Exit")
        menubar.add_cascade(label="File", menu=file1)
        root.config(menu=menubar)

        # Parâmetros de Entrada

        self.inputFrame = LabelFrame(self.root, text='Input Parameters', width=500, height=120, font=('TkDefaultFont', 10, "bold"))
        self.inputFrame.grid(row=0, column=0, padx=25, pady=15)

        # Caixas de escolha

        self.testLabel = Label(self.inputFrame, text='BW', wraplength=245, anchor=W)
        self.testLabel.place(x=40, y=5)
        bwChosen = StringVar()
        bwChoose = ttk.Combobox(self.inputFrame, textvariable=bwChosen, width=10)
        bwChoose['values'] = ['1.4 MHz', '3 MHz', '5 MHz', '10 MHz', '15 MHz', '20 MHz']
        bwChoose.place(x=10, y=25)
        bwChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='CP', wraplength=245, anchor=W)
        self.testLabel.place(x=135, y=5)
        cpChosen = StringVar()
        cpChoose= ttk.Combobox(self.inputFrame, textvariable=cpChosen, width=10)
        cpChoose['values'] = ['Normal', 'Extended']
        cpChoose.place(x=106, y=25)
        cpChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='MSC', wraplength=245, anchor=W)
        self.testLabel.place(x=230, y=5)
        mscChosen = IntVar()
        mscChoose= ttk.Combobox(self.inputFrame, textvariable=mscChosen, width=10)
        mscChoose['values'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        mscChoose.place(x=205, y=25)
        mscChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='MIMO', wraplength=245, anchor=W)
        self.testLabel.place(x=325, y=5)
        mimoChosen = StringVar()
        mimoChoose= ttk.Combobox(self.inputFrame, textvariable=mimoChosen, width=10)
        mimoChoose['values'] = ['without mimo', '2x2', '4x4', '8x8']
        mimoChoose.place(x=304, y=25)
        mimoChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='CA', wraplength=245, anchor=W)
        self.testLabel.place(x=430, y=5)
        caChosen = StringVar()
        caChoose= ttk.Combobox(self.inputFrame, textvariable=caChosen, width=10)
        caChoose['values'] = [1, 2, 3, 4, 5]
        caChoose.place(x=402, y=25)
        caChoose.current(0)

        # Botão cálcular

        botaoCalcular = Button(self.inputFrame, text="Calculate", borderwidth=3, cursor="hand2")
        botaoCalcular['command'] = self.naoFazNada
        botaoCalcular.place(x=217, y=60)

        # Parâmetros de Saída:

        self.ouputFrame = LabelFrame(self.root, text='Output Parameters', width=500, height=160, font=('TkDefaultFont', 10, "bold"))
        self.ouputFrame.grid(row=1, column=0, padx=25, pady=0)

        # Resultados

        self.PRBlabel = Label(self.ouputFrame, text='PBR', wraplength=245, anchor=W)
        self.PRBlabel.place(x=32, y=5)

        self.l1 = Label(self.ouputFrame, text=100, borderwidth=2, relief="groove", width=5)
        self.l1.place(x=25, y=27)
        

    def naoFazNada(self):
        pass



root = Tk()
Application(root)
# root.mainloop()
if __name__ == "__main__":
    root.mainloop()