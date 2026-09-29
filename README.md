# OOAD-2026-16
Ý tưởng dự án: Hệ thống Quản lý Bán hàng Affiliate (AfiliShop) 
AffiliShop là nền tảng (Web) kết nối Người bán (Merchant) và Cộng tác viên (Affiliate). Hệ thống cho phép Merchant đăng sản phẩm, tạo chiến dịch chiết khấu; Affiliate nhận link giới thiệu, chia sẻ đến khách hàng và nhận hoa hồng tự động khi đơn hàng hoàn tất.
1. Các vai trò trong hệ thống (Actors)
Guest (Khách vãng lai): Người dùng chưa đăng nhập.
Merchant (Chủ shop / Nhà bán hàng):
Là một cấp con của Guest (kế thừa các quyền cơ bản của Guest).
Customer (Khách mua hàng):
Là một cấp con của Guest (kế thừa các quyền cơ bản của Guest).
Affiliate (Đối tác tiếp thị liên kết):
Là một cấp con của Guest (kế thừa các quyền cơ bản của Guest).
2. Chi tiết công việc của từng vai trò
Guest (Khách vãng lai)
Đăng ký / Đăng nhập: Thực hiện tạo tài khoản hoặc đăng nhập vào hệ thống. Vì Merchant, Customer và Affiliate đều kế thừa từ Guest, cả 3 nhóm này đều có quyền thực hiện tính năng này.
Merchant (Chủ shop / Nhà bán hàng)
Cấu hình % hoa hồng: Bán hàng và cài đặt mức phần trăm hoa hồng chi trả cho Affiliate.
Xem báo cáo doanh số: Theo dõi tổng doanh thu, hiệu quả các chiến dịch tiếp thị.
Quản lý sản phẩm & Chiến dịch: Thêm/sửa/xóa sản phẩm và tạo các chiến dịch quảng bá.
Duyệt đơn hàng Affiliate: Xem xét và duyệt các đơn hàng phát sinh qua link tiếp thị để xác nhận chi trả hoa hồng.
Customer (Khách mua hàng)
Truy cập qua Affiliate Link: Bấm vào đường link giới thiệu của đối tác tiếp thị để vào xem sản phẩm.
Đặt hàng: Thực hiện mua hàng thành công trên hệ thống.
Affiliate (Đối tác tiếp thị liên kết)
Tạo/Lấy Affiliate Link: Tạo đường link chia sẻ riêng cho sản phẩm/chiến dịch để đi quảng bá.
Theo dõi lượt click & Đơn hàng: Xem thống kê số người bấm vào link và số đơn hàng ghi nhận thành công từ link đó.
Yêu cầu rút tiền hoa hồng: Đề nghị hệ thống thanh toán tiền hoa hồng đã tích lũy được.
3. Mối quan hệ đặc biệt giữa các chức năng
«tracks» (Ghi nhận/Theo dõi): Khi Customer thực hiện Truy cập qua Affiliate Link, hệ thống sẽ kích hoạt việc ghi nhận dữ liệu liên quan đến Tạo/Lấy Affiliate Link của Affiliate (để tính lượt click và lượt mua từ đúng đối tác).
«triggers» (Kích hoạt): Khi Customer hoàn tất việc Đặt hàng, hành động này sẽ tự động gửi yêu cầu/kích hoạt chức năng Duyệt đơn hàng Affiliate cho Merchant.
Sơ đồ UseCase:
<img width="821" height="810" alt="Aflilishop" src="https://github.com/user-attachments/assets/224767ef-3a3c-41b6-850c-77f048ca0994" />
