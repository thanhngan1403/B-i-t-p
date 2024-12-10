import json
import os

class SanPham:
    def __init__(self, ma_san_pham, ten, gia, ma_danh_muc):
        self.ma_san_pham = ma_san_pham
        self.ten = ten
        self.gia = gia
        self.ma_danh_muc = ma_danh_muc

    def __repr__(self):
        return f"SanPham({self.ma_san_pham}, {self.ten}, {self.gia}, {self.ma_danh_muc})"

class DanhMuc:
    def __init__(self, ma_danh_muc, ten):
        self.ma_danh_muc = ma_danh_muc
        self.ten = ten
        self.san_pham = []

    def them_san_pham(self, san_pham):
        self.san_pham.append(san_pham)

    def __repr__(self):
        return f"DanhMuc({self.ma_danh_muc}, {self.ten}, {self.san_pham})"

class QuanLySanPham:
    def __init__(self):
        self.danh_muc = []

    def them_danh_muc(self, danh_muc):
        self.danh_muc.append(danh_muc)

    def them_san_pham(self, san_pham):
        for danh_muc in self.danh_muc:
            if danh_muc.ma_danh_muc == san_pham.ma_danh_muc:
                danh_muc.them_san_pham(san_pham)
                return
        print("Không tìm thấy danh mục")

    def cap_nhat_san_pham(self, ma_san_pham, ten=None, gia=None):
        for danh_muc in self.danh_muc:
            for san_pham in danh_muc.san_pham:
                if san_pham.ma_san_pham == ma_san_pham:
                    if ten:
                        san_pham.ten = ten
                    if gia:
                        san_pham.gia = gia
                    return
        print("Không tìm thấy sản phẩm")

    def xoa_san_pham(self, ma_san_pham):
        for danh_muc in self.danh_muc:
            for san_pham in danh_muc.san_pham:
                if san_pham.ma_san_pham == ma_san_pham:
                    danh_muc.san_pham.remove(san_pham)
                    return
        print("Không tìm thấy sản phẩm")

    def tim_san_pham(self, ten_san_pham):
            ket_qua = []
            for danh_muc in self.danh_muc:
                for san_pham in danh_muc.san_pham:
                    if ten_san_pham.lower() in san_pham.ten.lower():  
                        ket_qua.append(san_pham)

            if ket_qua:
                ket_qua.sort(key=lambda x: x.ma_san_pham)  
                return ket_qua
            else:
                print("Không tìm thấy sản phẩm với tên:", ten_san_pham)
                return []

    def sap_xep_san_pham(self):
        for danh_muc in self.danh_muc:
            danh_muc.san_pham.sort(key=lambda x: x.ten)

    def luu_vao_file(self, ten_file):
        if not ten_file.endswith(".txt"):
            ten_file += ".txt"

        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, ten_file)

        with open(file_path, 'w', encoding='utf-8') as file:
            for danh_muc in self.danh_muc:
                file.write(f"Danh mục: {danh_muc.ma_danh_muc} - {danh_muc.ten}\n")
                for san_pham in danh_muc.san_pham:
                    file.write(f"  Sản phẩm: {san_pham.ma_san_pham} - {san_pham.ten} - {san_pham.gia} - {san_pham.ma_danh_muc}\n")
        print(f"Dữ liệu đã được lưu vào: {file_path}")

    def tai_tu_file(self, ten_file):
        if not ten_file.endswith(".txt"):
            ten_file += ".txt"

        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, ten_file)

        if not os.path.exists(file_path):
            print(f"Tệp {file_path} không tồn tại.")
            return

        self.danh_muc = []
        with open(file_path, 'r', encoding='utf-8') as file:
            danh_muc_hien_tai = None
            for line in file:
                line = line.strip()
                if line.startswith("Danh mục:"):
                    parts = line.split(":")[1].strip().split(" - ")
                    ma_danh_muc = int(parts[0])
                    ten = parts[1]
                    danh_muc_hien_tai = DanhMuc(ma_danh_muc, ten)
                    self.them_danh_muc(danh_muc_hien_tai)
                elif line.startswith("Sản phẩm:") and danh_muc_hien_tai:
                    parts = line.split(":")[1].strip().split(" - ")
                    ma_san_pham = int(parts[0])
                    ten = parts[1]
                    gia = float(parts[2])
                    ma_danh_muc = int(parts[3])
                    san_pham = SanPham(ma_san_pham, ten, gia, ma_danh_muc)
                    danh_muc_hien_tai.them_san_pham(san_pham)
        print(f"Dữ liệu đã được tải từ: {file_path}")

    def xuat(self):
        print("Danh sách danh mục và sản phẩm:")
        if not self.danh_muc:
            print("Chưa có danh mục hoặc sản phẩm nào.")
            return
        
        for danh_muc in self.danh_muc:
            print(f"\nDanh mục: {danh_muc.ten} (Mã: {danh_muc.ma_danh_muc})")
            if not danh_muc.san_pham:
                print("  Không có sản phẩm nào.")
            else:
                for san_pham in danh_muc.san_pham:
                    print(f"  - Sản phẩm: {san_pham.ten} (Mã: {san_pham.ma_san_pham}, Giá: {san_pham.gia})")

