TIÊU ĐỀ: Kiểm chứng và bàn giao — có biên bản rồi mới trao chìa khóa
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Đội thợ báo căn nhà đã xong. Chủ nhà hỏi: đã thử điện chưa? Người thợ đáp: dây mới, chắc là được.
CHỮ: "chắc là được"
CHỮ*: không phải bằng chứng
---
LỜI: Một câu tự tin không làm bóng đèn sáng. Muốn bàn giao, phải bật từng công tắc và ghi kết quả vừa đo.
CHỮ: tự tin ≠ bằng chứng
CHỮ*: phải kiểm NGAY BÂY GIỜ
---
LỜI: Verification before completion có một luật: không được nói xong, đã sửa hay mọi test đều qua nếu chưa chạy lệnh kiểm chứng mới nhất.
CHỮ*: KHÔNG TUYÊN BỐ XONG
CHỮ: nếu chưa kiểm chứng mới
---
LỜI: Quy trình có năm bước. Một, xác định lệnh nào chứng minh lời mình sắp nói. Hai, chạy đầy đủ. Ba, đọc toàn bộ kết quả và mã thoát.
CHỮ: 1 — chọn phép chứng minh
CHỮ: 2 — chạy đủ
CHỮ*: 3 — đọc kỹ
---
LỜI: Bốn, đối chiếu xem kết quả có thật sự chứng minh lời nói không. Năm, chỉ khi khớp mới báo hoàn tất kèm bằng chứng.
CHỮ: 4 — đối chiếu
CHỮ*: 5 — báo cùng bằng chứng
---
LỜI: Test qua không chứng minh hình ảnh đúng. Linter sạch không chứng minh chương trình build được. Một agent báo xong không chứng minh file đã thay đổi.
CHỮ: test ≠ hình đúng
CHỮ: lint ≠ build
CHỮ*: lời báo ≠ sản phẩm
---
LỜI: Ví dụ thật: dây chuyền video từng render sạch, nhưng một dòng lệnh trên slide bị ngắt làm đôi. Tiến trình thoát số không, hình vẫn sai.
CHỮ: exit 0
CHỮ*: slide vẫn có thể SAI
---
LỜI: Vì đầu ra là ảnh và video, phép kiểm đúng phải gồm chụp các frame đại diện rồi mở ra soi bằng mắt.
CHỮ: đầu ra là HÌNH
CHỮ*: phải MỞ HÌNH RA SOI
---
LỜI: Ta thử một lần. Bước một, chạy bộ kiểm mapping câu với slide và vùng an toàn. Bước hai, render video.
CHỮ: bước 1 — kiểm cấu trúc
CHỮ*: bước 2 — render
---
LỜI: Bước ba, dùng công cụ đọc thông số để xác nhận đúng một nghìn không trăm tám mươi nhân một nghìn chín trăm hai mươi và đúng thời lượng.
MÃ: 1080 × 1920
CHỮ*: đúng kích thước · đúng thời lượng
---
LỜI: Bước bốn, chụp các frame đầu, giữa và cuối. Mở từng ảnh, kiểm chữ, thương hiệu, vùng an toàn và cảnh chuyển.
CHỮ: đầu · giữa · cuối
CHỮ*: mở ảnh và SOI
---
LỜI: Khi toàn bộ kế hoạch đã xanh, finishing a development branch mới xuất hiện. Nó chạy lại toàn bộ test trước khi đưa lựa chọn bàn giao.
CHỮ: test toàn bộ lần cuối
CHỮ*: rồi mới bàn chuyện nhập nhánh
---
LỜI: Ba lựa chọn thường là nhập về nhánh gốc tại máy, đẩy lên và tạo pull request, hoặc giữ nguyên nhánh để xử lý sau.
CHỮ: 1 — nhập tại máy
CHỮ: 2 — tạo PR
CHỮ*: 3 — giữ nguyên
---
LỜI: Agent không được tự chọn thay bạn. Nhập nhánh và dọn khu thi công là quyết định của chủ công trình.
CHỮ: agent trình lựa chọn
CHỮ*: chủ dự án QUYẾT ĐỊNH
---
LỜI: Bây giờ ghép cả khóa lại: làm rõ ý tưởng, chốt thiết kế, quây khu riêng, viết kế hoạch, TDD, thi công, review, gỡ lỗi, kiểm chứng, rồi bàn giao.
CHỮ: HIỂU → KẾ HOẠCH → LÀM
CHỮ*: KIỂM → BÀN GIAO
---
LỜI: Chìa khóa không phải bằng chứng căn nhà đã xong. Biên bản kiểm tra mới là thứ cho phép bạn trao chìa khóa.
CHỮ: chìa khóa là lời tuyên bố
CHỮ*: biên bản mới là BẰNG CHỨNG
