D1={1:100,2:200,3:300}
D2={1:200,2:500,4:600}
D3={}
D3.update(D1)
D3.update(D2)
print(D3)
for i in D1.keys():
   for j in D2.keys():
       if i==j:
           D3[i]=D1[i]+D2[j]

print(D3)
