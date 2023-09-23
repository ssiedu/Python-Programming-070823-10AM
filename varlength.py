#non keyword
'''def Data(*x):
    print(x)
    for i in x:
        print(i)
    print(x[1])


Data(10,20,30,40,50)'''

#keyword **
def Data(**x):
    print(x)
    for i,j in x.items():
        print(i,j)

    print(x['b'])


Data(a=10,b=20,c=30)
