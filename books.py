import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class bookFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        
        self.table = []

        l1 = tk.Label(self,text="Choose Books", font=self.titlefont)
        l1.grid(row=0,column=0)
        searchText = tk.Label(self,text="Search:",font=self.titlefont)
        searchBox = tk.Entry(self,width = 50)
        searchText.grid(row=1,column=0)
        searchBox.grid(row=1,column=1,columnspan=2)
        addButton = tk.Button(text = "Add",command = self.add)
        addButton.grid(row=3,column=0)
        
        
        
        
        self.loadUp()
        
        

    def loadUp(self):
        columns = ("ID","TITLE","AUTHOR","PUBLISH DATE")
        tree = ttk.Treeview(self,columns=columns,show="headings")
        self.tree.bind("<Key>",self.search)
        
        for col in columns:
            tree.heading(col,text=col)
        
        
        c = self.parent.cursor
        results = c.execute("SELECT * FROM books")
        results = results.fetchall()
        
        for book in results:
            tree.insert("",tk.END,values=book)
        
        tree.grid(row=2,column=2,sticky="nsew")
    
    
    def add(self):
        pass
    
    
    def search(self):
        searchedText = searchBox.get()
        c = self.parent.cursor
        results = c.execute("SELECT * FROM books WHERE TITLE = ?%",(searchedText,))
        results = results.fetchall()
        
        for book in results:
            tree.insert("",tk.END,values=book)
        
        tree.grid(row=2,column=2,sticky="nsew")
    
    
    
