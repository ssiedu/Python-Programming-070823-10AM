L1=[11,44,3,11,6,14]

for i in range(len(L1)):
    for j in range(i,len(L1)):
        if L1[i]>L1[j]:
            temp=L1[i]
            L1[i]=L1[j]
            L1[j]=temp


print(L1)
            
