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
        books1=city.Books(self.user_input)
        books1.create_books()
        c1=city.City_canvas(self.frame1,books1)
        c1.pack()
##        for k in city_alternative.residents:
##                print(f"{k}:{city_alternative.residents[k].happiness}")




if __name__=='__main__':
    App()