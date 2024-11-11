import numpy as np

# Nhập hai ma trận A và B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Cộng hai ma trận
C = A + B
print("Ma trận A:")
print(A)
print("\nMa trận B:")
print(B)
print("\nMa trận C (A + B):")
print(C)

# Hàm tính ma trận hoán vị
def transpose(matrix):
    return np.transpose(matrix)

# Tìm ma trận hoán vị của A và B
A_transpose = transpose(A)
B_transpose = transpose(B)

print("\nMa trận hoán vị của A:")
print(A_transpose)
print("\nMa trận hoán vị của B:")
print(B_transpose)
