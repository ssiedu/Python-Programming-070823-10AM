class Base:#parent
    def __init__(self):
        self.r=eval(input("Enter radius of circle :"))


class Derive(Base):#child
    def calArea(self):
        self.area=3.14*self.r*self.r
        print("Area of circle :%.2f"%self.area)

D=Derive()
#D.getdata()
D.calArea()
