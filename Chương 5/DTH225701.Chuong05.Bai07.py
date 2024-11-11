def ToiUuChuoi(str):
    str = str.strip()
    str = ' '.join(str.split())
    str = str.lower()
    str = str.title()
    return str
s = input("Nhập chuỗi: ")
print("Chuỗi sau khi tối ưu: " + ToiUuChuoi(s))