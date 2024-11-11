s = input("Nhập chuỗi không dấu nha quý dị: ")
inhoa = 0
inthuong = 0
so = 0
dacbiet = 0
space = 0
nguyenam = 0
phuam = 0

for x in (s):
    if x.isupper():
        inhoa += 1
    if x.islower():
        inthuong += 1
    if x.isdigit():
        so += 1
    if (x.isdigit() != 1 and x.isalpha() !=1 and x.isspace() != 1):
        dacbiet += 1
    if x.isspace():
        space += 1
    if (x in ['a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I']):
        nguyenam += 1
    else:
        if x.isalpha():
            phuam += 1
print("Có ",inhoa," kí tự in hoa")
print("Có ",inthuong," kí tự in thường")
print("Có ",so," kí tự số")
print("Có ",dacbiet," kí tự đặc biệt")
print("Có ", space," kí tự là khoảng trắng")
print("Có ",nguyenam," kí tự là nguyên âm")
print("Có ",phuam," kí tự là phụ âm")