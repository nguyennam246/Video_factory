---
name: video-kynang
description: >
  Dây chuyền dựng VIDEO DẠY KỸ NĂNG MỚI dọc 9:16 (học tập, hướng dẫn, khóa học) từ
  tài liệu nguồn ra mp4 hoàn chỉnh. Dùng skill này bất cứ khi nào BOSS bảo "làm video
  dạy {X}", "dựng video hướng dẫn {X}", "video bài {N} khóa {Y}", "làm video về kỹ năng
  {X}", hoặc muốn làm video dạy người mới một công cụ/quy trình/kỹ năng. Bao gồm: giao
  kịch bản cho thợ 2 Opus 5 theo brief 3-giây-đầu, khuôn 10 slide [1,3,3,2,3,3,3,3,3,3],
  thước tự kiểm 0 API, chọn scene từ catalogue 18 mẫu, dựng deck escbase headless, sinh
  giọng edge NamMinh, soi ảnh, nghiệm thu bằng máy, ghi 4 sổ. Cũng kích hoạt khi nhắc
  "bài superpowers", "khóa học video", "kịch bản dạy học", "hook 3 giây", "ẩn dụ người
  thợ", "27 reveal", hay khi cần cập nhật quy trình làm video dạy học sau mỗi bài.
---

# LÀM VIDEO DẠY KỸ NĂNG MỚI

**Mục đích bộ video** (BOSS đặt): *"Tôi chỉ xem video là hiểu vấn đề và làm được, chia sẻ
lại được."* Dọc 9:16, tiếng Việt, xem trên điện thoại.

**Khác skill `/video-baocao` ở đâu:** kia là báo cáo tài chính (khuôn `[1,2,3,3,3,3,2,2,3,3]`,
25 reveal, cấm kết luận đắt/rẻ). **Skill này là bài DẠY** — khuôn `[1,3,3,2,3,3,3,3,3,3]`,
27 reveal, có ẩn dụ xuyên suốt, có phần đi chậm qua một lần chạy thử. Hai khuôn không
lẫn nhau được.

---

## ⭐ CHẠY MỘT LỆNH — `lam_bai.py` (lập 25/07/2026)

BOSS nói *"tạo video bài X"* thì **đừng gõ tay 6 lệnh nữa**. Chạy:

```bash
python3 video/lam_bai.py --ma sp09 --ten dieu_phoi --loai kynang --nguon <tài liệu> \
        --nghe cau_hoi_gai            # ⭐ mã kiểu hook — video/nghe/KIEU_HOOK.md
```

🆕 **`--nghe <mã kiểu hook>` (25/07)** bật khâu **nghề giữ mắt**: nhét luật 4 mốc vào đề
bài giao thợ 2, và **thêm một cổng chặn ở bước 3** (thước `thuoc_nghe.py`). Không nêu thì
runner chạy như cũ — nhưng bài sẽ **nhạt khúc giữa**, vì không ai lo giây 8-60.
Hai trục độc lập: `--goc` quyết *kể chuyện gì*, `--nghe` quyết *giữ mắt cách nào*.
Sổ chống lặp: `video/nghe/NHAT_KY.md` — **hai bài liền nhau không được cùng kiểu hook**.

Runner giữ đúng thứ tự 9 bước và **tự dừng ở 3 loại cổng**:

| Mã thoát | Nghĩa | Thợ 1 làm gì |
| :-: | :-- | :-- |
| `10` | thước FAIL (lệch khuôn câu / tràn safezone) | sửa rồi `--tu-buoc <n>` |
| `20` | thợ 2 hết quota hoặc hỏng | đọc `<deck>/_VIEC_CHO_THO1.md`, **tự làm nốt** rồi `--tu-buoc <n>`. ⚠️ ĐỪNG đổi sang API free — việc này cần TAY trên máy |
| `30` | đã chụp 10 ảnh, **chờ soi mắt** | `Read` TỪNG PNG rồi `--tu-buoc 8` |
| `40` | xong phần máy | báo BOSS nghe/xem, **cấm tự khen** |

