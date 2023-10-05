try:
    print("Try Block")
    x=int(input("Enter First Value :"))
    y=int(input("Enter Second Value :"))
    z=x/y    

except:
    print("Except Block")
    print("Some Error Occured")

else:
    print("Else Block")
    print("value of z :",z)


finally:
    print("Finally Block")
    print("program Executed")


print("Thank You")
