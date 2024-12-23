import numpy as np
#1
np.random.seed(0)
nhiet_do = np.round(np.random.uniform(low=15.0, high=35.0, size=30),2)
print("Nhiệt độ hàng ngày trong tháng:", nhiet_do)

#2
nhiet_do_trung_binh = np.mean(nhiet_do)
print("Nhiệt độ trung bình trong tháng:", round(nhiet_do_trung_binh, 2))

#ngày có nhiệt độ cao nhất, thấp nhất
ngay_nhiet_do_cao_nhat=np.argmax(nhiet_do)+1
ngay_nhiet_do_thap_nhat=np.argmin(nhiet_do)+1

print("Ngày có nhiệt độ cao nhất: ",ngay_nhiet_do_cao_nhat,", nhiệt độ :", nhiet_do[ngay_nhiet_do_cao_nhat])
print("Ngày có nhiệt độ thấp nhất: ",ngay_nhiet_do_thap_nhat,", nhiệt độ :", nhiet_do[ngay_nhiet_do_thap_nhat])

nhiet_do_chenh_lech = np.abs(np.diff(nhiet_do))
nhiet_do_chenh_lech_cao_nhat = np.argmax(nhiet_do_chenh_lech) + 1
print("Ngày có sự biến đổi nhiệt độ cao nhất: ",nhiet_do_chenh_lech, "Chênh lệch: ",nhiet_do_chenh_lech[nhiet_do_chenh_lech_cao_nhat-1])

#3
ngay_nhiet_do_tren_20 = np.where(nhiet_do > 20)[0] + 1
print("Ngày có nhiệt độ cao hơn 20 độ C:", ngay_nhiet_do_tren_20)

ngay_nhiet_do_tren_trung_binh = np.where(nhiet_do > nhiet_do_trung_binh)[0] + 1
print("Nhiệt độ của các ngày trên trung bình:", ngay_nhiet_do_tren_trung_binh)

ngay_chan = np.arange(2, 31, 2) 
nhiet_do_ngay_chan = nhiet_do[ngay_chan - 1]
print("Nhiệt độ của các ngày chẵn:", nhiet_do_ngay_chan)

ngay_le = np.arange(1, 31, 2)
nhiet_do_ngay_le = nhiet_do[ngay_le - 1]
print("Nhiệt độ của các ngày lẻ:", nhiet_do_ngay_le)


