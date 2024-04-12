import tkinter as tk
import control
import city

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        user_input_obj=control.Console(self)
        self.user_input=user_input_obj.dictionary
        bn=tk.Button(self,text="print",command=self.printDict).pack()
        self.mainloop()

    def printDict(self):
        c1=city.City(self)
        c1.pack(expand=True,fill="both")
        houses=[]
        for i in range(int(self.user_input["rows"])):
            for j in range(int(self.user_input["cols"])):
                obj=city.House(i,j,"pink")
                houses.append(obj)
        for i in houses:
            i.build_house(c1.canvas)



if __name__=='__main__':
    App()