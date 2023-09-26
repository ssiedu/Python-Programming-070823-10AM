class Series:
    def __init__(self,s=2,n=20):
        self.s=s
        self.num=n
    def SeriesNum(self):
        for i in range(self.s,self.num+1):
            print(i,end=" ")



S=Series()
S.SeriesNum()
