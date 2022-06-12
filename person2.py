from codecs import getencoder
from unicodedata import name


class Person:
    def __init__(self,name:str,gender:str,profession:str,study:str) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study 


    def work(self):
        print(f'{self.name} working as a {self.profession}')
    
    def show(self):
        print(f'name: {self.name} gender: {self.gender} profession: {self.profession} study: {self.study}')
    
#person1
jessa = Person('Jessa','Female','software Engineer','0')
jessa.work()
jessa.show()

#person2
john = Person('John','male','Doctor','15')
john.work()
john.show()

#person3
lisa = Person('Lisa','female','korean singer','10')
lisa.work()
lisa.show()
