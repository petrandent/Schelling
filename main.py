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
        self.frame1=tk.Frame(self)
        self.frame1.pack()
        self.books1=city.Books(self.user_input)
        self.books1.create_books()
        c1=city.City_canvas(self.frame1,self.books1)
        c1.pack()

    def relocate(self):
        self.frame1.destroy()
        self.frame_next=tk.Frame(self)
        self.frame_next.pack()
        self.books1.update_books()
        c_next=city.City_canvas(self.frame_next,self.books1)
        c_next.pack()


if __name__=='__main__':
    App()