# Báo cáo truy vết kịch bản HPD

Nguồn sự thật: `Research copy/baocao/hoso/HPD_HoSo.md` (bản dựng lại 24/07/2026 sau khi
cập nhật giá). HPD = Công ty cổ phần Thủy điện Đăk Đoa.

## 1. Bảng truy vết

| Dữ kiện trong lời đọc | Nguồn và vị trí |
| :-- | :-- |
| Biên lãi sau thuế 48% (2025) | `HPD_HoSo.md` ① Khoang 2, dòng 36 và 47; ghi "Hệ số Lợi nhuận sau thuế/Doanh thu thuần 0,46 (2024) → 0,48 (2025)" |
| Một nhà máy thủy điện tại Gia Lai | ① Khoang 1, dòng 18 và 25 (làng Đê Goh, xã Đak Sơmei) |
| Doanh thu thuần 2025: 51,56 tỷ | ① Khoang 1, dòng 15 (51.561.979.709 VND) |
| Lãi sau thuế 2025: 24,92 tỷ | ① Khoang 2, dòng 34 và 43 (24.922.735.658 VND) |
| Giá vốn bán điện 2025: 19,78 tỷ | ① Khoang 2, dòng 41 (19.775.413.400 VND) |
| Khấu hao TSCĐ 2025: 13,65 tỷ | ① Khoang 2 dòng 51; Khoang 3 dòng 64 (13.648.911.012 VND) |
| **Ưu đãi thuế TNDN 10% trong 15 năm, 2011 đến hết 2025; từ 2026 nộp 20%** | ① Khoang 4, **dòng 67 và 72** · nguồn gốc BCTC thuyết minh 4.18 |
| LNTT 2025 27,73 tỷ → LNST 24,92 tỷ | ① Khoang 2, dòng 42 và 43 (27.726.024 và 24.922.736 nghìn đồng) |
| Sản lượng 2025: 48,49 triệu kWh, đạt 127% kế hoạch | ① Khoang 1, dòng 21 và 26 (NQ điều 1) |
| Kế hoạch sản lượng 2026: 39,56 triệu kWh (thấp hơn thực hiện 2025) | ① Khoang 1, dòng 22 và 27 |
| Kế hoạch doanh thu 2026: 46,80 tỷ (thấp hơn thực hiện 52,17 tỷ) | ① Khoang 1, dòng 29; trường `kehoach.dt_nam_toi` |
| **Bảng kế hoạch 2026 chỉ ghi LNTT 29,66 tỷ, KHÔNG có dòng LNST** | trường `kehoach.*` dòng 254-258; đối chiếu gốc `baocao/MD/NQ/HPD_NQHD_2026.md` dòng 100-102 (bảng 2026) so với dòng 76-80 (bảng 2025 có ĐỦ cả LNTT và LNST) |
| Giá 16.200đ ngày 24/07/2026 | ③ ĐỊNH GIÁ & SỐ, dòng "Định giá: RẺ … giá hiện tại 16,200 (2026-07-24)" |
| EPS 2025 = 3.000đ · BVPS = 16.932đ | ③ bảng "HPD — Thủy điện · luật DQ", cột 2025 |
| Vay dài hạn cuối 2025 = 0 (đầu năm 15 tỷ) | ① Khoang 3, dòng 60 |
| Nợ vay/VCSH 0,25 (2024) → 0,11 (2025) | ③ bảng luật DQ, dòng "Nợ vay/VCSH" |
| Dòng tiền kinh doanh 2025: 38,87 tỷ | ① Khoang 2, dòng 35, 48, 50; trường `cfo.cfo_nam` |
| Kiểm toán chấp nhận toàn phần | ① Khoang 7, dòng 133 và 141; trường `kiemtoan.y_kien` |
| **ĐHĐCĐ ủy quyền thế chấp tài sản nhà máy bảo lãnh cho Sông Đà 11 (mẹ gián tiếp) "và các doanh nghiệp khác"** | ① Khoang 8, dòng 149, 150, 152; trường `blq.bao_lanh`; ② Sổ rủi ro dòng 349 |
| Tài liệu không nêu hợp đồng đã ký / hạn mức / dư nợ được bảo lãnh | ② Sổ rủi ro dòng 349, nguyên văn: "tài liệu KHÔNG nêu hợp đồng bảo lãnh đã ký, hạn mức hay dư nợ được bảo lãnh" |
| TSCĐ thế chấp 80,66 tỷ = 48% tổng tài sản 168,03 tỷ | ① Khoang 7 dòng 138, Khoang 8 dòng 154; trường `no.tai_san_cam_co`, `blq.tong_tai_san` |

Số tiền trong lời được đọc tròn cho tự nhiên; số chính xác giữ ở file `.man_hinh.md`.

## 2. Giá đã cập nhật trước khi viết lời

Hồ sơ trước đó ghi **16.400đ ngày 10/07/2026** (cũ 2 tuần). Theo luật đúc từ ca MSR
(chạy CẢ HAI nguồn, vì `capnhat_gia.py` làm mới giá và P/B nhưng KHÔNG làm mới P/E):

