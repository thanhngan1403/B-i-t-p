import math
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
pheptoan= input("Nhập phep toan: ")
if pheptoan=='+':
    kq=a+b
elif pheptoan=='-':
    kq=a-b
elif pheptoan=='*':
    kq=a*b
elif pheptoan=='/':
    if b != 0:
        kq=a/b
    else:
        print("khong the chia")
else:
    print("nhap phep toan khong hop le")
print("ket qua phep toan: ",kq)

