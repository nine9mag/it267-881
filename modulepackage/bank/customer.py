class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phone = ''
    
    def new_customer(self):
        self.name = input('Enter name: ')
        self.address = input('Enter address: ')
        self.phone = input('Enter phone: ')
    
    def cus_info(self):
        return f'name:({self.name}\nAddress: {self.address}\nPhone: {self.phone})'