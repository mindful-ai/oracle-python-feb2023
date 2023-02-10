class Employee(object):

    # Class variables
    empCount = 0

    # Constructor and Data Intialization
    def __init__(self, n, company = "MyCompany", salary="0"):
        self.name = n
        self.company = company
        self.salary = salary
        self.tax = 0
        Employee.empCount += 1

    def __repr__(self):
        return self.name.upper()

    def __str__(self):
        return self.name.upper() + "|" + self.company + "|" + self.salary

    def __len__(self):
        return Employee.empCount
        

    # Functions
    def printinfo(self):
        print(self.name.upper())
        print('-'*30)
        print('COMPANY    :', self.company)
        print('SALARY     :', self.salary)
        print('TAX        :', self.tax)
        

    def setsalary(self, newsalary):
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * float(self.salary.split()[0])
