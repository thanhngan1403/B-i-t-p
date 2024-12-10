import json
import os

class SinhVien:
    def __init__(self, ma_sinh_vien, ten, nam_sinh, ma_lop):
        self.ma_sinh_vien = ma_sinh_vien
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.ma_lop = ma_lop

    def __repr__(self):
        return f"SinhVien({self.ma_sinh_vien}, {self.ten}, {self.nam_sinh}, {self.ma_lop})"

class Lop:
    def __init__(self, ma_lop, ten):
        self.ma_lop = ma_lop
        self.ten = ten
        self.sinh_vien = []

    def them_sinh_vien(self, sinh_vien):
        self.sinh_vien.append(sinh_vien)

    def __repr__(self):
        return f"Lop({self.ma_lop}, {self.ten}, {self.sinh_vien})"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_lop = []

    def them_lop(self, lop):
        self.danh_sach_lop.append(lop)

    def them_sinh_vien(self, sinh_vien):
        for lop in self.danh_sach_lop:
            if lop.ma_lop == sinh_vien.ma_lop:
                lop.them_sinh_vien(sinh_vien)
                return
        print("Không tìm thấy lớp")

    def cap_nhat_sinh_vien(self, ma_sinh_vien, ten=None, nam_sinh=None):
        for lop in self.danh_sach_lop:
            for sinh_vien in lop.sinh_vien:
                if sinh_vien.ma_sinh_vien == ma_sinh_vien:
                    if ten:
                        sinh_vien.ten = ten
                    if nam_sinh:
                        sinh_vien.nam_sinh = nam_sinh
                    return
        print("Không tìm thấy sinh viên")

    def xoa_sinh_vien(self, ma_sinh_vien):
        for lop in self.danh_sach_lop:
            for sinh_vien in lop.sinh_vien:
                if sinh_vien.ma_sinh_vien == ma_sinh_vien:
                    lop.sinh_vien.remove(sinh_vien)
                    return
        print("Không tìm thấy sinh viên")

    def tim_sinh_vien(self, ten_sinh_vien):
        ket_qua = []
        for lop in self.danh_sach_lop:
            for sinh_vien in lop.sinh_vien:
                if ten_sinh_vien.lower() in sinh_vien.ten.lower():
                    ket_qua.append(sinh_vien)

        if ket_qua:
            ket_qua.sort(key=lambda x: x.ma_sinh_vien)
            return ket_qua
        else:
            print("Không tìm thấy sinh viên với tên:", ten_sinh_vien)
            return []

    def sap_xep_sinh_vien(self):
        for lop in self.danh_sach_lop:
            lop.sinh_vien.sort(key=lambda x: x.ten)

    def luu_vao_file(self, ten_file):
        if not ten_file.endswith(".json"):
            ten_file += ".json"

        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, ten_file)

        data = []
        for lop in self.danh_sach_lop:
            lop_data = {
                "ma_lop": lop.ma_lop,
                "ten": lop.ten,
                "sinh_vien": [{"ma_sinh_vien": sv.ma_sinh_vien, "ten": sv.ten, "nam_sinh": sv.nam_sinh} for sv in lop.sinh_vien]
            }
            data.append(lop_data)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Dữ liệu đã được lưu vào: {file_path}")

    def tai_tu_file(self, ten_file):
        if not ten_file.endswith(".json"):
            ten_file += ".json"

        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, ten_file)

        if not os.path.exists(file_path):
            print(f"Tệp {file_path} không tồn tại.")
            return

        self.danh_sach_lop = []
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for lop_data in data:
                lop = Lop(lop_data["ma_lop"], lop_data["ten"])
                for sv_data in lop_data["sinh_vien"]:
                    sinh_vien = SinhVien(sv_data["ma_sinh_vien"], sv_data["ten"], sv_data["nam_sinh"], lop.ma_lop)
                    lop.them_sinh_vien(sinh_vien)
                self.them_lop(lop)

        print(f"Dữ liệu đã được tải từ: {file_path}")

    def xuat(self):
        print("Danh sách lớp và sinh viên:")
        if not self.danh_sach_lop:
            print("Chưa có lớp hoặc sinh viên nào.")
            return

        for lop in self.danh_sach_lop:
            print(f"\nLớp: {lop.ten} (Mã: {lop.ma_lop})")
            if not lop.sinh_vien:
                print("  Không có sinh viên nào.")
            else:
                for sinh_vien in lop.sinh_vien:
                    print(f"  - Sinh viên: {sinh_vien.ten} (Mã: {sinh_vien.ma_sinh_vien}, Năm sinh: {sinh_vien.nam_sinh})")

def menu():
    print("\n--- Quản lý sinh viên ---")
    print("1. Thêm lớp")
    print("2. Thêm sinh viên")
    print("3. Cập nhật sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm sinh viên")
    print("6. Sắp xếp sinh viên")
    print("7. Lưu vào file")
    print("8. Tải từ file")
    print("9. Xuất danh sách")
    print("10. Thoát")

if __name__ == "__main__":
    quan_ly = QuanLySinhVien()

    while True:
        menu()
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            ma_lop = int(input("Nhập mã lớp: "))
            ten_lop = input("Nhập tên lớp: ")
            lop = Lop(ma_lop, ten_lop)
            quan_ly.them_lop(lop)
            quan_ly.xuat()
        elif choice == '2':
            ma_sinh_vien = int(input("Nhập mã sinh viên: "))
            ten_sinh_vien = input("Nhập tên sinh viên: ")
            nam_sinh = int(input("Nhập năm sinh sinh viên: "))
            ma_lop = int(input("Nhập mã lớp: "))
            sinh_vien = SinhVien(ma_sinh_vien, ten_sinh_vien, nam_sinh, ma_lop)
            quan_ly.them_sinh_vien(sinh_vien)
            quan_ly.xuat()
        elif choice == '3':
            ma_sinh_vien = int(input("Nhập mã sinh viên cần cập nhật: "))
            ten_sinh_vien = input("Nhập tên mới (bỏ qua nếu không thay đổi): ")
            nam_sinh = input("Nhập năm sinh mới (bỏ qua nếu không thay đổi): ")
            nam_sinh = int(nam_sinh) if nam_sinh else None
            quan_ly.cap_nhat_sinh_vien(ma_sinh_vien, ten_sinh_vien, nam_sinh)
            quan_ly.xuat()
        elif choice == '4':
            ma_sinh_vien = int(input("Nhập mã sinh viên cần xóa: "))
            quan_ly.xoa_sinh_vien(ma_sinh_vien)
            quan_ly.xuat()
        elif choice == '5':
            ten_sinh_vien = input("Nhập tên sinh viên cần tìm: ")
            sinh_vien = quan_ly.tim_sinh_vien(ten_sinh_vien)
            if sinh_vien:
                for sv in sinh_vien:
                    print(sv)
        elif choice == '6':
            quan_ly.sap_xep_sinh_vien()
            print("Đã sắp xếp sinh viên theo tên.")
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
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
