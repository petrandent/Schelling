import tkinter as tk
import random
import control
import city

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user_input_obj=control.Console(self)
        self.user_input_obj.pack()
        self.user_input=self.user_input_obj.dictionary
        btn=tk.Button(self,text="Print Map",command=self.printDict).pack()
        self.mainloop()

    def printDict(self):
        self.frame1=tk.Frame(self)
        self.frame1.pack()
        c1=city.City_canvas(self.frame1,self.user_input)
        c1.pack()












if __name__=='__main__':
    App()