try:
    x=10
    y='0'
    z=x/y
    print("value of z :",z)

except ZeroDivisionError:
    print("Divide By Zero Not allowed")

except TypeError:
    print("Type Mismatch")

except:
    print("Some Error Occured")
