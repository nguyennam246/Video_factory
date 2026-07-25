# TRUY VẾT — pnj_01_danhgia (25/07/2026)

**Góc:** `ho_voi` (Hố voi) · nhịp `[1,2,3,2,3,3,3,3,3,4]` = 27 reveal · thước `KETLUAN|27|380|DAT`
**Giọng:** edge `vi-VN-NamMinhNeural` `+14%` (mặc định bài tài chính, BOSS chốt 24/07)

## ⚠️ BÀI NÀY KHÁC MỌI BÀI TRƯỚC — ĐỌC TRƯỚC KHI TÁI DÙNG

**Không có `baocao/hoso/PNJ_HoSo.md`.** PNJ không có tài liệu nào trong `baocao/MD/` ⇒ cổng B0
của `chay_ruiro.py` chặn, chuỗi rủi ro ①② chưa từng chạy cho mã này. **BOSS chốt 25/07: làm
video ngay, không chạy chuỗi** — lý do: chuỗi đọc tài liệu **2025**, không thể chứa sự kiện
tháng 7/2026 vốn là toàn bộ câu chuyện của bài.

⇒ Nguồn sự thật của bài này là **3 tầng, không phải `_HoSo.md`**:
1. **Số nội bộ (mạnh nhất):** `dulieu/BCTC.db` tới Q1/2026 · `dulieu/gia.db` (đã cập nhật 25/07)
2. **`baocao/PNJ_BaoCao.md`** (13/07/2026) — giới thiệu DN, 431 cửa hàng
3. **Web có nguồn** — sự kiện tháng 7/2026 (bảng dưới)

## Số nội bộ — TỰ ĐO LẠI, KHÔNG LẤY TỪ BÁO

| Dữ kiện | Số | Lệnh kiểm |
| :-- | :-- | :-- |
| Giá 24/07/2026 | **30.750đ** (sàn, −6,96%, 41,3tr cp) | `sqlite3 dulieu/gia.db "SELECT date,close,volume FROM prices WHERE symbol='PNJ' ORDER BY date DESC LIMIT 3"` |
| Đỉnh 12 tháng | **127.000đ** (02/01/2026) | cùng bảng, `WHERE close>=120` |
| Rơi từ đỉnh | **−75,8%** | 30,75 ÷ 127,0 |
| Rơi tháng 7 | **−51,3%** / 16 phiên | 63,10 (02/07) → 30,75 (24/07) |
| DTT Q1/2026 | **17.245,2 tỷ** | `fin_items` PNJ KQKD_Q 2026 Q1 |
| LNST Q1/2026 | **1.467,4 tỷ** | cùng bảng, mục 19 |
| DTT / LNST Q1/2025 | **9.635,1 / 677,7 tỷ** | cùng bảng, 2025 Q1 |
| Tăng trưởng YoY | DTT **+79%** · LNST **+117%** | tính từ 2 dòng trên |
| Biên gộp | 21,3% (Q1/25) → **19,9%** (Q1/26) | LN gộp ÷ DTT |
| Chi phí lãi vay Q1/2026 | **50,6 tỷ** | cùng bảng |
| Vốn hóa | **15.735 tỷ** | 511.721.959 cp × 30.750đ — khớp đúng số báo chí |

**✅ Đối chứng chéo:** DTT 17.366 tỷ (tổng DT) và LNST 1.467 tỷ mà báo chí đăng **khớp từng số**
với `BCTC.db` tự đo. Không lấy số nào của bài từ báo mà không có bản đối chứng nội bộ.

## Web — sự kiện tháng 7/2026 (không có trong tài liệu 2025 nào)

