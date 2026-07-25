# PNJ 02 — "Việc cần làm" (dựng lại sau khi BOSS bác bài 01)

**Ngày:** 25/07/2026 · **Góc:** `viec_can_lam` (mới đẻ) · **Deck:** `deck_pnj02` (chép `deck_msr01`)
**Thay cho:** `PNJ_01_danhgia.mp4` (góc `ho_voi`) — BOSS bác 2 điểm:
① số giảm từ đỉnh SAI, ② góc hố voi "chưa hay lắm", muốn nói rõ **nhà đầu tư làm gì lúc này**.

---

## 🔄 BẢN 02b (25/07 chiều) — BOSS nghe rồi phán 3 điều, đã sửa cả 3

| BOSS phán | Đã làm |
| :-- | :-- |
| *"chỗ giải thích giá 127 điều chỉnh là không cần thiết"* | **Bỏ hẳn slide 5 cũ.** Thay bằng ĐỘ SÂU + TỐC ĐỘ + LƯỢNG KHỚP: −64% từ đỉnh tháng 1 · riêng tháng 7 −51% trong 16 phiên · phiên gần nhất khớp **41,3 triệu cp, lớn nhất lịch sử mã này**, gấp hơn 20 lần bình thường. Không còn chữ nào nhắc 127.000 / 84.667 / thưởng cổ phiếu |
| *"AI đọc chữ tiếng Anh hay lỗi, mã CP PNJ đọc lỗi"* | Dựng 2 bài thử cho BOSS nghe → **BOSS chốt: mã CP phương án C** (tên chữ cái kiểu Anh: `PNJ` → "Pi En Giây") · **tiếng Anh phương án B** (viết theo âm Việt: `superpower` → "su pơ pao ơ"). Đóng thành `tts/phat_am.json` + `tts/phat_am.py`, áp **CHỈ lên đường TTS** — phụ đề vẫn hiện "PNJ" |
| *"video hình như chưa hết mà đã dừng rồi"* | Đo ra đúng: đuôi **0,024s**, 1 giây cuối vẫn còn tiếng ở max **−4,8 dB**. Thêm `TAIL_SECONDS = 1.4` (vá **cả 2 nhánh**: `tts/common.py` và `split_voiceover.py`) + đóng **cổng ⑦** trong thước nghiệm thu |

⚠️ Lỗi đuôi có ở **MỌI bài trước** (MSR · HPD · PNJ 01) — chỉ là chưa ai gọi tên. Dựng lại
bài nào thì bài đó tự khỏi.

---

## 🔴 LỖI SỐ CỦA BÀI 01 — vì sao con số cũ sai (giữ lại để tra, KHÔNG còn trong video)

Bài 01 nói *"giảm 76% từ đỉnh 127.000đ"*. **Sai.** Bản 02 sửa số VÀ giải thích trên slide;
bản 02b giữ **số đúng** nhưng **bỏ phần giải thích** (BOSS: không cần thiết).

| | Bài 01 | Đúng |
| :-- | :-- | :-- |
| Đỉnh 30/01/2026 | 127.000 đ (giá thô) | **84.667 đ** (đã điều chỉnh) |
| Giảm từ đỉnh | −75,8% ❌ | **−63,7%** |
| Giảm từ 02/07 | −51,3% | −51,3% ✓ không đổi |

**Nguyên nhân:** ngày **23/04/2026** PNJ chốt quyền **thưởng cổ phiếu tỷ lệ 2:1** (sở hữu 2 cp
nhận thêm 1 = +50%), 341,3 tr → 511,8 tr cp. `dulieu/gia.db` lưu **giá thô, KHÔNG hồi tố**:
22/04 đóng 110.000 → 23/04 mở 75.100. Mọi giá trước 23/04 phải **chia 1,5** mới so được với
giá hôm nay.

**3 mỏ neo độc lập cùng chỉ một số:**
1. `dulieu/BCTC.db` bảng `fundamentals` (chụp 08/07/2026): `high52Week = 84666.67` = đúng 127.000 ÷ 1,5.
2. `dulieu/BCTC.db` bảng `dividends`: PNJ 2026 `stock_dividend = 50.0`.
3. Đứt gãy giá trong `gia.db` đúng ngày 23/04 (110,0 → 75,1; giá tham chiếu lý thuyết 73,33,
   nằm trong biên ±7%). Không có đứt gãy nào khác giữa 30/01 và 24/07.

⚠️ **Cảnh báo dùng lại:** vì `gia.db` không hồi tố, **mọi so sánh giá xuyên qua một lần chia
thưởng/chia tách đều sai** nếu không tự chia lại. PNJ còn chia thưởng 2022 (33,3%), 2019
(33,3%), 2018 (50%), 2015 (30%), 2012 (20%) ⇒ **cấm** so giá hôm nay với giá trước 2022 từ DB này.

---

## Bảng truy vết từng số trên slide

