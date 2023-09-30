class Base:
    def getdata(self):
        self.n1=eval(input("Enter First Number :"))
        self.n2=eval(input("Enter Second Number :"))

class Child1(Base):
    def calAdd(self):
        self.add=self.n1+self.n2
        print("Addition is :",self.add)

class Child2(Base):
    def calMul(self):
        self.mul=self.n1*self.n2
        print("Multiplication is :",self.mul)

class Child3(Base):
    def calDiv(self):
        self.div=self.n1/self.n2
        print("Division is :",self.div)


C1=Child1()
C1.getdata()
C1.calAdd()
C2=Child2()
C2.getdata()
C2.calMul()
C3=Child3()
C3.getdata()
C3.calDiv()




        
