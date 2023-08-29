n1=eval(input("Enter First Number :"))#100
n2=eval(input("Enter Second Number :"))#101
print("And :", n1>n2 and n1==n2)#false
print("or  :",n1!=n2 or n1>n2)#True
print("not :", not(n1<n2))#False
print("AND not :",(not(n1>n2)) and (n1<=n2))#True
print("Or Not  :",(not(n1) or (n1!=n2)))#True
print("and or not :",not(((n1>n2) and (n1==n2)) or (n1<n2)))#False
