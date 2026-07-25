# BRIEF THỢ 2 — DỰNG 6 BÀI SUPERPOWERS 03→08 (lập 25/07/2026)

**Người giao: thợ 1.** Đọc hết file này trước khi gõ lệnh đầu tiên. Nó gói sẵn mọi thứ
đã trả giá — làm theo thì không phải mò lại.

**Bối cảnh:** BOSS vừa duyệt bài 02 (`results/video/superpowers_02_cai_dat.mp4`) — *"video
tốt"* — và giao dựng 6 bài còn lại của khoá. Bài 02 là **khuôn mẫu**: chép cách làm của nó.

---

## 0. VIỆC CỦA BẠN — và việc TUYỆT ĐỐI KHÔNG LÀM

**LÀM, cho từng bài trong 6 bài:** viết lời (3 file) → chạy thước → dựng deck → validate →
capture → **soi từng ảnh** → vá → validate/capture/soi lại.

🔴 **KHÔNG LÀM — không thương lượng:**
- **KHÔNG render.** Không gọi `render_headless.py`, không ffmpeg dựng video.
  Lý do đã trả giá 24/07: render chạy nền trong phiên con thì khi phiên con kết thúc,
  tiến trình **mồ côi và treo** (0% CPU, không còn chromium). **Thợ 1 render.**
- **KHÔNG chạy `generate_tts.py`.** Thợ 1 sinh giọng cùng lượt render.
- **KHÔNG tự đổi giọng, tốc độ, nghỉ, palette.** Palette series superpowers là `sp`
  (xanh `#38bdf8` + hổ phách `#fbbf24`), deck mẫu đã đúng ⇒ **KHÔNG chạy `remap_palette.py`**
  (nó chỉ map TỪ bảng rose của bài 05; chạy trên deck đã đổi màu ⇒ **deck lai màu** mà
  script vẫn báo thành công).
- **KHÔNG đổi mẫu hình được giao** sang mẫu khác. Xem mục 3 để hiểu vì sao.

**Làm xong 1 bài thì báo, đừng đợi xong cả 6.** Thợ 1 render cuốn chiếu.

---

## 1. ĐỌC TRƯỚC (theo đúng thứ tự)

| # | File | Lấy gì |
| :-: | :-- | :-- |
| 1 | `video/.claude/skills/video-kynang/SKILL.md` | **Dây chuyền đầy đủ.** Đọc hết, nhất là mục 4 (bảng class mang nghĩa) và mục 6 (soi ảnh) |
| 2 | `video/.claude/skills/video-kynang/brief_tho2_opus.md` | **Luật viết lời**: 3 giây đầu, ẩn dụ trước thuật ngữ, khuôn 10 dòng |
| 3 | `video/kichban/superpowers/README.md` | Bối cảnh cả khoá 8 bài |
| 4 | `video/kichban/superpowers/0X_*.md` | **NGUỒN SỰ THẬT của bài đang làm.** Viết lại theo khuôn mới, **KHÔNG bịa thêm dữ kiện ngoài file này** |
| 5 | `video/kichban/escbase_10dong/sp02_cai_dat.txt` | **MẪU LỜI đã đạt** — nhịp câu đích |
| 6 | `video/escbase_template/headless/deck_sp02/index.html` | **MẪU DECK đã đạt** — chép cấu trúc |
| 7 | `video/escbase_template/docs/CATALOGUE_SCENE.md` | 18 mẫu hình + ảnh. **Tra bằng ẢNH, không tra bằng chữ** |

**Chỗ chạy:** `video/escbase_template/`, luôn dùng `.venv/bin/python` trong đó.

---

## 2. SÁU BÀI + SLUG + THUẬT NGỮ CẤM

| Bài | Nguồn `kichban/superpowers/` | Slug (dùng cho cả file lời lẫn deck) | `--thuatngu` (cấm xuất hiện trước dòng 5) |
| :-: | :-- | :-- | :-- |
| 03 | `03_brainstorming.md` | `sp03_brainstorming` → `deck_sp03` | `superpowers,skill,brainstorming,codex,agent,plugin` |
| 04 | `04_worktree_va_ke_hoach.md` | `sp04_worktree` → `deck_sp04` | `superpowers,skill,worktree,codex,agent,plugin,branch` |
| 05 | `05_tdd.md` | `sp05_tdd` → `deck_sp05` | `superpowers,skill,tdd,codex,agent,test,refactor` |
| 06 | `06_thuc_thi_va_review.md` | `sp06_thuc_thi` → `deck_sp06` | `superpowers,skill,review,codex,agent,subagent,code` |
| 07 | `07_debug_co_he_thong.md` | `sp07_debug` → `deck_sp07` | `superpowers,skill,debug,debugging,codex,agent,log` |
| 08 | `08_kiem_chung_va_ban_giao.md` | `sp08_ban_giao` → `deck_sp08` | `superpowers,skill,codex,agent,merge,commit,verification` |

