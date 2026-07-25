---
ten: Hố voi
ma: ho_voi
nhip: [1, 2, 3, 2, 3, 3, 3, 3, 3, 4]
---

# GÓC "HỐ VOI" — rơi sâu rồi, câu hỏi là rơi vì cái gì

**Tổng reveal 27 · mở vừa phải, dồn 4 câu ở dòng 10 để chốt mạnh.**

## Dùng khi
Giá đã **điều chỉnh sâu** và skill `/bat-day` có tín hiệu (CWI, chạm dải dưới Bollinger
tháng). Góc này KHÔNG phải để hô mua — nó tách **"rơi vì thị trường"** khỏi
**"rơi vì doanh nghiệp"**, đúng triết lý *hố voi trên con đường mua doanh nghiệp tốt*.

## 11 từ đầu
Nói **độ sâu** trước, tên mã sau.
Công thức: `Giảm {X} phần trăm trong {N} tháng. Câu hỏi không phải bao nhiêu.`

Ví dụ khuôn:
> *"Mất {X} phần trăm trong {N} tháng. Câu hỏi là mất vì cái gì."*

❌ Sai: "cơ hội", "bắt đáy", "giá hời" ở dòng 1 — vừa là `CAM_KHUYEN`, vừa đốt sạch
sức căng của cả bài.

## Nhịp kể từng dòng
| Dòng | Câu | Vai |
| :-: | :-: | :-- |
| 1 | 1 | **Độ sâu.** Một con số phần trăm, một khoảng thời gian |
| 2 | 2 | Mã nào. Ngành nào. Cả ngành cùng rơi hay chỉ mình nó |
| 3 | 3 | Ẩn dụ hố voi: đường vẫn đúng, hố là chuyện của mặt đường hay của cái xe |
| 4 | 2 | Đặt câu hỏi phân loại: cái gì đổi — giá, hay khả năng kiếm tiền |
| 5 | 3 | **Số liệu kinh doanh** trong đúng kỳ giá rơi. Doanh thu, biên, dòng tiền |
| 6 | 3 | Cái gì trong doanh nghiệp thực sự xấu đi. Nói thẳng, có số |
| 7 | 3 | Cái gì không đổi: tài sản, vị thế, tệp khách |
| 8 | 3 | So sánh nhịp rơi của mã với nhịp rơi của ngành/thị trường |
| 9 | 3 | Điều kiện để hố lấp lại — cái gì phải xảy ra, không phải "khi nào" |
| 10 | **4** | Chốt: hố sâu bao nhiêu **không** trả lời được câu hỏi nào; thứ trả lời được là gì |

## Bản đồ scene
| Dòng | Scene | Chuyển động |
| :-: | :-- | :-- |
| 1 | hero độ sâu | đường cong rơi vẽ từ trái sang, dừng ở đáy |
| 3 | ẩn dụ hố | con đường thẳng, một hố ở giữa — **scene tự dựng, chưa có trong kho** |
| 5-6 | `perf-compare` | các cột kinh doanh **so cùng kỳ**, không so với giá |
| 7 | `core-module-grid` | các ô "không đổi" giữ nguyên sáng khi mọi thứ khác mờ đi |
| 8 | hai đường chồng | đường mã và đường ngành vẽ chồng, lệch nhau chỗ nào thì nhấn chỗ đó |
| 9 | `workflow-grid` | điều kiện lấp hố, đánh số |
| 10 | `glowing-conclusion` | hố mở bài quay lại, lần này có đèn soi xuống đáy |

## Bẫy
- **Tuyệt đối không kết luận nên mua.** Góc này chỉ phân loại nguyên nhân rơi. Ai đọc
  xong tự quyết. Một chữ "cơ hội" là thước chặn ngay.
- Không dùng dữ liệu giá cũ: chạy đủ **4 lệnh cập nhật giá** trước khi viết lời
  (`capnhat_gia` → `fireant_pull` → `q5_calc` → `gen_trang_dn`). Chạy thiếu là P/E đứng
  yên mà không cảnh báo gì.
- Ẩn dụ hố voi là **của bộ này**, đừng đổi sang "bắt dao rơi" hay ẩn dụ khác giữa chừng.
