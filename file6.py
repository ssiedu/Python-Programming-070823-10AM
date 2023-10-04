file=open("Myfile5.txt","a")
n=int(input("Enter Limit :"))
for i in range(n):
    name=input("Enter Name :")
    rno=int(input("Enter Roll Number :"))
    marks=eval(input("Enter Marks :"))
    data=str(rno)+"\t"+name+"\t"+str(marks)+"\n"
    file.write(data)
file.close()
