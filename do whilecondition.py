c= "True"
while c==True:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    operation=(input("enter the operation"))
match operation:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print("error")
        d=int(input("do you want to continue"))
