class Series:
    def __init__(self):
        self.s=int(input("Enter start point :"))
        self.num=int(input("Enter End point :"))
    #def SeriesNum(self):
        for i in range(self.s,self.num+1):
            print(i,end=" ")



S=Series()
#S.SeriesNum()
