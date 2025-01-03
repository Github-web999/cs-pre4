class NhanVien:
    # Phương thức khởi tạo (constructor)
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong):
        self.maNhanVien = maNhanVien
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.chucVu = chucVu
        self.heSoLuong = heSoLuong
        
        # Tính chất 3: tính đóng gói (encapsulation) -> không cho phép tương tác trực tiếp với thuộc tính / phương thức cần bảo mật (private, protected, public - access modifier)
        self.__matKhau = "1234"
        
    # Phương thức tính lương
    def tinh_luong(self):
        return self.luongCoBan * self.heSoLuong
    
    def lay_mat_khau(self):
        return str(self.__matKhau + "abcdeft8793&^%")
    

nhanVienA = NhanVien(1, "Tran Thi A", 100, "mentor", 2)
# nhanVienB = NhanVien(2, "Tran Thi B", 200, "GiangVien", 4)

# print("Lương NV A:", nhanVienA.tinh_luong())
# print("Lương NV B:", nhanVienB.tinh_luong())

print(nhanVienA.lay_mat_khau())

#TODO: Tính chất kế thừa
class QuanLy(NhanVien):
    # Phương thức khởi tạo (constructor)
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong, bonus, danhSachPhongBan):
        #* gọi phương thức khởi tạo của lớp cha
        super().__init__(maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong) 
        
        #* định nghĩa thêm thuộc tính của riêng class con
        self.bonus = bonus
        self.danhSachPhongBan = danhSachPhongBan
        
    def tinh_luong(self):
        return self.luongCoBan * self.heSoLuong + self.bonus
        
class GiamDoc(NhanVien):
    # Phương thức khởi tạo (constructor)
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong, bonus, danhSachChiNhanh):
        #* gọi phương thức khởi tạo của lớp cha
        super().__init__(maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong)
        
        #* định nghĩa thêm thuộc tính của riêng class con
        self.bonus = bonus
        self.danhSachChiNhanh = danhSachChiNhanh
        
    # 1. Overloading (nhiều tham số -> khác triển khai): 1 hàm / phương thức có nhiều cách để triển khai. VD: phương thức khởi tạo
    # 2. Overriding (cùng tham số -> khác triển khai): 1 hàm được triển khai khác nhau tuỳ thuộc vào lớp đối tượng
    
    # => Tính chất 2: tính đa hình (Polymorphism)
    def tinh_luong(self):
        return self.luongCoBan * self.heSoLuong + self.bonus * 2

    

# nhanVienC = NhanVien(3, "Tran Thi C", 100, "mentor", 2) # -> 200    
# quanLyC = QuanLy(1, "Nguyen Van C", 100, "QuanLy", 2, 200, []) # -> 400
# giamDocC = GiamDoc(1, "Le Duc C", 100, "QuanLy", 2, 200, []) # -> 600

# print("Lương Nhân Viên:", nhanVienC.tinh_luong())
# print("Lương Quản Lý:", quanLyC.tinh_luong())
# print("Lương Giám Đốc:", giamDocC.tinh_luong())


