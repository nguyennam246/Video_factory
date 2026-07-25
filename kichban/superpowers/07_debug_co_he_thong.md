TIÊU ĐỀ: Systematic debugging — tìm chỗ ống vỡ trước khi thay vòi
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Vòi nước tầng hai chảy yếu. Người thợ đoán vòi hỏng, thay vòi mới. Nước vẫn yếu.
CHỮ: nước chảy yếu
CHỮ*: thay vòi — vẫn yếu
---
LỜI: Anh ta thay tiếp máy bơm, rồi thay van. Mỗi lần tốn thêm tiền, nhưng chưa lần nào biết nước mất áp ở đâu.
CHỮ: thay bơm · thay van
CHỮ*: vẫn chưa biết VÌ SAO
---
LỜI: Sửa mò là thay đồ ở nơi thấy triệu chứng. Gỡ lỗi có hệ thống là lần theo dòng nước tới đúng chỗ ống vỡ.
CHỮ: triệu chứng ở vòi
CHỮ*: nguyên nhân có thể ở nơi khác
---
LỜI: Skill systematic debugging có luật: chưa điều tra nguyên nhân gốc thì chưa đề xuất cách sửa.
CHỮ*: KHÔNG SỬA
CHỮ: khi chưa tìm nguyên nhân gốc
---
LỜI: Pha một là thu bằng chứng. Đọc hết lỗi, tái hiện ổn định, xem thay đổi gần đây, rồi đo đầu vào và đầu ra ở từng chặng.
CHỮ: pha 1 — BẰNG CHỨNG
CHỮ: đọc · tái hiện · đo
---
LỜI: Pha hai là tìm mẫu. So chỗ hỏng với một chỗ tương tự đang chạy được, rồi liệt kê mọi điểm khác nhau.
CHỮ: pha 2 — SO SÁNH
CHỮ*: chạy được ↔ đang hỏng
---
LỜI: Pha ba là nêu đúng một giả thuyết và thử bằng thay đổi nhỏ nhất. Sai thì bỏ giả thuyết, không chồng thêm hai cách sửa khác.
CHỮ: pha 3 — MỘT GIẢ THUYẾT
CHỮ*: một biến mỗi lần
---
LỜI: Pha bốn mới sửa nguyên nhân gốc. Trước khi sửa phải có một phép thử tái hiện lỗi; sau đó kiểm cả lỗi cũ lẫn những thứ xung quanh.
CHỮ: pha 4 — SỬA GỐC
CHỮ*: có test tái hiện trước
---
LỜI: Ví dụ thật của dự án này: một video có nhạc nhưng người xem không nghe rõ giọng. Đo file cho thấy giọng thuần khoảng âm hai mươi hai phẩy bốn đề xi ben.
CHỮ: lỗi thật
MÃ: giọng thuần ≈ −22,4 dB
---
LỜI: Sau khi trộn, toàn video chỉ còn khoảng âm ba mươi phẩy bảy đề xi ben. Dữ liệu chỉ đúng chặng làm âm lượng tụt: khâu trộn.
MÃ: sau trộn ≈ −30,7 dB
CHỮ*: lỗi nằm ở KHÂU TRỘN
---
LỜI: So công thức đang hỏng với cách trộn chuẩn, nguyên nhân lộ ra: bộ amix mặc định tự chia nhỏ mức của các kênh.
MÃ: amix normalize mặc định
CHỮ*: tự làm mọi kênh nhỏ đi
---
LỜI: Giả thuyết là tắt phép chuẩn hóa ấy và tự đặt mức từng kênh. Chỉ thay đúng biến đó, rồi đo lại.
MÃ: amix normalize=0
CHỮ*: thử đúng MỘT thay đổi
---
LỜI: Bản mới đo được khoảng âm mười tám phẩy tám đề xi ben. Số đo chứng minh đúng chặng đã đổi; còn hay hay dở thì người dùng phải nghe và phán.
MÃ: bản mới ≈ −18,8 dB
CHỮ: máy đo mức
CHỮ*: người nghe phán chất giọng
---
LỜI: Nếu ba cách sửa liên tiếp đều thất bại và mỗi cách lộ một lỗi ở chỗ khác, Superpowers yêu cầu dừng để xem lại kiến trúc.
CHỮ: 3 lần sửa vẫn thất bại
CHỮ*: dừng — hỏi lại KIẾN TRÚC
---
LỜI: Đừng thay vòi vì nước yếu ở vòi. Hãy đo đường ống, tìm đúng chỗ vỡ, rồi chỉ sửa một chỗ đó.
CHỮ: đừng sửa TRIỆU CHỨNG
CHỮ*: hãy sửa NGUYÊN NHÂN

