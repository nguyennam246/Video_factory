TIÊU ĐỀ: Hook — cái khoá, không phải lời dặn
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Tưởng tượng bạn thuê thợ về nhà. Nhưng sáng nào cũng là một người thợ mới.
CHỮ: mỗi sáng
CHỮ*: một người thợ MỚI
---
LỜI: Người thợ mới không biết gì về hôm qua. Nên sáng nào bạn cũng phải dặn lại từ đầu.
CHỮ: không biết gì về hôm qua
CHỮ*: sáng nào cũng dặn lại
---
LỜI: Bạn dặn: cái tủ hồ sơ gốc ở góc nhà, tuyệt đối đừng đụng vào.
CHỮ*: "Tủ hồ sơ gốc
CHỮ*: đừng đụng vào."
---
LỜI: Người thợ gật đầu. Hai mươi chín ngày đầu, không có chuyện gì.
CHỮ: ngày 1 → ngày 29
CHỮ*: không có chuyện gì
---
LỜI: Ngày thứ ba mươi, một người thợ vội. Quên lời dặn. Dọn luôn cái tủ.
CHỮ*: NGÀY 30
CHỮ: tủ hồ sơ gốc — mất
---
LỜI: Nhưng lỗi không nằm ở người thợ. Lỗi nằm ở chỗ bạn chỉ có lời dặn, mà không có cái khoá.
CHỮ: bạn có LỜI DẶN
CHỮ*: bạn không có CÁI KHOÁ
---
LỜI: Hook chính là cái khoá đó. Nó không nhờ ai nhớ. Nó chặn bàn tay lại, ngay lúc tay chạm vào tủ.
CHỮ*: HOOK = CÁI KHOÁ
CHỮ: chặn ngay lúc tay chạm vào
---
LỜI: Ví dụ thật của tôi. Trong máy tôi có một thư mục dữ liệu gốc. Mất là mất hẳn, không tải lại được.
CHỮ: thư mục dữ liệu gốc
CHỮ*: mất là mất hẳn
---
LỜI: Tôi lắp một cái khoá. Từ đó, hễ AI định chạy lệnh xoá hay ghi đè vào thư mục ấy, lệnh bị chặn trước khi kịp chạy.
MÃ: rm dulieu/BCTC.db → CHẶN
MÃ: sqlite3 ... SELECT → cho qua
CHỮ: lệnh chỉ ĐỌC vẫn chạy bình thường
---
LỜI: Cái khoá lắp được ở nhiều chỗ. Lúc thợ vừa bước vào cửa. Lúc thợ sắp với tay lấy đồ nghề. Hay lúc thợ chuẩn bị ra về.
CHỮ: lúc vừa vào cửa
CHỮ: lúc sắp cầm đồ nghề
CHỮ: lúc chuẩn bị ra về
---
LỜI: Mỗi chỗ có một cái tên. Nhớ hai cái đầu là đủ dùng.
MÃ: SessionStart — vừa vào cửa
MÃ: PreToolUse — sắp cầm đồ nghề
MÃ: Stop — chuẩn bị ra về
---
LỜI: Làm thế nào? Bạn viết một đoạn mã rất ngắn. Nó nhận vào tờ phiếu ghi thợ đang định làm gì, rồi trả lời đúng một chữ: cho, hay không cho.
CHỮ: nhận: "thợ định làm gì?"
CHỮ*: trả lời: CHO / KHÔNG CHO
---
LỜI: Rồi khai tên đoạn mã đó vào một file cài đặt. Hết. Không phải sửa gì bên trong AI cả.
MÃ: .claude/settings.json
CHỮ*: khai tên vào đây là xong
---
LỜI: Ta đi chậm qua một lần chặn thật, cho dễ hình dung. Bốn bước.
CHỮ*: MỘT LẦN CHẶN THẬT
CHỮ: bốn bước
---
LỜI: Bước một. AI định chạy một câu lệnh xoá file dữ liệu gốc.
CHỮ: bước 1 — AI định chạy
MÃ: rm dulieu/BCTC.db
---
LỜI: Bước hai. Trước khi lệnh chạy, tờ phiếu được chuyển tới đoạn mã của bạn. Trên phiếu ghi: công cụ là dòng lệnh, nội dung là câu xoá kia.
CHỮ: bước 2 — tờ phiếu tới tay bạn
MÃ: công cụ: Bash
MÃ: nội dung: rm dulieu/BCTC.db
---
LỜI: Bước ba. Đoạn mã của bạn đọc phiếu. Nó thấy có chữ xoá, và thấy đường dẫn nằm trong thư mục cấm. Nó trả lời: không cho.
CHỮ: bước 3 — đoạn mã soi phiếu
CHỮ: thấy "xoá" + thấy thư mục cấm
CHỮ*: trả lời: KHÔNG CHO
---
LỜI: Bước bốn. Lệnh không bao giờ chạy. AI nhận lại lời từ chối, kèm câu bạn dặn sẵn, và nó đi làm cách khác.
CHỮ: bước 4 — lệnh KHÔNG chạy
CHỮ*: AI đọc lời từ chối, đổi cách làm
---
LỜI: Điểm mấu chốt nằm ở bước hai. Cái khoá đứng trước, không phải đứng sau. Nếu nó chạy sau thì file đã mất rồi, chặn cũng vô nghĩa.
CHỮ: khoá đứng TRƯỚC
CHỮ*: đứng sau thì file đã mất
---
LỜI: Một mẹo khi thử. Muốn thử cái khoá chặn lệnh xoá, hãy nhắm vào một file không tồn tại. Khoá tốt thì nó chặn. Khoá hỏng thì lệnh xoá cũng chẳng xoá được gì.
CHỮ: thử khoá chặn lệnh xoá?
CHỮ*: nhắm file KHÔNG tồn tại
CHỮ: hỏng cũng vô hại
---
LỜI: Lời dặn thì có ngày bị quên. Cái khoá thì không.
CHỮ: Lời dặn có ngày bị quên.
CHỮ*: Cái khoá thì không.
