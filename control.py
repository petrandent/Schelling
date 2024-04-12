import tkinter as tk

class Spinbox(tk.Frame):
    def __init__(self,parent,text,min_val,max_val,increment,variable):
        """Class creating a labeled with text, tkinter spinbox, that is placed inside a parent widget with lowest value min_val, maximum value max val and with a user defined incrementation and connects to a variable"""
        super().__init__(parent)
        self.min_val=min_val
        self.max_val=max_val
        self.increment=increment
        self.variable=variable
        frame=tk.Frame(parent)
        frame.grid()
        frame.columnconfigure((0,1),weight=1)
        frame.rowconfigure(0,weight=1)
        tk.Label(frame,text=text).grid(row=0,column=0,padx=5,pady=5)
        tk.Spinbox(frame,from_=min_val,to=max_val,increment=self.increment,\
        textvariable=self.variable).grid(row=0,column=1,padx=5,pady=5)


class Console(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        frame=tk.Frame(parent,relief=tk.GROOVE,bd=3)
        frame.pack()
        self.row_num=tk.IntVar()
        self.col_num=tk.IntVar()
        self.num_of_races=tk.IntVar()
        self.pop_of_race=tk.IntVar()
        self.happiness=tk.StringVar()
        self.dictionary={}
        Spinbox(frame,"Number of Rows",1,10,1,self.row_num)
        Spinbox(frame,"Number of Columns",1,10,1,self.col_num)
        Spinbox(frame,"Number of Races",1,10,1,self.num_of_races)
        Spinbox(frame,"Race Population",1,20,1,self.pop_of_race)
        Spinbox(frame,"Happiness threshold",0,1,0.1,self.happiness)
        self.submit_btn=tk.Button(frame,text="Submit",command=self.submit)
        self.submit_btn.grid()


    def submit(self):
        self.dictionary.update({"rows":self.row_num.get()})
        self.dictionary.update({"cols":self.col_num.get()})
        self.dictionary.update({"races_num":self.num_of_races.get()})
        self.dictionary.update({"races_pop":self.pop_of_race.get()})
        self.dictionary.update({"happiness":self.happiness.get()})

















