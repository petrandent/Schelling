import tkinter as tk
import math
import random

canvas_size=400
colors=["blue","orange","black","yellow","brown","cyan","pink","green","purple","red"]

class House():
    """class for a house"""
    def __init__(self,coods,num_of_rows,num_of_cols,col):
        """enumeration for rows and columns starts from zero"""
        self.coods=coods
        self.col=col
        #self.resident=resident
        self.width=math.floor(400/num_of_cols)
        self.height=math.floor(400/num_of_rows)

    def __repr__(self):
        return f"House in row {self.coods[0]} and col {self.coods[1]}"

    def place_house(self,canvas):
        """Builds a square inside a canvas object"""
        canvas.create_rectangle(self.coods[1]*self.width,self.coods[0]*self.height,\
        (self.coods[1]+self.width)*self.width,(self.coods[0]+self.height)*self.height,fill=sef.col)


class City_canvas(tk.Frame):
    def __init__(self,parent,user_input,height=canvas_size,width=canvas_size):
        super().__init__(parent)
        frame1=tk.Frame(parent)
        frame1.pack()
        tk.Label(frame1,text="City Map").pack()
        self.canvas=tk.Canvas(frame1,height=height,width=width,bd=1,relief=tk.GROOVE,bg="blue")
        self.canvas.pack()
        self.houses=[]
        self.user_input=user_input
        self.rows=self.user_input["rows"]
        self.cols=self.user_input["cols"]
        self.num_of_races=self.user_input["races_num"]

    def distribute_houses(self):
        for i in range(self.user_input["rows"]):
            for j in range(self.user_input["cols"]):
                house=House((i,j),self.rows,self.cols,random.choice(colors[:self.num_of_races]))
                self.houses.append(house)
        for house in self.houses:
            self.canvas.create_rectangle(house.coods[1]*house.width,house.coods[0]*house.height,\
        (house.coods[1]+house.width)*house.width,(house.coods[0]+house.height)*house.height,fill="pink")




class Resident():
    def __init__(self,colour,position):
        """position is the coordinates of the house resident resides"""
        self.colour=colour
        self.happiness
        self.position=position

    def __repr__(self):
        return f"Resident of colour {self.colour} who lives in the house {self.position[0]},{self.position[1]}"

    def move(self,new_position):
        self.position=new_position






