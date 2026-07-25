# NHẬT KÝ GÓC ĐÃ DÙNG — hai mã liền nhau không được cùng góc

Ghi ngay sau khi chốt góc, TRƯỚC khi viết lời. Cột "scene mới đẻ ra" là kỷ luật bắt
buộc: **mỗi bài phải để lại ít nhất 1 scene mới** cho kho dùng chung, nếu không kho
không bao giờ lớn.

| Ngày | Mã | Góc | Scene mới đẻ ra | Ghi chú |
| :-- | :-- | :-- | :-- | :-- |
| 24/07 | MSR | *(chưa có thư viện góc)* | — | khuôn cứng cũ |
| 24/07 | HPD | *(chưa có thư viện góc)* | — | khuôn cứng cũ |
| 24/07 | TCL · SKV · MCF | *(chưa có thư viện góc)* | — | khuôn cứng cũ |
| 25/07 | **PNJ** | `ho_voi` | **đường có hố** (dòng 3) · **hai đường chồng lệch pha** (dòng 8) | **Bài đầu tiên dùng thư viện góc.** Không có `PNJ_HoSo.md` — mã chưa có tài liệu trong `baocao/MD/` nên chuỗi rủi ro bị B0 chặn; BOSS chốt làm video từ BCTC.db + gia.db + web có nguồn. Rơi −51% trong 16 phiên vì vụ kim cương ở công ty con giám định. 🔴 **BOSS BÁC** — xem dòng dưới |
| 25/07 | **PNJ (làm lại)** | `viec_can_lam` ⭐ góc mới | *(0 scene mới — CỐ Ý, xem ghi chú)* | **BOSS bác bài `ho_voi` vì 2 lẽ: ① số giảm từ đỉnh SAI — quên chia thưởng cổ phiếu 50% ngày 23/04 ⇒ "−76%" phải là **−64%** · ② "hố voi ở đây chưa hay lắm", muốn nói rõ **nhà đầu tư làm gì lúc này**.** Đẻ góc `viec_can_lam`: đổi câu hỏi từ *"rẻ chưa"* sang *"cái chưa biết lớn cỡ nào, và nó hiện ra ở đâu"*, kết bằng 3 việc kiểm chứng được. **Cố ý KHÔNG đẻ scene mới, cố ý lấy nhịp trùng khuôn mặc định** để tái dùng `deck_msr01` đã gỡ lỗi — BOSS vừa hỏi *"sao làm video tốn thời gian thế?"*, bài này đo thử đường đi RẺ NHẤT (xem `patch_history` 25/07) |

## Scene tự dựng đang chờ ai đó đẻ ra
Các góc đã đặt hàng những scene này nhưng kho **chưa có** — bài nào chạm tới thì dựng
rồi ghi vào đây:

- ~~**đường có hố** (góc `ho_voi`, dòng 3)~~ ✅ **ĐÃ DỰNG 25/07 (PNJ)** — `.pnj-road` trong
  `deck_pnj01/style.css`: SVG 320×96, 2 đoạn đường `stroke-dasharray` + hố `Q`-curve đỏ + chấm xe.
- **đổ dây chuyền** — khối tắt đèn lần lượt (góc `thu_giet_dn`, dòng 6)
- **tờ biên bản có tick** (góc `bang_chung`, dòng 3)
- **trục vòng đời 4 giai đoạn** (góc `dong_ho_chay`, dòng 3)
- ~~**hai trục chồng lệch pha** (góc `dong_ho_chay` dòng 6, `ho_voi` dòng 8)~~ ✅ **ĐÃ DỰNG 25/07
  (PNJ)** — `.pnj-dual`: 2 `polyline` chồng nhau (thị trường nét đứt xám gần phẳng vs mã nét liền
  đỏ dốc) + legend 2 chip. Dùng lại được cho `dong_ho_chay` dòng 6.
- **lớp bóc khỏi thanh giá** (góc `gia_da_tinh_san`, dòng 8)

## Mẫu kho escbase còn chưa đụng lần nào
`speed-gauge` + 4 hero. Góc `nghich_ly_so` và `dong_ho_chay` đều đã đặt `speed-gauge` —
bài nào chạy trước thì mở hàng.
