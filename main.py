from tkinter import messagebox
from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk

from ResourceLTE import ResourceLTE
import dados as dado
import iTBS as modTBS


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
        file1.add_command(label="Exit", command=self.exitLogin)
        menubar.add_cascade(label="File", menu=file1)
        self.root.config(menu=menubar)

        # Parâmetros de Entrada

        self.inputFrame = LabelFrame(self.root, text='Input Parameters', width=500, height=120, font=('TkDefaultFont', 10, "bold"))
        self.inputFrame.grid(row=0, column=0, padx=25, pady=15)

        # Caixas de escolha

        self.testLabel = Label(self.inputFrame, text='BW', wraplength=245, anchor=W)
        self.testLabel.place(x=40, y=5)
        self.bwChosen = StringVar()
        self.bwChoose = ttk.Combobox(self.inputFrame, textvariable=self.bwChosen, width=10)
        self.bwChoose['values'] = ['1.4 MHz', '3 MHz', '5 MHz', '10 MHz', '15 MHz', '20 MHz']
        self.bwChoose.place(x=10, y=25)
        self.bwChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='CP', wraplength=245, anchor=W)
        self.testLabel.place(x=135, y=5)
        self.cpChosen = StringVar()
        self.cpChoose= ttk.Combobox(self.inputFrame, textvariable=self.cpChosen, width=10)
        self.cpChoose['values'] = ['Normal', 'Extended']
        self.cpChoose.place(x=106, y=25)
        self.cpChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='MSC', wraplength=245, anchor=W)
        self.testLabel.place(x=230, y=5)
        self.mscChosen = IntVar()
        self.mscChoose= ttk.Combobox(self.inputFrame, textvariable=self.mscChosen, width=10)
        self.mscChoose['values'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        self.mscChoose.place(x=205, y=25)
        self.mscChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='MIMO', wraplength=245, anchor=W)
        self.testLabel.place(x=325, y=5)
        self.mimoChosen = StringVar()
        self.mimoChoose= ttk.Combobox(self.inputFrame, textvariable=self.mimoChosen, width=10)
        self.mimoChoose['values'] = ['without mimo', '2x2', '4x4', '8x8']
        self.mimoChoose.place(x=304, y=25)
        self.mimoChoose.current(0)

        self.testLabel = Label(self.inputFrame, text='CA', wraplength=245, anchor=W)
        self.testLabel.place(x=430, y=5)
        self.caChosen = StringVar()
        self.caChoose= ttk.Combobox(self.inputFrame, textvariable=self.caChosen, width=10)
        self.caChoose['values'] = [1, 2, 3, 4, 5]
        self.caChoose.place(x=402, y=25)
        self.caChoose.current(0)

        # Botão cálcular

        self.botaoCalcular = Button(self.inputFrame, text="Calculate", borderwidth=3, cursor="hand2")
        self.botaoCalcular['command'] = self.calculateRate

        self.botaoCalcular.place(x=217, y=60)

        # Parâmetros de Saída:

        self.ouputFrame = LabelFrame(self.root, text='Output Parameters', width=500, height=160, font=('TkDefaultFont', 10, "bold"))
        self.ouputFrame.grid(row=1, column=0, padx=25, pady=0)

        # Mensagens com os resultados

        self.PRBlabel = Label(self.ouputFrame, text='PBR', wraplength=245, anchor=W)
        self.PRBlabel.place(x=32, y=5)
        self.l1 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=5)
        self.l1.place(x=25, y=27)
        
        self.TBSlabel = Label(self.ouputFrame, text='TBS INDEX', wraplength=245, anchor=W)
        self.TBSlabel.place(x=84, y=5)
        self.l2 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=5)
        self.l2.place(x=95, y=27)

        self.TBSValuelabel = Label(self.ouputFrame, text='TBS VALUE', wraplength=245, anchor=W)
        self.TBSValuelabel.place(x=154, y=5)
        self.l3 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=5)
        self.l3.place(x=165, y=27)

        self.MODULADTIONlabel = Label(self.ouputFrame, text='MODULATION', wraplength=245, anchor=W)
        self.MODULADTIONlabel.place(x=229, y=5)
        self.l4 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=7)
        self.l4.place(x=240, y=27)

        self.RElabel = Label(self.ouputFrame, text='RE NUMBER', wraplength=245, anchor=W)
        self.RElabel.place(x=320, y=5)
        self.l5 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=5)
        self.l5.place(x=335, y=27)

        self.CPlabel = Label(self.ouputFrame, text='SYMBOLS QUANT', wraplength=245, anchor=W)
        self.CPlabel.place(x=390, y=5)
        self.l6 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=5)
        self.l6.place(x=420, y=27)

        self.mensagemTAXA = Label(self.ouputFrame, text='TRANSMISSION RATE OF THE LTE RELEASE 10 SYSTEM', wraplength=295, anchor=W)
        self.mensagemTAXA.place(x=100, y=65)

        self.mensagemEquation = Label(self.ouputFrame, text='Equation', wraplength=200, anchor=W)
        self.mensagemEquation.place(x=70, y=100)
        self.l7 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=6)
        self.l7.place(x=125, y=100)
        self.mensagemMbps1 = Label(self.ouputFrame, text='Mbps', wraplength=200, anchor=W)
        self.mensagemMbps1.place(x=175, y=100)

        self.mensagemPattern = Label(self.ouputFrame, text='Pattern', wraplength=200, anchor=W)
        self.mensagemPattern.place(x=280, y=100)
        self.l8 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=7)
        self.l8.place(x=330, y=100)
        self.mensagemMbps2 = Label(self.ouputFrame, text='Mbps', wraplength=200, anchor=W)
        self.mensagemMbps2.place(x=385, y=100)

    def calculateRate(self):

        calculateLTE = ResourceLTE()

        calculateLTE.bw = self.bwChosen.get()
        calculateLTE.prb, calculateLTE.sp = dado.PRB_SP(calculateLTE.bw)
        calculateLTE.cp = dado.CP(self.cpChosen.get())        
        calculateLTE.mimo = dado.MIMO(self.mimoChosen.get())
        calculateLTE.msc = int(self.mscChosen.get())
        calculateLTE.modulation, calculateLTE.indexTBS = dado.modulation(calculateLTE.msc)  # Retorna uma string (Ex.: '64 QAM') e o valor do indice TBS
        calculateLTE.valueTBS = int(modTBS.valueTBS(calculateLTE.indexTBS, calculateLTE.prb))
        calculateLTE.carrieAggregation = int(self.caChosen.get())

        self.l1['text'] = calculateLTE.viewPRB()
        self.l2['text'] = calculateLTE.tbsIndex()
        self.l3['text'] = calculateLTE.tbsValue()
        self.l4['text'] = calculateLTE.viewModulation()
        self.l5['text'] = calculateLTE.viewResourceElement()
        self.l6['text'] = calculateLTE.viewCP()
        self.l7['text'] = calculateLTE.calcTputLTE().__round__(2)
        self.l8['text'] = calculateLTE.calcTputLTE()
        
    def exitLogin(self):
        result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.root.destroy()  


root = Tk()
Application(root)
# root.mainloop()
if __name__ == "__main__":
    root.mainloop()