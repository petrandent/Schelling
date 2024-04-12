import tkinter as tk
import math

canvas_size=400

class House():
    """class for a house"""
    def __init__(self,coods,num_of_rows,num_of_cols,colour):
        """enumeration for rows and columns starts from zero"""
        self.coods=coods
        self.colour=colour
        self.width=math.floor(400/num_of_cols)
        self.height=math.floor(400/num_of_rows)

    def __repr__(self):
        return f"House in row {self.coods[0]} and col {self.coods[1]}"

    def build_house(self,canvas):
        """Builds a square inside a canvas object"""
        canvas.create_rectangle(self.coods[1]*self.width,self.coods[0]*self.height,\
        (self.coods[1]+self.width)*self.width,(self.coods[0]+self.height)*self.height,fill=self.colour)


class City(tk.Frame):
    def __init__(self,parent,height=canvas_size,width=canvas_size):
        super().__init__(parent)
        frame1=tk.Frame(parent)
        frame1.pack()
        tk.Label(frame1,text="City Map").pack()
        self.canvas=tk.Canvas(frame1,height=height,width=width,bd=1,relief=tk.GROOVE,bg="blue")
        self.canvas.pack()

