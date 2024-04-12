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
        c1=city.City(self)
        c1.pack()
        houses=[]
        rows=self.user_input["rows"]
        cols=self.user_input["cols"]
        num_of_races=self.user_input["races_num"]
        for i in range(self.user_input["rows"]):
            for j in range(self.user_input["cols"]):
                house=city.House((i,j),rows,cols,random.choice(colors[:num_of_races]))
                houses.append(house)
        for house in houses:
            house.build_house(c1.canvas)



if __name__=='__main__':
    App()
