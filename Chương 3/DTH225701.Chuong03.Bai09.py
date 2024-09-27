
def month_to_quarter(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    else:
        return "Tháng không hợp lệ"

# Nhập vào tháng từ người dùng
try:
    month = int(input("Nhập vào một tháng (1-12): "))
    quarter = month_to_quarter(month)
    print(f"Tháng {month} thuộc quý {quarter}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
