# BÁO CÁO ĐỒ ÁN: HỆ THỐNG QUẢN LÝ KẾT QUẢ HỌC TẬP
## 1. GIỚI THIỆU
Tên dự án: Student Result Management System (RMS)

Mục đích:Xây dựng ứng dụng desktop quản lý kết quả học tập sinh viên

Công nghệ:Python + Tkinter + SQLite

---

## 2. GIẢI QUYẾT VẤN ĐỀ

### Vấn đề hiện tại:
- Quản lý điểm bằng tay → dễ sai sót
- Khó tra cứu kết quả
- Không tính GPA tự động

### Giải pháp:
- Ứng dụng desktop thao tác dễ
- Lưu dữ liệu vào database
- Tính GPA tự động

---

## 3. SƠ ĐỒ KIẾN TRÚC HỆ THỐNG

```
┌─────────────────────────────────┐
│        GIAO DIỆN (GUI)          │
│      Tkinter + Python           │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│    LOGIC XỬ LÝ (Modules)        │
│ - StudentClass (Quản lý SV)     │
│ - ResultClass (Nhập điểm)       │
│ - ReportClass (Tra cứu)         │
│ - GPAClass (Tính GPA)           │
└─────────┬───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│   CƠ SỞ DỮ LIỆU (Database)     │
│       SQLite (rms.db)           │
└─────────────────────────────────┘
```

---

## 4. CÂU TRÚC FILE DỰ ÁN

```
project/
├── dashboard.py       → Cửa sổ chính
├── student.py         → Quản lý sinh viên
├── result.py          → Nhập kết quả
├── report.py          → Tra cứu báo cáo
├── gpa.py             → Tính GPA
├── create_db.py       → Tạo database
└── rms.db             → File dữ liệu
```

---

## 5. CÁC CHỨC NĂNG CHÍNH

### 5.1 Quản lý sinh viên
```
[Nhập tên] → [Nhập mã SV] → [Chọn môn] → [Save]
    ↓
[Hiển thị danh sách] → [Sửa/Xóa] → [Tìm kiếm]
```

### 5.2 Nhập kết quả
```
[Chọn mã SV] → [Search lấy tên] → [Nhập điểm]
    ↓
[Nhập tín chỉ] → [Submit] → [Lưu vào DB]
```

### 5.3 Tra cứu báo cáo
```
[Nhập mã SV] → [Search] → [Hiển thị kết quả]
    ↓
[Xem điểm từng môn] → [Xóa nếu cần]
```

### 5.4 Tính GPA
```
[Lấy tất cả điểm] → [Tính GPA từng môn]
    ↓
[GPA = Σ(GPA_môn × tín_chỉ) / Σ(tín_chỉ)]
    ↓
[Xếp loại: Xuất sắc/Giỏi/Khá/Trung bình/Yếu]
```

---

## 6. BẢNG DỮ LIỆU

### Bảng `student` (Sinh viên)
| Trường | Kiểu | Mô tả |
|--------|------|-------|
| id | Khóa chính | ID nội bộ |
| name | Text | Tên sinh viên |
| roll | Text | Mã số sinh viên |
| course | Text | Ngành học |
| description | Text | Ghi chú |

### Bảng `result` (Kết quả)
| Trường | Kiểu | Mô tả |
|--------|------|-------|
| rid | Khóa chính | ID kết quả |
| roll | Text | Mã sinh viên |
| name | Text | Tên sinh viên |
| course | Text | Tên môn học |
| marks_ob | Số | Điểm đạt được |
| full_marks | Số | Điểm tối đa |
| per | Số | Phần trăm (%) |
| credit | Số | Tín chỉ |

---

## 7. CÔNG THỨC TÍNH GPA

### Chuyển % → Điểm GPA (thang 4.0)
```
Nếu % >= 85  →  GPA = 4.0  (Xuất sắc)
Nếu % >= 80  →  GPA = 3.5  (Xuất sắc)
Nếu % >= 70  →  GPA = 3.0  (Giỏi)
Nếu % >= 60  →  GPA = 2.5  (Khá)
Nếu % >= 55  →  GPA = 2.0  (Khá)
Nếu % >= 40  →  GPA = 1.0  (Trung bình)
Nếu % <  40  →  GPA = 0.0  (Yếu)
```

### Tính GPA chung
```
GPA tổng = (GPA_môn1 × TC1 + GPA_môn2 × TC2 + ...) / (TC1 + TC2 + ...)
```

---

## 8. LUỒNG SỬ DỤNG HỆ THỐNG

```
START
  │
  ├─► [1] QUẢN LÝ SINH VIÊN
  │    ├─ Thêm sinh viên
  │    ├─ Sửa thông tin
  │    ├─ Xóa sinh viên
  │    └─ Tìm kiếm
  │
  ├─► [2] NHẬP KẾT QUẢ
  │    ├─ Chọn sinh viên
  │    ├─ Nhập điểm môn học
  │    └─ Lưu vào database
  │
  ├─► [3] TRA CỨU & XÓA
  │    ├─ Tìm kiếm theo mã SV
  │    ├─ Xem kết quả chi tiết
  │    └─ Xóa nếu cần
  │
  └─► [4] TÍNH GPA & XẾP LOẠI
       ├─ Tính GPA từng môn
       ├─ Tính GPA tổng
       └─ Hiển thị xếp loại học lực
END
```
