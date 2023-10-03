from multipledispatch import dispatch

@dispatch(int,int)
def product(fnum,snum):
    result=fnum*snum
    print("Product of two int value :",result)

@dispatch(float,float)
def product(fnum,snum):
    result=fnum*snum
    print("Product of two float value :",result)

@dispatch(int,int,int)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("Product of three int value :",result)

@dispatch(int,float,float)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("Product of three diff value :",result)

product(2.1,3.2)
product(10,20)
product(2,3,4)
product(2,2.1,3.1)



    
