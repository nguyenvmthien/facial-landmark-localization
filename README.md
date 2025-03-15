# facial-landmark-localization

- Lịch họp định kỳ: 15h T7 hàng tuần
- Lịch họp đột xuất (nếu có): 15h T4

# TODO: 15h T7, 22/03

- Tìm hiểu về paper được chọn (main method): https://docs.google.com/spreadsheets/d/1sRzfZNLsH_zDZupy-x-obUzrgvaA6J3C5kZf52neDnw/edit?gid=1260700319#gid=1260700319
- Viết thêm related works:
  - ERT (DLib)
  - Adaptive Wing
  - SPIGA
  - FaceXFormer
- Thử benchmark trên bộ dữ liệu 300W (chỉ test trên link Drive - https://drive.google.com/file/d/1VGT24gi5nd2TnGRLbHRtJkAGQbclkcJi/view):
  - ERT (DLib): Thiện
  - Adaptive Wing: Tín
  - SPIGA: Phát
  - FaceXFormer: Thông

# TODO: 15h T7, 01/03

- Tiếp tục hoàn thành phần "Related works"

# TODO: 15h T7, 22/02

- Viết phần nhỏ trước 1.1, giới thiệu chung về chủ đề
- Các thành viên viết thêm về một công trình vào related work

# TODO: 15h T7, 15/02

- Đọc 3 survey paper 1,4,5 để chuẩn bị làm chương 2
- Note:

```
- Trang đầu report không có mã số sinh viên thì có ổn không?
- Danh sách giảng viên hướng dẫn có bổ sung họ tên của trợ giảng hay không?
- Tất cả hình ảnh đưa vào report phải đảm bảo "sự rõ nét", không nên dùng các hình bị mờ.
- Nếu thanh logs báo lỗi thì thành viên chủ động sửa lỗi.
```

# TODO: 15h T6, 07/02

- Làm slide và viết report bằng tiếng Việt
- Viết report cho chapter 1 và tìm tài liệu cho chapter 2
- Link ghi chú các công trình liên quan: [Link](https://docs.google.com/spreadsheets/d/1sRzfZNLsH_zDZupy-x-obUzrgvaA6J3C5kZf52neDnw/edit?gid=0#gid=0)

## 21127731 - Nguyễn Trọng Tín

1.4. Đóng góp

- Báo cáo được khảo sát nhằm đóng góp nội dung gì.

## 21127739 - Vũ Minh Phát

1.2. Ý nghĩa về ứng dụng (thực tiễn) của chủ đề. => Đóng góp vào đời sống thường ngày

- Animation
- Face editing
- Thực tế tăng cường (AR)
- Human-Machine Interaction

## 22127401 - Nguyễn Quang Thông

1.1. Ý nghĩa về khoa học của chủ đề. => Đóng góp vào khoa học, nghiên cứu,

- Face recognition
- Facical expression and emotion analysis
- Eye tracking
- Attributes classification

## 22127398 - Nguyễn Văn Minh Thiện

1.3. Phát biểu bài toán

- Input, Ouput của hệ thống là gì.
- Framework chung của hệ thống gồm các công đoạn chính nào (chưa đi vào pp cụ thể).

# Công cụ làm đồ án

## Bắt buộc

- **Viết report**: `dùng LaTeX`
  - Template: https://www.overleaf.com/project/679f3b5ac4e6d540df06881b
- **Làm slide**: `LaTeX Beamer`
  - Template (có rồi): https://www.overleaf.com/project/67a4260a8d8a437eccba9c26

=> Dùng overleaf

- Hạn chế của Overleaf: Chỉ 2 người cùng làm 1 lúc  
   => Dùng 1 account chung để làm

## Tùy chọn

- Quản lý source code, báo cáo LaTeX, v.v.
  - GitHub repo: có rồi

# Cấu trúc của report

```
Chương 1. Giới thiệu
    1.0. Giới thiệu về chủ đề
    1.1. Ý nghĩa về khoa học của chủ đề.
    1.2. Ý nghĩa về ứng dụng của chủ đề.
    1.3. Phát biểu bài toán
        - Input, Ouput của hệ thống là gì.
        - Framework chung của hệ thống gồm các công đoạn chính nào (chưa đi vào pp cụ thể).
    1.4. Đóng góp
        - Báo cáo được khảo sát nhằm đóng góp nội dung gì.
Chương 2. Các công trình nghiên cứu liên quan (Related work)
    - Chọn lọc các công trình liên quan đến chủ đề.
    - Trình bày quá trình phát triển của các giải pháp liên quan đến chủ đề.
    - Lập bảng so sánh các giải pháp dựa trên một số tiêu chí tự chọn.
    - Nhằm trả lời được 2 câu hỏi:
        - Người ta đã làm gì rồi và mình muốn làm gì.
Chương 3. Phương pháp (state-of-the-art approach)
    - Chọn lấy một giải pháp tiên tiến để trình bày.
Chương 4. Cài đặt và thử nghiệm
    - Tận dụng source code có sẵn và tự viết để minh họa giải pháp ở chương 3.
Chương 5. Kết luận và hướng phát triển.
```
