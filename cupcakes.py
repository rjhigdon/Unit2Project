from abc import ABC, abstractmethod
import csv
from pprint import pprint


class Cupcake(ABC):
    size = "Regular"
    def __init__(self, name, price, flavor, vf):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.vf = vf     #is this a vegan friendly option
        self.topping = []

    @abstractmethod 
    def add_topping(self, *args):
        for topping in args:
            self.topping.append(topping)
    
    def __repr__(self):
        return f"<Cupcake name={self.name}> Toppings = {self.topping}>" 
       #allows for print of actually useful info instead of memory location

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, flavor, vf):
        super().__init__(name, price, flavor, vf)
        self.name = name
        self.price = price
        self.flavor = flavor
        self.vf = vf     #is this a vegan friendly option
        self.topping = []

    def add_topping(self, *args):
        for topping in args:
            self.topping.append(topping)

    def __repr__(self):
        return(f"The cupcake {self.name} is a {self.flavor} mini cupcake.")

class Normal(Cupcake):
    size = "normal"
    def __init__(self, name, price, flavor, vf):
        super().__init__(name, price, flavor, vf)
        self.name = name
        self.price = price
        self.flavor = flavor
        self.vf = vf     #is this a vegan friendly option
        self.topping = []

    def add_topping(self, *args):
        for topping in args:
            self.topping.append(topping)

    def __repr__(self):
        return(f"The cupcake {self.name} is a {self.flavor} regular sized cupcake.")

class Large(Cupcake):
    size = "large"
    def __init__(self, name, price, flavor,  vf):
        super().__init__(name, price, flavor, vf)
        self.name = name
        self.price = price
        self.flavor = flavor
        self.vf = vf     #is this a vegan friendly option
        self.topping = []

    def add_topping(self, *args):
        for topping in args:
            self.topping.append(topping)

    def __repr__(self):
        return(f"The cupcake {self.name} is a {self.flavor} large cupcake.")

strawberry = Normal("Strawberry",  4.00, "strawberry", False)
strawberry.add_topping("strawberry slices", "sprinkles")

reeses_mini = Mini("Reese's", 2.99, "PB & Chocolate", False)
reeses_mini.add_topping("Reese's minis")

cookies_n_cream = Normal("Cookies 'n' Cream", 4.75, "choocolate and sweet cream", False)
cookies_n_cream.add_topping("Oreo Crumbles")

zuccini_muffin = Normal("zuccini", 5.00, "zuccini", True)
# zuccini_muffin.add_topping('none')

pumpkin_spice = Large("pumpkin", 6.50, "pumpkin and spices", True)
pumpkin_spice.add_topping("icing", "brown sugar")

red_velvet = Normal("Red Velvet", 4.50, "dark chocolate", False)
red_velvet.add_topping("icing", "red sprinkles")



cupcake_list = [strawberry, reeses_mini, cookies_n_cream, zuccini_muffin, pumpkin_spice, red_velvet]

def csv_read(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
csv_read("sample.csv")


def write_new_csv(file, cupcakes):
    with open(file, "w", newline = "\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "vf", "topping"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "topping"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "vf": cupcake.vf, "topping": ", ".join(cupcake.topping)})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "vf": cupcake.vf})

write_new_csv("sample.csv", cupcake_list) 

def add_cupcake(file, cupcakes):
    with open(file, "a", newline = '\n') as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "vf", "topping"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        for cupcake in cupcakes:
            if hasattr(cupcake, "topping"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "vf": cupcake.vf, "topping": ", ".join(cupcake.topping)})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "vf": cupcake.vf})