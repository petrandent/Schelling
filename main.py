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
        bn=tk.Button(self,text="Print Map",command=self.printDict).pack()
        self.mainloop()

    def printDict(self):
        colors=["blue","orange","black","yellow","brown","cyan","pink","green","purple","red"]
        c1=city.City_canvas(self,self.user_input)
        c1.distribute_houses()
        c1.pack()





if __name__=='__main__':
    App()