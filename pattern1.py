for i in range(1,6):#row 1 2 3 4 5
    for j in range(1,6):#column1 2 3 4 5
        print("*",end=" ")
    print(end="\n")
print("--------------------------------------")

for i in range(1,6):
    j=1
    while j<6:
        print("*",end=" ")
        j=j+1
    print()
print("-----------------------------------")

i=1
while i<6:
    for j in range(1,6):
        print("@",end=" ")
    i=i+1
    print()
print("------------------------------------")

i=1
while i<6:#1 2 3
    j=1
    while j<6:#1 2 3 4 5 
        print("$",end=" ")
        j=j+1
    i=i+1
    print() 










