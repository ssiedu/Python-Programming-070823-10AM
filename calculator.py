while True:
    uc=int(input('''Do you want to continue ?
1.Yes
2.No
'''))
    if uc==1:
        num1=eval(input("Enter First Number :"))
        num2=eval(input("Enter Second Number :"))
        print('''Select Any One :-
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Modulus
''')
        ch=input("Enter your choice :")
        match ch:
            case '+':
                add=num1+num2
                print("{} + {} = {}".format(num1,num2,add))
            case '-':
                sub=num1-num2
                print("{} - {} = {}".format(num1,num2,sub))
            case '*':
                mul=num1*num2
                print("{} * {} = {}".format(num1,num2,mul))
            case '/':
                div=num1/num2
                print("{} / {} = {}".format(num1,num2,div))
            case '%':
                mod=num1%num2
                print("{} % {} = {}".format(num1,num2,mod))
            case _:
                print("Please Enter Valid Choice")
    else:
        break;