if __name__ == "__main__":
    quan_ly = QuanLySanPham()

    def menu():
        print("\n--- Quản lý sản phẩm ---")
        print("1. Thêm danh mục")
        print("2. Thêm sản phẩm")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm sản phẩm")
        print("6. Sắp xếp sản phẩm")
        print("7. Lưu vào file")
        print("8. Tải từ file")
        print("9. Xuất danh sách")
        print("10. Thoát")

    while True:
        menu()
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            ma_danh_muc = int(input("Nhập mã danh mục: "))
            ten_danh_muc = input("Nhập tên danh mục: ")
            danh_muc = DanhMuc(ma_danh_muc, ten_danh_muc)
            quan_ly.them_danh_muc(danh_muc)
            quan_ly.xuat()
        elif choice == '2':
            ma_san_pham = int(input("Nhập mã sản phẩm: "))
            ten_san_pham = input("Nhập tên sản phẩm: ")
            gia_san_pham = float(input("Nhập giá sản phẩm: "))
            ma_danh_muc = int(input("Nhập mã danh mục: "))
            san_pham = SanPham(ma_san_pham, ten_san_pham, gia_san_pham, ma_danh_muc)
            quan_ly.them_san_pham(san_pham)
            quan_ly.xuat()
        elif choice == '3':
            ma_san_pham = int(input("Nhập mã sản phẩm cần cập nhật: "))
            ten_san_pham = input("Nhập tên mới (bỏ qua nếu không thay đổi): ")
            gia_san_pham = input("Nhập giá mới (bỏ qua nếu không thay đổi): ")
            gia_san_pham = float(gia_san_pham) if gia_san_pham else None
            quan_ly.cap_nhat_san_pham(ma_san_pham, ten_san_pham, gia_san_pham)
            quan_ly.xuat()
        elif choice == '4':
            ma_san_pham = int(input("Nhập mã sản phẩm cần xóa: "))
            quan_ly.xoa_san_pham(ma_san_pham)
            quan_ly.xuat()
        elif choice == '5':
            ten_san_pham = input("Nhập tên sản phẩm cần tìm: ")
            san_pham = quan_ly.tim_san_pham(ten_san_pham)
            if san_pham:
                print(san_pham)
        elif choice == '6':
            quan_ly.sap_xep_san_pham()
            print("Đã sắp xếp sản phẩm theo tên.")
            quan_ly.xuat()
        elif choice == '7':
            ten_file = input("Nhập tên file để lưu: ")
            quan_ly.luu_vao_file(ten_file)
        elif choice == '8':
            ten_file = input("Nhập tên file để tải: ")
            quan_ly.tai_tu_file(ten_file)
            quan_ly.xuat()
        elif choice == '9':
            quan_ly.xuat()
        elif choice == '10':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")