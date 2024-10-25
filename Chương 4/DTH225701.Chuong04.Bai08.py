import math

# Nhập a và x
a = float(input("Nhập giá trị (a>0 và a!=1): "))
x = float(input("Nhập giá trin (x>0): "))
# Kiểm tra điều kiện a và x
if a <= 0 or a == 1:
    print("Giá trị a không hợp lệ. Vui lòng nhập a > 0 và a != 1.")
elif x <= 0:
    print("Giá trị x không hợp lệ. Vui lòng nhập x > 0.")
else:
    # Tính logarit cơ số a của x
    log_a_x = math.log(x, a)
    print(f"Giá trị log_{a}({x}) là: {log_a_x}")