---
ten: Nghịch lý số
ma: nghich_ly_so
nhip: [1, 1, 3, 3, 2, 3, 3, 3, 4, 3]
---

# GÓC "NGHỊCH LÝ SỐ" — hai con số đáng lẽ đi cùng nhau lại ngược nhau

**Tổng reveal 26 · nhịp mở DỒN DẬP (1-1), giữa chậm lại, dòng 9 dồn 4 câu để chốt.**

## Dùng khi
Hồ sơ có **hai chỉ số phá vỡ kỳ vọng thông thường**: doanh thu tăng mà dòng tiền âm ·
lợi nhuận tăng mà biên co lại · tồn kho phình nhanh hơn doanh số · nợ giảm mà chi phí
lãi tăng. Không có cặp số nào chọi nhau thì **đừng ép dùng góc này** — sẽ thành làm màu.

## 11 từ đầu (3 giây đầu)
Đọc thẳng **hai con số**, không dẫn nhập, không tên công ty trước số.
Công thức: `<số A>. <số B>. Hai con số cùng một doanh nghiệp.`

Ví dụ khuôn (thay bằng số thật của mã):
> *"Doanh thu tăng {A} phần trăm. Dòng tiền âm {B} tỷ. Cùng một năm."*

❌ Sai: *"Hôm nay chúng ta cùng nhìn vào báo cáo của mã X"* — mất 11 từ vào chỗ trống rỗng.

## Nhịp kể từng dòng
| Dòng | Câu | Vai |
| :-: | :-: | :-- |
| 1 | 1 | **Hai số chọi nhau.** Chưa nói tên mã |
| 2 | 1 | Gọi tên mã + ngành, một câu. Người xem vừa được mồi nên chịu nghe |
| 3 | 3 | Con số thứ nhất đến từ đâu — cơ chế, không phải nhận định |
| 4 | 3 | Con số thứ hai đến từ đâu |
| 5 | 2 | **Đặt câu hỏi đúng**: hai cái này cùng đúng thì điều gì phải xảy ra? |
| 6 | 3 | Giải thích khả năng 1 (lành tính) — kèm bằng chứng trong báo cáo |
| 7 | 3 | Giải thích khả năng 2 (đáng lo) — kèm bằng chứng |
| 8 | 3 | Cái gì phân biệt được hai khả năng đó. Nêu **chỉ số cần theo dõi** |
| 9 | 4 | Bối cảnh: ngành đang thế nào, mã này đứng đâu. Dồn 4 câu, nhịp nhanh |
| 10 | 3 | Chốt đối xứng: quay lại đúng hai con số mở bài, nhưng giờ người xem đọc được chúng |

## Bản đồ scene
| Dòng | Scene | Chuyển động |
| :-: | :-- | :-- |
| 1 | hero hai số | hai số hiện **cùng lúc**, đối xứng trái/phải, khác màu |
| 3-4 | `perf-compare` | hai cột chạy **ngược chiều nhau** — đây là hình chủ đạo của góc |
| 5 | `flow-diagram` | hai nhánh tách ra từ một điểm |
| 6-7 | `risk-cards-container` | thẻ lành tính (xanh) / thẻ đáng lo (hổ phách) lật lần lượt |
| 8 | `speed-gauge` ⭐ chưa dùng lần nào | kim chỉ vào vùng cần theo dõi |
| 10 | `glowing-conclusion` | hai số mở bài quay lại, nối bằng một đường sáng |

## Bẫy
- **Đừng phán khả năng nào đúng.** Góc này mạnh vì để ngỏ. Chốt "đây là dấu hiệu xấu"
  là vừa vi phạm luật cấm khuyến nghị, vừa làm hỏng sức căng.
- Hai số phải **kiểm chứng được trong hồ sơ**, ghi rõ kỳ nào. Số sai là hỏng cả bài.
- Dòng 1 và dòng 2 mỗi dòng chỉ 1 câu ⇒ slide 1-2 chỉ có 1 `.slide-element`.
  Đừng dựng slide 3 phần tử rồi thắc mắc vì sao `validate_mapping` FAIL.
