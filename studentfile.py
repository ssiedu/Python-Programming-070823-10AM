import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0
    def ReadMarks(self):
        print("Enter Marks of Student :")
        self.s1=eval(input("Enter marks of subject1:"))
        self.s2=eval(input("Enter marks of subject2:"))
        self.s3=eval(input("Enter marks of subject3:"))
    def display(self):
        print("Student Information :")
        print("Roll No :",self.rno)
        print("Name    :",self.name)
        print("Subject1 :",self.s1)
        print("Subject2 :",self.s2)
        print("Subject3 :",self.s3)


'''S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.ReadMarks()
S2.ReadMarks()
file=open("StudentData","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()'''

file=open("StudentData","rb")
try:
    while True:
        S=pickle.load(file)
        S.display()
except:
    file.close()

