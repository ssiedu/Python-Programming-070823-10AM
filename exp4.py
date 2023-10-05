try:
    num=int(input("Enter any number upto 100:"))
    if num>100:
        raise ValueError

except:
    print("Value is out of 100")

else:
    if num%2==0:
        print("Even number")
    else:
        print("Odd Number")
