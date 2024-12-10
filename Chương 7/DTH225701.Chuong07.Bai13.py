import xml.etree.ElementTree as ET
import os

def doc_nhom_thiet_bi(file_name):

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    tree = ET.parse(file_path)
    root = tree.getroot()
    nhoms = []
    for nhom in root.findall('nhom'):
        ma = nhom.find('ma').text
        ten = nhom.find('ten').text
        nhoms.append({'ma': ma, 'ten': ten})
    return nhoms

def doc_thiet_bi(file_name):

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    tree = ET.parse(file_path)
    root = tree.getroot()
    thietbis = []
    for thietbi in root.findall('thietbi'):
        ma_nhom = thietbi.get('manhom')
        ma = thietbi.find('ma').text
        ten = thietbi.find('ten').text
        thietbis.append({'manhom': ma_nhom, 'ma': ma, 'ten': ten})
    return thietbis

def hien_thi_nhom_thiet_bi(nhoms):
    print("\nDanh sách Nhóm thiết bị:")
    for nhom in nhoms:
        print(f"Mã nhóm: {nhom['ma']}, Tên nhóm: {nhom['ten']}")

def hien_thi_thiet_bi(thietbis):
    print("\nDanh sách Thiết bị:")
    for thietbi in thietbis:
        print(f"Mã thiết bị: {thietbi['ma']}, Tên thiết bị: {thietbi['ten']}, Nhóm: {thietbi['manhom']}")

def loc_thiet_bi_theo_nhom(thietbis, ma_nhom):
    print(f"\nDanh sách Thiết bị thuộc nhóm {ma_nhom}:")
    for thietbi in thietbis:
        if thietbi['manhom'] == ma_nhom:
            print(f"Mã thiết bị: {thietbi['ma']}, Tên thiết bị: {thietbi['ten']}")

def nhom_co_so_luong_thiet_bi_nhieu_nhat(nhoms, thietbis):
    counts = {nhom['ma']: 0 for nhom in nhoms}
    for thietbi in thietbis:
        counts[thietbi['manhom']] += 1
    max_nhom = max(counts, key=counts.get)
    max_count = counts[max_nhom]
    
    for nhom in nhoms:
        if nhom['ma'] == max_nhom:
            print(f"\nNhóm thiết bị có số lượng thiết bị nhiều nhất là {nhom['ten']} với {max_count} thiết bị.")
            break

def main():
    nhoms = doc_nhom_thiet_bi('nhomthietbi.xml')
    thietbis = doc_thiet_bi('thietbi.xml')

    while True:
        print("\n--- Quản lý thiết bị ---")
        print("1. Hiển thị danh sách Nhóm thiết bị")
        print("2. Hiển thị toàn bộ Thiết bị")
        print("3. Lọc danh sách Thiết bị theo Nhóm")
        print("4. Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất")
        print("5. Thoát")
        
        chon = input("Chọn chức năng: ")

        if chon == '1':
            hien_thi_nhom_thiet_bi(nhoms)
        elif chon == '2':
            hien_thi_thiet_bi(thietbis)
        elif chon == '3':
            ma_nhom = input("Nhập mã nhóm để lọc: ")
            loc_thiet_bi_theo_nhom(thietbis, ma_nhom)
        elif chon == '4':
            nhom_co_so_luong_thiet_bi_nhieu_nhat(nhoms, thietbis)
        elif chon == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