```
scripts/capnhat_gia.py --symbols HPD     → 2026-07-24 [VNDirect], ghi 10 dòng giá mới
scripts/fireant_pull.py pull HPD --update → fundamental + CDKT + KQKD + LCTT + cổ tức
scripts/q5_calc.py HPD  →  RẺ — CÓ BIÊN AN TOÀN
scripts/gen_trang_dn.py HPD  →  HPD_HoSo.md dựng lại
```

Kết quả: **16.200đ ngày 24/07/2026** (giảm 1,2% so với 16.400đ ngày 10/07).

## 3. Ba phương án hook

1. ⭐ **Bốn mươi tám phần trăm doanh thu thành lợi nhuận, ưu đãi thuế vừa hết hạn.** (16 từ)
2. **Mười lăm năm hưởng thuế mười phần trăm vừa kết thúc, năm nay đóng hai mươi.** (15 từ)
3. **Giá mười sáu nghìn hai trăm, giá trị sổ sách mười sáu nghìn chín trăm.** (14 từ)

Chọn phương án 1: từ đầu tiên là SỐ, nêu ngay một con số đẹp bất thường (biên 48%) rồi
đặt cạnh sự kiện làm người xem không tự trả lời được (ưu đãi vừa hết) — slide 4 mới trả lời.
Phương án 2 nói hết nguyên nhân ngay nên hết tò mò; phương án 3 dễ bị nghe thành gợi ý
"rẻ", chạm luật cấm khuyến nghị.

Câu chốt slide 10 đối xứng lại hook: *"Ưu đãi hết hạn là một chuyện, giữ lại bao nhiêu
sau thuế là chuyện khác."*

## 4. Hai vấn đề được chọn

**Vấn đề 1 — ưu đãi thuế hết hạn có LỊCH cụ thể.** Đây là quan hệ sắc nhất của HPD: biên
lãi sau thuế 48% và mức thuế thực nộp năm 2025 chỉ khoảng 10% đứng cùng nhau, mà ưu đãi
kết thúc đúng 31/12/2025. Từ 2026 thuế suất thông thường 20%. Đây là sự kiện bất lợi CÓ
TÊN + CÓ LỊCH, không phải suy đoán.

**Vấn đề 2 — bảng kế hoạch 2026 bỏ trống dòng lãi sau thuế.** Bảng kết quả 2025 trong
cùng nghị quyết ghi ĐỦ cả lợi nhuận trước thuế và sau thuế; bảng kế hoạch 2026 chỉ ghi
trước thuế. Kịch bản chỉ nêu đúng sự thật "bảng chỉ ghi lãi trước thuế, không ghi lãi sau
thuế" và **không** tự tính hộ con số sau thuế, vì tài liệu không đưa ra con số đó.

Đỉnh chu kỳ lợi nhuận (2025 bằng 1,57 lần trung bình nhiều năm) cũng quan trọng, nhưng
khuôn chỉ có hai vấn đề chính; bài chọn nói gián tiếp qua việc chính công ty đặt kế hoạch
sản lượng và doanh thu 2026 thấp hơn thực hiện 2025.

## 5. Mặt kia đã nêu (slide 7)

Ba cải thiện có thật, không phải câu cân bằng xã giao: vay dài hạn cuối 2025 về 0 (đầu năm
15 tỷ); nợ vay trên vốn chủ từ 0,25 xuống 0,11; dòng tiền kinh doanh 38,87 tỷ cao hơn lãi
sau thuế 24,92 tỷ; kiểm toán chấp nhận toàn phần.

## 6. Chỗ hồ sơ chưa đủ dữ kiện (slide 8)

ĐHĐCĐ đã ủy quyền cho ban quản trị đem công trình, máy móc nhà máy làm tài sản bảo đảm cho
khoản vay và bảo lãnh của công ty mẹ gián tiếp "và các doanh nghiệp khác" cho năm 2026 và
các năm tiếp theo. Bằng chứng mới ở **nấc ỦY QUYỀN**: tài liệu không nêu hợp đồng nào đã
ký, không nêu hạn mức, không nêu dư nợ được bảo lãnh. Kịch bản dừng đúng ở đó, không kết
luận công ty đã gánh nợ thay ai.

Lưu ý không được nối số: 80,66 tỷ TSCĐ thế chấp là bảo đảm cho khoản vay **của chính công
ty**, không phải giá trị đã bảo lãnh cho bên khác. Vì đặt hai con số cạnh nhau trên cùng một
slide gần như chắc chắn bị đọc thành "đã bảo lãnh 80,66 tỷ", **con số này đã được bỏ hẳn khỏi
slide 8**; slide chỉ nêu đúng ba chỗ tài liệu để trống (hợp đồng, hạn mức, dư nợ).

Hồ sơ cũng không đưa định giá tuyệt đối đáng tin cậy. Slide 6 chỉ đặt giá cạnh EPS và giá
trị sổ sách, không có giá mục tiêu, không kết luận đắt rẻ.

## 7. Kết quả tự kiểm

```text
dòng: 10 | câu/slide: [1, 2, 3, 3, 3, 3, 2, 2, 3, 3] | tổng câu: 25 | từ: 380
hook: 16 từ -> Bốn mươi tám phần trăm doanh thu thành lợi nhuận, ưu đãi thuế vừa hết hạn.
có dấu — : False
TỪ CẤM: KHÔNG
```

KETLUAN|25|380|DAT
