from cgitb import text


class Car:
    brand = "Toyota"
    
    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def printCarDetail(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"year: {self.year}")
        print(f"Price: {self.price}")

#staticmethod ไม่มีคำว่า self
    @staticmethod
    def get_static_method():
        text = "Static"
        print(f"In {text} method")
        #ตัวแปร text ไม่สามารถถูกเรียกใช้ใน printCarDetail() ได้
        #ตัวแปร text ใช้ได้แต่ใน get_static_method()

    #class method ต้องมีคำว่า cls
    @classmethod
    def get_class_method(cls):
        my_text = "Class"
        print(f"This is {my_text} method ")


    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail()

    #เรียกใช้ static method
    Car.get_static_method() #เรียกผ่าน class
    my_car.get_static_method() #เรียกผ่าน instace

    Car.get_class_method() #เรียกผ่าน class
    my_car.get_class_method() #เรียกผ่าน instace