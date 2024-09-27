import datetime

# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tạo đối tượng datetime từ ngày, tháng, năm đã nhập
ngay_hien_tai = datetime.date(nam, thang, ngay)

# Tính ngày kế tiếp
ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)

# In ra ngày kế tiếp
print("Ngày kế sau ngày vừa nhập: ", ngay_ke_tiep.strftime("%d/%m/%Y"))
