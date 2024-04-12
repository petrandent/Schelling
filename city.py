import tkinter as tk

class House():
    """class for a house"""
    def __init__(self,row,col,colour):
        """enumeration for rows and columns starts from zero"""
        self.row=row
        self.col=col
        self.colour=colour
        self.square_size=10

    def __repr__(self):
        return f"House in row {self.row} and col {self.col}"

    def build_house(self,canvas):
        """Builds a square inside a canvas object"""
        canvas.create_rectangle(self.row*self.square_size,self.col*self.square_size,\
        (self.row+1)*self.square_size,(self.col+1)*self.square_size,fill=self.colour)


class City(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        frame1=tk.Frame(parent)
        frame1.pack()
        self.square_size=100
        self.canvas=tk.Canvas(frame1,height=int(parent.user_input['rows'])*self.square_size,\
        width=int(parent.user_input["cols"])*self.square_size,bd=2,relief=tk.GROOVE,bg="blue")
        self.canvas.pack()





