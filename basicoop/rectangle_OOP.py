class Rectangle: 
    def __init__(self ,width ,length) -> None:
        self.width = width
        self.length = length
        self.area = 0

    def computer_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print(f'Rectangle area = {self.area}')

if __name__ == "__main__":
    rec = Rectangle(2,5)
    rec.computer_area()
    rec.print_area()