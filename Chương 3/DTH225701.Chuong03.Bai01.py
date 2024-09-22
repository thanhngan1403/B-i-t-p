print(" Chương trình kiểm tra năm nhuần")
year=int(input("Nhập 1 năm bất kì: "))
if(year % 4==0 and year % 100!=0 ) or year % 400==0:
    print("Năm: ",year,"là năm nhuần")
else:
    Pritn("Năm: ",year,"không là năm nhuần")