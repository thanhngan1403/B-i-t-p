import os

def Get_name1(name):
    return os.path.basename(name)
def Get_name2(name):
    return os.path.splitext(os.path.basename(name))

s = input("Nhập chuỗi: ")

print("Tên file:", Get_name1(s)) 
print("Tên file không có phần mở rộng:", Get_name2(s)[0])  
