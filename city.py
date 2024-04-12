import tkinter as tk
import math
import random

canvas_size=400

def colour_allocation(num_of_races,population_of_each_race):

    #full collection of 10 different colours as 10 is the maximum amount of different ethnicities
    colors=["blue","orange","black","yellow","brown","cyan","pink","green","purple","red"]

    #limitation of the above list according to the number of races selected by user
    colour_list_limited=colors[:num_of_races]

    #above list multiplied by population of each group gives full list of colours for all residents
    colour_list_full=population_of_each_race*colour_list_limited
    return colour_list_full


class House():
    """class for a house"""
    def __init__(self,coods,num_of_rows,num_of_cols):
        """enumeration for rows and columns starts from zero"""
        self.coods=coods
        self.resident=None
        self.color=""
        self.width=math.floor(canvas_size/num_of_cols)
        self.height=math.floor(canvas_size/num_of_rows)

    def __repr__(self):
        return f"House in row {self.coods[0]} and col {self.coods[1]}"

    def paint(self):
        if self.resident==None:
            self.color="gray"
        else:
            self.color=self.resident.color




class City_canvas(tk.Frame):
    def __init__(self,parent,user_input,height=canvas_size,width=canvas_size):
        super().__init__(parent)
        frame1=tk.Frame(parent)
        frame1.pack()
        tk.Label(frame1,text="City Map").pack()
        self.canvas=tk.Canvas(frame1,height=height,width=width,bd=1,relief=tk.GROOVE,bg="blue")
        self.canvas.pack()

        #basic attributes of the class (records of citizens and colour)
        self.residents={}
        self.addresses_record=[]
        self.houses={}  #dictionary with keys a tuple of coordinates and value a House object
        self.user_input=user_input
        self.rows=self.user_input["rows"]
        self.cols=self.user_input["cols"]
        self.races_pop=self.user_input["races_pop"]
        self.num_of_races=self.user_input["races_num"]

        #houses initial distribution inside the city canvas and populating houses dictionary and list for residents

        for i in range(self.user_input["rows"]):
            for j in range(self.user_input["cols"]):
                self.addresses_record.append((i,j))
                house_obj=House((i,j),self.rows,self.cols)
                self.houses[(i,j)]=house_obj
        col_aloc=colour_allocation(self.num_of_races,self.races_pop)
        random.shuffle(col_aloc)
        addresses_record=self.addresses_record
        random.shuffle(addresses_record)
        for j in range(self.races_pop*self.num_of_races):
            self.residents[j]=Resident(j,col_aloc[j],addresses_record[j])
            self.houses[addresses_record[j]].resident=self.residents[j]
        for house in self.houses.values():
            house.paint()
            print(house.color)
            self.draw_house(house)


    def draw_house(self,house):
        self.canvas.create_rectangle(house.coods[1]*house.width,house.coods[0]*house.height,\
        (house.coods[1]+house.width)*house.width,(house.coods[0]+house.height)*house.height,fill=house.color)




class Resident():
    def __init__(self,id_num,color,coords):
        """position is the coordinates of the house resident resides"""
        self.id_num=id_num
        self.color=color
        self.coords=coords

    def __repr__(self):
        return f"id num:{self.id_num}-colour:{self.color}-house:{self.coords[0]},{self.coords[1]}"

    def move(self,new_coords):
        self.coords=new_coords








