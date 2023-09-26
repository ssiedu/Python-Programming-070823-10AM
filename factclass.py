class Factorial:
    def getNum(self):
        self.num=int(input("Enter any number :"))
    def fact(self):
        i=1
        f=1
        while i<=self.num:
            f=f*i
            i=i+1
        print("Factorial of a number :",f)

F=Factorial()
F.getNum()
F.fact()
