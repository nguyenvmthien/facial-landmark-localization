# 🧠 Facial Landmark Localization

## 📌 Giới thiệu

Dự án này tập trung vào việc tìm hiểu chủ đề **Facial Landmark Localization** – định vị các điểm mốc đặc trưng trên khuôn mặt. Chúng tôi tiến hành khảo sát các công trình nghiên cứu trước đây và đào sâu vào kiến trúc của **FaceXFormer** – một mô hình sử dụng kiến trúc Transformer cho bài toán này.

Ngoài việc phân tích mô hình gốc, chúng tôi thực hiện **huấn luyện lại (pre-train)** mô hình trên một tập dữ liệu nhỏ hơn, đồng thời áp dụng kỹ thuật **autocast** để giảm chi phí tính toán.  
Mục tiêu chính của dự án là hiểu rõ cấu trúc của FaceXFormer và tổng quan quá trình nghiên cứu trong lĩnh vực này.

## 🧰 Công nghệ sử dụng

- 🔹 Python
- 🔹 PyTorch
- 🔹 Jupyter Notebook

## 📁 Cấu trúc thư mục

```plaintext
facial-landmark-localization/
├── Evaluate/           # Notebook đánh giá mô hình
├── Papers/             # Tài liệu nghiên cứu
├── Related-works/      # Tổng hợp công trình liên quan
├── Source/             # Mã nguồn chính
├── Surveys/            # Tổng quan các phương pháp
├── planning.md         # Kế hoạch thực hiện
└── README.md           # Tài liệu hướng dẫn
```

## ⚙️ Cài đặt và sử dụng

### 1. Clone repository

```bash
git clone https://github.com/nguyenvmthien/facial-landmark-localization.git
cd facial-landmark-localization
```

### 2. Tạo môi trường ảo (khuyến khích)

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Cài đặt phụ thuộc

```bash
pip install -r requirements.txt
```

### 4. Chạy các notebook

Mở Jupyter Notebook và thực thi các file `.ipynb` trong thư mục `Evaluate/` để xem kết quả đánh giá mô hình.

## 📊 Kết quả và đánh giá

Chi tiết về kết quả huấn luyện và đánh giá lại mô hình FaceXFormer được trình bày trong các notebook tại thư mục `Evaluate/`.  
Các thí nghiệm tập trung vào khả năng học lại trên dữ liệu nhỏ và tác động của kỹ thuật autocast đến hiệu suất mô hình.

## 📝 Giấy phép

Dự án được phát hành dưới giấy phép [MIT License](LICENSE).

## 👥 Nhóm thực hiện

- [Thien Nguyen](https://github.com/nguyenvmthien)
- [Vũ Minh Phát](https://github.com/vmphat)
- [thng292](https://github.com/thng292)
- [TrggTin Rio](https://github.com/TrggTin)
