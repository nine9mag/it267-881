#วิธีที่1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drinks

#วิธีที่2
from cafe import cafe_module
desserts = cafe_module.Desserts()
print(desserts.show_desserts())

drinks = cafe_module.Drinks()
print(drinks.show_drinks())                  #เมนูเดิม
drinks.add_drink('สมูทตี้')                    #เพิ่มเมนู
print(drinks.show_drinks())
drinks.add_drink('น้ำผลไม้')
print(drinks.show_drinks())