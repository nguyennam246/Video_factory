---
ten: Việc cần làm
ma: viec_can_lam
nhip: [1, 2, 3, 3, 3, 3, 2, 2, 3, 3]
---

# GÓC "VIỆC CẦN LÀM" — rơi sâu rồi, người xem hỏi *bây giờ làm gì*

**Tổng reveal 25 · nhịp trùng khuôn tài chính mặc định (cố ý: tái dùng deck đã gỡ lỗi).**

## Dùng khi
Người xem đã biết mã rơi sâu và câu hỏi thật của họ là **"lao vào bắt đáy hay đứng ngoài?"**.
Góc này KHÔNG trả lời câu đó — nó **đổi câu hỏi**: từ *"rẻ chưa?"* sang *"cái chưa biết
lớn cỡ nào, và nó sẽ hiện ra ở đâu?"*, rồi giao **việc cụ thể kiểm chứng được**.

Khác `ho_voi` ở chỗ: `ho_voi` dừng ở phân loại nguyên nhân rơi, xem xong vẫn không biết
làm gì. Góc này bắt buộc kết thúc bằng **hành động có địa chỉ** (mở đúng thuyết minh nào,
đếm đúng dòng tiền nào, viết ra trước con số nào).

## 11 từ đầu
Mở bằng **một hành vi có thật đang diễn ra**, không mở bằng giá.
Công thức: `{Chủ thể} đang {hành vi bất thường} gấp {N} lần {mốc bình thường}.`

❌ Sai: mở bằng "giá đã giảm X phần trăm" (ai cũng biết rồi, hết tò mò);
❌ Sai: "cơ hội", "bắt đáy", "đáng mua" ở bất kỳ đâu — vừa `CAM_KHUYEN` vừa phá cả góc.

## Nhịp kể từng dòng
| Dòng | Câu | Vai |
| :-: | :-: | :-- |
| 1 | 1 | **Hành vi bất thường.** Một con số so sánh, chưa nói giá |
| 2 | 2 | Mã nào, làm gì. **Nguồn của con số dòng 1** (ai công bố, ngày nào) |
| 3 | 3 | Chuyện gì đã xảy ra. Sự kiện gốc, có ngày |
| 4 | 3 | **Nghĩa vụ / ràng buộc** doanh nghiệp đang mang. Nói thẳng điều khoản |
| 5 | 3 | **Độ sâu · tốc độ · lượng khớp.** Rơi bao nhiêu, rơi nhanh cỡ nào, ai đang bán |
| 6 | 3 | Giá hôm nay đứng cạnh cái gì. Số tuyệt đối, **không phán đắt rẻ**. Nêu ngay chỗ số đó mỏng |
| 7 | 2 | **MẶT KIA** — cái tốt còn thật, có số |
| 8 | 2 | **Ô TRỐNG.** Con số quyết định mà chưa ai công bố. Đây là trục của cả bài |
| 9 | 3 | **Việc 1 và việc 2** — mở đúng thuyết minh nào, đếm đúng kỳ nào |
| 10 | 3 | **Việc 3 + chốt đối xứng:** rơi bao sâu không trả lời được gì; cái chưa biết mới trả lời |

## Bản đồ scene (khớp sẵn `deck_msr01`, chỉ thay chữ)
| Dòng | Scene | Ghi chú |
| :-: | :-- | :-- |
| 1 | hero + chip | 2 số đối nhau trên quầng, chip nhỏ ghi mốc so sánh |
| 2 | `hk-head` + `hk-names` | tên mã, quy mô, nguồn con số |
| 3 | `cm-cost` bars | mốc thời gian / quy mô sự kiện |
| 4 | `hk-branch` + `hk-answer` | điều khoản cũ ↔ điều khoản mới |
| 5 | `hk-head` + `hk-note` + `hk-names` | %ừ-đỉnh lớn ở đầu, tốc độ ở giữa, **lượng khớp** ở cuối |
| 6 | `hk-versus` | giá phải trả ↔ lãi nhận về, **hai vế CÙNG MÀU** |
| 7 | `sg-cond` + `hk-answer-ok` | cái tốt có thật, được phép tô tích cực |
| 8 | `hk-branch` + `hk-answer-no` | ô trống — dấu hỏi lớn, không phải kết luận xấu |
| 9 | `sg-num` 1·2·3 | **huy hiệu 1 KÝ TỰ** — chỉ số thứ tự, câu nằm ngoài huy hiệu |
| 10 | `hk-lockup` + `glowing-orb` | orb phải là **vàng** `rgba(255,176,32,…)` với palette `tc` |

## Bẫy
- **Ba việc phải KIỂM CHỨNG ĐƯỢC.** "Theo dõi sát", "cẩn trọng", "chờ thêm tín hiệu" là
  chữ rỗng. Việc đúng có địa chỉ: *tên thuyết minh*, *kỳ báo cáo*, *hạn công bố*.
- **Việc thứ ba luôn là "viết ra trước con số khiến bạn đổi ý"** — đó là thứ duy nhất
  biến bài thành nghề, và là cách trả lời "bắt đáy hay không" mà không khuyến nghị gì.
- **Không được để dòng 6 thành lời phán rẻ.** Đặt số cạnh số, rồi nói ngay chỗ số đó mỏng
  (bao nhiêu phần lãi đến từ một quý bất thường). Màu hai vế phải giống nhau.
- **Mã đã chia thưởng / chia tách trong kỳ đang so ⇒ PHẢI chia lại mốc đỉnh trước khi tính %,**
  vì `gia.db` lưu giá thô không hồi tố. Bỏ qua là sai ngay con số to nhất của bài (ca PNJ 01:
  nói −76%, đúng là −64%). **Nhưng đừng GIẢI THÍCH việc chia lại đó trên video** — BOSS nghe
  bản PNJ 02 rồi phán *"chỗ giải thích giá 127 điều chỉnh là không cần thiết"*. Tính đúng ở
  hậu trường, trên màn hình chỉ đưa **con số đã đúng**. Cách kiểm 30 giây: SKILL mục 2.
- **Dòng 5 nên có LƯỢNG KHỚP, không chỉ có %.** Người xem đang hỏi "bắt đáy hay không" thì
  thứ nói lên nhiều nhất là *ai đang bán và bán mạnh cỡ nào* — một phiên khớp gấp hàng chục
  lần bình thường là dữ kiện, không phải lời phán. Lấy từ `gia.db`, so với trung bình một
  cửa sổ nêu rõ (đừng lấy `avgVolume3m` trong `fundamentals` — nó là ảnh chụp cũ).
