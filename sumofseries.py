n=int(input("Enter End Limit :"))
i=int(input("Enter start Limit :"))
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i=i+1
print("Sum of series :",sum)
   