| Slide | Số | Nguồn |
| :-: | :-- | :-- |
| 1·2 | mua lại **gấp 5 lần** bán ra, từ 03/07 | PNJ công bố tại họp báo **21/07/2026** (Tuổi Trẻ, DNSE, Znews) |
| 2 | 431 cửa hàng, HOSE | hồ sơ doanh nghiệp |
| 3 | cựu GĐ **P-Lab** (PNJ sở hữu 100%) bị bắt; **>28.000 viên** kim cương | báo chí đầu 07/2026 |
| 4 | cam kết mua lại **70–90% giá hóa đơn**; giữ nguyên cam kết, **giãn tới 120 ngày**, có hạn mức/ngày | họp báo 21/07 |
| 5 | **−64%** từ đỉnh tháng 1 (đỉnh đã chia lại 84.667 đ, KHÔNG nói lên màn hình) · riêng tháng 7 **−51%** trong **16 phiên** (63.100 → 30.750) · phiên 24/07 khớp **41,3 triệu cp = lớn nhất lịch sử mã này**, gấp **24,5 lần** TB nửa đầu 2026 (1.688.842 cp) ⇒ đọc "hơn 20 lần" | `gia.db` (4.128 phiên từ 2010; 3 phiên lớn nhất: 24/07 41,3tr · 08/07 25,6tr · 16/07 14,7tr) |
| 6 | giá 24/07 = **30.750 đ**; 4 quý gần nhất lãi **3.619 tỷ**; **1.467 tỷ (40,5%)** từ Q1/2026 | `gia.db`; `std_quarter` Q2/25–Q1/26 = 437,0+495,7+1.218,9+1.467,4 |
| 7 | CFO Q1/2026 **+3.557,8 tỷ**; tiền 923,5 + đầu tư NH 3.586,4 = **4.509,9 tỷ** > vay 2.893,6 (vay dài hạn = 0) | `std_quarter` PNJ 2026Q1 |
| 8 | nghĩa vụ mua lại **chưa có con số công bố** | không tìm thấy ở bất kỳ nguồn nào — đó chính là nội dung slide |
| 9 | báo cáo bán niên **soát xét**; mục *dự phòng phải trả* + *nghĩa vụ tiềm tàng* | chuẩn mực trình bày BCTC |

**Số KHÔNG đưa lên màn hình** (biết nhưng cố ý bỏ, tránh thành lời phán đắt/rẻ):
P/E 4,35 · P/B 1,09 · EPS TTM 7.072đ · vốn hóa 15.735 tỷ · tồn kho 13.419 tỷ.
Lý do: `CAM_KHUYEN`. Bài đặt số cạnh số, để người xem tự kết luận.

---

## 3 phương án hook (chọn 1)

1. ⭐ **"Khách mang kim cương đến bán gấp năm lần số hàng bán ra."** — CHỌN.
   Hành vi có thật, đang diễn ra, có nguồn công ty tự công bố. Chưa nói giá ⇒ giữ tò mò.
2. "Ba mươi nghìn bảy trăm năm mươi đồng, thấp nhất kể từ khi chia thưởng." — bỏ: mở bằng
   giá là thứ ai cũng biết, hết sức căng ngay dòng 1.
3. "Một cam kết mua lại bảy mươi phần trăm hóa đơn, ký từ trước khi giá kim cương sập." —
   bỏ: dính từ cấm `sập`, và câu dài quá 16 từ.

## Tự kiểm
```
GÓC: Việc cần làm | nhịp: [1,2,3,3,3,3,2,2,3,3]
dòng 10 | câu/dòng khớp | tổng câu 25 | TỪ 380 | hook 13 từ | dấu — không | TỪ CẤM không
✅ ĐẠT hết 6 thước — ngay vòng 1 (bài HPD phải siết 3 vòng)
validate_slide --semantic-report: PASS (vòng 2; vòng 1 FAIL vì hero slide 1 tràn 4,48px)
Bản 02b: thay slide 5 xong phải siết 2 lần (381 -> 380 từ), thước bắt cả 2 lần.
tts/phat_am.py --kiem: 11/11 ca ĐẠT · 54 khoá
```

## Lỗi soi ảnh bắt được (1 lỗi, đều là lỗi NGHĨA)
- **Slide 10 `hk-lockup-a` màu ĐỎ** rgba(239,68,68) = "vế bị bác bỏ". Ở MSR đúng ("Giá lên là
  một chuyện" bị gạt sang), ở đây bọc câu **dạy nghề đứng vững** ⇒ màn hình bác một câu đúng.
  Vá: `.conclusion-content .hk-lockup-a` về trung tính, giữ hiệu ứng mờ dần.
- Ba bẫy khác **chặn trước bằng CSS ngay từ đầu**, không phải soi mới thấy (đã có trong SKILL
  mục 4): `hk-vs-old` đỏ ở slide 5 → `.vcl-flat` hai vế cùng màu · `hk-answer` trần không nền
  ở slide 4·8 → `.vcl-flat` · `glowing-orb` xanh → vàng.
