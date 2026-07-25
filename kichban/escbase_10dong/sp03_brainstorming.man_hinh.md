# MÀN HÌNH — sp03_brainstorming (Bài 03 khoá Superpowers)

Khuôn `[1,3,3,2,3,3,3,3,3,3]` = 27 reveal. Mỗi câu lời = 1 reveal.
Ẩn dụ xuyên khoá: **xây một căn nhà**. Vật thể chủ đạo bài này: **tấm bản vẽ** (bản thiết kế
giấy) — nối mạch từ "cuốn sổ tay thi công" của bài 02, KHÔNG lặp lại hình ảnh cuốn sổ/cái cổng.

⚠️ **Deck HTML/CSS của bài này CHƯA DỰNG ĐƯỢC trong phiên này** (xem báo cáo cuối). Bảng dưới
là **bản kế hoạch hình** để người dựng deck (thợ 1, hoặc chính tôi ở phiên có quyền chạy lệnh)
theo đúng mục 3 của brief: 2 mẫu MỚI bắt buộc `stream-visual` (slide 5) + `vpg-chat-message`
(slide 7); các slide còn lại tái dùng scene đã có trong `deck_sp02` (`workflow-grid`,
`flow-diagram`, `sc-file`, `hk-versus`, `mock-terminal`, `risk-cards-container`,
`glowing-conclusion`).

| Slide | Lời đọc (rút gọn) | Chữ lên màn hình | Hình gì chuyển động |
| :-: | :-- | :-- | :-- |
| 1 | Bếp vừa xây xong, sáu người chen trong lối đi rộng một mét | `BẾP: VỪA XÂY XONG` / `LỐI ĐI: 1 MÉT` | Hero giống cấu trúc slide 1 `deck_sp02` (orbit + tiêu đề). Orbit chip đổi thành 4 nhãn của quy trình brainstorming: `đọc trước` · `hỏi từng câu` · `so hướng` · `chờ duyệt`. Tiêu đề gradient: `"Bếp tiện?"`. `repo-stats` hai chip: `chỉ một câu dặn` / `1 mét lối đi` |
| 2 | Ngày đặt hàng chỉ một câu · ngày lắp tủ, mỗi người một cái bếp khác trong đầu | `NGÀY ĐẶT — 1 câu dặn` · `NGÀY LẮP — mỗi người 1 kiểu` | `workflow-grid` 3 cột (tái dùng class `deck_sp02` slide 2): cột 1 icon miệng nói (dặn dò), cột 2 icon người thợ gật, cột 3 icon tủ + dấu X (lệch). Route-lane packet chạy từ "một câu" tới "khác nhau trong đầu", kết ở nhãn "LỆCH" |
| 3 | Lỗi không ở tay nghề, họ lắp đúng cái họ nghĩ · lỗi ở chỗ trống chưa ai hỏi | `KHÔNG PHẢI: tay nghề` · `LÀ: chỗ trống chưa hỏi` | `flow-diagram` + `flow-strike` (tái dùng `deck_sp02` slide 3): reveal 1 nhãn "TAY NGHỀ KÉM?" bị gạch đỏ; reveal 2 proof-chip "vẫn lắp thẳng, lắp chắc, đúng cái họ nghĩ"; reveal 3 node mới "chỗ trống chưa ai hỏi" sáng lên |
| 4 | Chỗ trống bị lấp bằng phỏng đoán · bản vẽ chưa có nét nào | `PHỎNG ĐOÁN — mỗi người 1 kiểu` · `BẢN VẼ — 0 nét` | `sc-file` 2 thẻ (tái dùng class slide 7 của `deck_sp02`): thẻ 1 "BẢN VẼ" với icon tờ giấy trắng/đứt nét (trống); thẻ 2 "PHỎNG ĐOÁN" liệt kê 3 chip mâu thuẫn nhau (vd "1 người?" / "6 người?" / "xe lăn?") |
| 5 | Trang brainstorming: nối câu hỏi thành bản vẽ chung, không vẽ liều từ câu đầu, biến câu mơ hồ thành bản vẽ hai bên hiểu | `BRAINSTORMING` · dòng câu hỏi → BẢN VẼ | ⭐ **`stream-visual`/`stream-pipe`/`stream-data` (mẫu MỚI, ảnh mẫu `slide10.png`)**: ống dẫn nằm ngang, các gói `stream-data` (mỗi gói = 1 câu hỏi) chạy dọc ống từ node "Ý TƯỞNG MỜ" bên trái tới node "BẢN VẼ CHUNG" sáng dần bên phải khi gói đến nơi |
| 6 | Ví dụ thật dự án video: bài ba đến bài mười, tự đổi diện mạo · câu hỏi đầu: 8 bộ mặt làm tay hay 1 bộ quy tắc | `việc thật: bài 3 → 10` · `8 mẫu tay` ↔ `1 bộ quy tắc` | `hk-versus` (tái dùng class slide 7 của `deck_sp02`): node trái "8 BÀI, 8 DIỆN MẠO" (icon cây cọ, làm tay), mũi tên giữa, node phải "1 BỘ QUY TẮC" (icon bánh răng, tự động). Dưới có 2 proof-chip: "kiểm soát cao, tốn công" / "nhanh, cần luật chống trùng" |
| 7 | Bước 1 đọc bối cảnh trước · bước 2 hỏi đúng một câu, không dội mười câu | `BƯỚC 1 — đọc trước` · hỏi–đáp 1 câu | ⭐ **`vpg-chat-message`/`c-message`/`msg-bubble` (mẫu MỚI, ảnh mẫu `slide16.png`)**: reveal 1 nhãn nhỏ "bước 1: đọc công trường" (icon mắt/tài liệu); reveal 2-3 một cặp bong bóng chat giống `deck_sp02` slide 6 — bong bóng trái (icon agent/sổ) hỏi "8 mẫu tay hay 1 bộ quy tắc?", bong bóng phải (icon người) đang chờ trả lời |
| 8 | Bước 3 so hai hướng, nêu được/mất · bước 4 trình bản vẽ chờ duyệt · kết quả: bài ba làm mẫu, duyệt rồi mới nhân 7 bài | `3 — so hướng` · `4 — trình & CHỜ DUYỆT` · `KẾT QUẢ: mẫu = bài 03` | `mock-terminal` (tái dùng class slide 8 của `deck_sp02`): dòng lệnh giả lập hiển thị "so 2 hướng → được/mất", "trình bản vẽ… chờ duyệt", dòng cuối đóng dấu tích "mẫu: BÀI 03 → duyệt → nhân 7 bài" |
| 9 | Bẫy: liệt kê nhiều ý tưởng tưởng là xong · danh sách dài mà chưa ai chốt vẫn mơ hồ · cách né: chỉ dừng khi có quyết định + bản vẽ duyệt | `"liệt kê nhiều = XONG"?` · `dài mà chưa CHỐT = vẫn mơ hồ` · `dừng khi: quyết định + duyệt` | `risk-cards-container` đỏ/vàng/xanh (tái dùng nguyên cấu trúc slide 9 `deck_sp02`, đổi chữ) |
| 10 | Bản vẽ chốt xong, đội thợ xây đúng bếp cần · đổ móng nhanh không cứu nhà sai bản vẽ · chậm một nhịp để hỏi, nhanh cả quãng đường xây | `BẢN VẼ CHỐT → XÂY ĐÚNG` · `chậm để HỎI, nhanh để XÂY` | `glowing-conclusion` (tái dùng slide 10 `deck_sp02`): dội lại bố cục slide 1 (bếp + lối đi), nửa màn chia đôi: trái là cảnh slide 1 (bếp chật, đỏ), phải là bếp đúng kích thước lối đi (xanh) |

