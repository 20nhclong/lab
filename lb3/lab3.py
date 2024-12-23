import pandas as pd

# Đọc file stocks1.csv
stocks1 = pd.read_csv('lb3\stocks1.csv')

#Hiển thị 5 dòng đầu tiên của stocks1
print("5 dòng đầu tiên của stocks1 \n",stocks1.iloc[0:5])

# Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1
print(stocks1.dtypes)

# Xem thông tin tổng quan (info) của stocks1
print(stocks1.info())

#Kiểm tra dữ liệu Null
print(stocks1.isnull().sum())

#lab3.2
#Thay thế dữ liệu Null ở cột high,low bằng giá trị trung bình của cột high,low
stocks1['high']=stocks1['high'].fillna(stocks1['high'].mean())
stocks1['low']=stocks1['low'].fillna(stocks1['low'].mean())

#Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print(stocks1.info())

#lab3.3
# Đọc file stocks2.csv
stocks2 = pd.read_csv('lb3\stocks2.csv')

#Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks=stocks1.add(stocks2)

gia_trung_binh = stocks.groupby('date').mean()[['open', 'high', 'low', 'close']]
print("5 dòng đầu tiên của bảng giá \n",gia_trung_binh.iloc[0:5])

#lab3.4
companies = pd.read_csv('DATA/companies.csv')
print("5 dòng đầu tiên của companies \n",companies.iloc[0:5])

#Kết hợp stocks và companies dựa trên cột chung là symbol
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name')

#Tính giá đóng cửa (close) trung bình cho mỗi công ty
trung_binh_gia_dong_cua = merged_data.groupby('symbol')['close'].mean()
print("5 dòng đầu tiên của bảng giá đóng cửa \n",trung_binh_gia_dong_cua[0:5])

#lab3.5
#Tạo MultiIndex cho DataFrame
stocks.set_index(['date', 'symbol'])

#Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, cho mỗi mã chứng khoán
grouped_stocks = stocks.groupby(['date', 'symbol']).mean()

#Sắp xếp dữ liệu theo ngày và mã chứng khoán
grouped_stocks.sort_index()

#Hiển thị kết quả cho 5 ngày đầu tiên
print(grouped_stocks.head(5))

#Tạo Pivot Table từ DataFrame stocks
pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')

#Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
volume_totals = stocks.groupby('symbol')['volume'].sum()
pivot_table = pivot_table.assign(Total_Volume=volume_totals)

#Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp
pivot_table = pivot_table.sort_values(by='Total_Volume', axis=1, ascending=False)

#Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
print(pivot_table.iloc[:, :5])

