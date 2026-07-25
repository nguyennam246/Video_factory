# Bộ video phân tích rủi ro

Ẩn dụ xuyên bộ: **đi xem nhà trước khi mua**. Mặt tiền chỉ là phần dễ thấy; người xem phải xuống hầm, soi đường ống, đọc giấy tờ và chưa được biến một dấu hiệu chưa xác nhận thành bản án.

| File | Hồ sơ nguồn | Trục rủi ro | Số cảnh | Ước số từ |
| :-- | :-- | :-- | --: | --: |
| `ruiro_01_TCL.md` | `TCL_HoSo.md` | T5 phải thu bên liên quan; N17 cam kết thuê ngoài bảng; N10 bẫy lợi nhuận đỉnh chu kỳ | 15 | 391 |
| `ruiro_02_SKV.md` | `SKV_HoSo.md` | N4 phụ thuộc công ty mẹ; N11 cỗ máy bị điều tiết; T5 giao dịch bên liên quan, nhưng chưa xác nhận bản chất chiếm dụng vốn | 15 | 386 |
| `ruiro_03_MCF.md` | `MCF_HoSo.md` | N2 dòng tiền âm một năm đang tranh chấp, thuộc diện chờ soi và không tính là rủi ro | 15 | 357 |

Đối chiếu số liệu: mọi số, tỷ lệ, tên khoản mục và trạng thái hội tụ/tranh chấp dùng trong lời đều lấy từ mục ①, ② hoặc ③ của hồ sơ tương ứng. Không phát hiện mâu thuẫn phải xử lý và không thêm số do tự tính.

Kiểm parser `--loi`: cả 3 file đều thoát với mã 0 và in đủ 15 đoạn lời. Kiểm tĩnh: mỗi cảnh có đúng một dòng `LỜI:`, không có dấu `—` trong lời, không có dòng `CHỮ/CHỮ*` dài quá 34 ký tự, và mỗi bài nằm trong khoảng 330–420 từ.

KETLUAN|3|45|3