Runner **KHÔNG** thay skill này: khuôn, catalogue scene, luật ẩn dụ vẫn đọc ở đây.
Nó chỉ bỏ khâu gõ tay và đóng cổng chặn. Bước THỢ nó gọi tk 2 qua CLI, tự chọn model:
**opus cho kịch bản** (sai là hỏng cả bài), **sonnet cho sửa HTML** (cơ khí, có thước chặn).

---

## 0. BỐN LUẬT SỐNG CÒN — đọc lại mỗi lần

1. **AI KHÔNG NGHE ĐƯỢC.** Cấm viết "giọng nghe tự nhiên", "nhạc vừa phải", "đọc mượt".
   Mọi phán xét *giọng · nhịp · mức nhạc · mượt hay giật* để **BOSS nghe rồi phán**.
   Số đo của máy chỉ chứng minh "không còn nguyên nhân kỹ thuật", không thay được tai người.
2. **Đầu ra là ẢNH/VIDEO thì phải MỞ RA SOI.** `validate` PASS **không** có nghĩa slide
   đúng. Ca HPD: PASS cả 2 lượt mà soi ảnh vẫn ra 4 lỗi, 1 trong đó là lỗi NGHĨA.
   `Read` từng file PNG, và soi vài frame của video thật.
3. **ẨN DỤ TRƯỚC, TÊN KỸ THUẬT SAU.** Đây là chỗ trả giá đắt nhất dự án: BOSS xem bản 1
   bài Hook và **không hiểu**. Thuật ngữ cấm xuất hiện trước dòng 5 — máy đo được.
4. **3 GIÂY ĐẦU = 11 TỪ ĐẦU.** Giọng chạy 3,56 từ/giây (đo thật). Cái mất mát phải nằm
   trong 11 từ đầu tiên, không phải trong cả dòng hook.
5. 🆕 **BA GIÂY ĐẦU CHỈ BẮT ĐƯỢC MẮT, KHÔNG GIỮ ĐƯỢC MẮT.** Quy mốc rơi của video ngắn
   về khuôn này thì **mốc rơi 1 nằm gọn ở dòng 2**, **mốc rơi 2 ở dòng 5-7**. Luật cho
   hai mốc đó nằm ở **`video/nghe/`** (thư viện NGHỀ GIỮ MẮT, lập 25/07) — đọc trước khi
   viết lời, và bật cổng thước bằng `--nghe <mã kiểu hook>`.

---

## 1. CHIA VIỆC THEO MODEL — ai làm khâu nào

Đo thật 24/07/2026: **5 subagent Sonnet dựng song song bài 06→10** (khâu B1–B7), thợ 1
kiểm lại + render tuần tự ⇒ ra 6 mp4 đạt. Nhưng 4 lỗi NGHĨA của bài HPD chỉ lộ ra khi
**soi mắt từng ảnh**, không thước nào bắt được. Từ đó chia việc:

| Khâu | Giao ai | Vì sao |
| :-- | :-- | :-- |
| **Viết kịch bản** | 🔴 **Opus 5 (thợ 2)** | Khâu duy nhất phải *phán đoán* "người mới đã đủ chỗ trong đầu chưa". Sai ở đây thì cả bài hỏng, và thước không bắt được |
| Chọn scene từ catalogue | Opus, hoặc Sonnet có kèm mục 4 | Chọn hình **diễn đạt đúng ý câu**, không phải chọn hình đẹp |
| Dựng deck (sửa HTML/CSS, sync, validate) | ✅ **Sonnet** — chạy song song nhiều bài được | Việc cơ học, có thước chặn. Đã chạy trơn 5 bài song song |
| Sinh giọng, remap palette | ✅ Sonnet | Lệnh tất định |
| **Soi ảnh (nghĩa của màu)** | 🔴 **thợ 1 / phiên chính tự soi lại** | Đừng tin báo cáo của thợ. Lỗi `sg-warn` đỏ bọc câu tích cực chỉ mắt bắt được |
| **Render** | 🔴 **thợ 1 / phiên chính** | Render nền trong subagent hay **TREO MỒ CÔI** khi phiên con kết thúc (đã dính 24/07) |
| Phán giọng / mượt | 🔴 **BOSS** | AI không nghe được |

**🔴 SỬA 25/07: "thợ 2" KHÔNG phải `Agent` tool.** Thợ 2 = **tài khoản Claude thứ hai**,
gọi qua CLI (chạy bằng quota tài khoản khác — đó mới là điểm lợi):

