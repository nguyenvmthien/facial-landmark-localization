# facial-landmark-localization

- Lịch họp định kỳ: 15h T7 hàng tuần
- Lịch họp đột xuất (nếu có): 15h T4

# TODO: 13h CN, 11/05

- Họp review cho seminar
- Viết báo cáo cho seminar
  - Nội dung của chương 5 phải chia thành 3 phần rõ ràng
- Làm slide thuyết trình cho seminar
  - Link Canva đã gửi trong nhóm
- Làm demo cho seminar
  - Nếu quay sẵn video cho buổi trình bày thì phải dùng nền sáng

## Cấu trúc báo cáo

```
Chương 5 - Giới thiệu về tập dữ liệu, độ đo đánh giá, và kết quả thực nghiệm
|
5.1. Thực nghiệm trong paper (Thiện) => subsection
| - Giới thiệu về tập dữ liệu, độ đo đánh giá, thiết lập thí nghiệm
| - Kết quả và nhận xét
|
5.2. Thực nghiệm trên tập dữ liệu iBug (Tín)
| - ...
| - Kết quả và nhận xét
|
5.3. Ứng dụng (Thông)
| - ...
```

## Slide thuyết trình

1. Introduction => Thiện
2. Related works => Thiện
3. Method => Phát
4. Experiments & Demo
   - Trên paper => Thiện
   - Train model => Tín
   - Demo ứng dụng => Thông
5. Dicussion & Conclusion => Thông
   - Nếu chỉ huấn luyện trên 1 task landmark detection thì khi đưa mô hình vào ứng dụng thực tiễn, nó sẽ khó trong việc nắm bắt tư thế đầu của người dùng (vd: xoay đầu 1 góc, v.v.) => Nhấn mạnh việc huấn luyện multitask training (đặc biệt là head pose est và landmark detection)

# TODO: Demo

## Lấy số liệu để báo cáo

- Link Kaggle:
  1. Train coord w/ WingLoss: https://www.kaggle.com/code/vmphat/train-model-coord
  2. Train heatmap w/ STARLoss: https://www.kaggle.com/code/vmphat/train-model-heatmap
  3. Test pretrained model: https://www.kaggle.com/code/vmphat/test-pretrained-model
- Kết quả:
  - Ghi ở sheet "Evaluation" trong file https://docs.google.com/spreadsheets/d/1sRzfZNLsH_zDZupy-x-obUzrgvaA6J3C5kZf52neDnw/edit?gid=686017112#gid=686017112
- Thử với các backbone khác nhau
  - Làm sao tích hợp được với `FaceXFormer`????

## Demo sản phẩm

- Deploy webapp lên HuggingFace để dùng free GPU

# TODO: Lịch họp

- Lịch họp:
  - Tối T5 (01/05): 19h
  - Trưa CN (04/05): 13h
  - Tối T6 (09/05): 19h
  - Trưa CN (11/05): 13h
- Nội dung:
  - Làm phần thực nghiệm cho bài báo
  - Bảng phân công công việc
  - Viết báo cáo cuối kỳ:
    - Phát: Team Info + Working Title
  - Làm slide cho seminar:
    1. Introduction => Thiện
    2. Related works => Thiện
    3. Method => Phát
    4. Experiments & Demo
       - Trên paper => Thiện
       - Train model => Tín
       - Demo ứng dụng => Thông
    5. Dicussion & Conclusion => Thông
       - Nếu chỉ huấn luyện trên 1 task landmark detection thì khi đưa mô hình vào ứng dụng thực tiễn, nó sẽ khó trong việc nắm bắt tư thế đầu của người dùng (vd: xoay đầu 1 góc, v.v.) => Nhấn mạnh việc huấn luyện multitask training (đặc biệt là head pose est và landmark detection)
- Train model
  - Số lượng weights = Số lượng epoch + 1 (best)

# TODO: Đến deadline nộp báo cáo giữa kỳ

- Hoàn thành báo cáo giữa kỳ (midterm report) theo yêu cầu của giảng viên
- Bổ sung thêm những nội dung còn thiếu

# TODO: 19h tối T7, 12/04

- YC1,2,3 dựa vào bảng phân công trên Zalo
- Bổ sung ý tưởng cho YC3:
  - Thử train lại 1 task thôi xem được không + giảm model size
  - Viết thêm mục "completion progress" (xem hình của Thiện gửi) cho báo cáo giữa kỳ
- Paper FaceXFormer dùng version 3

# TODO: 19h tối T6, 11/04

- Hoàn thành midterm report dựa theo yêu cầu đã được giảng viên giải đáp vào sáng T5
- Yêu cầu chính xác cho midterm report: sẽ cập nhật vào T5 (10/04)

# TODO: Trưa và chiều T4, 09/04

- Sáng thứ T4 (ngày 09/04), rảnh lúc 11h30 (I81)
  - Bắt đầu họp vào 12h30 + meeting offline ở thư viện
- Viết các phần trong report cho báo cáo cuối kỳ
- Soạn câu hỏi cho giảng viên về yêu cầu của report giữa kỳ:

## Danh sách câu hỏi

