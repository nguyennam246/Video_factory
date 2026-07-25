# MÀN HÌNH — sp04_worktree (Bài 04 khoá Superpowers)

Khuôn `[1,3,3,2,3,3,3,3,3,3]` = 27 reveal. Mỗi câu lời = 1 reveal.
Ẩn dụ xuyên khoá: **xây một căn nhà**. Vật thể chủ đạo bài này: **khung cửa công trường riêng**
+ **tờ phiếu việc**. Nối mạch từ bài 03 (tấm bản vẽ) — bản vẽ đã duyệt xong, giờ đến lúc dựng
chỗ riêng để thi công mà không đụng nhà đang ở.

Deck: `escbase_template/headless/deck_sp04`, chép nền từ `deck_sp02` (palette `sp` đã đúng,
27 reveal khớp sẵn). 2 mẫu MỚI bắt buộc theo brief mục 3: **`webui-frame`/`vpg-media-full`/
`source-tag`** (slide 4) + **`workflow-grid`/`workflow-step`** dạng lưới 2×2 đánh số (slide 6).
Các slide còn lại tái dùng nguyên cấu trúc từng slide tương ứng của `deck_sp02`.

| Slide | Lời đọc (rút gọn) | Chữ lên màn hình | Hình gì CHUYỂN ĐỘNG |
| :-: | :-- | :-- | :-- |
| 1 | Thợ đập tường giữa phòng khách, bụi bay thẳng vào nồi cơm đang sôi | `BỤI VÀO NỒI CƠM` | Hero (tái dùng cấu trúc slide 1 `deck_sp02`: orbit + tiêu đề). Orbit chip đổi 4 nhãn: `khu riêng` · `phiếu việc` · `nền xanh` · `bằng chứng`. Core icon đổi từ sách sang `fa-door-closed` (cửa công trường). Tiêu đề gradient: `"Bụi Vào Nồi Cơm"`. `repo-stats`: `đập tường giữa bếp` / `3 ngày bụi lấn dần` |
| 2 | Ngày 1 kê bàn ăn sát tường đang đập · ngày 2 vôi vữa lấn tới cửa bếp · ngày 3 cả nhà bưng bát đứng ăn | `NGÀY 1 — bàn ăn sát tường` · `NGÀY 2 — vôi vữa lấn tới bếp` · `NGÀY 3 — đứng ăn, hết chỗ ngồi` | **`workflow-grid` 3 cột** (tái dùng nguyên class + layout slide 2 `deck_sp02`, đổi icon/chữ): cột 1 icon bàn ăn, cột 2 icon vôi vữa lan, cột 3 icon người đứng ăn. `vpg-route-lane` packet chạy từ "bàn ăn" → "vôi vữa lấn" → dừng ở "hết chỗ sạch". `hk-note`: "bếp mất luôn chỗ ngồi sạch" |
| 3 | Lỗi không ở thợ vụng, không ở việc khó · lỗi ở chỗ việc mới và việc cũ chung một khu, chưa quây riêng | `KHÔNG PHẢI: thợ vụng về` · `CŨNG KHÔNG: việc quá khó` · `LÀ: chung một khu, chưa quây riêng` | **`flow-diagram` + `flow-strike`** (tái dùng class slide 3 `deck_sp02`): reveal 1 node `flow-old` "thợ vụng về?" gạch đỏ; reveal 2 node `flow-old` thứ hai "việc quá khó?" gạch đỏ; reveal 3 node `flow-new` (đã pre-patch màu hổ phách qua wrapper `sp-flow-two`, KHÔNG dùng xanh lá vì đây là nguyên nhân cần chú ý) "chung một khu, chưa ai quây riêng" sáng lên |
| 4 | Dựng khung cửa công trường riêng, đi lối khác, nền cũ không suy suyển · treo sẵn phiếu việc ghi làm gì, đo bằng gì, xong nhìn đâu | `NHÀ ĐANG Ở — nền cũ không suy suyển` · `KHU CÔNG TRƯỜNG — đi lối khác` · `phiếu việc treo sẵn` | ⭐ **`webui-frame`/`vpg-media-full` (mẫu MỚI, ảnh mẫu `slide5.png`) — hai khung cửa sổ đặt cạnh nhau** thay vì 1 khung media lớn: khung trái viền xanh cyan "NHÀ ĐANG Ở" (icon nhà), khung phải viền hổ phách "KHU CÔNG TRƯỜNG" (icon mũ bảo hộ). Reveal 2: `source-tag` "treo sẵn phiếu việc: làm gì · đo bằng gì · xong nhìn đâu" |
| 5 | Khung cửa đó, trong Git, gọi là worktree · cho một nhánh một thư mục riêng · skill worktree luôn hỏi đã đứng khu riêng chưa, ưu tiên công cụ nền tảng | `WORKTREE` · `nhánh riêng · thư mục riêng` · `hỏi trước khi thi công` | **`hk-names` (tái dùng nguyên cấu trúc "GỌI TÊN" slide 5 `deck_sp02`)**: tên kỹ thuật lớn `WORKTREE`, `sg-verify` liệt kê "một nhánh" / "một thư mục riêng" / "không đụng chỗ đang dùng", `hk-note` "skill hỏi bạn đã đứng khu riêng chưa · ưu tiên công cụ nền tảng" |
| 6 | Khu riêng chưa đủ, cần phiếu việc gọi là kế hoạch thi công · mỗi nhiệm vụ ghi file, phép thử, lệnh chạy, kết quả · ví dụ thật: nhiệm vụ một tìm cảnh thiếu lời, thử trên mẫu 3 cảnh | `CẦN THÊM — phiếu việc` · `01 FILE · 02 THỬ · 03 LỆNH · 04 KẾT QUẢ` · `nhiệm vụ 1: cảnh thiếu lời` | ⭐ **`workflow-grid` lưới 2×2 đánh số (mẫu MỚI, ảnh mẫu `slide12.png`)**: 4 thẻ `01 FILE` / `02 PHÉP THỬ` / `03 LỆNH CHẠY` / `04 KẾT QUẢ`, mỗi thẻ 1 icon khác nhau. Reveal 3: `hk-note` "ví dụ thật: nhiệm vụ một — tìm cảnh thiếu lời, thử trên mẫu 3 cảnh" |
| 7 | Bước 1 tạo file mẫu 3 cảnh, cảnh 2 thiếu lời · bước 2 chạy kiểm tra, đòi báo lỗi đúng cảnh 2 · mỗi bước 2-5 phút, thấy kết quả ngay | `BƯỚC 1 — mẫu 3 cảnh, cảnh 2 thiếu lời` · `BƯỚC 2 — chạy kiểm tra` · `mỗi bước 2–5 phút` | `sc-file` (tái dùng class slide 7 `deck_sp02`, KHÔNG dùng `hk-versus` vì đây không phải 2 lựa chọn mà là chuỗi bước tuần tự): thẻ 1 "BƯỚC 1" nội dung tạo mẫu 3 cảnh; thẻ 2 "BƯỚC 2" nội dung chạy kiểm tra. Reveal 3: `hk-note` "mỗi bước 2-5 phút, làm xong là thấy kết quả ngay" |
| 8 | Bước 3 viết phần đọc tối thiểu · bước 4 chạy lại, đúng 1 lỗi ở cảnh 2, không thừa không thiếu · bước 5 chốt mốc, phiếu việc xong 1 dòng | `BƯỚC 3 — viết tối thiểu` · `BƯỚC 4 — đúng 1 lỗi, cảnh 2` · `BƯỚC 5 — chốt mốc` | `mock-terminal` (tái dùng class slide 8 `deck_sp02`): 3 dòng lệnh giả lập "viết tối thiểu", "chạy lại → đúng 1 lỗi, đúng cảnh 2", "chốt mốc nhiệm vụ". Reveal 2: `proof-chip` "không thừa không thiếu". Reveal 3: `hk-note` "phiếu việc coi như xong một dòng" |
| 9 | Bẫy 1: bỏ qua kiểm tra nền, nền hỏng không ai biết · bẫy 2: phiếu chỉ có tiêu đề lớn, không bằng chứng · cách né: đứng khu riêng bắt nền xanh trước, viết phiếu bắt mỗi bước có bằng chứng | `BẪY 1 — bỏ qua nền` · `BẪY 2 — phiếu mơ hồ` · `NÉ — nền xanh trước · mỗi bước có bằng chứng` | `risk-cards-container` đỏ/vàng/xanh (tái dùng nguyên cấu trúc slide 9 `deck_sp02`, đổi chữ) |
| 10 | Khu riêng giữ sạch, phiếu việc giữ đúng đường · cần cả hai trước khi cầm búa · không thì bụi vẫn bay vào nồi cơm đang sôi, lần này chẳng ai biết vì sao | `KHU RIÊNG → SẠCH` · `PHIẾU VIỆC → ĐÚNG ĐƯỜNG` · dội lại hook: `bụi vẫn bay vào nồi cơm` | `glowing-conclusion` (tái dùng slide 10 `deck_sp02`): tiêu đề + phụ đề chốt, `split-panel` "cần cả hai / trước khi cầm búa", `hk-lockup` dội nguyên hình ảnh nồi cơm đang sôi của slide 1 — icon đổi sang nồi/cửa đóng |