```bash
CLAUDE_CONFIG_DIR=/Users/simple/.claude-tk2 claude -p --model opus --permission-mode acceptEdits "<đề bài>"
```

`lam_bai.py` đã gói sẵn lệnh này. Gọi tay thì dán toàn bộ `brief_tho2_opus.md` vào đề bài
(thay 4 chỗ `{{...}}`) — thợ 2 khởi động NGUỘI, đừng rút gọn brief. Chi tiết + bẫy quyền:
skill `/goi-tho` ở gốc repo. `Agent` tool là **subagent trong phiên**, việc khác.

---

## 2. BƯỚC 1 — GIAO KỊCH BẢN CHO THỢ 2 (Opus 5)

Đọc `brief_tho2_opus.md`, thay 4 chỗ, gọi Agent. Trước khi gọi, thợ 1 phải chốt sẵn:

| Chỗ thay | Lấy ở đâu |
| :-- | :-- |
| `{{CHỦ_ĐỀ}}` | BOSS giao |
| `{{LÀM_ĐƯỢC_GÌ}}` | 1 câu, cụ thể, kiểm chứng được ("cài được plugin trong Codex") |
| `{{ĐƯỜNG_DẪN_NGUỒN}}` | tài liệu THẬT. Không có nguồn thì hỏi BOSS, đừng để thợ 2 tự bịa |
| `{{ẨN_DỤ}}` | **ẩn dụ của SERIES, không phải của bài.** Xem bảng dưới |

### Ẩn dụ đang dùng — ĐỪNG ĐỔI GIỮA BỘ
| Series | Ẩn dụ | Ghi chú |
| :-- | :-- | :-- |
| Bộ 10 bài dạy Claude Code | **người thợ mới mỗi sáng** | Xuyên suốt cả 10 bài |
| Khóa Superpowers (8 bài) | **xây một căn nhà** | `kichban/superpowers/README.md` |
| Series mới | BOSS chốt 1 ẩn dụ **sờ được** trước khi viết bài 01 | Đổi giữa bộ = người xem mất mạch |

**Nhận bài của thợ 2 thì tự chạy lại thước, đừng tin báo cáo:**
```bash
cd /Users/simple/Desktop/Cloud/video
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/{slug}.txt --thuatngu "tên,thuật,ngữ"
```
Rồi **tự đọc bản lời một lượt bằng con mắt người chưa biết gì**. Thước đo khuôn, không
đo được dễ hiểu.

---

## 3. BƯỚC 2 — CHỌN SCENE (⭐ khâu đang bỏ phí nhiều nhất)

**Đo ngày 25/07/2026: 16/18 mẫu hình của template CHƯA DÙNG LẦN NÀO** trong 14+ video.
Cả bộ xoay quanh `mock-terminal` (7 deck) + `risk-cards-container` (1 deck). Đó là lý do
xem 3 bài liền nhau thấy "cùng một cái khuôn" — không phải template nghèo, mà **chưa mở kho**.

**Sau bài sp02 (25/07): 11/18 mẫu vẫn chưa dùng.** Đã mở thêm 5 mẫu — `workflow-grid` ·
`flow-diagram` · `core-module-grid` · `vpg-chat-message` · `glowing-conclusion`.
Còn để dành: `perf-compare` · `speed-gauge` · `revenue-balance` · `cpu-chip` ·
`stream-visual` · `vpg-traffic-pole` · `webui-frame` · 4 hero. **Bài sau lấy tiếp mẫu MỚI,
đừng quay lại 5 mẫu vừa dùng** — mục tiêu là mỗi bài trông khác bài trước.

**Bắt buộc mở catalogue trước khi sửa HTML:**
`escbase_template/docs/CATALOGUE_SCENE.md` — tra **bằng ẢNH** (`docs/assets/catalogue/slideN.png`),
không tra bằng chữ. `Read` ảnh rồi mới chọn.

