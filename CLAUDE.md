# CHỈ DẪN CHO CLAUDE — DỰ ÁN CON `video/` (lập 23/07/2026)

**Điểm vào duy nhất: đọc `video/HANDOFF.md` TRƯỚC khi làm bất kỳ việc gì.**
Luật gốc repo (CLAUDE.md gốc) vẫn áp dụng; file này chỉ thêm luật RIÊNG của video.
Cách chạy + định dạng file kịch bản: `video/README.md`.

**BOSS** = người dùng / chủ dự án. Mục đích: bộ video ngắn dạy **Claude Code**,
tiếng Việt, dọc 9:16 — *"chỉ xem video là hiểu vấn đề và làm được, chia sẻ lại được."*

## LUẬT RIÊNG VIDEO (đúc từ bẫy đã trả giá — chi tiết trong HANDOFF)
1. **AI KHÔNG NGHE ĐƯỢC.** Không nghe được file mình tạo, không mở được video mạng
   xã hội. Mọi phán xét *giọng hay dở / đọc sai dấu / nhịp / mức nhạc* BẮT BUỘC để
   BOSS nghe rồi phán. CẤM viết "giọng nghe tự nhiên" — đó là bịa. Cách đúng: dựng
   bài thử nhiều phương án cho BOSS chọn (khuôn: `kichban/00*_thu_giong.md`).
2. **Đầu ra là ẢNH/VIDEO thì phải MỞ RA SOI.** Exit 0 không có nghĩa slide đúng
   (đã từng render sạch mà dòng lệnh ngắt làm đôi). `Read` file PNG / soi mắt frame
   trước khi báo xong.
3. **Giọng ĐÃ CHỐT — 2 chuẩn theo dây chuyền:** Pillow (`lam_video.py`):
   `edge:vi-VN-NamMinhNeural:+14%` + `NGHỈ: 0.9` (BOSS duyệt 2 vòng 20 giọng); escbase:
   ElevenLabs **"Nhật - Narrative & Compelling"** qua `config/tts.json` (BOSS duyệt 23/07
   đêm). KHÔNG tự đổi giọng/tốc độ/nghỉ — muốn đổi thì dựng bài thử cho BOSS.
4. **Kịch bản viết theo khuôn 7 nhịp** (HANDOFF mục ⭐ CÔNG THỨC — phần trả giá đắt
   nhất dự án): cảnh đời thường trước, ẩn dụ sờ được trước tên kỹ thuật, ví dụ THẬT
   có số, đi chậm qua 1 lần chạy thử, câu chốt đối xứng. Ẩn dụ "người thợ mới mỗi
   sáng" xuyên suốt cả bộ — đừng đổi. BOSS chốt: *"không cần làm quá ngắn — đúng là
   đủ"* (bài dạy 100-165 giây là bình thường).
5. **Render cả bộ → CHẠY NỀN.** 1 bài ~2-4 phút; quá 10 phút là Bash tool cắt.
6. **Tiền API:** edge-tts free vô hạn — render thoải mái. Gemini TTS ~11-12 lượt/key/
   ngày — hỏi BOSS trước khi chạy lô. Cache TTS `state/video_tts/` theo hash: sửa
   slide render lại = 0 lượt API; ĐỪNG xoá cache.
7. **Đo rồi thì đừng đoán lại.** Bảng ĐO THẬT trong HANDOFF (thời gian render, hạn
   mức TTS, cỡ file) là số đo có ngày — tra trước, chỉ đo lại khi nghi đã đổi.

## NGHI THỨC (hook trong `video/.claude/` tự nhắc khi mở phiên tại video/)
- **Đầu phiên:** hook `nap_handoff.py` tự nạp 2 khoang sống của `video/HANDOFF.md`
  (📍 TRẠNG THÁI + 🎯 ĐANG THI CÔNG DỞ). Còn lại tự đọc khi cần — kỷ luật token.
- **Cuối phiên:** 4 sổ ghi VỀ GỐC repo (không mở sổ riêng, tránh tri thức phân mảnh):
  `../tri_thuc/patch_history.md` (mục mới LÊN ĐẦU) · `../tri_thuc/kinh_nghiem.md`
  (bẫy, kèm ngày) · cập nhật `video/HANDOFF.md` (trạng thái + việc chờ, giữ GỌN) ·
  sửa `lam_video.py`/định dạng kịch bản → cập nhật `video/README.md`.
- Hook `nhac_nghi_thuc.py` chặn 1 lần lúc Stop nếu sửa `.py`/`.sh` mà chưa ghi sổ.
- Hook khóa dữ liệu thô của repo gốc vẫn hiệu lực (gọi xuyên lên `../.claude/hooks/`).
- Thước hook 0 API: `python3 video/.claude/hooks/_thu_hook.py` — chạy sau khi sửa
  hook hoặc đổi khung HANDOFF.

## BẢN ĐỒ (gọn)
| Đường dẫn | Là gì |
| :-- | :-- |
| `video/HANDOFF.md` | Trạng thái + việc chờ + công thức kịch bản — ĐIỂM VÀO |
| `video/lam_video.py` | Dây chuyền kịch bản → mp4 (neo `BASE_DIR` = gốc repo) |
| `video/kichban/` | 10 bài dạy + truyện + bài thử giọng |
| `video/escbase_template/` | Template mua 199k (dây chuyền HTML/CSS thay Pillow — đang thử) |
| `video/README.md` | Cách chạy + định dạng kịch bản đầy đủ |
| **`video/thanh_pham/`** | ⭐ **CHỖ CỐ ĐỊNH BOSS TÌM VIDEO** (BOSS chốt 25/07/2026): `baocao/` video mã CP · `kynang/` video dạy. Nghiệm thu xong là copy về đây + ghi 1 dòng README |
| `../results/video/` | Bãi làm việc: bản render thô/nháp (gitignore — dựng lại được). **KHÔNG bảo BOSS tìm video ở đây** |
| `../state/video_tts/` · `../state/tieng_tach/` | Cache giọng · tiếng cắt từ CapCut (gitignore) |
| `video/key.rtf` | Key tay của BOSS — ĐÃ gitignore, KHÔNG commit, không đọc to ra chat |

Phụ thuộc ngoài: `ffmpeg` (brew) · `Pillow` + `edge-tts` (`.venv` gốc repo) · font macOS
có sẵn (`Arial Unicode.ttf` + `Menlo.ttc`).
