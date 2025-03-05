import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class loginFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        # The parent is a link to the main App. If you need to remember values "globally",
        # you should store them in self.parent
        # 
        # for example:
        self.parent.loggedInUser = None
        
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")

        l1 = tk.Label(self,text="Welcome to the Library", font=self.titlefont)
        l1.grid(row=0,column=0)

        # Add code here to display a login screen
        
        
        
        
        
        # Do not run any actual code in __init__
        # Because this will be run as soon as the program loads

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        pass


    def submit(self):
        # check the contents of the entry boxes and see if they have logged in correctly
        # if so, set self.parent.loggedInUser
        self.parent.loggedInUser = None

        # Then switch frames
        self.parent.switchFrame("books")