L1=[1,2,3]
L2=[4,5,6]
L3=[]
for i in range(len(L1)):
    for j in range(i,i+1):
        k=L1[i]+L2[j]
        L3.append(k)
        
print(L3)        
