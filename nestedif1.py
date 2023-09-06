fnum=int(input("Enter First Number :"))
snum=int(input("Enter Second Number :"))
if fnum!=snum:
    if fnum>snum:
        print("{} is greater than {}".format(fnum,snum))
    else:
        print("{} is greater than {}".format(snum,fnum))
else:
    print("Both are Equal")
