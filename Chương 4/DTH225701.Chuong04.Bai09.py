import math

def Can_Bachai_long(n):
    ketqua = n
    for i in range(n):
        ketqua = math.sqrt(ketqua)
    return ketqua

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra điều kiện n
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    # Tính căn bậc hai lồng nhau
    ketqua = Can_Bachai_long(n)
    print(f"Giá trị căn bậc hai lồng nhau của {n} là: {ketqua}")
