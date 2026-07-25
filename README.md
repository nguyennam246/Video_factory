# KỊCH BẢN VIDEO HƯỚNG DẪN CLAUDE CODE (BOSS duyệt 23/07/2026)

Bộ 10 video dọc 9:16 (xem trên điện thoại), mỗi bài ~60-90 giây, tiếng Việt.
Mục tiêu BOSS đặt: *"chỉ xem video là hiểu vấn đề và làm được, chia sẻ lại được."*

**Trạng thái + việc chờ: `video/HANDOFF.md`.** File này chỉ dạy cách chạy.

## ⭐ Làm một bài bằng MỘT lệnh (dây chuyền escbase headless — đường chính từ 24/07)
```bash
python3 video/lam_bai.py --ma msr02 --ten danhgia --loai baocao --goc nghich_ly_so
```
9 bước theo đúng thứ tự, **tự dừng ở cổng chặn** thay vì chạy tiếp rồi hỏng ở cuối:

| Bước | Loại | Việc |
| :-: | :-- | :-- |
| 1 | THỢ (opus) | viết kịch bản 10 dòng đúng khuôn |
| 2 | THỢ (sonnet) | sửa `index.html`: thay chữ + THAY SCENE |
| 3 | MÁY | `sync_script` + **đối chiếu số câu với khuôn** ← cổng |
| 4 | MÁY | sinh giọng edge NamMinh `+14%` |
| 5 | MÁY | `remap_palette` (chỉ 1 lần — lần 2 ra deck lai màu) |
| 6 | MÁY | `validate_slide --semantic-report` ← cổng |
| 7 | MÁY→THỢ 1 | chụp 10 PNG rồi **DỪNG chờ soi mắt** ← cổng |
| 8 | MÁY | `render_headless` (~3 phút) → copy vào `results/video/` (bãi làm việc) |
| 9 | MÁY | nghiệm thu 6 phép đo → **copy bản cuối vào `thanh_pham/`** → dừng chờ BOSS nghe |

Mã thoát: `10` thước FAIL · `20` thợ 2 hết quota (đọc `<deck>/_VIEC_CHO_THO1.md`, tự làm nốt) ·
`30` chờ soi ảnh · `40` chờ BOSS. Chạy tiếp: `--tu-buoc <n>`.

**`--goc` quyết định NHỊP KỂ của bài** — mỗi mã một góc khác nhau thì mỗi bài một nhịp khác
nhau. Không truyền thì về khuôn mặc định (mọi bài cùng nhịp — chính là cái làm bộ cũ trông
giống nhau). Danh sách góc + cách chọn: `video/goc/README.md`. Nhật ký + kỷ luật đẻ scene
mới: `video/goc/NHAT_KY.md`.

🆕 **`--nghe` quyết định CÁCH GIỮ MẮT** (25/07) — hai trục độc lập với `--goc`:

```bash
python3 video/lam_bai.py --ma sp09 --ten dieu_phoi --loai kynang \
        --goc <mã góc>      # kể chuyện gì  → ra nhịp
        --nghe <mã hook>    # giữ mắt cách nào → ra kiểu mở bài + 4 luật
```

Nêu `--nghe` thì runner nhét luật giữ mắt vào đề bài giao thợ 2 và **thêm một cổng chặn ở
bước 3**. Thư viện: `video/nghe/` — 10 kiểu hook, hai mốc rơi tính ra từ nhịp đọc 3,56
từ/giây (mốc 1 ở **dòng 2**, mốc 2 ở **dòng 5-7**), nhịp ngắt mẫu, câu đáng chụp màn hình,
trần ý mới. Sổ chống lặp: `video/nghe/NHAT_KY.md` (2 bài liền không cùng kiểu hook).

Thước riêng, 0 API, ba chế độ:
```bash
T=video/.claude/skills/video-kynang/thuoc/thuoc_nghe.py
python3 $T <lời.txt> <README_slug.md> --thuatngu "a,b"   # đo kịch bản + khai báo
python3 $T --trung <deck_mới> <deck_trước>               # trùng scene, ngưỡng 60%
python3 $T --moc "1,3,3,2,3,3,3,3,3,3"                   # tính lại mốc rơi khi đổi nhịp
```
🆕⭐ **`--duong` quyết định ĐI ĐƯỜNG NÀO** (25/07, BOSS lệnh sau khi hỏi *"quy trình chuẩn rồi,
render cũng nhanh, sao tổng thể tốn thời gian thế?"*). Đo thật: **render KHÔNG tốn** (186,9s
máy chạy, 0 token). Tốn nằm ở 3 luật ta tự đặt.