### Bản đồ scene → vai slide của bài DẠY
| Dòng | Vai | Scene nên lấy | Class gốc |
| :-: | :-- | :-- | :-- |
| 1 | HOOK | hero theo chất liệu: repo GitHub / ảnh nguồn / logo | `ask-github-mark` · `vpg-source-hero` · `vpg-logo-hero` |
| 2-3 | cảnh đời thường, vấn đề lộ ra | **Flow diagram** (cũ → mới, gạch trạng thái cũ) | `flow-diagram` · `flow-strike` |
| 4 | ẩn dụ sờ được | **Traffic-light pole** hoặc scene tự chế theo ẩn dụ | `vpg-traffic-pole` · `lightable` |
| 5 | gọi tên kỹ thuật | **Highlight mode** — nhấn từng phần trong 1 scene | `core-module-grid` · `highlightable` |
| 6 | ví dụ THẬT có số | **Performance compare bars** — số thành thanh chạy | `perf-compare` · `perf-bar` |
| 7-8 | chạy thử 4 bước | **Workflow grid** (bước đánh số) + **Mock terminal** | `workflow-grid` · `mock-terminal` |
| 9 | bẫy | **Risk cards** (đỏ/vàng/xanh) | `risk-cards-container` |
| 10 | câu chốt đối xứng | **Final lockup** | `glowing-conclusion` · `glowing-orb` |

**Cách lấy:** mở `template/visual-pattern-gallery/index.html`, tìm `data-slide="<N>"`,
copy khối DOM + CSS tương ứng từ `style.css`, đổi chữ/số/nhãn.
**Giữ số `.slide-element` = số câu của dòng script.**

### 3 thứ đã đo khi mở kho lần đầu (sp02, 25/07) — đỡ mò lại
1. **CSS gốc của mẫu hình PHẦN LỚN ĐÃ CÓ SẴN** trong style.css của deck (thừa kế từ
   starter). Kiểm trước khi chép, đừng chép đè cả khối:
   ```bash
   for c in workflow-grid flow-diagram core-module-grid msg-bubble risk-cards-container \
            glowing-conclusion mock-terminal packet lightable highlightable; do
     printf "%-22s %s\n" "$c" "$(grep -c "\.$c" headless/deck_XX/style.css)"; done
   ```
   Ca sp02: chỉ thiếu **bộ helper kích thước `vpg-*` + `.packet` + keyframes**. Chép đúng
   ngần đó là đủ, đặt **CUỐI FILE** (style.css có tới 4 khối `:root` chồng nhau).
2. **`.slide-element` tìm theo `querySelectorAll` ⇒ nằm sâu bao nhiêu cũng được.** Thẻ con
   trong grid tự làm 1 reveal được; không bắt buộc là con trực tiếp của `.slide-content`.
3. **Mẫu hình gallery mặc định TRÀN safezone** khi nhét chữ tiếng Việt (dài hơn nhãn mẫu).
   Ca sp02: 5/10 slide FAIL ngay lượt validate đầu, siết 3 vòng mới PASS. Tính trước
   ~2-3 vòng siết, đừng coi là hỏng.

### Ràng buộc không được phá
- Safezone `100px 28px 200px` — nửa dưới là chỗ phụ đề, đừng đặt chữ quan trọng.
- Nhãn ≥11-12px · kicker 13-20px · số chính 42-51px (đo trên khung 390).
- Visual chính phải **lấp gần đủ safezone**; scene lọt thỏm giữa slide là lỗi.
- **Hai slide liền nhau không được cùng một dạng hộp** — đổi hình, đổi chuyển động,
  hoặc đổi vai màu.
- Hạt/shimmer/glow nền **không tính** là animation có nghĩa. Phải có: scanner quét,
  packet chạy, thanh đầy lên, đèn bật, trạng thái cũ bị gạch.

---

## 4. BƯỚC 3 — DỰNG DECK

Chép từ **`deck_sp01`** (bài dạy đã ra mp4, khuôn 27 reveal khớp sẵn, palette `sp` đúng
⇒ **không phải chạy `remap_palette.py`**).

```bash
cd /Users/simple/Desktop/Cloud/video/escbase_template
cp -R headless/deck_sp01 headless/deck_{slug}
rm -rf headless/deck_{slug}/output headless/deck_{slug}/output_headless
cp ../kichban/escbase_10dong/{slug}.txt headless/deck_{slug}/script-90s.txt
.venv/bin/python sync_script.py headless/deck_{slug} headless/deck_{slug}/script-90s.txt
# sửa index.html: thay chữ + THAY SCENE theo mục 3; đổi <title>, <meta>, cả hai ?v=
.venv/bin/python validate_slide.py headless/deck_{slug} --semantic-report   # phải PASS
```

