import tkinter as tk
import math
import random


canvas_size=400


class Books():
    def __init__(self,user_input):
        self.user_input=user_input

        """#books for the records of houses,residents, and all addresses."""
        #dictionary with keys a tuple of coordinates and value a House object
        self.houses={}

        #dictionary with keys the resident id number and value a resident object
        self.residents={}

        #list that has all the possible addresses of the city in x,y tuples.
        self.addresses_record=[]

        #dictionary of houses with no residents
        self.unoccypied_houses={}

    def create_books(self):
        #user defined parameters
        self.rows=self.user_input["rows"]
        self.cols=self.user_input["cols"]
        self.races_pop=self.user_input["races_pop"]
        self.num_of_races=self.user_input["races_num"]

        #houses initial distribution inside the city canvas and populating houses dictionary and list for residents
        #fill adresses record and fills the houses dictionary with house objects.
        for i in range(self.rows):
            for j in range(self.cols):
                self.addresses_record.append((i,j))
                house_obj=House((i,j),self.rows,self.cols)
                self.houses[(i,j)]=house_obj

        #limits the number of the colours according to the number of races
        #and shuffles lists with random order of colour and addresses to allocate to the residents randomly.
        #lastly creates resident objects and populates and updates houses dictionary
        colour_alloc=colour_allocation(self.num_of_races,self.races_pop)
        random.shuffle(colour_alloc)
        random.shuffle(self.addresses_record)
        for i in range(self.races_pop*self.num_of_races):
            self.residents[i]=Resident(i,colour_alloc[i],self.addresses_record[i])
            resident_coords=self.residents[i].coords
            self.houses[resident_coords].resident=self.residents[i]
            self.houses[resident_coords].colour=self.residents[i].colour

        #calculation of neighbours and happiness of each resident, and testing
        for i in self.residents:
            self.residents[i].find_neighbours(self.addresses_record)
        for i in self.residents:
            self.residents[i].calculate_happiness(self.houses)
        for i in self.residents:
            print(f"{self.residents[i].colour}//{self.residents[i].coords}:{self.residents[i].happiness}")





    def update_books(self):
        pass



class House():
    """class for a house"""
    def __init__(self,coods,num_of_rows,num_of_cols):
        """enumeration for rows and columns starts from zero"""
        self.coods=coods
        self.resident=None
        self.colour="gray"
        self.width=math.floor(canvas_size/num_of_cols)
        self.height=math.floor(canvas_size/num_of_rows)

    def __repr__(self):
        return f"House({self.coods[0]},{self.coods[1]}):{self.colour}"



class City_canvas(tk.Frame):
    def __init__(self,parent,books,height=canvas_size,width=canvas_size):
        super().__init__(parent)
        frame1=tk.Frame(parent)
        frame1.pack()
        tk.Label(frame1,text="City Map").pack()
        self.canvas=tk.Canvas(frame1,height=height,width=width,bd=1,relief=tk.GROOVE,bg="blue")
        self.canvas.pack()

        #drawing a house is done.
        for house in books.houses.values():
            self.draw_house(house)

    def draw_house(self,house):
        self.canvas.create_rectangle(house.coods[1]*house.width,house.coods[0]*house.height,\
        (house.coods[1]+1)*house.width,(house.coods[0]+1)*house.height,fill=house.colour)


class Resident():
    def __init__(self,id_num,colour,coords):
        """position is the coordinates of the house resident resides"""
        self.id_num=id_num
        self.colour=colour
        self.coords=coords
        self.happiness=0
        self.neighbours=[]

    def __repr__(self):
        return f"id_num:{self.id_num}-colour:{self.colour}-house:({self.coords[0]},{self.coords[1]})"

    def move(self,new_coords):
        self.coords=new_coords

    def find_neighbours(self,address_rec):
        searching=[(self.coords[0]+1,self.coords[1]),(self.coords[0]-1,self.coords[1]),
                    (self.coords[0],self.coords[1]+1),(self.coords[0],self.coords[1]-1),
                    (self.coords[0]+1,self.coords[1]+1),(self.coords[0]+1,self.coords[1]-1),
                    (self.coords[0]-1,self.coords[1]+1),(self.coords[0]-1,self.coords[1]-1)]
        for i in searching:
            if i in address_rec:
                self.neighbours.append(i)

    def calculate_happiness(self,houses):
        counter=0
        for i in self.neighbours:
            if houses[i].colour==self.colour:
                counter+=1
        self.happiness=round(counter/len(self.neighbours),2)



def colour_allocation(num_of_races,population_of_each_race):
    #full collection of 10 different colours as 10 is the maximum amount of different ethnicities
    colors=["blue","orange","black","yellow","brown","cyan","pink","green","purple","red"]

    #limitation of the above list according to the number of races selected by user
    colour_list_limited=colors[:num_of_races]

    #above list multiplied by population of each group gives full list of colours for all residents
    colour_list_full=population_of_each_race*colour_list_limited
    return colour_list_full