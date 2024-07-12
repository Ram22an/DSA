class Employee:
    # actually we don't have public private and static variable
    # we can access all the variable outside the class
    # for public var just use name of variable 
    VAr1=None
    # for protected variable use _nameofvariable
    _Var2=None
    # for private variable use __nameofvariable
    __Var3=None
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def PrintAll(self):
        return[self.empid,self.name,self.salary]
print(Employee.VAr1)
print(Employee._Var2)
# print(Employee.__Var3)
# to access the private variable use _classname__variablename
print(Employee._Employee__Var3)
E1=Employee()
print(E1.PrintAll())
E2=Employee(1,"Raman","1cr")
print(E2.PrintAll())