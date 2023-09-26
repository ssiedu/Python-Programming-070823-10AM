class Series:
    def getdata(self,s,n):
        self.s=s
        self.num=n
    def SeriesNum(self):
        for i in range(self.s,self.num+1):
            print(i,end=" ")



S=Series()
S.getdata(1,10)
S.SeriesNum()
