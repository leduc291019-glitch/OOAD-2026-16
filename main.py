class QuanLyBanHang:
    def __init__(self):
        self.danh_sach_san_pham = []

    def them_san_pham(self, san_pham):
        self.danh_sach_san_pham.append(san_pham)

    def hien_thi_danh_sach(self):
        for san_pham in self.danh_sach_san_pham:
            print(san_pham)

    def tim_kiem_san_pham(self, ten_san_pham):
        for san_pham in self.danh_sach_san_pham:
            if san_pham.ten == ten_san_pham:
                return san_pham
        return None
class SanPham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def __str__(self):
        return f"{self.ten} - {self.gia} VND"
class NhaCungCap:
    def __init__(self, ten, dia_chi):
        self.ten = ten
        self.dia_chi = dia_chi

    def __str__(self):
        return f"{self.ten} - {self.dia_chi}"
NhaCungCap1 = NhaCungCap("Công ty ABC", "123 Đường A, Quận 1, TP.HCM")
print(NhaCungCap1)