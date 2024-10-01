from math import sqrt 
a=float (input("Nhập cạnh a>0: "))
b=float (input("Nhập cạnh b>0: "))
c=float (input("Nhập cạnh c>0: "))
if(a<=0 or b<=0 or c<=0) or (a+b) <=c or b+c <= a:
    print("Tam giác không hợp lệ")
else:
    cv=a+b+c
    p=cv/2
    dt=sqrt(p*(p-a)*(p-b)*(p-c))
    print("diện tíchh tam giác: ",dt)