**Người xem xong phải LÀM ĐƯỢC gì** (viết lời bám đúng cái này):

| Bài | Làm được |
| :-: | :-- |
| 03 | Đưa một yêu cầu mơ hồ qua vòng hỏi đáp tới lúc có thiết kế mình hiểu và gật đầu được |
| 04 | Tách việc mới ra chỗ riêng để không đụng việc đang chạy; nhìn một bản kế hoạch biết nó chia mấy hạng mục, thứ tự nào |
| 05 | Đi đúng ba nhịp: viết phép thử cho nó HỎNG trước, làm cho nó chạy, rồi mới dọn |
| 06 | Giao việc theo từng hạng mục nhỏ; nghiệm thu hỏi hai câu khác nhau — "đúng thứ tôi đặt không" trước, "làm có tử tế không" sau |
| 07 | Gặp lỗi thì đi bốn pha thay vì đoán rồi sửa bừa |
| 08 | Đòi bằng chứng thay vì tin lời "đã xong"; biết chọn cách nhập việc vào nhánh chính |

**ẨN DỤ CỦA CẢ KHOÁ, ĐỪNG ĐỔI GIỮA BỘ: xây một căn nhà** (đội thợ, công trường, bản vẽ,
sổ tay thi công). Bài 02 đã dùng hình *"mang cuốn sổ qua cổng"* — bài 03 nối mạch từ đó,
đừng lặp lại nguyên hình ảnh ấy. Đổi ẩn dụ giữa bộ = người xem mất mạch.

---

## 3. ⭐ MẪU HÌNH ĐƯỢC CHIA SẴN — PHẦN QUAN TRỌNG NHẤT CỦA BRIEF NÀY

**Vì sao có mục này:** đo ngày 25/07 — **16/18 mẫu hình của template chưa dùng lần nào**
trong 14+ video. Cả bộ xoay quanh `mock-terminal`. Đó là lý do xem 3 bài liền nhau thấy
"cùng một cái khuôn". Bài 02 mở thêm 5 mẫu, còn 11 mẫu chưa đụng.

Thợ 1 đã chia sẵn để **6 bài không đụng nhau**. Đây là ràng buộc, không phải gợi ý:

| Bài | Mẫu MỚI bắt buộc dùng | Ảnh tra trước | Vì sao mẫu đó hợp bài đó |
| :-: | :-- | :-- | :-- |
| 03 | **`stream-visual`** (`stream-pipe` · `stream-data`) + **`vpg-chat-message`** (`c-message` · `msg-bubble`) | `slide10.png` · `slide16.png` | Dòng câu hỏi chảy qua rồi kết lại thành bản vẽ; vòng hỏi đáp từng câu |
| 04 | **`webui-frame`** (`vpg-media-full` · `source-tag`) + **`workflow-grid`** (`workflow-step` · `packet`) | `slide5.png` · `slide12.png` | Khung cửa sổ = hai khu làm việc tách nhau; kế hoạch chia hạng mục đánh số |
| 05 | **`vpg-traffic-pole`** (`vpg-lamp` · `lightable`) + **`flow-diagram`** (`flow-old` · `flow-strike` · `flow-new`) | `slide15.png` · `slide7.png` | ⭐ **Cột đèn đỏ/vàng/xanh đúng NGHĨA ĐEN vòng Đỏ-Xanh-Dọn — chỗ đắc địa nhất cả bộ, dùng cho tử tế**; cách cũ (xây xong mới thử) bị gạch |
| 06 | **`perf-compare`** (`perf-bar` · `perf-row`) + **`core-module-grid`** | `slide6.png` · `slide13.png` | Thanh so sánh "giao cả căn nhà một lượt" ↔ "giao từng phòng"; liệt kê các mặt phải kiểm |
| 07 | **`cpu-chip`** (`chip-body` · `chip-core` · `chip-pins`) + **`workflow-grid`** | `slide9.png` · `slide12.png` | ⭐ **Có scanner quét qua từng lớp — đúng nghĩa "dò tìm chỗ vỡ theo lớp"**; bốn pha đánh số 01-04 |
| 08 | **`revenue-balance`** (`balance-beam` · `column-fill`) + **`glowing-conclusion`** (`glowing-orb` · `icon-badge`) | `slide17.png` · `slide18.png` | ⭐ **Cái cân: lời "ĐÃ XONG" đặt lên cân với bằng chứng thật, cân nghiêng bên nào**; câu chốt khép cả khoá |

