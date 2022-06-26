from employee import Employee

class EmpIT(Employee):  #ถ้าสร้างclassโดยการสืบทอดต้องใส่()
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.department = "IT"
    
    def add_skill(self,skill:str):
        self.skill = skill

    def add_experience(self,exp:str):
        self.experience = exp

    def emp_detail(self):
        super().emp_detail() #แสดง id , name
        #หากไม่ต้องการแสดง id,name ก็ไม่ต้องมี super().emp_detail()
        #overriding method
        print(f'skill: {self.skill}')
        print(f'experience: {self.experience}')


    def it_salary(self):
        self._emp_salary()
