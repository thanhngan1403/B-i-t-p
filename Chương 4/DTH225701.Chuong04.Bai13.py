def TongUS(n):
    if n <= 0:
        return 0  # Trả về 0 nếu n không phải là số nguyên dương

    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i  # Nếu i là ước số của n, cộng vào tổng

    return tong

# Kiểm tra số hoàn thiện 
def KT_SHT(n):
    if n == TongUS(n):
        print(" Đây là số hoàn thiện")
    else:
        print(" Đây không phải số hoàn thiện")

# Kiểm tra số thịnh vượng
def KT_STV(n):
    if n < TongUS(n):
        print(" Đây là số thịnh vượng")
    else:
        print(" Đây không phải số thịnh vượng")

n = int(input("Nhập số nguyên dương n: "))
while n < 0:
    n = int(input("Nhập lại số nguyên dương n: "))
print("a. ")
KT_SHT(n)
print("b. ")
KT_STV(n)

