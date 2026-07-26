# VFG 01 — "Nghịch lý số": lãi 6 tháng vẫn tăng, dòng tiền kinh doanh âm 43 tỷ

**Ngày:** 26/07/2026 · **Góc:** `nghich_ly_so` (⭐ lần đầu dùng) · **Deck:** `deck_vfg01`
(chép `deck_pnj02`, thay chữ + 3 scene mới) · **Giọng:** edge `vi-VN-NamMinhNeural` `+14%`

## ⭐ ĐIỂM KHÁC MỌI BÀI TRƯỚC: LỜI KHÔNG DO XƯỞNG PHIM VIẾT

Kịch bản đến từ **PHÒNG PHÂN TÍCH PTBC** của dự án Research (chân ④ biên tập), không phải
do bước b1 của `lam_bai.py` sinh ra. Chuỗi đã đi trước khi tới xưởng phim:

```
4 nhà AI viết MÙ (fable · sol/Codex · qwen3.8 · kimi-k3)
   → phản biện chéo 4 bài → trọng tài (8 đồng thuận / 8 tranh chấp)
   → PTBC/VFG/30_banthao_cuoi.md
   → K5b RÀ SOÁT SỐ: đối chiếu 23 mệnh đề với nguồn gốc (21 khớp, 2 lệch đã vá)
   → đọc thẳng BCTC hợp nhất Q2/2026 (PDF chữ ký số, vfc.com.vn, công bố 21/07/2026)
   → BOSS DUYỆT → PTBC/VFG/31_loi_doc.txt  (26 câu · 380 từ · thước DAT)
```
File lời của xưởng phim = **bản sao** `31_loi_doc.txt`, chỉ khác đúng 1 chỗ (mục dưới).

## 🔴 MỘT LỖI SỐ BẮT ĐƯỢC Ở XƯỞNG PHIM (26/07, sau khi BOSS đã duyệt lời)

| | Bản BOSS duyệt | Bản dựng video |
| :-- | :-- | :-- |
| Dòng 9 | "tiền và tiền gửi hơn sáu trăm tỷ, **bằng nửa giá thị trường**" | "…, **một phần ba giá thị trường**" |

**Vì sao:** tiền + đầu tư TC ngắn hạn 30/06/2026 = **661,7 tỷ** (gói 03). Vốn hóa 24/07 =
41.712.614 cp × 45.900 đ = **1.915 tỷ** ⇒ tỷ lệ **34,6%**, không phải một nửa.
Con số *"54% thị giá"* trong gói 00 mục E là của **tiền ròng 24.763 đ/cp** (≈1.033 tỷ, tính
trên mỗi cổ phiếu) — hai đại lượng khác nhau bị ghép làm một khi rút gọn thành lời đọc.
Giữ số **661,7 tỷ** (đọc thẳng từ BCTC gốc) và sửa **tỷ lệ**, vì số kia mới là số truy được
tới nguồn. Bỏ thêm 1 từ ("vừa") ở câu cuối dòng 9 để giữ đúng trần **380 từ**.
→ Muốn quay lại nguyên văn BOSS duyệt: sửa 1 dòng trong `vfg_01_danhgia.txt` rồi chạy lại
`generate_tts.py` + render (không phải dựng lại deck).

## Nhịp + bản đồ slide

`nhip: [1, 1, 3, 3, 2, 3, 3, 3, 4, 3]` = **26 reveal / 380 từ / lời 106,85s**

| Slide | Vai (theo `goc/taichinh/nghich_ly_so.md`) | Scene |
| :-: | :-- | :-- |
| 1 | hai số chọi nhau, **chưa nói tên mã** | 🆕 `vfg-duel` |
| 2 | gọi tên mã + ngành, đúng 1 câu | `hk-head` + `hk-names` |
| 3 | con số thứ nhất đến từ đâu | `hk-note` + chip biên gộp |
| 4 | con số thứ hai đến từ đâu | 🆕 `vfg-jump` (544 → 878 tỷ, +61%) |
| 5 | đặt đúng câu hỏi, hai nhánh tách ra | `hk-branch` 2 ô **cùng màu trung tính** |
| 6 | khả năng LÀNH + bằng chứng | kicker `vfg-chip-ok` |
| 7 | khả năng ĐÁNG LO + bằng chứng | 🆕 `vfg-drain` (100 đ lãi → ~25 đ tiền) |
| 8 | cái gì phân biệt hai khả năng | ⭐ `speed-gauge` **mở hàng** (recolor) |
| 9 | bối cảnh, dồn 4 câu | `hk-names` + `hk-note` + `hk-branch` |
| 10 | chốt đối xứng, quay lại hai số mở bài | `hk-lockup` + `mien-tru` |