**Cách lấy:** ảnh ở `escbase_template/docs/assets/catalogue/slideN.png` — **`Read` ảnh
trước, rồi mới chọn chỗ đặt**. DOM ở `template/visual-pattern-gallery/index.html`
(tìm `data-slide=`), CSS cùng tên trong `style.css` cạnh nó.
Các slide còn lại tái dùng scene của `deck_sp02`.

⚠️ **`vpg-traffic-pole` dùng `.lightable`** ⇒ slide đó cần `data-mode="traffic-light"`, và ở
chế độ đó **số reveal = số `.slide-element` + số `.lightable`**. Tính cho khớp số câu; nếu
không khớp thì **đừng bật mode**, cho `.lit-red` / `.lit-yellow` / `.lit-green` tĩnh như
`deck_sp02` slide 9 đã làm (đã chạy được, chép thẳng).

---

## 4. KHUÔN LỜI — 10 DÒNG, `[1,3,3,2,3,3,3,3,3,3]` = 27 REVEAL

| Dòng | Vai | Số câu |
| :-: | :-- | :-: |
| 1 | **HOOK** — cảnh đời thường + mất mát | **1** |
| 2 | Cảnh tiếp. Vấn đề lộ ra ở "ngày thứ N" | 3 |
| 3 | **Chỉ đúng chỗ đau**: lỗi KHÔNG ở đâu, mà ở đâu | 3 |
| 4 | **Ẩn dụ sờ được** (vẫn chưa gọi tên kỹ thuật) | 2 |
| 5 | **Giờ mới gọi tên kỹ thuật** + nói nó làm gì bằng chữ thường | 3 |
| 6 | **Ví dụ THẬT có số** | 3 |
| 7 | Chạy thử — bước 1, bước 2 | 3 |
| 8 | Chạy thử — bước 3, bước 4 + kết quả nhìn thấy được | 3 |
| 9 | **Bẫy** người mới hay sập + cách né | 3 |
| 10 | **Câu chốt đối xứng lại hook** | 3 |

⇒ **330-450 từ · 93-127 giây.** Số câu là ràng buộc CỨNG (1 câu = 1 hiệu ứng hiện chữ).

### 🔴 BA GIÂY ĐẦU = 11 TỪ ĐẦU
Giọng chạy **3,56 từ/giây** (đo thật 2 bài). Trong 11 từ đầu phải có đủ **cảnh sờ được**
(có người, có đồ vật) **và** **mất mát hoặc nghịch lý**.
**Cấm mở bài bằng:** "Hãy tưởng tượng…", "Bạn có biết…", "Trong bài này…", "Hôm nay chúng
ta…", "Xin chào…", "Có một…". **Viết 3 phương án hook, chọn 1, ghi 2 cái kia vào README.**

Mẫu đạt (bài 02): *"Sổ tay thi công còn ngoài cổng, tường đã xây xong ba ngày."*

### 🔴 ẨN DỤ TRƯỚC, TÊN KỸ THUẬT SAU
Chỗ trả giá đắt nhất dự án: BOSS xem bản 1 một bài và **không hiểu**, vì tên kỹ thuật ném ra
từ cảnh 4 khi trong đầu người xem chưa có chỗ đặt nó. Dòng 1-4 **chỉ có cảnh đời thường và
ẩn dụ sờ được**. Ẩn dụ phải SỜ ĐƯỢC (cái khoá, cuốn sổ, cột đèn, cái cân) — không được là
"cơ chế", "lớp bảo vệ", "luồng xử lý": đó vẫn là khái niệm đội lốt ẩn dụ.

### Luật viết từng chữ
- **Lời đọc CŨNG LÀ PHỤ ĐỀ** ⇒ tắt tiếng đọc chữ vẫn phải hiểu.
- **Số viết ra CHỮ** ("ba mươi ba nghìn"). ⚠️ đội từ rất nhanh — *"hai mươi bảy phẩy bảy tỷ"*
  = 6 từ. Phải cắt thì **cắt ở SỐ** (đọc tròn), đừng cắt ý.
- **Cấm dấu `—`** (TTS đọc xấu). **1 dòng ≤ 55 từ.**
- **Cấm chữ lập trình**: `stdin` `stdout` `JSON` `API` `CLI` `config` `deploy` `commit`
  `repo` `parse` `endpoint` `schema` `exit code` `stack trace` `runtime` `framework`.
