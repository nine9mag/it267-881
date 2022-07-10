class Horse:
    def __init__(self,max_height:float,name:str,color:str) -> None:
        self.max_height = max_height
        self.name = name
        self.color = color
        self.max_height = 200
        self.name = 'Khan Khan'
        self.color = 'Grey'

    def run(self):
        print(f"{self.name}is running")

    def showname(self):
        print(f"Name : {self.name()}")

    def showdetail(self):
        print(self.name())
        print(self.color())
        print(self.max_height())



   
    #max_height = 200
    #name = 'Khan Khan'
    #color = 'Grey'
    

    
        