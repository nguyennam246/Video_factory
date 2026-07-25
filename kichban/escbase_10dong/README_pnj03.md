# PNJ 03 — "Vết nứt niềm tin và hai tiền lệ ngành trang sức"

**Ngày dựng:** 25/07/2026 · **Deck:** `escbase_template/headless/deck_pnj03`
**Lời:** `pnj03_01_niemtin.txt` (16 dòng · 38 reveal · 424 từ) · **Góc:** `hai_tien_le` (góc MỚI)
**Giọng:** edge `vi-VN-NamMinhNeural` `+14%` · tổng lời **126,27s**

---

## 1. NGUỒN CỦA LỜI — KHÔNG phải AI tự viết

Kịch bản gốc là **`kichban/pnj_dam_chay_kim_cuong.md`** — bản 3, **BOSS tự chỉnh 2 vòng
ngày 25/07/2026** (xem `video/HANDOFF.md` mục 25/07 tối). Bước dựng này **không viết lại
một câu nào**; chỉ làm 3 việc:

1. Tách 15 khối `LỜI:` thành 15 dòng `script-90s.txt` (nguyên văn, không sửa chữ).
2. **Thêm dòng 16** — slide thương hiệu, theo lệnh BOSS trong phiên: *"cuối video làm thêm
   1 slide có đường link website dungladu.vn, làm nổi bật, tầm 2 giây"*.
3. Chuyển các dòng `CHỮ:` / `MÃ:` của BOSS thành chữ trên màn hình (xem mục 3).

## 2. VÌ SAO KHÔNG DÙNG LẠI KHUÔN 10 SLIDE

Kịch bản BOSS có **15 cảnh**, nhịp câu `[2,1,2,3,2,3,3,2,3,4,3,2,4,2,3]`. Engine escbase chỉ
ép *số câu dòng N = số `.slide-element` slide N*, **không ép khuôn** — nên nhịp của BOSS được
giữ nguyên, không cắt gọt cho vừa khuôn cũ. Đã lập góc mới `goc/taichinh/hai_tien_le.md`
để thước đọc đúng nhịp này.

**Thước kịch bản (0 API):** `KETLUAN|40|424|DAT` — đạt cả 6 phép đo.
Trần từ của góc này là **390-460** (khuôn 10 dòng cũ là 300-380) vì bài dài 16 dòng;
trần hook là 22 từ (dòng 1 của BOSS = 20 từ, 2 câu). **Chỉ nới trần ĐỘ DÀI —
danh sách từ cấm `CAM_HE_THONG` / `CAM_DOA` / `CAM_KHUYEN` giữ nguyên, và bài này không
dính từ nào.** Hồi quy: bài `pnj02` cũ chạy lại vẫn `DAT`.

## 3. CHỮ MÀN HÌNH — LỆCH DUY NHẤT SO VỚI KỊCH BẢN GỐC

| Slide | BOSS ghi trong kịch bản | Trên màn hình | Vì sao |
| :-: | :-- | :-- | :-- |
| 9 | `MÃ: ROE 21,5% · Z 11,0 · M sạch` | `>20%` *sinh lời trên vốn, nhiều năm liền* + `sạch` *sổ sách, không dấu hiệu bất thường* | ① "Z 11,0 · M sạch" là **ngôn ngữ hệ thống nội bộ**, người xem không giải mã được (BOSS cấm 24/07). ② Lời đọc nói *"hơn hai mươi phần trăm **nhiều năm**"*, còn 21,5% là số của **một** năm — để cạnh nhau thì màn hình và giọng nói hai chuyện khác nhau. **Nếu BOSS muốn giữ nguyên số 21,5% thì sửa 1 dòng HTML, không phải dựng lại.** |

Mọi số còn lại **nguyên văn của BOSS**: 68.000đ → 30.750đ · 28.000 viên · 03/07/2026 ·
7 phiên sàn · 4 phiên sàn liền 21-24/07 · 41 triệu cp · −500 triệu bảng · Signet ·
83 tấn vàng giả · 2.828 tỷ (+33,8%) · 5 đợt / 120 ngày · sổ sách 26-28k.

