# BÀI 05 — TDD, viên gạch chưa hề thử tải — bảng hình

Scene bắt buộc mới: **slide 4 = `vpg-traffic-pole`** (tĩnh, không bật `data-mode="traffic-light"` vì
chỉ có 2 câu mà pole có 3 đèn — theo đúng lối thoát brief mục 3 cho phép, kiểu `deck_sp02` slide 9).
**Slide 9 = `flow-diagram`** (flow-old bị gạch = "mã trước, test sau"; flow-new = "test trước, mã sau"),
đặt ở đây vì đúng khớp lý do brief nêu ("cách cũ xây xong mới thử bị gạch") — không đặt lại ở slide 3
để khỏi trùng scene với chính flow-diagram, và để `data-slide="2"` (slide 3) dùng lại các mảnh có sẵn
trong `deck_sp02` (`hk-strike`, `vpg-proof-chip`, `hk-note`) thay vì mở lại flow-diagram ở đó.

⚠️ Màu ĐỎ trong bài này = "phép thử đang hỏng, ĐÚNG như mong đợi" (tốt), không phải cảnh báo lỗi —
mọi khung `sg-warn`/đỏ trong bài phải đi kèm chữ xác nhận đó là điều nên xảy ra, không để trơ một mình
trông như báo lỗi thật.

| Slide | Lời rút gọn | Chữ lên màn hình | Hình gì CHUYỂN ĐỘNG |
| :-: | :-- | :-- | :-- |
| 1 | Người thợ đóng dấu đạt lên viên gạch, chưa từng đặt cân nặng nào lên nó | **"Chưa hề thử tải"** · phụ đề "TDD, bài 05" · chip: "đóng dấu đạt" / "chưa từng cân" | Tái dùng hero `deck_sp02` (icon quyển sổ → đổi icon viên gạch/cân), orbit ring quay, 2 chip bay vào |
| 2 | Xưởng dựng cả tường từ gạch đã đóng dấu; ngày 10 vẫn ổn, ngày 15 sụp một góc | kicker "chưa ai thử tải" · tiêu đề "Mười lăm ngày sau" · 3 ô: XƯỞNG / NGÀY 10 / NGÀY 15 | Tái dùng `workflow-grid` + `vpg-route-lane` của `deck_sp02` slide 2: route-lane chạy packet "đóng dấu → đứng thẳng → sụp góc"; `hk-note` đỏ hiện "một góc tường sụp xuống" |
| 3 | Lỗi không ở tay nghề, mà ở việc con dấu chưa từng bị thử | kicker "không phải" · tiêu đề gạch "tại thợ ẩu?" · proof-chip "gạch đúng loại, thợ vẫn giỏi" · hk-note "con dấu đạt CHƯA TỪNG bị thử" | Dùng lại mảnh có sẵn trong `deck_sp02` (không mở flow-diagram ở đây): thẻ tiêu đề có `hk-strike` gạch ngang "tại thợ ẩu?", rồi `vpg-proof-chip` hiện lên, rồi `hk-note` sáng lên nhấn nguyên nhân thật |
| 4 | ⭐ Coi cả vòng như cây cột đèn 3 màu, đèn đỏ bật trước tiên, cố ý | nhãn cột đèn: "ĐỎ · DỌN · XANH" · caption "bật đỏ trước, cố ý" | **`vpg-traffic-pole` mới, TĨNH**: 3 đèn đã sáng sẵn (`lit-red`/`lit-yellow`/`lit-green` bake cứng, không dùng `data-mode`), reveal 1 = cả cột đèn hiện lên; reveal 2 = `vpg-proof-chip` "để chắc mắt còn thấy nó sáng" |
| 5 | Việc này tên là TDD: đỏ là test thất bại, xanh là mã tối thiểu, dọn là bước cuối | tên lớn **"TDD"** · 3 chip: "ĐỎ — thất bại" / "XANH — mã tối thiểu" / "DỌN — mã sạch, vẫn xanh" | Tái dùng `hk-names` + `sg-verify` của `deck_sp02` slide 5: tên TDD hiện lớn, 3 `sg-vchip` hiện lần lượt đúng thứ tự Đỏ→Xanh→Dọn |
| 6 | Ví dụ thật: một tập tin tự chấm phép thử của bộ hook, không tốn lượt mô hình nào, trần 13.000 ký tự | thẻ file: `_thu_hook.py` · dòng "0 lượt mô hình" · badge số "13.000 ký tự" | Tái dùng `sc-file` (thẻ dạng tập tin) của `deck_sp02` slide 7: reveal 1 thẻ file hiện tên, reveal 2 dòng "tự chấm chính bộ hook", reveal 3 proof-chip có con số thật |
| 7 | Giả sử thêm luật mới; bước 1 tạo lỗi nhỏ nhất, bước 2 chạy thấy đỏ đúng lý do | terminal: "LUẬT MỚI — thiếu khoang trạng thái" · dòng lệnh bước 1 · dòng lệnh bước 2 (đỏ) | Tái dùng `mock-terminal` của `deck_sp02` slide 8: 3 dòng terminal hiện lần lượt, dòng bước 2 tô màu đỏ (đỏ = ĐÚNG như mong đợi, có chữ chú thích kèm, không để trơ) |
| 8 | Bước 3 thêm kiểm tra tối thiểu, bước 4 chạy hết mọi test, tất cả phải xanh | 2 ô: "BƯỚC 3 — mã tối thiểu" / "BƯỚC 4 — test mới + test cũ" · proof-chip "tất cả xanh" | Tái dùng `workflow-grid` của `deck_sp02` slide 2 (đổi nhãn NGÀY→BƯỚC): 2 ô hiện, rồi proof-chip xanh sáng lên |
| 9 | ⭐ Bẫy: viết mã trước, test sau, không phải TDD. Né bằng cách bắt test đỏ trước khi có mã | flow cũ gạch: "mã trước · test sau" · flow mới sáng: "test trước · mã sau" · hk-note "y như bắt gạch chịu tải trước khi đóng dấu" | **`flow-diagram` mới cho bài này**: `flow-old` + `flow-strike` gạch ngang "mã trước, test sau"; `flow-new` + `flow-glow` sáng lên "test trước, mã sau"; `hk-note` chốt cách né |
| 10 | Đừng đóng dấu rồi mới thử gạch; để test đỏ trước, xanh sau đó mới có nghĩa | **"Đừng đóng dấu rồi mới thử gạch"** · dòng chốt: "một cân nặng thật đã từng đặt lên nó" | Tái dùng `glowing-conclusion` của `deck_sp02` slide 10: orb sáng dần, icon đổi thành viên gạch/cân, lockup line hiện cuối cùng |
