---
description: Nghi thức ĐẦU PHIÊN video/ — đọc HANDOFF, nhận việc chờ
argument-hint: [việc BOSS muốn làm, để trống nếu chỉ muốn xem trạng thái]
---
Thực hiện nghi thức đầu phiên cho dự án con `video/`:

1. Đọc `HANDOFF.md` của video/ (đủ cả file — hook đầu phiên chỉ nạp 2 khoang sống).
2. Tóm tắt cho BOSS: trạng thái hiện tại + danh sách việc chờ theo thứ tự ưu tiên
   (ghi rõ nguồn ở mục nào trong HANDOFF).
3. Nhắc lại 2 luật sống còn trước khi làm: **AI KHÔNG NGHE ĐƯỢC** (mọi phán xét giọng
   để BOSS nghe) và **đầu ra ảnh phải MỞ RA SOI** (không tin exit code).
4. Nếu BOSS đã nêu việc cụ thể bên dưới: tra `../tri_thuc/kinh_nghiem.md` nhóm bẫy
   liên quan (video/render/TTS), đọc `video/README.md` nếu đụng định dạng kịch bản,
   rồi xác nhận lại cách hiểu việc với BOSS trước khi bắt tay làm.

Việc BOSS giao (nếu có): $ARGUMENTS
