class item:
    def __init__(self,name:str,price:float,quantity=1) -> None:
        #ตรวจสอบ price, quanlity ว่าต้อง > 0 assert=shortnote เอาไว้ตรวจสอบ
        assert price > 0,f"price {price} must greater than 0"
        assert quantity >0,f"quantity {quantity} must greater than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    
    #instance method ต้องมีคำว่า self เสมอ
    #จะเรียกใช้ method ที่ได้ต้องมีการสร้าง object
    def total_price(self):
        return self.price * self.quantity
        #self.total = self.price * self.quantity
        #return self.total

    def __del__(self):
        print("Object was destroy")

if __name__ == "__main__":
    item1 = item("Monitor",5600)
    item2 = item("Mouse",1500,2)
    print("=== Total Price ===")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")
