from tkinter import *
from tkinter import font
from MainGame import *


class MainWindow(Frame):

    def __init__(self,master = None):
        Frame.__init__(self)
        self.configure(width=500,height=100)
        police = font.Font(self, size=20, family="Arial")
        self.t = Label(self, text="WTF", font= police)
        self.t.grid(sticky= NSEW, pady= 20)

class BoardView(Canvas):
    def __init__(self, master = None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg= "blue")

        self.joueur = 1
        self.coul = "yellow"
        self.p = []
        self.perm = True





root = Tk()
root.geometry("500x550")
root.title("Connect 4 - v1.0 -- Jan Kasper")

info = MainWindow(root)
info.grid(row=0,column= 0)

t = BoardView(root)
t.grid(row=1, column= 0)

root.mainloop()
