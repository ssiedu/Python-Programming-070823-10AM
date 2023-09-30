class Base:
    def getdata(self):
        print("This is Base Class Function")

class Derive(Base):
    def getdata(self):
        #Base.getdata(self)
        super().getdata()
        print("This is Derive Class Function")


D=Derive()
D.getdata()