## 4. BỘ SCENE MỚI — deck này KHÔNG chép scene của 12 deck cũ

BOSS yêu cầu *"dùng scene mới, dựng html đẹp lạ, phù hợp với ca này"*. Toàn bộ 16 slide dựng
bằng **hệ class riêng `nn-*`** (viết trong `<style>` của `index.html`, không đụng `style.css`
139 KB dùng chung ⇒ không ảnh hưởng deck nào khác). Trùng scene với deck liền trước = **0%**.

| Scene mới | Ở slide | Là gì |
| :-- | :-: | :-- |
| `nn-gem` + `crack` | 1, 16 | viên kim cương cắt bằng nét vàng, một **vết nứt đỏ** chạy dọc |
| `nn-bg` (6 biến thể) | tất cả | nền tối + hai lớp **đường mặt cắt kim cương** chéo nhau, che bằng mask hình tròn |
| `nn-rail` | 1 | 68.000đ gạch ngang → 30.750đ |
| `nn-stairs` | 3 | 7 vạch đỏ tụt dần = 7 phiên sàn |
| `nn-lane` | 4 | hai làn nhìn: người thường (xám) / nhà đầu tư giá trị (vàng) |
| `nn-file` + `nn-quote` | 5, 8 | **hai hồ sơ tiền lệ CÙNG khung CÙNG cỡ** (bẫy số 1 của góc) |
| `nn-eq` | 7 | phương trình: kim loại ≠ trang sức = niềm tin + hãnh diện |
| `nn-crackline` | 7 | đường nứt ngang chạy hết bề ngang |
| `nn-past` + `nn-tag` | 9 | ô số quá khứ **có nhãn thời điểm** (bẫy số 2 của góc) |
| `nn-scale` + `nn-stamp` | 10 | cán cân **ngang bằng** + con dấu đỏ "TÒA CHƯA TUYÊN" |
| `nn-ruler` | 13 | thước giá 3 mốc, **cố ý không tô màu phán xét** |
| `nn-watch` | 14 | ba thẻ theo dõi |
| `nn-brand` | 16 | tên miền chữ serif lớn có ánh kim |

**Icon:** bộ **Lucide** (giấy phép ISC, dùng thương mại được) — nhân viên tra cứu lấy 14 icon
từ `raw.githubusercontent.com/lucide-icons/lucide`, đã kiểm `xml.dom.minidom` parse sạch
**14/14**, kích thước 273-587 byte. Dán **inline dạng `<symbol>`** trong `index.html` ⇒ render
không phụ thuộc mạng. 13 icon dùng thật; icon "vòng/nhẫn trang sức" **không có** trong các bộ
mã nguồn mở phổ biến (nhân viên tra 2 lần rồi dừng đúng luật), thay bằng `diamond` cùng bộ.

**Chữ:** tiêu đề dùng **Playfair Display** (serif) — cố ý khác 12 deck cũ vốn dùng Inter cho
mọi thứ; đây là thứ tạo cảm giác "hộp trang sức" mà không cần thêm hình.

## 5. SLIDE 16 — YÊU CẦU CỦA BOSS

- Chữ `dungladu.vn` **37px serif có gradient ánh kim**, giữa khung, dưới là viên kim cương nhỏ.
- **Tự tắt watermark góc** ở slide này (`:has(.slide[data-slide="15"].active)`) để tên miền
  không hiện hai lần trên cùng một khung.
- Dài **3,91s** (2,5s lời + 1,4s đuôi bắt buộc `TAIL_SECONDS`). BOSS xin "tầm 2s" — 2s trơn
  sẽ cắt phựt đúng cái bệnh đã vá 25/07, nên để 2,5s lời + đuôi.
