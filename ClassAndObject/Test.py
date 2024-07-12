class TestClass:
    VAr1=5
    def __init__(self):
        self.VAr1=0
        # we can also do something like 
        # we can also create variable if they don't exists
        # example
        self.A=1
        # here we are creating a variable
        # and they are instance object variable
    # this is a instance method
    def f1(self):
        pass
    # this is a static method
    @staticmethod
    def F2():
        pass
    # this is a class method 
    @classmethod
    def F3(cls):
        print(cls.VAr1)
        # in the class method __init__ 
    def F3real(self):
        print(self.VAr1)
    def ShowFunction():
        print("Hello")
Obj=TestClass() # this is a instance object
# if we write TestClass() this will call a function which will return reference to this object
Obj.F3()
# or we can also use TestClass.F3()
Obj.F3real()
# The first output (5) is from the F3 class method, which prints the class variable VAr1.
# The second output (0) is from the F3real instance method, which prints the instance variable VAr1.