- **Cấm chữ rỗng**: "mạnh mẽ", "tuyệt vời", "thay đổi cuộc chơi", "đột phá".
- **Đừng nén cho ngắn.** BOSS chốt: *"không cần làm quá ngắn — đúng là đủ."*

### Sản phẩm — 3 file/bài, không ghi file nào khác
```
video/kichban/escbase_10dong/<slug>.txt           ← LỜI, đúng 10 dòng, không tiêu đề, không dòng trống
video/kichban/escbase_10dong/<slug>.man_hinh.md   ← bảng Slide | Lời rút gọn | Chữ màn hình | Hình gì CHUYỂN ĐỘNG
video/kichban/escbase_10dong/README_<slug>.md     ← truy vết + 3 hook + kết quả thước
```
Cột "hình gì chuyển động" phải là **chuyển động CÓ NGHĨA** (thanh đầy lên, đèn bật, gói tin
chạy, scanner quét, trạng thái cũ bị gạch) — **không phải "hạt bay nền"**.

### Thước — chạy tới khi ra `DAT`, không thương lượng
```bash
cd /Users/simple/Desktop/Cloud/video
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/<slug>.txt --thuatngu "<cột thuật ngữ ở bảng mục 2>"
```
⚠️ Thước đo **khuôn, độ dài, từ cấm, đối xứng**. Nó **KHÔNG** đo được *bài có dễ hiểu không*.
Đọc lại bản cuối bằng con mắt người chưa biết gì: *"tới dòng này, người xem đã có đủ chỗ
trong đầu để đặt câu này chưa?"*

---

## 5. DỰNG DECK

```bash
cd /Users/simple/Desktop/Cloud/video/escbase_template
cp -R headless/deck_sp02 headless/deck_spXX
rm -rf headless/deck_spXX/output headless/deck_spXX/output_headless
cp ../kichban/escbase_10dong/<slug>.txt headless/deck_spXX/script-90s.txt
.venv/bin/python sync_script.py headless/deck_spXX headless/deck_spXX/script-90s.txt
# sửa index.html: thay chữ, THAY SCENE theo mục 3, đổi <title>, <meta>, và CẢ HAI ?v=
.venv/bin/python validate_slide.py headless/deck_spXX --semantic-report   # phải PASS
.venv/bin/python capture_slides.py headless/deck_spXX
```
Kiểm reveal, phải in ra `[1, 3, 3, 2, 3, 3, 3, 3, 3, 3]`:
```bash
python3 -c "import re;s=open('/Users/simple/Desktop/Cloud/video/escbase_template/headless/deck_spXX/index.html',encoding='utf-8').read();print([p.count('slide-element') for p in re.split(r'<div class=\"slide[ \"]',s)[1:]])"
```

### 🔴 CHÉP DECK CŨ LÀ THỪA KẾ CẢ *NGHĨA* CỦA STYLE, KHÔNG CHỈ HÌNH
Sau khi thay chữ, duyệt lại từng class mang MÀU/NGHĨA, hỏi *"câu MỚI nằm trong đó có đúng
sắc thái đó không":*

| Class | Sắc thái nó áp | Lỗi đã dính THẬT |
| :-- | :-- | :-- |
| `sg-warn` | khung **cảnh báo đỏ** | HPD slide 10 bọc câu **tích cực** ⇒ màn hình cảnh báo một điều tốt |
| `hk-strike` | **gạch ngang = phủ định** | MSR slide 10 gạch ngang câu chốt ĐÚNG |
| `hk-vs-old` | đỏ = vế **xấu** | HPD slide 6 tô đỏ một vế trung tính ⇒ ngầm phán "xấu" |
| `flow-new` | xanh lá = **trạng thái mới, TỐT** | sp02 slide 3 bọc *"cuốn sổ chưa vào công trường"* = **nguyên nhân gây lỗi** ⇒ xanh lá khen một điều xấu. Vá: đổi hổ phách |
| `core-module` | **mờ có chủ đích** — nó thiết kế cho `data-mode="highlight"` | sp02 slide 4: deck không dùng mode đó ⇒ 4 thẻ mờ gần như không đọc được, mà `validate` PASS. `deck_sp02` đã có khối CSS bật sáng lại ở cuối `style.css`, thừa kế được |
| `sg-num` | huy hiệu **1 KÝ TỰ** | HPD slide 5 nhét `"KH 2026"` ⇒ chữ tràn |

