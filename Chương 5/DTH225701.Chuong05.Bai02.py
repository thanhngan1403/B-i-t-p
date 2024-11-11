def ToiUuChuoi(str):
    str = str.strip()
    str = ' '.join(str.split())
    return str
s = input("Nhập chuỗi: ")
print("Chuỗi sau khi tối ưu: " + ToiUuChuoi(s))

