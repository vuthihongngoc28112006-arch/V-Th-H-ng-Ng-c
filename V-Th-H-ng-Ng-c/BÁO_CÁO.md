# HỆ THỐNG QUẢN LÝ KẾT QUẢ HỌC TẬP SINH VIÊN

## 1. Giới thiệu
Ứng dụng desktop quản lý điểm số sinh viên bằng Python + SQLite.

**Tác dụng:**
- Quản lý thông tin sinh viên
- Nhập và lưu kết quả học tập
- Tra cứu điểm số
- Tính GPA tự động

## 2. Các chức năng chính

### F1: Quản lý sinh viên
- Thêm sinh viên (tên, mã số, ngành)
- Sửa thông tin
- Xóa sinh viên
- Tìm kiếm theo tên

### F2: Nhập kết quả
- Chọn sinh viên
- Nhập điểm đạt được
- Nhập điểm tối đa
- Nhập số tín chỉ

### F3: Xem báo cáo
- Tra cứu kết quả theo mã sinh viên
- Hiển thị điểm từng môn
- Xóa kết quả nếu cần

### F4: Tính GPA
- Tính GPA theo thang 4.0
- Xếp loại học lực tự động

## 3. Cấu trúc dự án

```
project/
├── dashboard.py      # Cửa sổ chính
├── student.py        # Quản lý sinh viên
├── result.py         # Nhập kết quả
├── report.py         # Xem báo cáo
├── gpa.py            # Tính GPA
├── create_db.py      # Tạo database
└── rms.db            # SQLite database
```

## 4. Database

**Bảng student:**
- id (khóa chính)
- name (tên sinh viên)
- roll (mã sinh viên)
- course (ngành học)
- description (ghi chú)

**Bảng result:**
- rid (khóa chính)
- roll (mã sinh viên)
- name (tên sinh viên)
- course (môn học)
- marks_ob (điểm đạt được)
- full_marks (điểm tối đa)
- per (phần trăm)
- credit (tín chỉ)

## 5. Cách dùng

### Cài đặt:
```bash
pip install pillow
python create_db.py
python dashboard.py
```

### Quy trình:
1. **Student**: Thêm sinh viên mới
2. **Result**: Nhập điểm cho sinh viên
3. **Report**: Xem kết quả
4. **GPA**: Tính điểm trung bình

## 6. Công thức GPA

| Phần trăm | Điểm GPA |
|-----------|----------|
| ≥ 85% | 4.0 |
| ≥ 80% | 3.5 |
| ≥ 70% | 3.0 |
| ≥ 60% | 2.5 |
| ≥ 55% | 2.0 |
| ≥ 40% | 1.0 |
| < 40% | 0.0 |

**Xếp loại:**
- GPA ≥ 3.6: Xuất sắc
- GPA ≥ 3.2: Giỏi
- GPA ≥ 2.5: Khá
- GPA ≥ 2.0: Trung bình
- GPA < 2.0: Yếu

## 7. Hướng phát triển
- Thêm màn hình đăng nhập
- Xuất báo cáo PDF/Excel
- Biểu đồ thống kê
- Giao diện đẹp hơn (PyQt, CustomTkinter)
