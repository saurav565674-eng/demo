a = float(input("enter no"))
print(f"{a}years={round(a* 365)}  days" )

a= int (input("enter no"))
b= a//60
c = a%60
print(f"{a} is {b} hours {c} minutes")
 
a= input("enter no")
print(a[-1])
a= int(input("enter no"))
print(f"{a%10} last digit")

b= input("trecher /student =")
a= int(input("enter age no"))
print("Eligible ",b == "student" and a < 20)