- **Câu 1:** Số trang kỳ vọng trong báo cáo đồ án giữa kỳ: từ `x` => `y` trang

```
- Báo cáo giữa kỳ: Không có giới hạn về số trang nhưng nên trình bày đầy đủ các ý được yêu cầu
- Báo cáo cuối kỳ: 20-30 trang
```

- **Câu 2:** Nội dung của báo cáo giữa kỳ sẽ bao gồm những phần gì?
  - Dùng cấu trúc report hiện tại của nhóm để hỏi xem thầy sẽ cần phần nào trong báo cáo giữa kỳ

```
- 3 yêu cầu trên Moodle là "yêu cầu tối thiểu" phải có trong báo cáo giữa kỳ
- Nhóm có thể viết thêm các nội dung khác nếu muốn. Ví dụ:
  - Cấu trúc chung của báo cáo cuối kỳ, nội dung chính của các chapter
  - Danh sách tài liệu tham khảo được sử dụng trong báo cáo giữa kỳ và cuối kỳ
```

- **Câu 3:** Hỏi lại 3 yêu cầu của báo cáo giữa kỳ

```
Midterm report không có format cụ thể, nhưng phải có đủ 3 ý, có thể trình bày thêm các nội dung khác

[1] YC1: Giới thiệu về chủ đề, bài toán, task cần thực hiện là gì?

[2] YC2:
- Nêu ra tên? Năm paper ra mắt? Link bài báo? Công trình này có được công bố trên 1 hội nghị lớn nào hay không?
- Mô tả phương pháp, mục đích của method này là gì, input đầu vào là gì, output đầu ra là gì?
- Nêu những điểm nổi bật của phương pháp?
- Có thể nói thêm về cách hoạt động của mothod? Nếu nhóm đã hiểu về phương pháp thì cho một ví dụ minh họa để xem dữ liệu đầu vào sẽ trải qua những bước biến đổi như thế nào khi đi vào framework?

[3] YC3: (Làm sao để làm ra được sản phẩm demo?)
- How?: Làm sao để chạy được phần thực nghiệm? Nhóm sẽ trình bày ra cách mà nhóm sẽ thực nghiệm như thế nào?
- Thu thập dữ liệu, huấn luyện, tinh chỉnh về RAM, v.v.
- Đây là phần để nhóm tự do sáng tạo

[4] Nêu thêm tài liệu tham khảo được sử dụng
```

- **Câu 4:** Sẽ hỏi rõ hơn về yêu cầu "How to conduct demo?"
  - Thầy sẽ quan tâm cấu trúc trình bày vào buổi seminar của nhóm như thế nào: Từ `intro` -> `related works` -> `method` -> `experiment` -> `conclusion` -> `demo`?

```
- YC3: Xem phần trả lời ở câu 3
- Phần method không cần trình bày phương pháp được đề cập trong sách mà sẽ trình bày 1 phương pháp SOTA mà nhóm tìm được ở bên ngoài
```

- **Câu 5:** Có cần trình bày step-by-step về mặt toán học khi chạy và huấn luyện mô hình hay không?

```

```

- **Câu 6:** Về yêu cầu "You need to do more experiments and analyses" thì có phải thầy mong muốn nhóm sẽ tiến hành các thí nghiệm để so sánh giữa các mô hình trên các tập dữ liệu khác nhau hay không? Hay thầy muốn nhóm sẽ thực hiện nhiều ứng dụng từ "facial landmark detection".

```
- Nếu được thì nhóm có thể tiến hành huấn luyện lại mô hình trên các tập dữ liệu nhỏ hơn để kiểm tra lại số liệu của mô hình xem có khớp với số liệu được công bố hay không?
- Nhóm sẽ cần xây dựng 1 ứng dụng nhỏ để demo cho thầy thấy được khả năng của mô hình mà nhóm đã chọn (vd: mô hình xác định điểm mốc trên khuôn mặt tốt như thế nào?), sau đó có thể cải tiến thêm ứng dụng (vd: gắn mắt kính lên mặt, v.v.)
```

- **Câu 7:** Trong báo cáo nhóm sẽ trình bày 2 phương pháp: (1) phương pháp cổ điển trong sách version 2; và (2) phương pháp SOTA là `FaceXFormer`. Trong buổi thuyết trình nhóm có cần trình bày chi tiết phương pháp truyền thống hay không? Hay nhóm chỉ cần tập trung nhiều vào phương pháp SOTA?

```
- Đối với cả báo cáo và thuyết trình: Nhóm không cần trình bày phương pháp cũ được đề cập trong sách mà tập trung vào SOTA method luôn
```

- **Câu 8:** Với yêu cầu "Đã học được gì từ chapter trong sách" thì nhóm sẽ trình bày nội dung trong sách phiên bản 2 (thầy cung cấp) hay phiên bản 3 (mới nhất)? Nội dung trong sách 3E sẽ hiện đại hơn đã đề cập đến các kiến trúc tiên tiến như transformer, và đề xuất các multitask framework, v.v.

