class SinhVien:
    def __init__(self, maSV, tenSV, diemToan, diemVan, diemHoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.diemToan = diemToan
        self.diemVan = diemVan
        self.diemHoa = diemHoa

    def tinh_diem_trung_binh(self):
        return (self.diemToan + self.diemVan + self.diemHoa) / 3

    def xep_loai(self):
        dtb = self.tinh_diem_trung_binh()
        if dtb >= 8:
            return "Giỏi"
        elif dtb >= 6.5:
            return "Khá"
        elif dtb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

def in_thong_tin_sinh_vien(sinh_vien):
    print(f"Mã sinh viên: {sinh_vien.maSV}")
    print(f"Tên sinh viên: {sinh_vien.tenSV}")
    print(f"Điểm Toán: {sinh_vien.diemToan}")
    print(f"Điểm Văn: {sinh_vien.diemVan}")
    print(f"Điểm Hóa: {sinh_vien.diemHoa}")
    print(f"Điểm trung bình: {sinh_vien.tinh_diem_trung_binh()}")
    print(f"Xếp loại: {sinh_vien.xep_loai()}")
    print("------------------------")

# Danh sách sinh viên
danh_sach_sinh_vien = [
    SinhVien("SV001", "Nguyễn Văn A", 8, 7, 9),
    SinhVien("SV002", "Trần Thị B", 6, 5, 4),
    SinhVien("SV003", "Lê Văn C", 9, 8, 7),
    SinhVien("SV004", "Phạm Thị D", 5, 6, 5),
    SinhVien("SV005", "Võ Văn E", 7, 8, 6)
]

# In thông tin tất cả sinh viên
print("Danh sách tất cả sinh viên:")
for sinh_vien in danh_sach_sinh_vien:
    in_thong_tin_sinh_vien(sinh_vien)

# Tìm sinh viên có điểm trung bình cao nhất
sinh_vien_gioi_nhat = max(danh_sach_sinh_vien, key=lambda x: x.tinh_diem_trung_binh())
print("\nSinh viên có điểm trung bình cao nhất:")
in_thong_tin_sinh_vien(sinh_vien_gioi_nhat)

# Tìm sinh viên có điểm Hóa thấp nhất
sinh_vien_hoa_thap_nhat = min(danh_sach_sinh_vien, key=lambda x: x.diemHoa)
print("\nSinh viên có điểm Hóa thấp nhất:")
in_thong_tin_sinh_vien(sinh_vien_hoa_thap_nhat)