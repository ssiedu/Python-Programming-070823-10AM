file=open("Myfile4.txt","w")
for i in range(5):
    name=input("Enter Name :")
    file.write(name+"\n")
file.close()
