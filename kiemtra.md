#Sơ đồ Usecase:
<img width="936" height="817" alt="Kiemtra" src="https://github.com/user-attachments/assets/e419e27a-cd87-4495-bed6-9c2e7cb874ba" />
#sơ đồ lớp ( class diagram )
<img width="957" height="1099" alt="Class diagram" src="https://github.com/user-attachments/assets/d3584821-d12e-4886-976a-05f723ae96bf" />

#mô tả 2 use case:
#use case: đặt bàn& đặt món trước
tác nhân chính ( actor): khách hàng
tác nhân phụ : nhân viên thu ngân (tác nhân tiếp nhận chức năng)
chức năng :Cho phép khách hàng liên hệ hoặc truy cập hệ thống để giữ chỗ trước (số lượng người, giờ đến) và chọn sẵn món ăn/đồ uống để nhà hàng chuẩn bị trước khi đến.
#use case : ghi nhận order tại bàn
tác nhân(actor): nhân viên thu ngân
tác nhân phụ: khách hàng ( yêu cầu đặt món )
chức năng:ghi nhận các món ăn của khách đã order tại bàn
#giải thích 1 lớp sơ đồ kết hợp trong class diagram 
#PhieuOder và ThucDon ( đây là quan hệ nhiều - nhiều (n-n))
Một PhieuOrder có thể chứa nhiều món trong ThucDon.
Một món trong ThucDon có thể xuất hiện trong nhiều PhieuOrder khác nhau của các bàn khác nhau.


