class Juicemachine :
    Menu_type = "Juice"
    total = 0
    price = 25
    def __init__(self,menu:str,size='R') -> None:
        self.menu = menu
        self.size = size.upper()  

    
    def check_menu(self):
        menu_dictionary = {'OJ':25,'AJ':25,'WJ':30,'PJ':30}
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == "L" :
            self.price +=5
        else:
            self.price
    
        Juicemachine.total = self.price

    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu},({self.size} * ฿{self.price}) => ฿{Juicemachine.total}'

    
if __name__ == "__main__" :
    order1 = Juicemachine("WJ","L")
    order2 = Juicemachine("OJ","R")
    order3 = Juicemachine("PJ","L")


    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())
