class Vehicle:
    def __init__(self,name,wheel,max,vin) -> None:
        self.name = name
        self.wheel = wheel
        self._maxspeed = max
        self.__vin = vin
    
    def set_vin(self,vin):
        self.__vin = vin

    def v_detail(self):
        print("====================")
        print(f'name: {self.name}')
        print("====================")
        print(f'wheel: {self.wheel}')
        print("====================")
        print(f'max: {self._maxspeed}')
        print("====================")
        print(f'vin : {self.__vin}')
        print("====================")