class EvenOdd:
    def getdata(self):
        self.num=int(input("Enter any number :"))
    def checkNum(self):
        if self.num%2==0:
            print("Even Number")
        else:
            print("Odd Number")


EO=EvenOdd()
EO.getdata()
EO.checkNum()
