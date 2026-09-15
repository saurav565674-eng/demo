# is_raining= False
# if is_raining == True:
#     print("raining outside")
# else:
#     print("not raining")

# person = int(input("enter age"))
# if person >= 18:
#     print ("person is 18 ")
# else :
#     print("doesn't match age")    

# age= 17
# has_id=True
# if age >=18:
#     if has_id:
#         print("entry allowed")
#     else :
#         print("declined")
# else:
#     print("unkown")

# n = int(input("enter no"))
# if n%2 ==0 :
#     print("no is even")
# else:
#     print("no is odd")

# age = int(input("enter age"))
# price = int(input("enter amount"))
# if age <12 :
#     print("teckit price",price-price*10/100)
# else :
#     print("full price",price)

# mark = int(input("enter mark"))
# if mark >=90 and mark<=100 :
#     print("o")
# elif mark>=80  and mark<=90:
#     print("a")
# elif mark>=65  and mark<=80:
#     print("b")
# elif mark>=35 and mark<=65:
#     print("c")
# elif mark >=0 and mark<=35:
#     print("f")
# else :
#     print("invaild")

# n = int(input(" enter no"))
# if n>0:
#     print("positive")
# elif n==0:
#     print("neutral")
# elif n<0:
#     print("negative")
# else :
#     print("invalid")

# a= int(input ("enter value"))
# b= int(input ("enter value"))
# c =int(input ("enter value"))
# if a>b:
#     print("greater no",a)
# elif b>c:
#     print("greater no",b)
# else:
#     print(" greater no ",c)

# year = int (input ("enter year"))
# if year%4==0 and year%100!=0:
#     print("its leap year")
# else :
#     print("not leap year")
# a= int (input(" enter value"))
# b= int(input("enter value"))
# n=int(input("enter no"))
# match n:
#     case 1: 
#         print("addition",a+b)
#     case 2:
#         print("substration",a-b)
#     case 3:
#         print("multiple",a*b)
#     case 4:
#         if b==0:
#             print("division is zero")
#         else:
#             print("division",a/b)
#     case _:
#         print("invalid case")

# a = input("player 1 choose rock ,paper,scissor:")
# b = input("player 2 choose rock ,paper,scissor:")
# if (a == "rock " and b=="scissor") or (a=="paper"and b== "rock")or (a=="scissor" and b=="paper"):
#     print ("player is winner") 
# elif a==b:
#     print("it is tie")
# else :
#     print ("player 2 is winner")

# a= input("traffic signal:")
# if a=="red":
#     print("stop")
# elif a=="yellow":
#     print("ready")
# elif a=="green":
#     print("go")
# else:
#     print("invalid color")

# balance=5000
# password=1234
# print("1.check balance \n 2.deposit \n 3.witdraw \n 4.exit")
# n= int(input("enter your choice"))
# match n:
#     case 1:
#         user =int(input("enter password"))
#         if user== password:
#             print("balance",balance)
#         else :
#             print("invalid password ")
#     case 2:
#         amount = int(input ("enter amount to deposit:"))
#         balance += amount
#         print("amount deposited",balance)
#     case 3:
#         amount =int(input ("amount to be withdraw"))
#         if balance > amount:
#             balance -= amount 
#             print("balance remaind",balance)
#         else :
#             print("insuffienct balance")
#     case 4:
#         print("thank for visiting")
#     case _:
#         print("invalid choice !!please choice valid no:")