**Bài dạy thì màu cũng phải dạy đúng. Đỏ chỉ dùng cho cái người xem PHẢI tránh.**
⚠️ Riêng bài 05: màu ĐỎ mang nghĩa *"phép thử đang hỏng, ĐÚNG như mong đợi"* — tức điều
**TỐT**. Đừng để màn hình trông như đang báo lỗi. Ghi rõ trong README cách bạn xử lý.

---

## 6. SOI ẢNH — KHÂU KHÔNG BỎ ĐƯỢC

`Read` **TỪNG** file `/tmp/escbase-qa/deck_spXX/slide1.png` … `slide10.png`. Soi 5 thứ:
1. chữ tràn / đè / nhãn quá nhỏ
2. khoảng trống chết (visual lọt thỏm giữa safezone)
3. **màu có mâu thuẫn với nghĩa của câu không** (bảng mục 5)
4. số trên màn hình có khớp lời đọc không
5. **hai slide liền nhau có cùng một dạng hộp không**

**`validate` PASS KHÔNG có nghĩa slide đúng.** Bằng chứng: bài HPD PASS cả 2 lượt mà soi ảnh
vẫn ra 4 lỗi, 1 trong đó là lỗi NGHĨA. Bài sp02 thước `DAT` ngay vòng đầu + validate PASS mà
vẫn còn 3 lỗi. Vá xong thì **validate lại + capture lại + soi lại**.

---

## 7. BỐN BẪY ĐÃ TRẢ GIÁ — ĐỪNG DẪM LẠI

1. 🔴 **DÙNG ĐƯỜNG DẪN TUYỆT ĐỐI cho mọi lệnh đọc/ghi file.** cwd bị reset giữa phiên ít
   nhất 2 lần. Đã dính: `cat >> style.css` tạo file **rác** ở gốc template (sửa không vào
   deck), và `ls` báo "không có file" trong khi file có thật.
   ⚠️ **Dấu hiệu duy nhất của ca thứ nhất: validate in ra SỐ Y HỆT LƯỢT TRƯỚC.**
   **Số đo đứng im sau khi sửa ⇒ nghi sửa nhầm file, đừng nghi thước.**
2. ⚠️ **Mẫu hình gallery mặc định TRÀN safezone** khi nhét chữ tiếng Việt (dài hơn nhãn mẫu).
   Ca sp02: **5/10 slide FAIL lượt validate đầu, siết 3 vòng mới PASS.** Tính trước 2-3 vòng
   siết, đừng coi là hỏng. CSS thêm ghi **CUỐI** `deck_spXX/style.css` (file có 4 khối
   `:root` chồng nhau, khối sau thắng).
3. ⚠️ **Mẫu gallery có thể phụ thuộc một `data-mode`.** Chép mẫu nào cũng phải hỏi *"nó cần
   mode nào"* — xem `core-module` và `vpg-traffic-pole` ở trên.
4. ⚠️ **`.slide-element` tìm bằng `querySelectorAll`** ⇒ nằm sâu bao nhiêu cũng thành 1 reveal.
   Thẻ con trong grid tự làm reveal được, không bắt buộc là con trực tiếp của `.slide-content`.

**Số đo tham chiếu (đừng đoán lại):** sp02 = 394 từ · giọng 113,2s · render 235,4s
(69,3 ms/khung) · 24,7 MB. Nhịp đọc **3,56 từ/giây** ⇒ ước lượng được độ dài ngay từ bản nháp.

---

## 8. BÀN GIAO — báo gì cho thợ 1 (mỗi bài một lần, đừng đợi xong cả 6)

1. Đường dẫn 3 file lời + deck.
2. Dán **nguyên dòng** `KETLUAN|...` của thước và **nguyên dòng in reveal**.
3. `validate` PASS hay không.
4. Đã dùng 2 mẫu hình được giao ở slide nào.
5. Lỗi bạn tự soi ảnh bắt được và đã vá.
6. **Chỗ bạn thấy còn yếu nhất, nói thẳng.** Đừng tự khen.

⚠️ **Cấm phán về giọng, nhịp, nhạc, mượt hay giật — AI không nghe được.** Cái đó để BOSS nghe
rồi phán. Đừng bao giờ viết "giọng nghe tự nhiên" — đó là bịa.

**Thợ 1 sẽ tự chạy lại thước, tự soi lại ảnh, rồi mới render.** Không phải vì không tin bạn,
mà vì đó là luật của dây chuyền: đầu ra là ảnh thì phải mở ra soi, không tin exit code.