```
- Có thể dùng nội dung trong sách 2E hoặc 3E đều được
- Nếu dùng nội dung trong sách 3E thì phải đính kèm cuốn sách 3E (file .PDF) vào bài nộp giữa kỳ luôn
- Không cần phải trình bày phương pháp được đề cập trong sách vì nó có thể đã quá cũ rồi
- Nhóm chỉ dùng sách để xác định chủ đề và hiểu rõ hơn về bài toán.
```

- **Câu 9:** Với yêu cầu trình bày SOTA method trong báo cáo giữa kỳ thì nhóm sẽ trình bày nội dung gì:
  - Motivation & Idea, Đặc điểm nổi bật (multitask framework), v.v.?
  - Có cần trình bày sâu vào kiến trúc không? Hay phần kiến trúc có thể để dành vào cuối kỳ để trình bày chi tiết hơn?

```
- Trong báo cáo giữa kỳ chỉ cần trình bày giống như được mô tả trong phần trả lời của câu 3
- Trong báo cáo cuối kỳ mới cần phải trình bày chi tiết hơn về kiến trúc của phương pháp SOTA
```

## Những nội dung khác có liên quan

- Báo cáo có thể viết tiếng Việt hay tiếng Anh đều được (thầy khuyến khích viết tiếng Anh)
- Nên viết thành paragraph chứ không nên liệt kê
- Nên đánh tài liệu tham khảo vào phần trình bày
- Chọn chủ đề trong sách, nhưng có thể chọn phương pháp bên ngoài và thực nghiệm lại phương pháp (chạy phương pháp trên dataset) đã chọn
- Nếu không có khả năng train model thì phải hiểu rất rõ phương pháp để trình bày lại cho 2 thầy
- Nếu có thể nâng cấp, cải tiến mô hình thì sẽ tốt hơn
- Chỉ 1 thành viên dại diện nộp bài lên Moodle

## Final Submission

- Ngày nộp trên Moodle có thể sớm hơn ngày seminar trên lớp
- Các nội dung cần nộp (xem rõ hơn trên Moodle):
  - `PPT`: Nộp file thuyết trình
    - Đến buổi seminar, thầy cho phép chỉnh sửa lại slide nếu cần, nhưng phải nói cho thầy biết để thầy mở lại link nộp bài
    - Nên làm slide trên PowerPoint hoặc Google Slide để có thể nộp file .ppt hoặc .pptx
    - Có thể nộp file .PDF nếu nhóm làm trên Canva
  - `Báo cáo`: Report từ 20-30 trang (File PDF)
    - Thầy khuyến khích nên có đủ các phần như trong file báo cáo của 1 nhóm trong năm trước (file này nhóm mình có rồi)
    - Phần `Related works`: 2-3 phương pháp trước đó rồi mới dẫn nhập cho phương pháp của nhóm (các phương pháp trước đó có nhược điểm gì mà mình cần phải có phương pháp mới)
    - Phần `Method`: Nên trình bày step-by-step các hoạt động của method (có thể dùng hình ảnh minh họa cho dễ hiểu)
    - Phần `Demo`: Có thể quay video demo để chiếu lên cho thầy và các bạn xem, nêu về phần cứng sử dụng, v.v.
    - Phần `Experiment`: Trình bày thêm về các tập dữ liệu được sử dụng, metric để đánh giá, đưa vào một vài hình ảnh thực nghiệm
    - Phần `References`: Phải nêu chi tiết về tài liệu tham khảo (nên dùng định dạng citation chuẩn)
  - `Source code`: Toàn bộ source code và dữ liệu liên quan (có thể nộp file nén hoặc gửi link GitHub của nhóm)
  - `.DOC`: File mô tả công việc chi tiết của từng thành viên trong nhóm
    - File .doc cố gắng trình bày rõ nội dung phân công công việc cho mỗi thành viên
- Nộp 1 file .txt chứa link đến Google Drive trên Moodle

## Seminar cuối kỳ

- Thuyết trình trên lớp (offline), các bạn khác và 2 TA sẽ nghe, có phần ký tên vào bảng điểm
- Mỗi nhóm có đúng `15 phút` thuyết trình (cả slide + demo), sau 15 phút bắt buộc dừng thuyết trình và chuyển sang vấn đáp (thường là trả lời từ 1-2 câu)
  - Slide đừng dài quá, không nên viết quá nhiều chữ, chỉ cần viết các ý chính thôi
  - Nên có hình ảnh minh họa cho dễ hiểu
- Tất cả nhóm vấn đáp vào 1 buổi sáng như đi học thông thường
- Khi trình bày thì tất cả thành viên sẽ đứng ở trên bục, không bắt buộc tất cả thành viên phải trình bày, nhưng khuyến khích các thành viên trình bày phần mà mình được phân công
- Thầy sẽ đặt các câu hỏi cho nhóm, thành viên nào trả lời cũng được
- Sau nghỉ lễ sẽ có lịch để seminar
  - Seminar sẽ diễn ra vào tuần đầu tiên của tháng 5
  - Có thể tổ chức vào sáng T5 (ngày 08/05)

## Task cho SOTA method

- Chapter SOTA method: FaceXFormer
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
