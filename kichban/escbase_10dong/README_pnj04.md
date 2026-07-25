# PNJ 04 — bản THAY ÁO của PNJ 03 ("hồ sơ điều tra" + ảnh thật)

**Ngày dựng:** 25/07/2026 · **Deck:** `escbase_template/headless/deck_pnj04`
**Lời:** `pnj04_01_hoso.txt` — nền là lời PNJ 03, sửa theo 2 đợt BOSS phán (mục 1 + mục 1b).
16 dòng · 38 reveal · 444 từ · giọng edge `vi-VN-NamMinhNeural` `+14%` · lời **129,20s**
· thước `KETLUAN|38|444|DAT`

> PNJ 04 **không phải bài mới**. Cùng kịch bản, cùng nhịp, cùng số liệu với
> `PNJ_03_niemtin.mp4` — chỉ đổi **áo** (bộ scene + theme) và **thêm ảnh thật**, để BOSS
> xem hai bản cạnh nhau rồi chọn ngôn ngữ thị giác cho ca này.

---

## 1. LỜI ĐỔI ĐÚNG MỘT CHỖ — BOSS bắt 25/07

> BOSS: *"lời có thay đổi là chờ **kết luận của cơ quan điều tra**, không phải toà án."*

Vụ PNJ đang ở giai đoạn **khởi tố / điều tra**, chưa tới xét xử ⇒ nói "tòa chưa tuyên" là
đặt vụ việc sai giai đoạn tố tụng. Sửa ở cả 4 chỗ trong CÙNG một lượt:

| Chỗ | Cũ | Mới |
| :-- | :-- | :-- |
| lời đọc (dòng 10) | "Nhưng đó là lời công ty, **tòa chưa tuyên**." | "…, **cơ quan điều tra chưa kết luận**." |
| kịch bản gốc `pnj_dam_chay_kim_cuong.md:45` | như trên | như trên |
| con dấu đỏ slide 10 | `TÒA CHƯA TUYÊN` | `CHƯA CÓ KẾT LUẬN ĐIỀU TRA` |
| ô theo dõi slide 14 | "diễn biến vụ án — *tới khi tòa tuyên*" | "— *tới khi có kết luận*" |

Số câu không đổi ⇒ **38 reveal giữ nguyên**, không phải dựng lại nhịp. Lời dài thêm 2 từ
(424 → 426), vẫn trong trần 390-460 của góc `hai_tien_le`.
⚠️ `PNJ_03_niemtin.mp4` đã render TRƯỚC khi có bản sửa này ⇒ bản 03 vẫn mang chữ cũ.

## 1b. ĐỢT SỬA THỨ HAI — BOSS xem bản render rồi phán 7 điều (25/07 khuya)

