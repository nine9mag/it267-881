#วิธีที่1
from cafe_module import Desserts
from cafe_module import Drinks

#desserts = Desserts()
#print(desserts.show_desserts())
#drinks = Drinks()
#print(drinks.show_drinks())

#วิธีที่2
desserts = Desserts()
print(desserts.show_desserts())

drinks = Drinks()
print(drinks.show_drinks())                  #เมนูเดิม
drinks.add_drink('สมูทตี้')                    #เพิ่มเมนู
print(drinks.show_drinks())
drinks.add_drink('น้ำผลไม้')
print(drinks.show_drinks())