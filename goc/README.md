# THƯ VIỆN GÓC TIẾP CẬN (lập 25/07/2026)

**Vấn đề nó giải:** trước ngày này, mọi bài tài chính bị ép chung một nhịp thở —
`KHUON = [1,2,3,3,3,3,2,2,3,3]` là hằng số cứng trong thước. MSR, HPD, TCL, SKV, MCF
kể chuyện gì cũng phải nhét vừa một cái khung. Xem 3 bài liền là thấy "cùng một khuôn".

**Sự thật kỹ thuật:** engine escbase chỉ ép ĐÚNG MỘT điều (`auto_render.py:951`):

> số câu của dòng N **phải bằng** số `.slide-element` của slide N

Nó KHÔNG quan tâm khuôn là gì, KHÔNG bắt phải 10 dòng. Cái khuôn cứng là **ta tự trói**
để tái dùng deck cho nhanh. Thư viện này cởi trói mà không phá ràng buộc kỹ thuật.

---

## Dùng thế nào

```bash
# 1. Chọn góc: Opus đọc hồ sơ + Q8 (valuation-check) + Q9 (devil-advocate) rồi chọn
# 2. Chạy runner với góc đó
python3 video/lam_bai.py --ma msr02 --ten danhgia --loai baocao --goc nghich_ly_so

# Thước kiểm kịch bản theo nhịp của góc (không còn hằng số cứng):
python3 video/.claude/skills/video-baocao/thuoc/thuoc_kichban.py <lời.txt> --goc nghich_ly_so
```

Không truyền `--goc` thì thước quay về khuôn cũ — bài cũ vẫn chạy được.

---

## BA TẦNG RÀNG BUỘC — đừng lẫn

| Tầng | Gồm | Xử lý |
| :-- | :-- | :-- |
| **Kỹ thuật** — vỡ là video hỏng | số câu = số reveal · ≤55 từ/dòng · không dấu `—` · safezone | **giữ tuyệt đối** |
| **Chất lượng** — bỏ là bài dở | 11 từ đầu phải có mất mát · cấm mở bài yếu · cấm từ rỗng · cấm thuật ngữ trước ẩn dụ · trần từ theo nhịp 3,56 từ/giây | **giữ — đây mới là "kỹ thuật hấp dẫn"** |
| **Khuôn cứng** | `đúng 10 dòng` · `số câu phải bằng đúng KHUON` | **đã bỏ, thay bằng góc** |

---

## 🔴 LUẬT CẤM VẪN NGUYÊN GIÁ TRỊ

Góc là để **hấp dẫn**, KHÔNG phải để giật gân. Với bài tài chính, mọi góc vẫn chịu:

- **Cấm kết luận đắt/rẻ, cấm khuyến nghị mua bán** dưới mọi hình thức (`CAM_KHUYEN`).
- **Cấm ngôn ngữ dọa dẫm** (`CAM_DOA`).
- **Cấm ngôn ngữ hệ thống nội bộ** (`CAM_HE_THONG`).

Sức hút phải đến từ **nghịch lý có thật trong số liệu**, không phải từ tính từ mạnh.
Nghịch lý số liệu hấp dẫn hơn giật gân, vì nó để người xem tự đi tới kết luận —
và đó cũng là cách duy nhất vừa hút vừa không hứa hẹn gì.

---

## Chọn góc thế nào

Opus đọc hồ sơ + Q8 + Q9, rồi hỏi: **"Điều gây bất ngờ nhất ở mã này là gì?"**
Câu trả lời rơi vào ô nào thì lấy góc đó.

| Điều bất ngờ nhất là… | Góc |
| :-- | :-- |
| Hai con số đáng lẽ đi cùng nhau lại ngược nhau | `nghich_ly_so` |
| Giá đang ngầm giả định một điều khó xảy ra | `gia_da_tinh_san` |
| Có một thứ đủ sức chấm dứt cuộc chơi | `thu_giet_dn` |
| Vừa rơi rất sâu, câu hỏi là rơi vì cái gì | `ho_voi` |
| Lời kể và con số trong báo cáo không khớp | `bang_chung` |
| Ngành/chu kỳ đang ở khúc nào của vòng đời | `dong_ho_chay` |

Hai mã liền nhau **không được cùng góc**. Ghi góc đã dùng vào `NHAT_KY.md` cùng thư mục.

---

## Thêm góc mới

Chép một file `.md` sẵn có, sửa header rồi viết lại 5 mục. Header máy đọc:

```
---
ten: <tên tiếng Việt>
ma: <slug_khong_dau>
nhip: [1, 1, 3, 3, 2, 3, 3, 3, 4, 3]
---
```

`nhip` = số câu từng dòng = số `.slide-element` từng slide. Tổng reveal nên nằm
khoảng 24-30; tổng từ 300-380 (bài tài chính) để ra 85-107 giây ở nhịp 3,56 từ/giây.