```bash
# mặc định — mã MỚI / góc MỚI, chịu tốn để kho scene lớn thêm
python3 video/lam_bai.py --ma msr02 --ten danhgia --loai baocao --goc nghich_ly_so

# ⭐ bài LÀM LẠI / bài gấp / nhịp trùng deck cũ
python3 video/lam_bai.py --ma pnj03 --ten hanhdong --loai baocao \
        --goc viec_can_lam --duong re
```

| | `mo-duong` (mặc định) | `re` |
| :-- | :-- | :-- |
| Kịch bản (b1) | spawn **thợ 2 Opus nguội**, bảo nó "tự tra tài liệu trong repo" | **bàn giao thợ 1** — phiên chính đang giữ sẵn số liệu, spawn agent nguội là trả tiền hai lần |
| Deck (b2) | spawn Sonnet + **bắt đẻ ≥1 scene mới** + tra catalogue **bằng ảnh** (12 MB/18 ảnh) | **bàn giao thợ 1**, chép deck đã ra video thật, **chỉ thay chữ**, 0 scene mới |
| Mẫu (`--mau`) | `deck_thu` | **tự chọn** deck trong `DECK_DA_GO_LOI` có nhịp **trùng** nhịp bài. Không có deck khớp ⇒ **dừng, gợi ý 3 cách sửa** |
| Soi ảnh (b7) | liệt kê 10 PNG để `Read` từng cái | `contact_sheet.py` ghép 1 tấm ⇒ **LƯỚT 1 lượt → ZOOM slide đáng ngờ** |
| Palette (b5) | luôn chạy `remap_palette` | đo `style.css` còn mã nào **cần đổi thật** không; 0 thì đặt `_DA_REMAP` để bỏ qua |

🔴 **Đường rẻ KHÔNG cắt cổng chặn nào** — thước kịch bản (b3), `validate` (b6), soi ảnh (b7)
vẫn đủ. Nó chỉ đổi **ai làm** và **thứ tự soi**. Đánh đổi thật: 0 scene mới ⇒ kho scene không
lớn thêm, bài trùng nhịp bài cũ.

**Đảo chiều quan trọng:** đường rẻ bắt **viết lời VỪA nhịp deck sẵn có**, thay vì bẻ deck cho
vừa lời. Deck lệch nhịp là runner chặn ngay, không đợi tới bước render.

Đo thật bài PNJ 02: **0 subagent · 0 scene mới · 2 lượt đọc ảnh** (thay 20-30) · thước kịch
bản ĐẠT ngay vòng 1 · 1 lỗi soi ảnh. Bài PNJ 01 cùng ngày đi đường mặc định: 2 subagent +
2 scene tự dựng + 4 lỗi chỉ soi ảnh mới thấy.

```bash
# contact sheet chạy riêng cũng được (tự đếm số slide, nhận tên deck hoặc đường dẫn)
cd video/escbase_template && .venv/bin/python contact_sheet.py deck_pnj02
```

Tham số khác: `--loai baocao` (khuôn tài chính + palette `tc`) · `--mau deck_XX` (ép deck mẫu) ·
`--lam-lai` (làm lại cả bước THỢ) · `--bo-qua-soi` (chỉ khi render lại y hệt).

## 🆕 Máy đọc sai mã CP / chữ tiếng Anh? — TỪ ĐIỂN PHÁT ÂM (25/07/2026)

BOSS nghe rồi chốt: **mã cổ phiếu = tên chữ cái kiểu Anh** (`PNJ` → "Pi En Giây") ·
**chữ tiếng Anh = viết theo âm Việt** (`superpower` → "su pơ pao ơ", `hook` → "húc").

⚠️ **Đừng viết cách đọc vào `script-90s.txt`** — phụ đề lấy đúng chuỗi đó, sẽ hiện
"Pi En Giây" thay vì "PNJ". Hai đường đã tách sẵn trong dây chuyền:

```
script-90s.txt ──┬──> timing.json["text"] ──> PHỤ ĐỀ      (giữ chữ GỐC)
                 └──> doc_am() ──> engine  ──> GIỌNG ĐỌC  (chữ đọc)
```

**Thêm từ = sửa JSON, không sửa code:** `escbase_template/tts/phat_am.json`
(nhóm `ma_cophieu` / `tieng_anh`). Khớp theo biên từ, không phân biệt hoa thường,
khoá dài thắng khoá ngắn.

