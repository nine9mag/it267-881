class student:
    def __init__(self,id:str,name:str,major='IT') -> None:
        self.id = id 
        self.name = name
        self.major = major
    
    def printstudentdetail(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"major:{self.major}")

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":

    #person
    Jessica = student("111","Jessica","IT")
    Jessica.printstudentdetail()

    John = student("112","John","MKT")
    John.printstudentdetail()

    James = student("113","James")
    James.printstudentdetail()

    