## GHI CHÚ CHO NGƯỜI DỰNG DECK
- **Vật thể giữ nguyên xuyên bài:** tấm bản vẽ (tờ giấy), cái bếp, lối đi. Slide 10 phải dội
  đúng bố cục slide 1 để câu chốt có tác dụng.
- **Thuật ngữ đầu tiên (`Superpowers`, `brainstorming`) chỉ được xuất hiện ở slide 5** — slide
  1-4 chỉ có cảnh bếp/thợ/bản vẽ, không một chữ tiếng Anh nào.
- Slide 5 và slide 7 là **2 mẫu hình MỚI bắt buộc theo brief** — không tự đổi sang mẫu khác.
  `vpg-traffic-pole`/`lightable` KHÔNG dùng cho bài này (đó là mẫu dành riêng cho bài 05).
- Màu vai: xanh = đúng hướng/đã duyệt, đỏ = sai/mơ hồ, hổ phách = cần chú ý (chỗ trống, chưa
  chốt). Đỏ chỉ gắn vào cái người xem PHẢI tránh (tay nghề kém — bị gạch bỏ vì đó là ý SAI;
  bẫy ở slide 9).
- `sc-file` (slide 4) và `hk-versus` (slide 6) là class đã có sẵn trong `deck_sp02/style.css`
  (thừa kế từ slide 4 và slide 7 gốc) — kiểm bằng `grep -c` trước khi chép thêm CSS.
