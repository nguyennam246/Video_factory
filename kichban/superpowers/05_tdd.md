TIÊU ĐỀ: TDD — thử viên gạch trước khi xây bức tường
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Một xưởng gạch nói viên gạch chịu được một trăm ký. Họ đặt viên gạch lên bàn, nhưng không đặt tải lên. Rồi đóng dấu đạt.
CHỮ: lời hứa: chịu 100 kg
CHỮ*: chưa hề đặt tải
---
LỜI: Con dấu ấy không chứng minh được gì. Muốn biết phép thử có tác dụng, ta phải thấy nó bắt được viên gạch chưa đạt.
CHỮ: phép thử phải BẮT được lỗi
CHỮ*: trước khi đóng dấu đạt
---
LỜI: TDD áp dụng đúng nguyên tắc đó cho mã nguồn: viết phép thử trước, nhìn nó thất bại đúng lý do, rồi mới viết mã chạy thật.
CHỮ*: TDD
CHỮ: test trước · mã sau
---
LỜI: Vòng này có ba màu. Đỏ: viết một test nhỏ và thấy nó thất bại. Xanh: viết ít mã nhất để test qua. Dọn: làm mã sạch hơn mà test vẫn xanh.
CHỮ: ĐỎ — test thất bại
CHỮ: XANH — mã tối thiểu
CHỮ*: DỌN — sạch, vẫn xanh
---
LỜI: Điểm khó nhất không phải viết test. Điểm khó là bắt buộc phải nhìn thấy màu đỏ trước.
CHỮ: test viết sau
CHỮ*: không chứng minh nó bắt được lỗi
---
LỜI: Nếu test vừa viết đã qua, có thể chức năng đã tồn tại, hoặc test đang kiểm nhầm thứ. Phải sửa test cho tới khi nó thất bại đúng lý do mong đợi.
CHỮ: test qua ngay?
CHỮ: có thể kiểm nhầm
CHỮ*: sửa tới khi đỏ ĐÚNG
---
LỜI: Ví dụ thật trong dự án này có một thước kiểm hook không tốn API.
MÃ: video/.Codex/hooks/_thu_hook.py
CHỮ*: thước kiểm 0 API
---
LỜI: Giả sử ta thêm luật: khi file bàn giao mất khoang trạng thái, hook phải báo lỗi. Ta đi chậm qua bốn bước.
CHỮ: luật mới
CHỮ*: thiếu khoang trạng thái → BÁO LỖI
---
LỜI: Bước một, tạo đầu vào thiếu đúng khoang đó. Viết test đòi mã thoát khác không và có câu báo rõ.
CHỮ: bước 1 — tạo lỗi nhỏ nhất
CHỮ*: đòi đúng mã + đúng lời báo
---
LỜI: Bước hai, chạy test. Nó phải đỏ vì hook hiện chưa biết luật mới, không phải đỏ vì gõ sai tên file.
CHỮ: bước 2 — nhìn thấy ĐỎ
CHỮ*: đỏ đúng lý do
---
LỜI: Bước ba, thêm phần kiểm tra tối thiểu vào hook. Không tiện tay sửa tên hàm, đổi cấu trúc hay thêm ba luật khác.
CHỮ: bước 3 — mã tối thiểu
CHỮ*: không sửa lan
---
LỜI: Bước bốn, chạy test mới và toàn bộ thước cũ. Khi tất cả xanh, mới dọn tên biến hoặc tách hàm nếu cần.
CHỮ: bước 4 — test mới + test cũ
CHỮ*: xanh rồi mới dọn
---
LỜI: Bẫy quen thuộc là viết mã trước, giữ nó làm tài liệu tham khảo, rồi viết test quanh chính cách mã đã làm. Đó là test sau, không phải TDD.
CHỮ: mã trước · test sau
CHỮ*: KHÔNG phải TDD
---
LỜI: Một test tốt kiểm hành vi thật và chỉ một hành vi. Nếu tên test có ba chữ và, hãy cân nhắc tách nó.
CHỮ: 1 test
CHỮ*: 1 hành vi rõ
---
LỜI: Đừng đóng dấu rồi mới thử gạch. Hãy để phép thử thất bại trước, để bạn biết màu xanh sau đó có ý nghĩa.
CHỮ: thấy ĐỎ trước
CHỮ*: màu XANH mới có nghĩa

