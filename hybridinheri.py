class Base:
    def getdata(self):
        self.l=eval(input("Enter Length of rectangle :"))
        self.b=eval(input("Enter breadth of rectangle :"))

class Parent1(Base):
    def getArea(self):
        self.rarea=self.l*self.b


class Parent2:
    def getRadius(self):
        self.r=eval(input("Enter radius of circle :"))
    def calArea(self):
        self.carea=3.14*self.r*self.r


class Child(Parent1,Parent2):
    def display(self):
        print("Area of rectangle :",self.rarea)
        print("Area of Circle :",self.carea)


C=Child()
C.getdata()
C.getArea()
C.getRadius()
C.calArea()
C.display()





        
