---
ten: Cái giá đã tính sẵn điều gì
ma: gia_da_tinh_san
nhip: [1, 2, 2, 4, 3, 3, 3, 2, 3, 3]
---

# GÓC "CÁI GIÁ ĐÃ TÍNH SẴN ĐIỀU GÌ" — đọc ngược từ thị giá ra giả định

**Tổng reveal 26 · dòng 4 dồn 4 câu (chỗ nặng nhất: bóc giả định), sau đó thưa dần.**

## Dùng khi
Q8 (`/valuation-check`) cho thấy **thị giá chỉ hợp lý nếu một điều kiện khó xảy ra**:
tăng trưởng phải giữ ở mức lịch sử chưa từng có · biên phải không co · một mảng mới
phải thành công. Góc này biến định giá khô khan thành câu chuyện có kịch tính,
**mà không cần nói đắt hay rẻ**.

## 11 từ đầu
Nói thẳng **cái giá thị trường đang đòi**, dưới dạng điều kiện.
Công thức: `Ở mức giá này, {mã} phải làm được {điều X} trong {N} năm.`

Ví dụ khuôn:
> *"Giá hôm nay đòi mã này tăng trưởng {X} phần trăm, suốt năm năm."*

❌ Sai: bất kỳ câu nào chứa "đắt", "rẻ", "hấp dẫn", "cơ hội".

## Nhịp kể từng dòng
| Dòng | Câu | Vai |
| :-: | :-: | :-- |
| 1 | 1 | **Điều kiện thị trường đang đòi.** Một câu, một con số |
| 2 | 2 | Vì sao đọc ngược được: giá là tổng của các kỳ vọng. Nói bằng ẩn dụ, chưa dùng chữ "chiết khấu" |
| 3 | 2 | Mã này là ai, làm gì ra tiền |
| 4 | **4** | **Bóc giả định**: giá hiện tại ngầm giả định 3-4 điều. Liệt kê từng điều một |
| 5 | 3 | Điều nào trong đó có bằng chứng ủng hộ — dẫn số thật từ hồ sơ |
| 6 | 3 | Điều nào chưa có bằng chứng |
| 7 | 3 | Lịch sử: doanh nghiệp đã từng làm được mức đó chưa. Ngành có ai làm được chưa |
| 8 | 2 | Nếu một giả định trượt thì phần nào của giá mất đi |
| 9 | 3 | Cái cần theo dõi để biết giả định đang đúng hay trượt |
| 10 | 3 | Chốt đối xứng: lặp lại điều kiện mở bài, thêm câu "con số đó đã có trong giá rồi" |

## Bản đồ scene
| Dòng | Scene | Chuyển động |
| :-: | :-- | :-- |
| 1 | hero điều kiện | con số điều kiện hiện lớn giữa khung, nhịp đập chậm |
| 2 | `flow-diagram` | giá tách ngược thành các mảnh kỳ vọng — **chạy ngược chiều mũi tên** |
| 4 | `core-module-grid` | 4 ô giả định bật sáng lần lượt, ô cuối để trống màu |
| 5-6 | `risk-cards-container` | ô có bằng chứng đóng dấu xanh, ô chưa có để xám |
| 7 | `perf-compare` | cột "đã từng đạt" vs cột "giá đang đòi" |
| 8 | lớp bóc | thanh giá bị bóc mất một tầng khi giả định tắt |
| 10 | `glowing-conclusion` | điều kiện mở bài quay lại |

## Bẫy
- **Ranh giới mỏng nhất của cả thư viện.** "Giá đang đòi X" là mô tả; "giá quá cao"
  là khuyến nghị. Chỉ được ở vế đầu. Đọc lại `CAM_KHUYEN` trước khi nộp.
- Giả định phải lấy từ Q8 đã chạy, **không tự bịa mô hình mới trong lúc viết lời**.
- Dòng 4 có 4 câu ⇒ slide 4 phải có đúng 4 `.slide-element`, và 4 phần tử đó phải
  **vừa safezone** — đây là slide dễ tràn nhất của góc này.