Kiểm số reveal sau khi sửa HTML:
```bash
python3 -c "import re;s=open('headless/deck_{slug}/index.html',encoding='utf-8').read();\
print([p.count('slide-element') for p in re.split(r'<div class=\"slide[ \"]',s)[1:]])"
# phải in ra [1, 3, 3, 2, 3, 3, 3, 3, 3, 3]
```

🎨 **Palette theo SERIES, không theo bài:** superpowers/bài dạy = `sp` (xanh `#38bdf8` +
hổ phách `#fbbf24`). ⚠️ `remap_palette.py` chỉ map TỪ bảng rose của bài 05 — chép deck
đã đổi màu rồi remap tiếp ⇒ **deck lai màu** mà script vẫn báo thành công.

### 🔴 CHÉP DECK CŨ LÀ THỪA KẾ CẢ *NGHĨA* CỦA STYLE, KHÔNG CHỈ HÌNH
Sau khi thay chữ, duyệt lại từng class mang MÀU/NGHĨA, hỏi *"câu MỚI nằm trong đó có
đúng sắc thái đó không":*

| Class | Sắc thái nó áp | Lỗi đã dính thật |
| :-- | :-- | :-- |
| `sg-warn` | khung **cảnh báo đỏ** | HPD slide 10: bọc câu **tích cực** ⇒ màn hình cảnh báo một điều tốt. Vá: `hk-note` |
| `hk-strike` | **gạch ngang = phủ định** | MSR slide 10: gạch ngang câu chốt ĐÚNG ⇒ màn hình phủ nhận một sự thật |
| `hk-vs-old` | đỏ = vế **xấu** | HPD slide 6: tô đỏ một vế trung tính ⇒ ngầm phán "xấu" |
| `hk-answer-no` / `hk-answer-ok` | xấu / tốt | kiểm câu bên trong có đúng cực đó không |
| `sg-num` | huy hiệu **1 KÝ TỰ** | HPD slide 5: nhét `"KH 2026"` ⇒ chữ tràn, lòi ra thành bóng mờ |
| `flow-strike` | gạch = **cách làm CŨ đã bỏ** | dùng cho cách làm mới là phủ định chính bài mình dạy |
| `flow-new` | xanh lá = **trạng thái mới, TỐT** | sp02 slide 3: bọc *"cuốn sổ chưa vào công trường"* = **nguyên nhân gây lỗi** ⇒ xanh lá đang khen một điều xấu. Vá: đổi sang hổ phách (chỗ phải chú ý), không dùng đỏ vì bài không doạ |
| `core-module` | **mờ có chủ đích** — nó thiết kế cho `data-mode="highlight"`, sáng lên khi được tô | sp02 slide 4: deck KHÔNG dùng highlight mode ⇒ cả 4 thẻ hiện ra mờ gần như không đọc được, mà `validate` PASS. ⚠️ **Lấy mẫu hình từ gallery thì phải hỏi: nó có phụ thuộc một `data-mode` không?** |

**Bài dạy thì màu cũng phải dạy đúng.** Đỏ chỉ dùng cho cái người xem PHẢI tránh.

---

## 5. BƯỚC 4 — GIỌNG

🔴 **GIỌNG MẶC ĐỊNH: `edge:vi-VN-NamMinhNeural` `+14%`.** BOSS nghe bản ElevenLabs "Nhật"
rồi phán **"âm thanh tệ quá, dùng lại mẫu âm thanh ban đầu như các video khác đi"**
(24/07/2026). **Đừng tự ý dùng ElevenLabs** — vừa tệ hơn theo tai BOSS, vừa tốn tiền.
Muốn đổi thì dựng **bài thử ngắn** cho BOSS nghe TRƯỚC (khuôn `kichban/00*_thu_giong.md`),
đừng đốt cả lượt render. **KHÔNG tự đổi giọng/tốc độ/nghỉ.**

```bash
.venv/bin/python generate_tts.py headless/deck_{slug} \
    --engine edge --voice vi-VN-NamMinhNeural --rate "+14%"
```
edge-tts **miễn phí vô hạn**, render thoải mái. Cache theo hash ở `state/video_tts/`:
sửa slide render lại = 0 lượt API. **ĐỪNG xoá cache.**

