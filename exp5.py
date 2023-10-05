try:
    num=int(input("Enter Any Number :"))
    assert num%2==0

except:
    print("Invalid Input")

else:
    rec=1/num
    print("Reciprocal of number :",rec)
