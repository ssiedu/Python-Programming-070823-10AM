L1=[11,2,10,55,34,7]

'''for i in range(len(L1)):
    for j in range(len(L1)):
        if L1[i]<L1[j]:
            L1[i]=L1[j]'''
            

for i in L1:
    for j in L1:
        if i>j:
            i=j
            
print(i)
print(L1)            
