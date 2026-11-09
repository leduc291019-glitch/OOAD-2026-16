# BÁO CÁO PHÂN TÍCH VÀ THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (OOAD)
## ĐỀ TÀI: HỆ THỐNG QUẢN LÝ BÁN HÀNG AFFILIATE (AFILISHOP) - OOAD-2026-16

Lê Anh Đức 

## I. MÔ TẢ YÊU CẦU HỆ THỐNG

### 1. Ý tưởng dự án
**AffiliShop** là nền tảng Web kết nối Người bán (**Merchant**) và Cộng tác viên (**Affiliate**). Hệ thống cho phép Merchant đăng sản phẩm, tạo chiến dịch chiết khấu; Affiliate nhận link giới thiệu, chia sẻ đến khách hàng và nhận hoa hồng tự động khi đơn hàng hoàn tất.

### 2. Các vai trò trong hệ thống (Actors)
* **Guest (Khách vãng lai):** Người dùng chưa đăng nhập.
* **Merchant (Chủ shop / Nhà bán hàng):** Kế thừa các quyền cơ bản của Guest.
* **Customer (Khách mua hàng):** Kế thừa các quyền cơ bản của Guest.
* **Affiliate (Đối tác tiếp thị liên kết):** Kế thừa các quyền cơ bản của Guest.

---

## II. SƠ ĐỒ USE CASE (USE CASE DIAGRAM)

### 1. Quy chuẩn thiết kế
* **Boundary (Đường biên hệ thống):** Hình chữ nhật bao quanh các Use Case, ghi rõ tiêu đề: **`Hệ thống Quản lý Bán hàng Affiliate (AffiliShop)`**.
* **Quy tắc đặt tên:** Tất cả các Use Case đều bắt đầu bằng động từ.

### 2. Sơ đồ Use Case
<img width="833" height="767" alt="TLD1QnGn5BxdLpmMRFMmxLrAQLcX7bfiRKKzBJ6JdOIT96CcKHRr81uyUB5uycOfHIeANaIOHJniwV_8Fp4pxHicRBtCPhvzt_VollVDLkMeTLuLfE0J1yw0bRbma4dBcPD6asegTKajLL1IDgKvFtIpWaFpDzLvmGcXp1aBWntFApS0Ma6Eq1wtJ51zXIf4joSJMKZgU0jJX4U-SaPnswACaAu33Ew7-Njm8ioFTGuT7MvV7G-5AUyCu1K" src="https://github.com/user-attachments/assets/bd42fb07-7e9b-4892-b805-0d314ea1396b" />

### 3. Nội dung chi tiết các Use Case và Mối quan hệ
* **Nhóm Use Case của Guest (Khách vãng lai):**
  * **Đăng ký / Đăng nhập:** Tạo tài khoản hoặc đăng nhập vào hệ thống (Merchant, Customer và Affiliate đều kế thừa quyền này).
* **Nhóm Use Case của Merchant (Nhà bán hàng):**
  * **Quản lý sản phẩm & Chiến dịch:** Thêm, sửa, xóa sản phẩm và tạo các chiến dịch quảng bá.
  * **Cấu hình % hoa hồng:** Thiết lập mức phần trăm chiết khấu chi trả cho Affiliate.
  * **Duyệt đơn hàng Affiliate:** Kiểm tra và xác nhận các đơn hàng phát sinh qua link tiếp thị để chi trả hoa hồng.
  * **Xem báo cáo doanh số:** Theo dõi tổng doanh thu và hiệu quả các chiến dịch tiếp thị.
* **Nhóm Use Case của Affiliate (Cộng tác viên):**
  * **Tạo/Lấy Affiliate Link:** Tạo đường dẫn chia sẻ riêng biệt cho từng sản phẩm/chiến dịch để quảng bá.
  * **Theo dõi lượt click & Đơn hàng:** Xem thống kê số lượt nhấp vào link và số đơn hàng ghi nhận thành công.
  * **Yêu cầu rút tiền hoa hồng:** Gửi đề nghị thanh toán số tiền hoa hồng đã tích lũy đủ điều kiện.
* **Nhóm Use Case của Customer (Khách mua hàng):**
  * **Truy cập qua Affiliate Link:** Bấm vào đường link giới thiệu của cộng tác viên để xem thông tin sản phẩm.
  * **Đặt hàng:** Thực hiện lên đơn và mua hàng trên hệ thống.
* **Mối quan hệ giữa các Use Case (`«include»`, `«extend»`, `«tracks»`, `«triggers»`):**
  * **`«include»`:** Use Case *Đặt hàng* bao hàm (`«include»`) Use Case *Kiểm tra tồn kho và tính tiền*; Use Case *Yêu cầu rút tiền hoa hồng* bao hàm (`«include»`) Use Case *Kiểm tra số dư khả dụng*.
  * **`«extend»` (và `«tracks»` / `«triggers»`):** 
    * Khi Customer thực hiện *Truy cập qua Affiliate Link*, hệ thống kích hoạt (`«tracks»` / `«extend»`) việc ghi nhận lượt click gắn với *Tạo/Lấy Affiliate Link* của Affiliate.
    * Khi Customer hoàn tất *Đặt hàng* qua link tiếp thị, hệ thống tự động kích hoạt (`«triggers»` / `«extend»`) chức năng *Duyệt đơn hàng Affiliate* cho Merchant.

