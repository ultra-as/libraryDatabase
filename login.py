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
        username = tk.Label(self,text="Username:", font=self.titlefont)
        password = tk.Label(self,text="Password:", font=self.titlefont)
        username.grid(row=1,column=0)
        password.grid(row=2,column=0)
        self.errorMsg = tk.Label(self,text="",fg="red",font=self.titlefont)
        self.errorMsg.grid(row=4,column=1)
        self.entry1 = tk.Entry(self, width = 30)
        self.entry1.grid(row=1,column = 1)
        self.entry1.focus()
        self.entry1.bind("<Return>", self.submit)
        self.entry1.bind("<Down>",self.down)
        self.entry2 = tk.Entry(self, width = 30,show = "*")
        self.entry2.grid(row=2,column = 1)
        self.entry2.bind("<Return>", self.submit)
        self.entry2.bind("<Up>",self.up)
        
        self.b1 = tk.Button(text = "Submit",command = self.submit)
        self.b1.grid(row=3,column=0)

        # Add code here to display a login screen
        
        
        
        
        
        # Do not run any actual code in __init__
        # Because this will be run as soon as the program loads

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        pass
    def down(self,e=None):
        self.entry2.focus()
    
    def up(self,e=None):
        self.entry1.focus()


    def submit(self,e=None):
        # check the contents of the entry boxes and see if they have logged in correctly
        # if so, set self.parent.loggedInUser
        uName = self.entry1.get()
        pWord = self.entry2.get()
        c = self.parent.cursor
        results = c.execute("SELECT * from users WHERE username = (?) AND password = (?)",(uName,pWord,))
        results = results.fetchall()
        print(results)
        if(results != []):
            self.parent.switchFrame("books")
            self.parent.loggedInUser = uName
        else:
            self.errorMsg.config(text="Incorrect information!")
            
        self.parent.loggedInUser = None

        # Then switch frames