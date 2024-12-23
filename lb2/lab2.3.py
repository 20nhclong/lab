import numpy as np

#Đọc dữ liệu từ 2 tập tin vào list

def doc_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

efficiency = doc_file('efficiency.txt')
shifts = doc_file('shifts.txt')

#Tạo numpy array từ list và kiểm tra kiểu dữ liệu
array_shifts = np.array(shifts)
print("Kiểu dữ liệu của array_shifts:", array_shifts.dtype)

array_efficiency = np.array(efficiency, dtype=float)
print("Kiểu dữ liệu của array_efficiency:", array_efficiency.dtype)

#Tính hiệu suất sản xuất trung bình của các ca làm việc
hieu_suat_buoi_sang = np.mean(array_efficiency[array_shifts == 'Morning'])
print("Hiệu suất trung bình ca Morning:", hieu_suat_buoi_sang)

hieu_suat_khac = np.mean(array_efficiency[array_shifts != 'Morning'])
print("Hiệu suất trung bình các ca khác:", hieu_suat_khac)

#Tạo mảng dữ liệu có cấu trúc
nhan_vien = np.zeros(len(array_shifts), dtype={'names': ('shift', 'efficiency'), 'formats': ('U10', 'float')})
nhan_vien['shift'] = array_shifts
nhan_vien['efficiency'] = array_shifts

#Sắp xếp mảng workers theo efficiency
sap_xep = np.sort(nhan_vien, order='efficiency')
print("Ca làm việc có hiệu suất cao nhất:", sap_xep[-1]['shift'])
print("Ca làm việc có hiệu suất thấp nhất:", sap_xep[0]['shift'])

