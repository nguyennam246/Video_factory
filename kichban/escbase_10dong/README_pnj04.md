# PNJ 04 — bản THAY ÁO của PNJ 03 ("hồ sơ điều tra" + ảnh thật)

**Ngày dựng:** 25/07/2026 · **Deck:** `escbase_template/headless/deck_pnj04`
**Lời:** y hệt PNJ 03 (`pnj03_01_niemtin.txt`) trừ ĐÚNG MỘT câu — xem mục 1.
16 dòng · 38 reveal · 426 từ · giọng edge `vi-VN-NamMinhNeural` `+14%` · lời **126,90s**

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
