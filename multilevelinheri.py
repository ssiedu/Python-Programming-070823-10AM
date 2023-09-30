class GrandParent:
    def getdata(self):
        self.n1=eval(input("Enter First number :"))
        self.n2=eval(input("Enter Second Number :"))


class Parent(GrandParent):
    def calAdd(self):
        self.add=self.n1+self.n2


class Child(Parent):
    def display(self):
        print("Addition is :",self.add)


C=Child()
C.getdata()
C.calAdd()
C.display()
