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
        self.searchText = tk.Label(self,text="Search:",font=self.titlefont)
        self.searchBox = tk.Entry(self,width = 50)
        self.searchText.grid(row=1,column=0)
        self.searchBox.grid(row=1,column=1,columnspan=2)
        self.addButton = tk.Button(text = "Add",command = self.add)
        self.addButton.grid(row=3,column=0)
        
        self.searchText = tk.Label(self,text="Owned:",font=self.titlefont)
        self.searchBox = tk.Entry(self,width = 50)
        self.searchText.grid(row=4,column=0)
        self.searchBox.grid(row=4,column=1,columnspan=2)
        
        
        
        
        
        
        
        self.loadUp()
        self.searchBox.bind("<KeyRelease>",self.search)
        
        

    def loadUp(self):
        self.books = []
        columns = ("ID","TITLE","AUTHOR","PUBLISH DATE")
        columns2 = ("ID","TITLE","AUTHOR","PUBLISH DATE","OWNER")
        self.tree = ttk.Treeview(self,columns=columns,show="headings")
        self.tree2 = ttk.Treeview(self,columns=columns2,show="headings")
        
        for col in columns2:
            self.tree2.heading(col,text=col)
            
        self.tree2.grid(row=5,column=2,sticky="nsew")
        
        for col in columns:
            self.tree.heading(col,text=col)
        
        
        c = self.parent.cursor
        results = c.execute("SELECT * FROM books")
        self.books = results.fetchall()
        
        for book in self.books:
            self.tree.insert("",tk.END,values=book)
        
        self.tree.grid(row=2,column=2,sticky="nsew")
        
        
    
    
    def add(self):
        selected = self.tree.selection()
        
        if(selected):
            book = self.tree.item(selected[0])["values"]
            self.parent.cursor.execute("INSERT INTO owned VALUES (?,?,?,?,?,?)",(book[0],book[1],book[2],book[3],book[4],self.parent.loggedInUser))
            self.parent.db.commit()
            self.loadUp()
    
    
    def search(self,e=None):
        searchedText = self.searchBox.get().lower()
        matchingBooks = [book for book in self.books if any(searchedText in str(value).lower() for value in book)]
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for book in matchingBooks:
            self.tree.insert("", tk.END, values=book)
    
    
    
