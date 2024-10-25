import math

# Nhập tọa độ điểm A
x1 = float(input("Nhập tọa độ x của điểm A: "))
y1 = float(input("Nhập tọa độ y của điểm A: "))

# Nhập tọa độ điểm B
x2 = float(input("Nhập tọa độ x của điểm B: "))
y2 = float(input("Nhập tọa độ y của điểm B: "))

# Tính độ dài đoạn thẳng AB
do_dai_AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Xuất độ dài đoạn thẳng AB
print(f"Độ dài đoạn thẳng AB là: {do_dai_AB}")
