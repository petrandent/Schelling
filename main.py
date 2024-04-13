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

        btn=tk.Button(self,text="Print Map",command=self.printer).pack()
        next_btn=tk.Button(self,text="Relocate >>",command=self.relocate).pack()
        self.mainloop()

    def printer(self):
        self.books1=city.Books(self.user_input)
        self.books1.create_books()
        self.c1=city.City_canvas(self,self.books1)
        for i in self.books1.houses:
            item=self.c1.draw_house(self.books1.houses[i])

    def relocate(self):
        self.books1.update_books()



if __name__=='__main__':
    App()