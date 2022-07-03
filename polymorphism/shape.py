class Shape:
    def __init__(self) -> None:
        self.__shape = None
        self.__area = 0
    #shape property
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self,value):
        self.__shape = value

    #area property
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self,value):
        self.__area = value
    
    #abstract method
    def compute_area(self):
        pass