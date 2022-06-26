from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commision = 30
        self.department = 'marketing'

    def add_location(self,location:str):
        self.location = location

    def add_commision(self,commision):
        self.commision = commision

    def emp_detail(self):
        super().emp_detail()
        print(f'location: {self.location}')
        print(f'commision: {self.commision}%')

    def mkt_salary(self):
        self._emp_salary()