---

## III. SƠ ĐỒ LỚP (CLASS DIAGRAM)

### 1. Sơ đồ lớp tổng quát (Biểu diễn quan hệ và tính nhiều)
Sơ đồ tổng quát gồm các hộp 1 ngăn chứa Tên Lớp và bản số (Multiplicity). Các mối quan hệ nhiều - nhiều (`n - n`) đã được tách thành hai mối quan hệ một - nhiều (`1 - n`) thông qua lớp trung gian:
* Quan hệ `n - n` giữa `DonHang` và `SanPham` được tách qua lớp trung gian **`ChiTietDonHang`** (`1` Đơn hàng có `1..*` Chi tiết đơn hàng; `1` Sản phẩm nằm trong `0..*` Chi tiết đơn hàng).
* Quan hệ `n - n` giữa `Affiliate` và `ChienDich` được tách qua lớp trung gian **`AffiliateLink`** (`1` Affiliate tạo `0..*` AffiliateLink; `1` Chiến dịch/Sản phẩm có `0..*` AffiliateLink).

<img width="986" height="1056" alt="class diagram" src="https://github.com/user-attachments/assets/cbc21e9d-97da-410a-9a8b-725e28baa186" />

### 2. Diễn giải chi tiết từng lớp (Đầy đủ 3 ngăn: Tên lớp, Thuộc tính, Phương thức)

1. **Lớp `Guest` / `NguoiDung` (Lớp cha tổng quát hóa)**
   * **Thuộc tính:** `- maNguoiDung: String`, `- hoTen: String`, `- email: String`, `- matKhau: String`, `- soDienThoai: String`
   * **Phương thức:** `+ dangKy(): Boolean`, `+ dangNhap(email: String, matKhau: String): Boolean`, `+ dangXuat(): void`

2. **Lớp `Merchant` (Kế thừa từ `NguoiDung`)**
   * **Thuộc tính:** `- maMerchant: String`, `- tenShop: String`, `- diaChiShop: String`
   * **Phương thức:** `+ quanLySanPham(): void`, `+ taoChienDich(): ChienDich`, `+ cauHinhHoaHong(tyLe: double): Boolean`, `+ duyetDonHangAffiliate(maDon: String): Boolean`, `+ xemBaoCaoDoanhSo(): BaoCao`

3. **Lớp `Affiliate` (Kế thừa từ `NguoiDung`)**
   * **Thuộc tính:** `- maAffiliate: String`, `- soDuHoaHong: double`, `- taiKhoanNganHang: String`
   * **Phương thức:** `+ taoAffiliateLink(maSP: String): AffiliateLink`, `+ theoDoiClickVaDonHang(): ThongKe`, `+ yeuCauRutTien(soTien: double): PhieuRutTien`

4. **Lớp `Customer` (Kế thừa từ `NguoiDung`)**
   * **Thuộc tính:** `- maCustomer: String`, `- diaChiGiaoHang: String`
   * **Phương thức:** `+ truyCapLink(url: String): SanPham`, `+ datHang(dsSanPham: List): DonHang`

5. **Lớp `SanPham`**
   * **Thuộc tính:** `- maSanPham: String`, `- tenSanPham: String`, `- donGia: double`, `- soLuongTon: int`, `- moTa: String`
   * **Phương thức:** `+ capNhatThongTin(): Boolean`, `+ kiemTraTonKho(soLuong: int): Boolean`

6. **Lớp `ChienDich`**
   * **Thuộc tính:** `- maChienDich: String`, `- tenChienDich: String`, `- phanTramHoaHong: double`, `- ngayBatDau: Date`, `- ngayKetThuc: Date`
   * **Phương thức:** `+ kichHoatChienDich(): Boolean`, `+ tinhMucChietKhau(giaTriDon: double): double`

7. **Lớp `AffiliateLink` (Lớp trung gian kết nối `Affiliate` và `ChienDich`/`SanPham`)**
   * **Thuộc tính:** `- maLink: String`, `- urlGioiThieu: String`, `- soLuotClick: int`, `- soDonThanhCong: int`
   * **Phương thức:** `+ sinhDuongDan(): String`, `+ ghiNhanClick(): void`, `+ ghiNhanDonHang(): void`

8. **Lớp `DonHang`**
   * **Thuộc tính:** `- maDonHang: String`, `- ngayDat: DateTime`, `- tongTien: double`, `- trangThaiDon: String`, `- tienHoaHong: double`
   * **Phương thức:** `+ taoDonHang(): Boolean`, `+ capNhatTrangThai(trangThaiMoi: String): void`, `+ tinhHoaHongAffiliate(): double`

9. **Lớp `ChiTietDonHang` (Lớp trung gian tách quan hệ `n - n` giữa `DonHang` và `SanPham`)**
   * **Thuộc tính:** `- maChiTiet: String`, `- soLuongMua: int`, `- donGiaLucMua: double`, `- thanhTien: double`
   * **Phương thức:** `+ tinhThanhTien(): double`

---

## IV. SƠ ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAM)
... (Còn60 dòng dòng)
