from math import sqrt
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a==0: 
    if b == 0 and c == 0:
        
        print("vo so nghiem")
    elif b== 0 and c!=0:
        print("vo nghiem ")
    else:
        x=-c/b
        print("nghiem x=",x)
else:
    delta = b**2-4*a*c
    if delta<0:
        print("vo nghiem")
    elif delta==0:
        x=-b/(2*a)
        print("nghiem kep x1=x2=",x)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print("nghiem x1=",x1)
        print("nghiem x2=",x2)