🎵 **Nhạc nền:** `synth_lofi` cho series dạy học (BOSS chốt 25/07). Chuẩn độ to bằng
**LUFS −22,7**, không phải RMS — BOSS bắt được lỗi máy không thấy: RMS bằng nhau mà tai
vẫn nghe to hơn 3,1 dB. ⚠️ 5 preset đều pad + arp chậm, **không có bộ gõ** ⇒ "sôi động"
không chữa được bằng âm lượng.

---

## 6. BƯỚC 5 — SOI ẢNH (không bỏ được, không giao thợ)

```bash
.venv/bin/python capture_slides.py headless/deck_{slug}   # ra /tmp/escbase-qa/deck_{slug}/
```
Rồi **`Read` TỪNG file `slide1.png` … `slide10.png`**. Soi 5 thứ:
1. chữ tràn / đè / nhãn quá nhỏ
2. khoảng trống chết (visual lọt thỏm giữa safezone)
3. **màu có mâu thuẫn với nghĩa của câu không** (bảng mục 4)
4. số trên màn hình có khớp lời đọc không
5. **hai slide liền nhau có cùng một dạng hộp không** — bài dạy mà 10 slide cùng khuôn
   là lỗi nội dung, không phải lỗi thẩm mỹ

Vá xong thì **`validate` lại + `capture` lại + soi lại đúng những slide đã sửa**.

---

## 7. BƯỚC 6 — RENDER + NGHIỆM THU BẰNG MÁY

```bash
.venv/bin/python headless/render_headless.py headless/deck_{slug}   # CHẠY NỀN, 4-10 phút
```
⚠️ File đích là **`output_headless/final_headless.mp4`**. `silent.mp4` xuất hiện trước
vài phút là bản **chưa có tiếng** — đừng tưởng xong.
🔴 **Render ở phiên chính, KHÔNG trong subagent** (treo mồ côi khi phiên con kết thúc).
🔴 **`TAB_CAPTURE_WARMUP` giữ 0.8 — ĐỪNG nâng.** Nâng 3.0 làm hụt khung + giãn timeline +17s.

```bash
cp headless/deck_{slug}/output_headless/final_headless.mp4 \
   /Users/simple/Desktop/Cloud/results/video/{slug}.mp4

.venv/bin/python ../.claude/skills/video-baocao/thuoc/nghiem_thu_video.py \
   /Users/simple/Desktop/Cloud/results/video/{slug}.mp4 \
   headless/deck_{slug}/output/voiceover_concat.mp3
```

🔴 **NGHIỆM THU ĐẠT RỒI THÌ COPY NGAY VỀ CHỖ CỐ ĐỊNH** (BOSS chốt 25/07/2026 — `results/video/`
là **bãi làm việc** lộn xộn, BOSS không tìm video ở đó):
```bash
mkdir -p /Users/simple/Desktop/Cloud/video/thanh_pham/kynang/bai_XX_<tên_dễ_nhớ>
cp /Users/simple/Desktop/Cloud/results/video/{slug}.mp4 \
   /Users/simple/Desktop/Cloud/video/thanh_pham/kynang/bai_XX_<tên_dễ_nhớ>/
```
Rồi cập nhật bảng `kynang/` trong `thanh_pham/README.md`. Trạng thái chỉ ghi cái MÁY đo;
**cấm ghi "duyệt"** — AI không nghe được, chỉ BOSS nghe rồi phán mới là duyệt.
(dùng chung thước nghiệm thu với `/video-baocao` — đo 6 việc: khổ hình/bt709 · dB ·
lệch giọng theo khung · hụt khung · đứng hình 4 giây đầu · **phụ đề có thật**.)

🔴 **PHỤ ĐỀ LÀ PHÉP ĐO BẮT BUỘC VỚI DECK MỚI.** Lỗi 24/07/2026 là lỗi **IM LẶNG**: dây
chuyền chỉ đọc cache, deck mới ra video **không có phụ đề** mà vẫn PASS mọi phép đo khác.
Đếm pixel vùng y≈1330-1520.

