from vehicle import Vehicle


class Motocycle(Vehicle):
    def __init__(self, name, wheel, max, vin) -> None:
        Vehicle.__init__(name, wheel, max, vin)

    def set_cc(self,cc):
        self.cc = cc

    def v_detail(self):
        Vehicle.v_detail(self)
        print(f'cc: {self.cc}')