```bash
cd video/escbase_template
.venv/bin/python tts/phat_am.py --kiem                            # thước 0 API, 11 ca
.venv/bin/python tts/phat_am.py "PNJ va hook trong Claude Code"   # thử 1 câu
```
Cache tiếng khoá theo **chữ đọc** ⇒ sửa từ điển là tự sinh lại giọng, không phải xoá cache tay.

**Muốn đổi kiểu đọc thì dựng bài thử cho BOSS nghe TRƯỚC** (AI không nghe được):
```bash
.venv/bin/python thu_phat_am.py ../kichban/00c_thu_phatam_ma_cp.txt ../thanh_pham/thu_am/thu.mp3
```

## 🆕 Video cắt phựt lúc dứt câu? — `TAIL_SECONDS` (25/07/2026)

BOSS: *"video hình như chưa hết mà đã dừng rồi"*. Đo: đuôi **0,024s**, 1 giây cuối vẫn còn
tiếng ở max **−4,8 dB**. Nay `TAIL_SECONDS = 1.4` giữ slide cuối thêm 1,4s.
Đặt ở `escbase_template/tts/common.py`; **vá cả 2 nhánh** (`tts/common.py` +
`split_voiceover.py`). Thước nghiệm thu có **cổng ⑦**: 0,8s cuối phải ≤ −45 dB.
⛔ Đừng nối im lặng vào mp4 sau render — lệch `timing.json`.

## 🔒 KHOÁ RENDER — một lúc chỉ MỘT tiến trình quay (BOSS lệnh 25/07)

Hai bản render chạy cùng lúc **làm hỏng output chứ không chỉ làm chậm**: main thread không
kịp thì timeline giãn ra (đo 23/07: hình 180,6s trong khi giọng 112,9s) và **không script nào
báo lỗi** — mp4 vẫn ra, vẫn exit 0, chỉ là hình lệch tiếng.

Khoá cắm **trong 3 script làm việc thật**, không cắm ở `lam_bai.py` — vì còn bị gọi tay:
`headless/render_headless.py` · `auto_render.py` · `capture_slides.py`.
KHÔNG khoá `validate_slide.py` / `dung_nhac_synth.py` (chạy vài giây, đo layout chứ không quay).

```bash
python3 video/khoa_render.py --kiem          # ai đang giữ khoá?
python3 video/khoa_render.py --viec "render tay" -- <lệnh>      # bọc 1 lệnh bất kỳ
python3 video/khoa_render.py --cho-khoa 600 --viec X -- <lệnh>  # xếp hàng, chờ tối đa 10 phút
```

Bị chặn thì mọi thứ thoát **mã 50** và `lam_bai.py` nói rõ *"deck KHÔNG hỏng, chỉ đang xếp
hàng"* — đừng nhầm với render lỗi rồi đi sửa deck.

Dùng `flock` của hệ điều hành, **tự nhả khi tiến trình chết** ⇒ không có chuyện file khoá cũ
chặn cả máy. `ps` không thay được: nó chỉ đúng vào đúng giây mình nhìn.

## Làm video từ file kịch bản (nhánh Pillow cũ — vẫn chạy được)
```bash
.venv/bin/python video/lam_video.py video/kichban/01_hooks.md
```
Ra `results/video/01_hooks.mp4` (1080×1920) — đó là **bãi làm việc**. Bản cuối nghiệm thu
xong phải copy về **`thanh_pham/`** (`baocao/` cho video mã CP · `kynang/` cho video dạy) —
đó là CHỖ CỐ ĐỊNH DUY NHẤT BOSS tìm video. Thêm `--canh 1-3` để render thử vài cảnh.

Dây chuyền: **0 đồng, không cần đăng ký gì.**
`Gemini TTS free` (giọng) + `Pillow` (slide chữ) + `ffmpeg` (ghép). Audio TTS được
**cache theo hash lời đọc** (`state/video_tts/`) — sửa slide rồi render lại KHÔNG gọi API lần nữa.

