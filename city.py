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



    def create_books(self):
        #user defined parameters
        self.rows=self.user_input["rows"]
        self.cols=self.user_input["cols"]
        self.races_pop=self.user_input["races_pop"]
        self.num_of_races=self.user_input["races_num"]
        self.threshold=self.user_input["threshold"]

        #houses initial distribution inside the city canvas and populating houses dictionary and list for residents
        #fill adresses record and fills the houses dictionary with house objects.
        for i in range(self.rows):
            for j in range(self.cols):
                self.addresses_record.append((i,j))
                house_obj=House((i,j),self.rows,self.cols)
                self.houses[(i,j)]=house_obj

        #limits the number of the colours according to the number of races
        #and shuffles lists with random order of colour and addresses to allocate to the residents randomly.
        #creates resident objects and populates and updates houses dictionary
        colour_alloc=colour_allocation(self.num_of_races,self.races_pop)
        random.shuffle(colour_alloc)
        random.shuffle(self.addresses_record)
        for i in range(self.races_pop*self.num_of_races):
            self.residents[i]=Resident(i,colour_alloc[i],self.addresses_record[i])
            resident_coords=self.residents[i].coords
            self.houses[resident_coords].resident=self.residents[i]
            self.houses[resident_coords].colour=self.residents[i].colour


    def neighbours_happiness(self):
        """calculation of neighbours and happiness of each resident, and testing"""
        for i in self.residents:
            self.residents[i].find_neighbours(self.addresses_record)
        for i in self.residents:
            self.residents[i].calculate_happiness(self.houses)
##        for i in self.residents:
##            print(f"{self.residents[i].id_num}-->{self.residents[i].colour}//{self.residents[i].coords}:{self.residents[i].happiness}")


    def update_books(self):
        """one random unhappy resident moves to a random unoccupied house"""
        #list of tuples of coords of houses with no residents
        unoccupied_houses=[]

        #list of id nums of residents who are unhappy
        unhappy_residents_ids=[]

        #populate unoccupied_houses list
        for i in self.houses:
            if self.houses[i].resident==None:
                unoccupied_houses.append(self.houses[i].coords)
        self.neighbours_happiness()

        #fill unhappy residents
        for i in self.residents:
            if self.residents[i].happiness<self.threshold:
                unhappy_residents_ids.append(i)

        moving_resident=random.choice(unhappy_residents_ids)
        new_house=random.choice(unoccupied_houses)
        unhappy_residents_ids=[]
        unoccupied_houses=[]

        #update of books
        self.houses[self.residents[moving_resident].coords].resident=None
        self.houses[self.residents[moving_resident].coords].colour="gray"
        self.residents[moving_resident].coords=new_house
        self.houses[new_house].resident=self.residents[moving_resident]
        self.houses[new_house].colour=self.residents[moving_resident].colour
        print(f"{self.residents[moving_resident].coords} : evacuation")
        print(f"{moving_resident} --> {new_house}")
        print(f"{self.houses[new_house].coords} is now {self.houses[new_house].colour}")


class House():
    """class for a house"""
    def __init__(self,coords,num_of_rows,num_of_cols):
        """enumeration for rows and columns starts from zero"""
        self.coords=coords
        self.resident=None
        self.colour="gray"
        self.width=math.floor(canvas_size/num_of_cols)
        self.height=math.floor(canvas_size/num_of_rows)

    def __repr__(self):
        return f"House({self.coords[0]},{self.coords[1]}):{self.colour}"



class City_canvas(tk.Frame):
    def __init__(self,parent,books,height=canvas_size,width=canvas_size):
        super().__init__(parent)
        self.house_list=[]
        frame1=tk.Frame(parent)
        frame1.pack()
        tk.Label(frame1,text="City Map").pack()
        self.canvas=tk.Canvas(frame1,height=height,width=width,bd=1,relief=tk.GROOVE,bg="blue")
        self.canvas.pack()

    def draw_houses(self,houses):
        for house in houses.values():
            item=self.canvas.create_rectangle(house.coords[1]*house.width,house.coords[0]*house.height,\
            (house.coords[1]+1)*house.width,(house.coords[0]+1)*house.height,fill=house.colour)
            self.house_list.append(item)




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
    """limits the number of selected colours according to user input"""
    #full collection of 10 different colours as 10 is the maximum amount of different ethnicities
    colors=["blue","orange","black","yellow","brown","cyan","pink","green","purple","red"]

    #limitation of the above list according to the number of races selected by user
    colour_list_limited=colors[:num_of_races]

    #above list multiplied by population of each group gives full list of colours for all residents
    colour_list_full=population_of_each_race*colour_list_limited
    return colour_list_full