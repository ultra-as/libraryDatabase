import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class bookFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")

        l1 = tk.Label(self,text="Choose Books", font=self.titlefont)
        l1.grid(row=0,column=0)

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        pass
