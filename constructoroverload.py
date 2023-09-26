class Add:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def __init__(self):
        self.num1=10
        self.num2=20
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition is :",self.add)


A=Add()
A.calAdd()
