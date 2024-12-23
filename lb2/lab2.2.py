import numpy as np

import csv

# Đọc dữ liệu từ file CSV
def read_csv_to_list(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

file_path = 'lb2/diem_hoc_phan.csv'
data_list = read_csv_to_list(file_path)
data_array = np.array(data_list[1:], dtype=float)  # Chuyển đổi thành mảng NumPy và bỏ qua hàng tiêu đề

def chuyen_doi(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 8.0 <= diem <= 8.4:
        return 'B+'
    elif 7.0 <= diem < 8:
        return 'B'
    elif 6.5 <= diem < 7:
        return 'C+'
    elif 5.5 <= diem < 6:
        return 'C'
    elif 5.0 <= diem < 5.5:
        return 'D+'
    elif 4.0 <= diem < 5:
        return 'D'
    else:
        return 'F'

diem_doi = np.vectorize(chuyen_doi)(data_array[:, 2:])

#chia tách từng học phần
diem_hp1 = data_array[:, 2]
diem_hp2 = data_array[:, 3]
diem_hp3 = data_array[:, 4]

#Phân tích dữ liệu theo từng học phần
def phan_tich(diem):
    tong = np.sum(diem)
    trung_binh = np.mean(diem)
    std_dev = np.std(diem)
    return tong, trung_binh, std_dev

phan_tich_hp1 = phan_tich(diem_hp1)
phan_tich_hp2 = phan_tich(diem_hp2)
phan_tich_hp3 = phan_tich(diem_hp3)

#Phân tích điểm tổng hợp
credit_counts = np.unique(diem_doi, return_counts=True)

