while True:
    p=input(" enter +,-,*,/,!,exit")
    match p:
        case '+':
            n=int(input("enter no"))
            b=int(input("enter no"))
            print("addition",n+b)
        case '-':    
            n=int(input("enter no"))
            b=int(input("enter no"))
            print("substration",n-b)
        case '*': 
            n=int(input("enter no"))
            b=int(input("enter no"))
            print("multiplecation",n*b)
        case '/':    
            n=int(input("enter no"))
            b=int(input("enter no"))
            if b==0:
                print("zero")
            else:
                print("devision",n/b)
        case '!':
            n=int(input("enter no"))
            f=1
            while n>1:
                f *= n
                n -=1

            print ("factorial",f)

        case 'exit':
            print("exited")
            break

        case _:
            print("invalid try again")