| Dữ kiện dùng trong bài | Nguồn |
| :-- | :-- |
| GĐ cũ công ty giám định P-Lab (công ty con PNJ) bị bắt; 141 chuyến, >28.000 viên kim cương từ Hồng Kông 2024→nay, ~280 tỷ; thủ đoạn mài số GIA rồi khắc số P-Lab | [VnExpress](https://vnexpress.net/duong-day-buon-lau-hon-28-000-vien-kim-cuong-5092792.html) · [Dân trí](https://dantri.com.vn/kinh-doanh/vu-buon-lau-28000-vien-kim-cuong-nguyen-ceo-bi-bat-phia-p-lab-noi-gi-20260702203335746.htm) |
| Chủ tịch Cao Thị Ngọc Dung: 28.000 viên kim cương lậu **không đi vào hệ thống phân phối PNJ** | [VnExpress](https://vnexpress.net/ba-cao-thi-ngoc-dung-28-000-vien-kim-cuong-buon-lau-khong-vao-he-thong-pnj-5094012.html) · [Tuổi Trẻ](https://tuoitre.vn/ba-cao-thi-ngoc-dung-28000-vien-kim-cuong-nhap-lau-khong-di-vao-he-thong-phan-phoi-cua-pnj-100260706194438214.htm) |
| Kim cương ≈ **33% doanh thu trang sức** (10% rời + 23% trang sức); SSI hạ dự phóng LNST 2026 → **3.333 tỷ** (−236 tỷ), khuyến nghị + giá mục tiêu "đang xem xét" | [CafeF/SSI](https://cafef.vn/uoc-tinh-kim-cuong-chiem-33-doanh-thu-mang-trang-suc-cua-pnj-ssi-canh-bao-188260706182002376.chn) |
| Cam kết mua lại **70–90% giá hóa đơn**, nay **giãn trả tới 120 ngày**; Diamond Standard Index **thấp nhất kể từ 2002** | [DNSE](https://www.dnse.com.vn/senses/tin-tuc/the-kho-cua-pnj-kim-cuong-the-gioi-rot-khong-phanh-nhung-van-phai-mua-lai-gia-cao-chot-vot-35249658) |
| Lab-grown 1 carat **−79%** từ đầu 2020 → ~768 USD (FT); Zimnisky rough −15% (2023) −18% (2024), ~−40% từ đỉnh 2021-22; lab-grown >55% lượng nhẫn cầu hôn phương Tây | tổng hợp web 22/07/2026 |
| PNJ lập tổ giám sát đặc biệt tại P-Lab | [CafeF](https://cafef.vn/pnj-lap-to-giam-sat-dac-biet-tai-p-lab-sau-vu-28000-vien-kim-cuong-nhap-lau-1882607072150269.chn) |
| VN-Index 1.686,11 (24/07), từ ~1.850 đầu tháng 7 ⇒ **≈ −9%** | [Vietstock](https://vietstock.vn/2026/07/chung-khoan-tuan-20-24072026-ap-luc-chua-ha-nhiet-1636-1470917.htm) |

## 3 PHƯƠNG ÁN HOOK (BOSS đổi được)

1. ✅ **CHỌN** — `Năm mươi mốt phần trăm biến mất trong mười sáu phiên, lợi nhuận vẫn lập đỉnh.` (16 từ, đúng trần)
   *Lý do:* mở bằng SỐ, có mất mát trong 11 từ đầu (`biến mất` ở từ 6-7), và dựng ngay nghịch lý
   người xem **không tự trả lời được** — rơi một nửa mà lãi lập đỉnh thì rơi vì cái gì. Không hé nguyên nhân.
2. `Bảy mươi sáu phần trăm từ đỉnh, và báo cáo gần nhất vẫn là quý lãi lớn nhất.` — độ sâu lớn hơn
   (−76% ép hơn −51%) nhưng dùng mốc 6 tháng nên loãng tính "vừa xảy ra"; và ăn mất câu chốt slide 10.
3. `Hai mươi tám nghìn viên kim cương, và một nửa giá trị doanh nghiệp.` — giật nhất, nhưng mở bằng
   **vụ án** thay vì độ sâu ⇒ trái công thức 11 từ đầu của góc `ho_voi`, và nói luôn nguyên nhân ⇒ hết tò mò.

## Tự kiểm 4 luật cấm
- **CẤM kết luận đắt/rẻ:** ✅ không có. `q5_result` PNJ có nhãn P/E `RẺ` và P/B 0,83 (dưới sổ sách)
  — **cố ý KHÔNG dùng**, vì (a) skill cấm kết luận giá, (b) chính `q5_result` ghi *"CẤM dùng PB —
  nghi phải thu/tồn kho phình, book có thể ảo"*. Không có chữ P/E, P/B nào trong bài.
- **CẤM khuyến nghị:** ✅ slide 10 có câu miễn trừ; không có từ nào trong `CAM_KHUYEN`.
- **CẤM dọa dẫm:** ✅ thước xác nhận 0 từ trong `CAM_DOA`. Không dùng "bốc hơi" dù báo chí dùng đầy.
- **CẤM ngôn ngữ hệ thống:** ✅ 0 từ. Không nhắc chuỗi rủi ro / B0 / hồ sơ.

## Cân bằng — chống bóp méo
Bài nói điều xấu (slide 6-7) **và** điều không đổi (slide 8: nợ vay mỏng 50,6 tỷ, cửa hàng/nhà
máy/mảng vàng nguyên, phát ngôn của Chủ tịch). Vụ án là **cá nhân GĐ cũ của công ty con**, đang
điều tra — bài **không** quy kết doanh nghiệp, và slide 7 dẫn nguyên văn phản hồi của Chủ tịch.
**Không nêu tên cá nhân bị bắt trong lời đọc** (không cần cho phân tích; giữ tên ở bảng nguồn trên).

## Giới hạn phải nói rõ với BOSS
- Số kinh doanh mới nhất là **Q1/2026 (tháng 1-3)** — trước sự kiện. Bài đã nói thẳng câu này
  ở slide 5 (`Đó là báo cáo gần nhất, có trước khi giá rơi`) thay vì để người xem tự suy.
- Tỷ trọng 33% và các số về giá kim cương thế giới là **ước tính của bên thứ ba**, không phải
  số PNJ công bố. Slide 6 nói "khoảng".
- VN-Index đầu tháng 7 lấy mốc "~1.850" từ báo (khoảng), nên bài viết "khoảng chín phần trăm".
