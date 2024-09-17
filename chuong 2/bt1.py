import math 
try:
    r=float(input ("Mời bạn nhập bán kính hình tròn: "))
    cv=2*math.pi*r
    dt=r**2
    print("chu vi=",cv)
    print("dien tich=",dt)
except:
    print("Lỗi rồi!")    