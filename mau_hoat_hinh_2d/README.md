# Mẫu video hoạt hình 2D kể chuyện (BOSS duyệt 24/10/2026)

Video gốc: hướng dẫn web đèn xanh "Mua rẻ, tránh của rẻ mà ôi" bản 13 (8 phút 47 giây, 1080×1920).
Thành phẩm: `thanh_pham/kynang/huongdan_denxanh_nhap13/`. Nguồn sống + lịch sử 13 bản:
`Research copy/web_gooddeal/denxanh_huongdan/video_hd9/` và sổ `../LAM_TIEP.md`.

## Kiểu hình BOSS chọn
- Nền kem `#FBF5EA`, xanh thương hiệu `#0E6B53`, san hô `#F0654A`, phông Be Vietnam Pro.
- Nhân vật dẫn chuyện SVG phẳng (đầu tròn, áo xanh cổ V), 2 tay, đổi tư thế theo biểu cảm:
  `chi` trình bày · `nghi` chống cằm · `ngac` 2 tay giơ · `lo` = ảnh "Tiếng thét" (Sol vẽ, `hinh/nv_thet.png`).
- Thẻ trắng bo góc, dấu đỏ "đập", nhãn vàng kiểu giấy ghim, vòng tròn đỏ đếm số, phụ đề chạy từng chữ.
- Logo góc phải = `dungladu.vn`; cảnh cuối là nút `dungladu.vn`.

## Máy (thư mục `may/`, chạy trong thư mục chứa trang HTML)
1. Lời: tệp `Cxx|câu. câu.` (xem `loi_mau.txt`). Mã cổ phiếu viết theo cách đọc ("Ét Xi Ét"), bảng `DOC` trong HTML đổi lại thành chữ mã trên phụ đề. Tiền đọc kiểu người Việt ("một tỷ bảy trăm bốn mươi hai triệu").
2. Giọng: `uv run --no-project --with edge-tts python tieng_tu.py loi.txt` → `nhip.json` (mốc từng chữ) + `tieng/giong.wav`. Giọng NamMinh +14 % (free).
3. Hình: `phim2d_mau.html` — mỗi cảnh 1 khối `canh('Cxx', html)`; hẹn giờ bằng `T(câu, giây)` hoặc `moc('Cxx', câu, 'chữ')` bám đúng chữ đang đọc. Cảnh chèn giữa đặt tên `C15a`, `C15a2` (sắp theo chữ cái).
4. Soi trước: `TRANG=x.html python3 quay3d.py --anh soi t1 t2 …` → mở PNG soi (exit 0 không chứng minh hình đúng).
5. Quay: `TRANG=x.html python3 quay3d.py khung` (Mac M1 ~0,045 giây/khung, 9 phút video ≈ 10 phút).
6. Tiếng động + nhạc: `uv run --no-project --with numpy --with scipy python am_thanh2.py` (đọc `su_kien.json`).
7. Ghép: `ffmpeg -framerate 24 -i khung/%06d.jpg -i tieng/tron2.wav -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart ra.mp4`.
8. Ảnh thật thẻ bát cơm: `chup_sang2.py` (thẻ dựng từ `denxanh/legos/batcom/view.ve`, DENXANH_KHACH=1, ghép vào khuôn trang sảnh, data-theme sáng).

## Hình minh hoạ dùng lại (`hinh/`)
| Tệp | Là gì |
|:--|:--|
| `nv_thet.png` + `.json` | Nhân vật gốc mặt "Tiếng thét", nền trong; `.json` = toạ độ khớp khung SVG 300×560 |
| `thien_nga.png` | Thiên nga đen phẳng (bẫy không ai thấy trước) |
| `goc_chi.png`, `goc_om.png` | Nhân vật gốc chụp từ SVG — mẫu đưa Sol khi cần tư thế mới |
| `to_sol1.png` | Bộ 4 tư thế toàn thân Sol vẽ (BOSS KHÔNG dùng: đổi tạo hình) |
| `de_thet.md`, `de_thien_nga.md` | Đề giao Sol vẽ |
Trong HTML còn vẽ sẵn (SVG): cá tươi→cá ôi (`CA`, `hoaOi`), tiệm phở (`PHO`), xe máy tay ga, máy bay (`MAYBAY`), cọc tiền 500.000 (`TIEN`), vi rút, kim cương, nhà máy, biểu đồ đường + vòng đếm %.

## Luật BOSS rút ra (24/10)
- Hình cần biểu cảm/chi tiết → giao GPT Sol vẽ (`codex exec -m gpt-5.6-sol -i mau.png`, nền `#00FF00` rồi tách nền), kèm ảnh nhân vật gốc, dặn giữ nguyên nét. Claude tự vẽ SVG biểu cảm bị chê xấu.
- Chỉ nêu SỰ THẬT có nguồn; không đưa số dự báo tiêu cực về doanh nghiệp (dễ bị kiện). Người mới bị khởi tố → "sai phạm", không "gian lận".
- Mỗi lượt sửa = bản số mới (`phim2d_vN.html`, `loi_vN.txt`), không sửa đè.
