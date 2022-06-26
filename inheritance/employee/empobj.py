#สร้างพนักงานit
from empit import EmpIT

mike = EmpIT('001','Mike',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#สร้างพนักงาน MKT
from empmkt import EmpMKT

anna = EmpMKT('002','anna',35000)
#anna.add_location('Bangkok')
#anna.add_commision('30')
anna.emp_detail()
anna.mkt_salary()

jess = EmpMKT('003','jess',35000)
jess.add_location('Chiang Mai')
jess.add_commision(35)
jess.emp_detail()
jess.mkt_salary()