Cuối cùng **soi mắt 2-3 frame của video thật** (không chỉ tin ảnh deck).

**Mốc tham chiếu đã đo:** superpowers-01 93,3s / 332 từ · **superpowers-02 113,2s / 394 từ /
24,7 MB / render 235,4s = 69,3 ms-khung** · escbase 05→10 84-102s · file 1080 nét 17-25 MB.
📏 **Nhịp đọc edge NamMinh +14% = 3,56 từ/giây** (2 bài khớp nhau) ⇒ ước lượng được độ dài
video ngay từ bản nháp lời, không phải render mới biết.

⚠️ **Đường dẫn TƯƠNG ĐỐI là bẫy thật của dây chuyền này.** cwd bị reset giữa chừng ít nhất
2 lần trong một phiên. Hậu quả đã dính: `cat >> style.css` tạo file rác ở gốc template (sửa
không vào deck, validate in ra **số y hệt lượt trước** — dấu hiệu duy nhất), và `ls` báo
"không có final_headless.mp4" trong khi file có thật. **Dùng đường dẫn tuyệt đối cho mọi
lệnh đọc/ghi file.** Số đo đứng im sau khi sửa ⇒ nghi sửa nhầm file, đừng nghi thước.

---

## 8. BƯỚC 7 — BÁO BOSS + GHI 4 SỔ

Báo BOSS phải **tách bạch**: cái gì máy đo được (nêu số), cái gì cần BOSS nghe/xem rồi
phán (mượt · giọng · dễ hiểu chưa). **Cấm tự khen.**

Ghi sổ **VỀ GỐC REPO** (không mở sổ riêng trong `video/`):
1. `tri_thuc/patch_history.md` — mục mới **LÊN ĐẦU**.
2. `tri_thuc/kinh_nghiem.md` — bẫy mới, 1-3 dòng kèm **ngày**.
3. `video/HANDOFF.md` — 2 khoang sống, **GIỮ GỌN** (hook cắt ở 7000/5000 ký tự).
4. **CẬP NHẬT CHÍNH SKILL NÀY** — xem mục 9.

---

## 9. ⭐ MỖI LẦN LÀM VIDEO XONG PHẢI CẬP NHẬT SKILL NÀY

BOSS lệnh: *"mỗi lần làm video thì cập nhật skill"*, để lần sau không phải mò lại.
Sau mỗi bài làm đúng 4 việc:

1. **Thêm 1 dòng vào NHẬT KÝ** dưới đây (số đo thật, đừng đoán).
2. **Lỗi mới soi ra mà thước không bắt được** ⇒ thêm dòng vào bảng class ở **mục 4**.
3. **Scene mới lấy từ catalogue** ⇒ đánh dấu vào bản đồ mục 3 (mục tiêu: kéo con số
   "16/18 chưa dùng" xuống). Scene tự chế đắt giá ⇒ ghi lại tên class.
4. **Luật/khuôn mới BOSS chốt** ⇒ sửa thẳng vào mục tương ứng, ghi ngày.

### NHẬT KÝ BÀI ĐÃ LÀM

| Ngày | Bài | Video | Dài | Từ | Scene mới dùng | Lỗi soi ra |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 24/07/2026 | superpowers 01 | `superpowers_01_tong_quan.mp4` | 93,3s | 332 | (chưa mở catalogue) | — · chờ BOSS phán |
| 25/07/2026 | superpowers 02 | `superpowers_02_cai_dat.mp4` | 113,2s · 24,7 MB · render 235,4s (69,3 ms/khung) | 394 | **5 mẫu**: workflow-grid · flow-diagram · core-module-grid · chat-bubbles · glowing-conclusion | **3 lỗi, không lỗi nào thước bắt được**: ① dòng 7-8 gọi "bốn bước" nhưng thực ra là **hai đường cài khác nhau** ⇒ người mới làm tuần tự cả 4 rồi tắc (lỗi HIỂU, thợ 2 viết đúng khuôn vẫn dính) · ② `core-module` mờ không đọc được · ③ `flow-new` xanh lá bọc nguyên nhân gây lỗi |

