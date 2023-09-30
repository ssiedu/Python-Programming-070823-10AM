class Base:
    def __init__(self):
        print("This is Base Class Function")

class Derive(Base):
    def __init__(self):
        Base.__init__(self)
        #super().__init__()
        print("This is Derive Class Function")


D=Derive()


