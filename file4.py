file=open("Myfile3.txt","w")
name=input("Enter any name :")
age=int(input("Enter age of person :"))
file.write(name+" ") 
file.write(str(age))
file.close()
