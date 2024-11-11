# Kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Khởi tạo mảng
M = [3, 6, 7, 8, 11, 17, 2, 90, 2.5, 4, 5, 8]

# Khởi tạo các danh sách kết quả
odd_numbers = []
even_numbers = []
prime_numbers = []
non_prime_numbers = []

# Duyệt qua mảng và phân loại các số
for num in M:
    if isinstance(num, int):  # Chỉ xử lý các số nguyên
        if num % 2 != 0:
            odd_numbers.append(num)
        else:
            even_numbers.append(num)
        
        if is_prime(num):
            prime_numbers.append(num)
        else:
            non_prime_numbers.append(num)

# In kết quả
print("Các số lẻ:", odd_numbers)
print("Số lượng số lẻ:", len(odd_numbers))

print("Các số chẵn:", even_numbers)
print("Số lượng số chẵn:", len(even_numbers))

print("Các số nguyên tố:", prime_numbers)

print("Các số không phải là số nguyên tố:", non_prime_numbers)
