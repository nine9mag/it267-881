from vehicle import Vehicle

class Bus:
    def __init__(self,name,wheel,max,vin) -> None:
        #super().__init__(name,wheel,max,vin)
        Vehicle.__init__(self,name,wheel,max,vin)

    def set_color(self,color):
        self.color = color
    
    def set_capacity(self,capacity):
        self.capacity = capacity

    def v_detail(self):
        Vehicle.v_detail(self)
        print(f'color: {self.color}')
        print("====================")
        print(f'capacity: {self.capacity}')
        print("====================")