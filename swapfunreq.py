def swap(fnum,snum):
    temp=fnum
    fnum=snum
    snum=temp
    print("First Number :",fnum)
    print("Second Number :",snum)

x=int(input("Enter first number :"))
y=int(input("Enter Second Number :"))
swap(x)