## Định dạng file kịch bản
```
TIÊU ĐỀ: Hooks — nguyên tắc là chữ, hook là rào
GIỌNG: Kore
---
LỜI: Câu người đọc nói ra. Xuống dòng không có tiền tố = nối tiếp câu trên.
CHỮ: dòng chữ thường trên màn hình
CHỮ*: dòng NHẤN (to hơn, màu xanh)
MÃ: dòng chữ đơn cách, màu cam — dùng cho lệnh/tên file
---
LỜI: ...
GIỌNG: Orus
KIỂU: Đọc chậm rãi, trầm ấm
```
- `---` ngăn cảnh. Mỗi cảnh = 1 slide + 1 đoạn giọng đọc.
- `LỜI:` bắt buộc (nội dung đọc). `CHỮ/CHỮ*/MÃ` tuỳ chọn, xếp theo thứ tự viết.
- `GIỌNG:` **trong** một cảnh = đổi giọng riêng cảnh đó (dùng cho bài thử giọng).
  `GIỌNG:` ở đầu file = giọng chung cả bài.
- `KIỂU:` = dặn lối đọc (chậm/trầm/vùng miền). **Không hiện trên màn hình, không đọc ra tiếng.**
- `TIẾNG: <đường dẫn>` = dùng **file tiếng có sẵn** cho cảnh đó, bỏ qua mọi engine TTS.
  Nhận `.mp3 .m4a .wav .aac`… Đây là cửa để dùng **CapCut · ElevenLabs · Vbee · giọng BOSS tự đọc**.

## Dùng giọng từ tool GUI (CapCut "Thanh niên tự tin", ElevenLabs…)
CapCut không có API. Nhưng **chỉ cần dán 1 lần, xuất 1 file** — máy tự cắt ra từng cảnh.

**Bước 1 — lấy lời đọc:**
```bash
.venv/bin/python video/lam_video.py video/kichban/01_hooks.md --loi
```
**Bước 2 — dán vào CapCut** (app hoặc [bản web](https://www.capcut.com/vi-vn/tools/text-to-speech)),
⚠️ **mỗi cảnh một đoạn riêng, cách nhau một dòng trống** — chỗ CapCut nghỉ hơi giữa các đoạn
chính là chỗ máy sẽ cắt. Chọn giọng, xuất **audio only** ra 1 file duy nhất.

**Bước 3 — cắt tự động rồi render:**
```bash
.venv/bin/python video/lam_video.py video/kichban/01_hooks.md --tach-tieng ~/Downloads/capcut.mp3
.venv/bin/python video/lam_video.py video/kichban/01_hooks.md --tieng-thu-muc state/tieng_tach/01_hooks
```
Máy dò khoảng lặng, lấy N-1 chỗ nghỉ **dài nhất** làm ranh giới → đúng N mẩu. Thiếu chỗ nghỉ
thì nó báo lỗi và bảo dán lại, **không cắt bừa**. Muốn chỉ định tay 1 cảnh: dùng `TIẾNG:` trong
kịch bản (ưu tiên cao hơn `--tieng-thu-muc`).
- Lời đọc **cũng hiện làm phụ đề** dưới đáy → xem tắt tiếng vẫn hiểu.
- Giọng: `Kore` (chắc) · `Charon` (giảng giải) · `Puck` (tươi) · `Leda` (trẻ) — đổi ở dòng `GIỌNG:`.

## Danh sách bài
| # | File | Nội dung |
| :-- | :-- | :-- |
| 1 | `01_hooks.md` | Hook — luật thành rào chắn máy |
| 2 | `02_claude_md.md` | CLAUDE.md — trí nhớ dài hạn của dự án |
| 3 | `03_slash_command.md` | Slash command — đóng gói việc lặp lại |
| 4 | `04_subagent.md` | Subagent — chia việc, cô lập ngữ cảnh |
| 5 | `05_skill.md` | Skill — nghề tự bật đúng lúc |
| 6 | `06_mcp.md` | MCP — cắm công cụ ngoài vào Claude |
| 7 | `07_plan_mode.md` | Plan mode — bắt bàn bạc trước khi gõ |
| 8 | `08_checkpoint.md` | Checkpoint — quay ngược khi sửa hỏng |
| 9 | `09_context.md` | Ngữ cảnh & token — vì sao phiên dài thì đắt |
| 10 | `10_ket.md` | Ghép 9 mảnh thành một dây chuyền |

## Khóa Superpowers cho Codex

`kichban/superpowers/` có 8 bài, đi từ cài plugin tới brainstorming, worktree,
writing plans, TDD, thực thi–review, systematic debugging, kiểm chứng và bàn giao.
Xem lộ trình tại `kichban/superpowers/README.md`.

Ví dụ lấy lời bài đầu:

```bash
.venv/bin/python video/lam_video.py video/kichban/superpowers/01_tong_quan.md --loi
```
