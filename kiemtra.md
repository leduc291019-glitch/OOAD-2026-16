#Sơ đồ Usecase:
<img width="936" height="817" alt="Kiemtra" src="https://github.com/user-attachments/assets/e419e27a-cd87-4495-bed6-9c2e7cb874ba" />
#sơ đồ lớp ( class diagram )
<img width="957" height="1099" alt="Class diagram" src="https://github.com/user-attachments/assets/d3584821-d12e-4886-976a-05f723ae96bf" />


## 3. Mô tả Chi tiết 2 Use Case Tiêu biểu

### 3.1. Use Case: Đặt bàn & Đặt món trước
* **Tác nhân chính (Actor):** Khách hàng
* **Tác nhân phụ:** Nhân viên thu ngân / Hệ thống tiếp nhận
* **Mục đích:** Cho phép khách hàng liên hệ hoặc truy cập hệ thống để giữ chỗ trước (số lượng người, giờ đến) và chọn sẵn món ăn/đồ uống để nhà hàng chuẩn bị trước khi đến.
* **Điều kiện tiên quyết:** Bàn tại khung giờ yêu cầu còn trống; danh mục thực đơn đang hoạt động.
* **Luồng sự kiện chính:**
  1. Khách hàng cung cấp thông tin liên hệ: Tên khách hàng, số điện thoại, thời gian dự kiến đến và số lượng khách.
  2. Hệ thống kiểm tra tình trạng bàn và hiển thị các bàn phù hợp còn trống.
  3. Khách hàng duyệt thực đơn, chọn món ăn/đồ uống cùng số lượng và ghi chú riêng.
  4. Hệ thống hiển thị bảng tổng hợp thông tin đặt bàn kèm tổng số tiền tạm tính.
  5. Khách hàng xác nhận đặt giữ chỗ.
  6. Hệ thống lưu phiếu đặt trước và chuyển trạng thái bàn tương ứng sang "Đã giữ chỗ".

---

### 3.2. Use Case: Ghi nhận Order tại bàn
* **Tác nhân chính (Actor):** Nhân viên thu ngân
* **Tác nhân phụ:** Khách hàng
* **Mục đích:** Ghi nhận thông tin số bàn, thông tin khách, giờ gọi món và danh sách các món ăn/đồ uống khách đã gọi trực tiếp tại bàn.
* **Điều kiện tiên quyết:** Thu ngân đã đăng nhập hệ thống; bàn đang ở trạng thái sẵn sàng đón khách hoặc đã đặt trước.
* **Luồng sự kiện chính:**
  1. Thu ngân chọn số bàn mà khách đang ngồi trên hệ thống.
  2. Thu ngân nhập tên khách hàng, giờ gọi món và các ghi chú chung (nếu có).
  3. Thu ngân chọn các món từ danh mục thực đơn theo yêu cầu của khách, chỉ định số lượng và ghi chú riêng cho từng món.
  4. Hệ thống kiểm tra, cập nhật danh sách món gọi và tính tổng tiền tạm thời.
  5. Thu ngân xác nhận lưu phiếu order; hệ thống cập nhật trạng thái bàn sang "Đang phục vụ".

---

## 4. Giải thích Lớp kết hợp (Association Class) trong Class Diagram

### quan hệ nhiều nhiều:
* **PhieuOrder-ThucDon($N - N$):** 
  * Một `PhieuOrder` có thể chứa nhiều món trong `ThucDon`.
  * Một món trong `ThucDon` có thể xuất hiện trong nhiều `PhieuOrder` của các bàn khác nhau.