## GHI CHÚ CHO NGƯỜI DỰNG DECK
- **Vật thể giữ nguyên xuyên bài:** khung cửa công trường riêng, tờ phiếu việc, nồi cơm đang sôi
  (slide 10 phải dội đúng hình nồi cơm của slide 1 để câu chốt có tác dụng).
- **Thuật ngữ đầu tiên (`worktree`, `skill`) chỉ được xuất hiện ở slide 5** — slide 1-4 chỉ có
  cảnh nhà/bếp/khung cửa, không một chữ tiếng Anh nào.
- Slide 4 và slide 6 là **2 mẫu hình MỚI bắt buộc theo brief mục 3** — không tự đổi sang mẫu khác.
  Slide 4 không có ảnh chụp thật (không có screenshot worktree thật) nên dùng `webui-frame`/
  `vpg-media-full` làm KHUNG (không nhét `<img>`), bên trong là icon + nhãn tự dựng — vẫn đúng
  class brief yêu cầu, không phải mẫu khác.
- Slide 6 dùng `workflow-grid vpg-workflow-large` KHÔNG có modifier `sp-grid-3` (modifier đó ép
  3 cột cho slide 2) → mặc định `vpg-workflow-large` là lưới 2 cột, đúng bố cục 2×2 4 thẻ như
  ảnh mẫu `slide12.png`.
- Màu vai: xanh cyan = trạng thái ổn định/đang dùng, hổ phách = cần chú ý (khu mới, chỗ trống,
  chưa quây riêng), đỏ chỉ dùng cho 2 giả thuyết SAI ở slide 3 và 2 bẫy ở slide 9. Node
  `flow-new` ở slide 3 đã được pre-patch màu hổ phách qua wrapper `sp-flow-two` (kế thừa từ
  `deck_sp02`) — KHÔNG đổi lại xanh lá, vì nội dung bọc trong đó là nguyên nhân gây lỗi cần chú
  ý, không phải tin tốt.
- `sc-file` (slide 7), `hk-names`/`sg-verify` (slide 5), `mock-terminal` (slide 8) là class đã có
  sẵn trong `deck_sp02/style.css` (thừa kế từ starter) — kiểm bằng `grep -c` trước khi chép thêm
  CSS. Chỉ cần thêm CSS mới cho cặp khung cửa sổ ở slide 4 (`.sp-window-pair`, `.sp-window`,
  `.sp-window-bar`, `.sp-window-dot`, `.sp-window-title`, `.sp-window-body`).
