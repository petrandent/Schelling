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
        next_btn=tk.Button(self,text="Relocate >>",command=self.movement).pack()
        self.mainloop()

    def printer(self):
        self.books1=city.Books(self.user_input)
        self.books1.create_books()
        self.canva=city.City_canvas(self,self.books1)
        self.canva.draw_houses(self.books1.houses)


    def movement(self):
        self.books1.update_books()
        self.canva.draw_houses(self.books1.houses)







if __name__=='__main__':
    App()