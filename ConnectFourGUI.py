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

        for i in range(0,340,int(400/6)):
            liste_rangee = []
            for j in range(0,440, int(500/7)):
                liste_rangee.append(Slot(j,i))

            self.p.append(liste_rangee)
        #self.bind("<Button-1>", self.detCol)



root = Tk()
root.geometry("500x550")
root.title("Connect 4 - v1.0 -- Jan Kasper")

info = MainWindow(root)
info.grid(row=0,column= 0)

t = BoardView(root)
t.grid(row=1, column= 0)

root.mainloop()
