# KẾ HOẠCH TỔNG THỂ — NHÁNH RENDER HEADLESS DETERMINISTIC (lập 24/07/2026)

**Giám đốc (Fable) lập sau khi tham vấn Codex CLI + Kimi K3 (Qwen chết key 401).**
Nguyên văn tham vấn: `scratchpad/thamvan_codex.md` + `thamvan_kimi.md` (đường dẫn scratchpad
phiên 24/07; đã chắt lọc hết vào đây — mất file gốc không sao).

## MỤC TIÊU
Trị dứt **giật 2-3s đầu** của dây chuyền escbase (gốc: quay real-time getDisplayMedia,
trình duyệt quá tải lúc khởi động → rớt frame nướng vào video; vá warmup đã thất bại,
xem HANDOFF). Chuẩn đầu ra: **nét như bản cũ (1080×1920 native) · nhẹ 15-25MB/90-100s ·
mượt từ frame 0 · render ≤5 phút/bài · timeline khớp audio tuyệt đối**.

## LUẬT SẮT CỦA NHÁNH
1. **KHÔNG SỬA BẤT KỲ FILE NÀO của dây chuyền cũ**: `auto_render.py`, `render_edgetts.py`,
   `generate_tts.py`, các deck cũ trong `slide/`, `capture_slides.py`… chỉ ĐỌC/IMPORT.
2. Mọi file mới nằm trong `escbase_template/headless/`. Deck thử = **BẢN COPY** của deck
   bài 05 vào `headless/deck_thu/` (sửa thoải mái app.js trong bản copy).
3. Rollback = xoá thư mục `headless/`. Không có bước nào chạm nhánh cũ.

## KIẾN TRÚC (chốt từ tham vấn — 2 chuyên gia đồng thuận trừ ghi chú ⚡)

### 1. Thời gian ảo: `renderAt(t)` tường minh (Codex), KHÔNG dùng CDP virtual time
- Viết state machine timeline từ `timing.json` (NGUỒN CHÂN LÝ DUY NHẤT cho cả reveal
  lẫn SFX — lệch 2 nguồn là bug sync phổ biến nhất): mốc t nào slide nào, reveal nào.
- Reveal CSS transition: commit style ẩn → add `.visible` → **ép reflow**
  (`getComputedStyle`/`offsetWidth`) → `document.getAnimations()` lấy transition →
  `pause()` → mỗi frame `currentTime = t − t_reveal`. GIỮ REFERENCE (transition xong
  có thể biến mất khỏi getAnimations). Lượng tử hóa mốc reveal về biên frame.
- Canvas particles: viết lại `tick()` trong app.js (bản copy) thành hàm thuần theo t
  tuyệt đối, mô phỏng bước vật lý CỐ ĐỊNH độc lập fps đầu ra. `Math.random()` →
  PRNG seed theo `hash(slideIndex, revealIndex, particleIndex)` (không phụ thuộc
  thứ tự gọi).
- Trước frame 0: `await document.fonts.ready` + decode hết asset; asset phải local
  (fetch treo trong lúc render từng frame).

### 2. Capture (Kimi): CDP `Page.captureScreenshot` JPEG q95 + `optimizeForSpeed`
- Playwright headless, viewport 390×693 + `device_scale_factor=2.769230769230769`
  (đúng công thức NÉT của nhánh cũ → ra 1080×1918 native, pad 1920 sau).
- Mỗi frame: `renderAt(t)` → chờ 1 rAF (chống trả surface cũ) → capture → pipe
  base64→bytes vào **ffmpeg stdin** (`-f image2pipe -vcodec mjpeg`), x264 nén song song.
  KHÔNG ghi 3000 PNG rời. Chú ý backpressure (drain stdin, kẻo EPIPE ở frame ~2500).
- `N = ceil(D_audio × fps)` với D đo từ SỐ SAMPLE THẬT của voiceover (decode WAV mà
  đếm — MP3 có encoder delay ~25-50ms, đừng tin header).
- ⚡ Codex cảnh báo JPEG+H.264 = 2 lần lossy → bước nghiệm thu PHẢI zoom 400-800%
  soi chữ mảnh; nếu nhoè thì nâng q hoặc đổi PNG cho frame tĩnh.

### 3. Encode: 30fps · `libx264 -crf 18 -preset medium` · `yuv420p` · **BT.709 tv-range**
- (screenshot là RGB full-range — không ép tv-range + tag BT.709 là đen bạc màu trên
  mobile). `-g 60 -movflags +faststart`, AAC 128k/48kHz. ⚡ preset slow đo thử sau, không chặn.

### 4. Audio trộn OFFLINE toàn bộ (bỏ hẳn thu WebAudio real-time)
- Voiceover = master thời lượng. Nhạc nền: `-stream_loop -1` + `atrim` tường minh
  (KHÔNG dựa `-shortest`). SFX reveal: đặt tại các mốc t của timeline bằng
  `adelay=<ms>:all=1` (decode WAV trước). Mọi input `asetpts=PTS-STARTPTS` + 48kHz.
- `amix` **BẮT BUỘC `normalize=0`** (bẫy volume pumping đã trả giá ở nhánh cũ) →
  `alimiter=0.95` cuối. Mức đích: mean ~−17dB như bộ đã duyệt.
- SFX reveal lấy đâu: v1 dùng file tick có sẵn trong `state/tieng_tach/` hoặc tổng hợp
  1 tiếng tick ngắn bằng ffmpeg sine — KHÔNG chặn; thiếu SFX vẫn nghiệm thu được.

## NGHIỆM THU (đo bằng máy, 0 API — trước khi trình BOSS)
1. **Thời lượng**: |video − voiceover| ≤ 1 frame (nhánh cũ lệch +0,49…0,71s).
2. **Hụt khung**: phép đo chuẩn của dự án — max độ sáng dải 200px sát mép phải > 2
   ở 5 mốc rải đều (HANDOFF mục 📍).
3. **Determinism**: render 2 lần, hash-compare 10 frame mẫu — phải TRÙNG.
4. **Nét**: trích frame có chữ nhỏ, zoom soi, Read đối chiếu frame cùng cảnh của
   `escbase_05_skill.mp4` cũ.
5. **Mượt frame 0**: trích frame 0/0.5/1/1.5/2/2.5/3s — chuyển động particles phải
   liên tục (nhánh cũ rớt frame đoạn này). Phán quyết mượt CUỐI CÙNG là của BOSS.
6. **Số đo**: thời gian render, cỡ file, volumedetect ghi vào báo cáo.

## PHÂN CÔNG
- **Thợ 2 (subagent)**: dựng toàn bộ code trong `headless/` + deck_thu + chạy thử
  ĐOẠN NGẮN (5-10s đầu) để tự kiểm. KHÔNG render cả bài trong phiên subagent
  (bẫy render mồ côi 24/07).
- **Thợ 1 / phiên chính**: render cả bài chạy NỀN + đo nghiệm thu + trình BOSS.
- **BOSS**: nghe/xem bản thử bài 05 headless, phán mượt/giật — AI không tự phán.

## VIỆC SAU KHI BOSS DUYỆT (chưa làm)
- Áp bộ vá deterministic cho các deck còn lại (script tự vá app.js từng deck).
- Đo thử preset slow vs medium; cân nhắc 2 worker chia dải frame nếu cần nhanh hơn.
- Ghi sổ: patch_history + kinh_nghiem + HANDOFF trỏ về nhánh này.
