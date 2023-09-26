class Addition:
    def getdata(self):
        self.__num1=eval(input("Enter First Number :"))
        self.num2=eval(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.__num1+self.num2
    def display(self):
        print("Sum is :",self.add)

A=Addition()
A.getdata()
A.calAdd()
A.display()
print("First Number :",A.num2)
