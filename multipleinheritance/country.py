from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation_density(self):
        return self.population / self.area
    
    def show_detail(self):
        #ชื่อประเทศ
        print(f'Country: {self.name}')
        #สถานที่ตั้ง
        print(self.getcordinate())
        #พท. ประชากร ความหนาแน่น
        print(f'Area: {self.area}')
        print(f'Population: {self.population}Million')
        print(f'Density: {self.getpopulation_density()}')
        #Time Zone,climate,temperature,weather
        print(f'TimeZone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperature(C): {self.celsius}')
        print(f'Temperature(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')
        print()

