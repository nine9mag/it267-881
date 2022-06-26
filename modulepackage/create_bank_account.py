#เรียกใช้packageจากmoduleอื่น
from bank.account import accout
from bank.customer import Customer

#สร้าง object ของ customer ที่ชื่อ paul
#ข้อมูลลูกต้า paul , nontaburi,012-345-6789
Paul = Customer()
Paul.new_customer()

#สร้าง object ของ account เพื่อเปิดบัญชีใหม่ให้กับ Paul
#ข้อมูลการเปิดบัญชี 'Saving','0123-4578',500
Paul_acc = accout()
Paul_acc.open_account(Paul.name,'Saving','0123-4578',500)

#แสดงข้อมูลของ customer paul
print(Paul.cus_info())

#แสดงข้อมูล
print(Paul_acc.display_balance())