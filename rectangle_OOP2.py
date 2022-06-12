class Rectangle: 
    def __init__(self) -> None:
        self.width = 0
        self.length = 0
        self.area = 0
    def get_data(self):
        self.width = float(input('Enter width:'))
        self.length = float(input('Enter length:'))

    def computer_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print(f'Rectangle area = {self.area}')

if __name__ == "__main__":
    rec = Rectangle()
    rec.get_data()
    rec.computer_area()
    rec.print_area()