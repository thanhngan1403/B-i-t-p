import random
import csv
import os

def tao_csv(ten_file):
    with open(ten_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for _ in range(10):
            dong = [random.randint(1, 100) for _ in range(10)]
            writer.writerow(dong)
    print(f"Tập tin {ten_file} đã được tạo.")

def doc_csv(ten_file):
    try:
        with open(ten_file, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            for index, row in enumerate(reader, start=1):
                dong = list(map(int, row))
                tong = sum(dong)
                print(f"Tổng giá trị của dòng {index}: {tong}")
    except FileNotFoundError:
        print(f"Tệp {ten_file} không tồn tại.")

if __name__ == "__main__":
    ten_file = "data.csv"

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, ten_file)
    
    tao_csv(file_path)
    doc_csv(file_path)
