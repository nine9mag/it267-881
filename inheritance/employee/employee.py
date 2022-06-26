class Employee:
    def __init__(self,id,name,salary) -> None:
        self.id = id
        self.name = name
        self._salary = salary

    def emp_detail(self):
        print(f'id: {self.id}')
        print(f'name: {self.name}')
    
    def _emp_salary(self):      #ถ้าเห็น#ให้ใส่_ #ถ้าเห็น-ให้ใส่__
        print(f'salary:{self._salary}')
        