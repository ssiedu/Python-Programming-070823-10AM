import threading
import time
def square(num):
    for n in num:
        time.sleep(0.1)
        print("Square :",n**2)


def cube(num):
    for n in num:
        time.sleep(0.5)
        print("Cube :",n**3)


list1=[2,3,4,5]

t1=threading.Thread(target=square,args=(list1,))
t2=threading.Thread(target=cube,args=(list1,))
t1.start()
#time.sleep(0.5)
t2.start()
t1.join()
t2.join()
print("Successfully Executed")
