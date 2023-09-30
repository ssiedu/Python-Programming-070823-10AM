class Base1:
    def getLen(self):
        self.Len=eval(input("Enter Length of rectangle :"))


class Base2:
    def getBre(self):
        self.bre=eval(input("Enter Breadth of rectangle :"))

class Child(Base1,Base2):
    def calArea(self):
        self.area=self.Len*self.bre
        print("Area of rectangle :",self.area)


C=Child()
C.getLen()
C.getBre()
C.calArea()
