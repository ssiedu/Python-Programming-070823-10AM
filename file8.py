list1=[]
file=open("Myfile7.txt","w")
for i in range(5):
    name=input("Enter Name of Students :")
    list1.append(name+"\n")

file.writelines(list1)
file.close()