| 25/07/2026 | superpowers 03 | `superpowers_03_brainstorming.mp4` | 117,3s · 24,9 MB | 444 | `stream-visual` · `chat-bubbles` | thợ 2 tự siết 477→444 |
| 25/07/2026 | superpowers 04 | `superpowers_04_worktree.mp4` | 116,8s · 25,4 MB | 444 | `webui-frame` · `workflow-grid` | — |
| 25/07/2026 | superpowers 05 | `superpowers_05_tdd.mp4` | 118,4s · 25,8 MB | 445 | **`traffic-pole`** · `flow-diagram` | 🔴 **cột đèn xếp ĐỎ/DỌN/XANH trong khi lời dạy Đỏ→Xanh→Dọn — MÀN HÌNH DẠY NGƯỢC LỜI.** Thợ 1 soi ảnh mới thấy. Vá: đổi cả nhãn lẫn màu đèn. Thợ 2 tự siết 495→445 |
| 25/07/2026 | superpowers 06 | `superpowers_06_thuc_thi.mp4` | 121,0s · 26,6 MB | 450 | **`perf-compare`** · `core-module-grid` | 🔴 `.vpg-proof-chip` là **flex** ⇒ mỗi `<b>` thành một flex item, câu bị **xé thành nhiều cột**, đọc ra chữ khác hẳn ý. Vá: `display:block` |
| 25/07/2026 | superpowers 07 | `superpowers_07_debug.mp4` | 114,6s · 24,7 MB | 424 | **`cpu-chip`** · `workflow-grid` | 🔴 `.chip-core` xanh lá bọc chữ **"VỠ"** = khen một khiếm khuyết. Thợ 2 tự NÊU nghi vấn nhưng không dám vá — nêu ra là đúng việc. Lệch giọng **0,000 khung** |
| 25/07/2026 | superpowers 08 | `superpowers_08_ban_giao.mp4` | 104,6s · 23,2 MB | 368 | **`revenue-balance`** · `glowing-conclusion` | — |

### 🔴 BA LỖI CỦA LƯỢT 03→08 — ĐỀU LÀ LỖI *MÀN HÌNH NÓI SAI*, THƯỚC VÀ VALIDATE ĐỀU PASS

Lỗi bài 05 là đắt nhất và đáng nhớ nhất: **không xấu, không tràn, không sai chính tả — chỉ là
xếp sai thứ tự nên màn hình dạy ngược lời đọc.** Không phép đo máy nào bắt được loại này.
⇒ Khi slide có **thứ tự** (bước 1-2-3, vòng lặp, đèn đỏ-vàng-xanh), soi ảnh phải hỏi thêm một
câu: *"thứ tự trên màn hình có đúng thứ tự trong lời không?"*

**Bài học lớn nhất của lượt sp02:** thước ra `DAT` **ngay vòng đầu** và `validate` PASS,
nhưng vẫn còn 3 lỗi. Cả 3 chỉ lộ ra khi **đọc lời bằng đầu người mới** và **soi từng ảnh**.
⇒ Thước là điều kiện CẦN, không phải điều kiện ĐỦ. Đừng bỏ bước 2 (tự đọc) và bước 5 (soi ảnh).

---

## 10. TRA NHANH

| Cần gì | Ở đâu |
| :-- | :-- |
| Brief giao thợ 2 Opus | `.claude/skills/video-kynang/brief_tho2_opus.md` |
| Thước kịch bản dạy (0 API) | `.claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py` |
| Thước nghiệm thu video | `.claude/skills/video-baocao/thuoc/nghiem_thu_video.py` (dùng chung) |
| **Catalogue 18 scene + ảnh** | `escbase_template/docs/CATALOGUE_SCENE.md` |
| Kho DOM/CSS để copy | `escbase_template/template/visual-pattern-gallery/` |
| Luật deck escbase (visual, QA) | `escbase_template/CLAUDE.md` · `WORKFLOW.md` |
| Luật riêng dự án video | `video/CLAUDE.md` |
| Trạng thái + việc chờ | `video/HANDOFF.md` |
| Bẫy kỹ thuật toàn dự án | `tri_thuc/kinh_nghiem.md` |
| Kịch bản khóa Superpowers | `video/kichban/superpowers/` |

**Phụ thuộc ngoài:** `ffmpeg` (brew) · `.venv` trong `escbase_template/` (Pillow,
playwright, edge-tts) · font macOS có sẵn.
