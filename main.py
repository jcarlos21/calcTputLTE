from tkinter import *
from tkinter import Tk

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("LTE Throughput Calculator")
        self.root.configure(background="blue")
        self.root.geometry("550x350")
        self.root.iconbitmap("img/venda1.ico")
        self.root.resizable(False, False)
        
        self.backGroundImage = PhotoImage(file="img/background.png")
        self.label = Label(self.root, image=self.backGroundImage)
        self.label.place(x=0, y=0)
        self.label.image = self.backGroundImage


root = Tk()
Application(root)
# root.mainloop()
if __name__ == "__main__":
    root.mainloop()