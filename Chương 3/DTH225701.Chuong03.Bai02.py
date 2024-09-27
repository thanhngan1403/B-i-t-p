print("Chương trình đếm số ngày trong 1 tháng")
thang=int(input("Nhập vào một tháng: "))
if thang in (1,3,5,7,10,12):
    print("Tháng",thang,"có 31 ngày")
elif thang in(4,6,8,9,11):
    print("Tháng",thang,"có 30 ngày")
elif thang==2:
  
    year= int(input("nhập vào 1 năm: "))
    if(year % 4==0 and year % 100 !=0) or year % 400 ==0:
        print("Tháng", thang,"là tháng có 29 ngày")
    else:
        print("Tháng", thang,"là tháng có 28 ngày")
else:
    print("Tháng",thang,"Không hợp lệ")

        


