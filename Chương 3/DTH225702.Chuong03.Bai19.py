x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = x  # Bắt đầu với x là phần tử đầu tiên trong chuỗi
for i in range(1, n+1):
    tu = x**(2*i+1)  # Tính x mũ (2i+1), chỉ lấy các số lẻ
    mau = 1
    for j in range(1, (2*i+2)):  # Tính giai thừa của (2i+1)
        mau *= j
    s += tu / mau
print("S({0},{1})={2}".format(x, n, s))