- Cách đọc: thêm khoá `dungladu.vn → "Đúng Là Đủ chấm vi en"` vào `tts/phat_am.json`.
  ⚠️ **Cần BOSS nghe xác nhận** — AI không nghe được, và tên miền có thể đọc là "Dũng"
  chứ không phải "Đúng". Sửa = sửa 1 dòng JSON, không phải dựng lại video.
  Thêm luôn `Buffett → "Ba phét"` (dòng 4 có đọc tên này) — **cũng cần BOSS nghe phán**.

## 6. TỰ KIỂM (0 API)

| Phép đo | Kết quả |
| :-- | :-- |
| `thuoc_kichban.py --goc hai_tien_le` | `KETLUAN|40|424|DAT` |
| hồi quy thước trên bài cũ `pnj02 --goc viec_can_lam` | `DAT` (không vỡ) |
| số `.slide-element` từng slide vs số câu | khớp 16/16 |
| `validate_slide.py --semantic-report` | **PASS** |
| safezone layout-box 16 slide | OK 16/16 |
| `tts/phat_am.py --kiem` | ĐẠT · 57 khoá |
| soi ảnh | contact sheet + zoom slide 1/6/10/13/14/16 |

### 🔴 LỖI NẶNG NHẤT — CHỈ SOI FRAME VIDEO THẬT MỚI THẤY (vòng render 1)

Ảnh deck đúng, `validate` PASS, nghiệm thu máy **7/7 ĐẠT** — nhưng soi frame thật thì
**reveal cuối của slide 1 không bao giờ hiện lên màn hình**, và reveal cuối slide 10 chỉ
hiện **0,52 giây**.

Nguyên nhân (đọc thẳng `auto_render.build_click_timeline`, không đoán):
- Lịch reveal chia theo **vị trí ký tự** của câu trong dòng ⇒ câu ngắn đứng cuối dòng dài
  thì hiện ở ~95% thời lượng slide.
- Riêng **slide HOOK có luật riêng** (`auto_render.py:1014`): reveal 2 được đặt **đúng lúc
  dứt giọng đọc** ⇒ `t = 6,72s` trên slide dài `6,72s` = **0,00 giây trên màn**. Luật này
  vô hại với khuôn cũ vì slide 1 khuôn cũ luôn **1 câu / 1 reveal**; bài này là bài đầu
  tiên có hook 2 câu nên mới lộ.

Cách vá (**không đụng code dùng chung**, chỉ đổi dấu câu, giữ nguyên từ của BOSS):
dòng 1 gộp 2 câu thành 1 (`giá.` → `giá,`) · dòng 10 gộp 2 câu chót (`công ty.` → `công ty,`).
Nhịp `[2,…,4,…]` → `[1,1,2,3,2,3,3,2,3,3,3,2,4,2,3,1]`, 38 reveal, số từ **không đổi**.
Thước tất định kèm theo: bảng *"reveal cuối còn lại trên màn bao nhiêu giây"* — sau khi vá,
**không slide nào < 1,2s**.

**Lỗi soi ảnh deck bắt được và đã vá:** ① slide 13 — đường trục thước giá **cắt ngang chữ nhãn**
(vạch chia nằm dưới trục, rời khỏi mốc) ⇒ đẩy trục xuống đáy, vạch chia nối lên nhãn ·
② slide 13 — câu chốt xuống dòng thành *"…cho / không"*, ép ngắt dòng đúng chỗ ·
③ slide 14 — ba thẻ theo dõi lệch chân chữ vì thẻ 1 dài 2 dòng ⇒ đẩy dòng phụ xuống đáy thẻ ·
④ slide 10 — dấu `—` trên màn hình đổi thành dấu phẩy.

## 7. CÒN LẠI PHẢI ĐỂ BOSS PHÁN (AI KHÔNG NGHE ĐƯỢC)

1. Giọng đọc `dungladu.vn` và `Buffett` — đúng chưa.
2. Nhịp bài 16 slide (~128 giây) có dài quá không.
3. Slide 16 có "nổi bật" đúng ý không, có muốn thêm dòng kêu gọi khác không.
