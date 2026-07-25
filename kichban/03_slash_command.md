TIÊU ĐỀ: Slash command — cái nút bấm tự chế
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Có những lời dặn bạn nói lại gần như mỗi ngày.
CHỮ: những lời dặn
CHỮ*: nói lại mỗi ngày
---
LỜI: Ví dụ, mỗi lần bắt đầu buổi làm việc, bạn đều dặn AI đúng một đoạn.
CHỮ: mỗi lần bắt đầu buổi làm
CHỮ*: đúng một đoạn dặn
---
LỜI: Đọc file bàn giao. Xem việc nào đang dở. Báo lại cho tôi trước khi tự làm gì.
CHỮ: "đọc file bàn giao"
CHỮ: "xem việc nào đang dở"
CHỮ: "báo tôi trước khi tự làm"
---
LỜI: Gõ lần thứ nhất thì đủ. Lần thứ năm bắt đầu lười. Lần thứ mười, bạn gõ thiếu mất một ý.
CHỮ: lần 1 — đủ
CHỮ: lần 5 — lười
CHỮ*: lần 10 — gõ thiếu
---
LỜI: Mà thiếu ý nào thì AI bỏ qua đúng ý đó. Nó không đọc được cái bạn định nói.
CHỮ*: thiếu ý nào — bỏ qua ý đó
---
LỜI: Slash command là cách bạn cất đoạn dặn ấy vào một cái nút. Từ đó chỉ bấm nút.
CHỮ*: CẤT ĐOẠN DẶN VÀO MỘT NÚT
CHỮ: từ đó chỉ bấm nút
---
LỜI: Cách làm chỉ đúng một bước: tạo một file trong thư mục lệnh.
MÃ: .claude/commands/dauphien.md
CHỮ*: chỉ một bước, tạo 1 file
---
LỜI: Tên file chính là tên lệnh. File tên đầu phiên thì gõ gạch chéo đầu phiên là chạy.
MÃ: dauphien.md  →  /dauphien
CHỮ*: tên file = tên lệnh
---
LỜI: Bên trong file viết gì? Viết đúng cái bạn vẫn gõ tay. Không cú pháp, không dấu ngoặc, không gì hết. Nó là lời dặn bằng tiếng Việt bình thường.
CHỮ: nội dung = lời dặn thường
CHỮ*: KHÔNG phải lập trình
---
LỜI: Trong dự án của tôi có năm cái nút như vậy. Hai cái dùng nhiều nhất là đầu phiên và cuối phiên.
MÃ: /dauphien — đọc bàn giao, nhận việc
MÃ: /cuoiphien — ghi lại 4 cuốn sổ
---
LỜI: Cái nút cuối phiên tiết kiệm cho tôi nhiều nhất. Vì đó là việc dễ quên nhất: xong việc thì ai cũng muốn nghỉ, không muốn ngồi ghi sổ.
CHỮ: việc dễ quên nhất
CHỮ*: ghi sổ sau khi đã xong việc
---
LỜI: Muốn truyền thêm dữ liệu vào nút thì dùng một chỗ trống. Bạn gõ lệnh kèm mã cổ phiếu, nó tự điền vào đúng chỗ.
MÃ: $ARGUMENTS
MÃ: /nghiencuu PMS CKD
CHỮ: chỗ trống tự điền
---
LỜI: Đừng nhầm cái nút với cái nghề. Nút là bạn bấm thì nó chạy. Nghề là nó tự nhận ra lúc nào cần rồi tự bật. Bài sau tôi nói về cái nghề.
CHỮ: nút = BẠN bấm
CHỮ*: nghề = NÓ tự bật
---
LỜI: Khi nào thì nên làm nút? Khi bạn đã gõ đúng đoạn đó tới lần thứ ba. Chưa tới ba lần thì chưa biết mình thật sự cần gì.
CHỮ: làm nút khi nào?
CHỮ*: sau lần gõ thứ BA
---
LỜI: Việc lặp đi lặp lại mà làm bằng tay, sớm muộn cũng có ngày làm thiếu một bước.
CHỮ: Việc lặp làm bằng tay
CHỮ*: sớm muộn cũng thiếu bước.
