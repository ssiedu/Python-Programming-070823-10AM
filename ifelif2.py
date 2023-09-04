ch=input("Enter any character :")
if ch>='a' and ch<='z':
    print("Lower Case Letter")
elif ch>='A' and ch<='Z':
    print("Upper Case Letter")
elif ch>='0' and ch<='9':
    print("Digit")
else:
    print("Special Symbol")
