# facial-landmark-localization

- Lịch họp định kỳ: 15h T7 hàng tuần
- Lịch họp đột xuất (nếu có): 15h T4

# TODO: Trưa và chiều T4, 09/04

- Sáng thứ T4 (ngày 09/04), rảnh lúc 11h30 (I81)
  - Bắt đầu họp vào 12h30 + meeting offline ở thư viện
- Viết các phần trong report cho báo cáo cuối kỳ
- Soạn câu hỏi cho giảng viên về yêu cầu của report giữa kỳ:
  - **Câu 1:** Số trang kỳ vọng trong báo cáo đồ án giữa kỳ: từ `x` => `y` trang
  - **Câu 2:** Nội dung sẽ bao gồm những phần gì?
    - Dùng cấu trúc report hiện tại của nhóm để hỏi xem thầy sẽ cần phần nào trong báo cáo giữa kỳ
  - **Câu 3:** Hỏi lại 2 yêu cầu đầu tiên cho chắc chắn
  - **Câu 4:** Sẽ hỏi rõ hơn về yêu cầu "How to conduct demo?"
    - Thầy sẽ quan tâm cấu trúc trình bày vào buổi seminar của nhóm như thế nào: Từ `intro` -> `related works` -> `method` -> `experiment` -> `conclusion` -> `demo`?
  - **Câu 5:** Có cần trình bày step-by-step về mặt toán học khi chạy và huấn luyện mô hình hay không?
  - **Câu 6:** Về yêu cầu "You need to do more experiments and analyses" thì có phải thầy mong muốn nhóm sẽ tiến hành các thí nghiệm để so sánh giữa các mô hình trên các tập dữ liệu khác nhau hay không? Hay thầy muốn nhóm sẽ thực hiện nhiều ứng dụng từ "facial landmark detection".
  - **Câu 7:** Trong báo cáo nhóm sẽ trình bày 2 phương pháp: (1) phương pháp cổ điển trong sách version 2; và (2) phương pháp SOTA là `FaceXFormer`. Trong buổi thuyết trình nhóm có cần trình bày chi tiết phương pháp truyền thống hay không? Hay nhóm chỉ cần tập trung nhiều vào phương pháp SOTA?
  - **Câu 8:** Với yêu cầu "Đã học được gì từ chapter trong sách" thì nhóm sẽ trình bày nội dung trong sách phiên bản 2 (thầy cung cấp) hay phiên bản 3 (mới nhất)? Nội dung trong sách 3E sẽ hiện đại hơn đã đề cập đến các kiến trúc tiên tiến như transformer, và đề xuất các multitask framework, v.v.
  - **Câu 9:** Với yêu cầu trính bày SOTA method trong báo cáo giữa kỳ thì nhóm sẽ trình bày nội dung gì:
    - Motivation & Idea, Đặc điểm nổi bật (multitask framework), v.v.?
    - Có cần trình bày sâu vào kiến trúc không? Hay phần kiến trúc có thể để dành vào cuối kỳ để trình bày chi tiết hơn?
- Chapter 4: FaceXFormer
  - Motivation & Idea: Tín
  - Dicussion & Conclusion: Tín
  - Multitask training: Thiện
  - Các phần còn lại: Thông & Phát

# TODO: 15h T7, 29/03

- Tập trung vào `FaceXFormer` làm method chính
- Lấy phần tổng quan của `SPIGA`
  - Phần 2: Vẫn dựa chủ yếu vào sách + mở rộng thêm một số nội dung từ bài báo về công trình đó
    - Thêm phương pháp attention
- (Phát) Chương 2: Related works (tiến trình phát triển)
  - Bắt đầu từ phương pháp trong sách
  - Rồi mở rộng thêm từ các bài báo khác
  - 4 hướng chính: Thống kê + Coordinate regression + Heatmap regression + Transformer
- (Tín) Chương 3: Method trong sách (2E)
- (4 người đọc) Chương 4: SOTA method FaceXFormer
- (Thiện) Chương 5: Giới thiệu về tập dữ liệu, metric đánh giá, kết quả thực nghiệm
- (Thiện) Chương 6: Kết luận + Hướng phát triển trong tương lai (+ Hạn chế nếu có)
- (Thông) Chương 7: Demo ứng dụng (ảnh + video + camera (live))
- Note:
  - Từ chương 4 trở đi chỉ làm trên SOTA
- Output:
  - Viết báo cáo hoặc xây demo

# TODO: 15h T7, 22/03

- Mỗi người đọc 2 bài báo về `SPIGA` và `XFormer`
- Thử benchmark trên bộ dữ liệu `300W private` (Link Kaggle: https://www.kaggle.com/datasets/fcbf18ebbaa22b293898032c9190efeb737a2204b226031a905f91769f2b19cc):
  - ERT (DLib): Thiện
  - Adaptive Wing: Tín
  - SPIGA: Phát
  - FaceXFormer: Thông
- Sau khi chạy xong sẽ điền kết quả vào sheet Evaluation
- Viết thêm related works

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