**Scene mới để lại cho kho:** `vfg-duel` (hero hai số — góc `nghich_ly_so` đặt hàng) ·
`vfg-jump` (một số nhảy bậc, dùng lại được cho mọi bài có "từ X lên Y") · `vfg-drain`
(hai cột lãi-trên-sổ vs tiền-thật). Cộng **mở hàng `speed-gauge`** của kho template —
bản kho tô **xanh #00e676 = "tốt"**, bài này cấm phán tốt/xấu nên phải recolor về palette
`tc` (đỏ → hổ phách → trắng), kim chỉ vùng trắng = **chưa phân định**.

## Hook — 3 phương án, chọn 1

| | Hook | Vì sao |
| :-: | :-- | :-- |
| ⭐ **chọn** | *"Lãi sáu tháng vẫn tăng, dòng tiền kinh doanh âm bốn mươi ba tỷ."* | 14 từ, mở bằng SỐ, đúng công thức góc (hai số chọi nhau, chưa nói tên mã). **BOSS đã duyệt** ở khâu PTBC |
| B | *"Bán hàng nhiều hơn, thu tiền ít hơn. Cùng một doanh nghiệp."* | mất số cụ thể ⇒ yếu hơn |
| C | *"Khoản khách nợ tăng ba trăm ba mươi tư tỷ trong sáu tháng."* | một số đứng một mình, chưa thành nghịch lý |

⚠️ **DÒNG 1 PHẢI LÀ MỘT CÂU** (luật 7b của SKILL) — hook này nối 2 vế bằng dấu phẩy, đúng luật.

## Tự kiểm — chạy được lại, 0 API

| Thước | Kết quả |
| :-- | :-- |
| `thuoc_kichban.py --goc nghich_ly_so` | `KETLUAN\|26\|380\|DAT` — 6/6 thước, 0 từ cấm |
| đếm reveal `index.html` | `[1,1,3,3,2,3,3,3,4,3]` khớp nhịp góc |
| `validate_slide.py --semantic-report` | **PASS**, safezone 10/10 OK |
| reveal cuối ≥1,2s (mục 7b) | **KHÔNG CÒN** slide nào <1,2s |
| dòng miễn trừ | có, ngoài `.slide-content`, không mang class reveal |
| `tts/phat_am.py --kiem` | ĐẠT 11/11 sau khi thêm `VFG` → `Vi Ép Gi` |

## Nguồn số trên màn hình

Toàn bộ số lấy từ `Research copy/PTBC/VFG/03_bctc_q2_2026_trichyeu.md` (đọc thẳng PDF gốc
BCTC hợp nhất Q2/2026, công bố 21/07/2026) và `00_goi_nguyenlieu.md`:
171,09 tỷ · +10,1% · biên gộp 25,1%→25,7% · CFO 6T −43,1 tỷ · phải thu 544,3→878,4 tỷ ·
tồn kho 1.178,7 tỷ · phải trả người bán 823,2 tỷ · tiền+ĐTTC 661,7 tỷ · 99,5 tỷ chứng khoán
kinh doanh · không khách nào chiếm từ 10% phải thu (TM II.2a) · nợ quá hạn 28 tỷ (BCTC kiểm
toán 2025, TM9) · cổ tức 2025 40% mệnh giá theo **nghị quyết** · cho PAN vay 350 tỷ năm 2025,
đã thu hồi trong năm.

⚠️ Số **"~25 đồng tiền thật trên 100 đồng lãi, ba năm qua"** (slide 7) là số của bản thảo
PTBC, không nằm trong gói 03 — nếu dựng lại bài này thì tra lại từ `ketqua.db`/BCTC trước.
