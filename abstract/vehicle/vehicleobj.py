#vehicleobj.py
from vehiclesubclass import *

#create car object
c = Car("Mazda",250)
c.year = 2020
c.gear = 7
c.seat = 4
c.show_detail()
c.maintanance = 2022
c.show_maintanance()

#create truck object
t = Truck("Isuzu",120)
t.capacity = 1000
t.wheels = 4
t.show_detail()
t.show_price()

#create motocycle object
m = Motocycle("Honda",100)
m.cc = 160
m.model = "NEW PCX"
m.show_detail()