| # | BOSS nói | Đã sửa thành |
| :-: | :-- | :-- |
| 1 | *"Máy đo quá khứ nói máy khoẻ — câu này máy móc. Chỉ nên nói quá khứ sinh lời tốt, tỷ suất sinh lời trên vốn hơn 20% nhiều năm liền"* | Lời slide 9: **"Quá khứ sinh lời tốt. Tỷ suất sinh lời trên vốn hơn hai mươi phần trăm nhiều năm liền, …"**; nhãn màn hình `số đo của quá khứ` → `nhìn lại quá khứ` (giữ mốc thời gian, bỏ giọng máy móc) |
| 2 | *"niềm tin rạn → niềm tin rạn nứt"* | Sửa cả lời đọc lẫn chữ slide 11 |
| 3 | *"Câu cổ phiếu quỹ cũng cần soi vô duyên, không liên quan gì nội dung trước. Thay bằng: cách công ty xử lý khủng hoảng khi khách tới bán"* → rồi BOSS chỉnh tiếp: *"cổ đông tới bán là sai. **Khách tới bán lại nữ trang**"* | 🔴 **BOSS bắt được LỖI SỰ THẬT, không chỉ lỗi câu chữ.** Tra ngược nguồn (`pnj_01_danhgia.txt`, `pnj02_01_hanhdong.txt`, báo 22/07/2026): PNJ **cam kết mua lại nữ trang của KHÁCH bằng 70–90% giá hóa đơn**; sau vụ việc **khách bán lại gấp 5 lần lượng bán ra**; tiền trả **giãn tới 120 ngày, có hạn mức mỗi ngày**. ⇒ chữ **"5 đợt"** trong bản PNJ 03 là **đọc nhầm con số "gấp 5 LẦN"**, và gán nhầm sang **cổ phiếu quỹ** (chuyện khác hẳn). Lời nay: **"Cách công ty xử lý khủng hoảng khi khách tới bán lại nữ trang cũng nói lên nhiều điều. Tiền trả giãn tới một trăm hai mươi ngày, có hạn mức mỗi ngày, đúng lúc dòng tiền đang báo động."** · 2 ô số màn hình thành **`70–90%` cam kết mua lại theo giá hóa đơn** và **`120 ngày` tiền trả giãn tới, có hạn mức mỗi ngày`**. ⚠️ **`PNJ_03_niemtin.mp4` vẫn mang con số sai này** — đừng dùng bản 03 |
| 4 | *"Giá trị sổ sách phải lấy chính xác theo báo cáo Q1 mới nhất trong BCTC.db, khoảng 28k. Kiểm tra lại"* | **BOSS đúng.** Tra `std_quarter` Q1/2026: VCSH mẹ **14.401,17 tỷ**, vốn điều lệ 3.413,19 tỷ ⇒ 341,3tr cp, sau thưởng 50% (23/04) là **512,0tr cp** ⇒ **28.128đ/cp**. Con số cũ "26–28k" là ước chừng. Lời đọc: *"giá trị sổ sách khoảng hai mươi tám nghìn một cổ phiếu"*; màn hình: **`28.128đ · sổ sách/cp · Q1/2026`**. (P/B = 30.750/28.128 = **1,09** — vẫn đúng câu "giá nhỉnh hơn sổ sách") |
| 5 | *"Rẻ hơn trước, không phải cho không — khó hiểu"* | **"Rẻ hơn trước, nhưng chưa phải cho không"** (lời + chữ màn hình) |
| 6 | *"Bỏ câu xem thêm tại…, chỉ giữ đúng là đủ chấm vi en"* | Dòng 16 còn đúng `dungladu.vn` (từ điển `phat_am.json` đọc thành *"Đúng Là Đủ chấm vi en"*). Slide chốt còn **1,97s lời + 1,4s đuôi** |
| 7 | *"Chữ dungladu.vn bị render thiếu chân chữ g"* | Bệnh của `background-clip:text` + `line-height:1.1` — hộp chữ cắt mất phần dưới đường chân. Vá: `line-height:1.42` + `padding-bottom:10px` trong `.hs-brand-url` (vá ở **cả theme lẫn deck**). Đã soi lại ảnh: chân chữ `g` đủ |

Sau đợt này: 444 từ (trần góc 390-460) · **38 reveal không đổi** · lời 128,38s.

## 2. THEME 02 "HỒ SƠ ĐIỀU TRA" — áo mới, tiền tố `hs-`

Khối `<style>` tự chứa: `escbase_template/themes/theme_02_ho_so_dieu_tra.css.html`
(thư viện theme dùng lại được — xem `themes/README.md`). Trùng `style.css` chung = 0%.

| Trục | Theme 01 "vết nứt kim cương" (PNJ 03) | Theme 02 "hồ sơ điều tra" (PNJ 04) |
| :-- | :-- | :-- |
| nền | hộp trang sức tối + mặt cắt kim cương chéo | phòng hồ sơ xanh thép + **lưới blueprint** |
| thẻ | bo góc 14px, viền vàng | **góc vuông 3px**, viền thép, có **gáy "HỒ SƠ"** dọc |
| tiêu đề | Playfair Display (serif) | **Oswald condensed IN HOA** |
| nhãn/số | Inter | **IBM Plex Mono** |
| dấu | con dấu đỏ | con dấu đỏ 2 viền (giữ) |
| ảnh | không có | **3 ảnh thật** — xem mục 3 |

Palette engine giữ nguyên khoá **`tc`** của series tài chính (luật series, không tự đổi) —
nên vẫn còn quầng ấm của hạt nền; phần khung/chữ thì đã sang xanh thép.

## 3. BA ẢNH THẬT — BOSS lệnh 25/07 ("dùng đi, còn hình ảnh của tiền lệ bên trung quốc nữa")

| Slide | Ảnh | Vai | Chú thích trên màn |
| :-: | :-- | :-- | :-- |
| 4 | `img/buffett.jpg` | chân dung nhỏ trong làn "nhà đầu tư giá trị" | (không) |
| 5 | `img/ratners.jpg` | ảnh kẹp trong hồ sơ tiền lệ 1 | `GERALD RATNER · ẢNH TƯ LIỆU` |
| 8 | `img/kingold.jpg` | ảnh kẹp trong hồ sơ tiền lệ 2 | `83 TẤN "VÀNG" · ẢNH MINH HOẠ` |

**Nghiệm thu bản cuối:** 1080×1920 · 128,400s · mean −17,1 dB · lệch giọng +0,454 khung · 0 khung
đứng hình · phụ đề đủ 9 mốc · đuôi −91,0 dB ⇒ **7/7 ĐẠT**; reveal-cuối ≥1,2s sạch; soi 11 frame thật.

Nguồn + giấy phép từng ảnh: `deck_pnj04/source/links.txt`. Ảnh Kingold là **CC0** lấy từ
Wikimedia (ảnh dựng, KHÔNG phải vàng thật của Kingold ⇒ bắt buộc chú thích "ảnh minh hoạ").
Danh tính ông Ratner đã **kiểm chéo** với ảnh có nguồn trên Commons trước khi ghi tên.

🔴 **Bẫy đã trả giá trong lượt này:** ảnh đặt thành DẢI NGANG full-width (76px cao) thì
`object-fit:cover` cắt mất trán và cằm — soi ảnh mới thấy, `validate` vẫn PASS. Khuôn đúng
cho chân dung là **ô dọc 76×92 kẹp cạnh chữ** (`.hs-shot`), giống ảnh ghim trong hồ sơ thật.

## 4. SLIDE 1 — BIỂU ĐỒ GIÁ RƠI BẰNG SỐ THẬT (BOSS lệnh)

Thay viên kim cương nứt bằng **đường giá thật 31 phiên** (12/06 → 24/07/2026), đọc CHỈ-ĐỌC
từ `Research copy/dulieu/gia.db`, vẽ thẳng bằng SVG trong DOM (không phụ thuộc thư viện,
nét không vỡ ở mọi dsf). Chú thích mono ghi rõ khoảng ngày + "giá đóng cửa".
Cửa sổ 6 tuần này **không chứa ngày chia thưởng 23/04/2026** ⇒ giá thô dùng được, không
dính bẫy "giảm X% từ đỉnh" đã bắt ở PNJ 01.

## 5. SLIDE 16 — CHỈ MỘT DÒNG + LOGO CHÌA KHOÁ NẰM NGANG (BOSS lệnh)

Bỏ viên kim cương, bỏ gạch chỉ, bỏ dòng "đọc báo cáo doanh nghiệp, có nguồn".
Còn đúng: **logo chìa khoá của website xoay ngang** (`transform:rotate(-90deg)`, bow bên
trái, răng chỉ sang phải) + **`dungladu.vn`**. SVG dán inline từ
`/Users/simple/Desktop/website/chiakhoa.svg` (đổi id gradient thành `hs-keyg` cho khỏi
đụng id khác trong deck). Watermark góc vẫn tự tắt ở slide này.
