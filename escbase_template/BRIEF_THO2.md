# BRIEF THỢ 2 — dựng 1 deck escbase (bài 06→10)

Đọc hết file này trước khi gõ lệnh đầu tiên. Nó gói sẵn mọi thứ đã trả giá để
biết — làm theo thì không phải mò lại.

---

## 1. VIỆC CỦA BẠN — và việc TUYỆT ĐỐI KHÔNG làm

**Làm:** B1 → B7 (chép khuôn, đồng bộ lời, dựng `index.html`, đổi màu, validate,
chụp ảnh, **soi từng ảnh**).

**KHÔNG LÀM: B8/B9 — không render, không gọi `render_edgetts.py`, không ffmpeg.**
Lý do đã trả giá 24/07: render chạy nền trong phiên con thì khi phiên con kết thúc
tiến trình bị **mồ côi và treo** (0% CPU, không có chromium). Thợ 1 (phiên chính)
render. Bạn dựng xong thì bàn giao.

**Cũng KHÔNG:** viết lại lời, sửa chữ trong lời, tự chọn màu khác bảng phân sẵn.

---

## 2. ĐẦU VÀO

| Thứ | Ở đâu |
| :-- | :-- |
| **Lời đã chốt** (10 dòng = 10 slide) | `video/kichban/escbase_10dong/<bài>.txt` |
| Nội dung gốc (đọc để HIỂU, không chép) | `video/kichban/0X_*.md` |
| **Deck mẫu để chép** | `slide/claude-code-skill-cam-nang` (bài 05, mới nhất, sạch) |
| Chỗ chạy | `video/escbase_template/`, luôn dùng `.venv/bin/python` |

Lời đã được viết theo khuôn 7 nhịp của BOSS rồi. **Nhiệm vụ của bạn là dựng HÌNH
cho lời đó**, không phải biên tập lời.

---

## 3. BẢNG PHÂN BÀI (lấy đúng dòng của mình)

| Bài | File lời | Slug deck phải tạo | Mã màu |
| :-- | :-- | :-- | :-- |
| 06 | `06_mcp.txt` | `claude-code-mcp-phich-cam` | `06` sky + lime |
| 07 | `07_plan_mode.txt` | `claude-code-plan-mode-ban-truoc` | `07` teal + cam |
| 08 | `08_checkpoint.txt` | `claude-code-checkpoint-quay-nguoc` | `08` tím + lục |
| 09 | `09_context.txt` | `claude-code-token-cang-lau-cang-dat` | `09` cam + sky |
| 10 | `10_ket.txt` | `claude-code-ghep-chin-manh` | `10` lục + vàng |

Màu đã phân trung tâm để 10 bài không đụng nhau (01 xanh lá · 02 indigo · 03 amber ·
04 cyan · 05 rose). **Đừng tự đổi.**

---

## 4. BẢY BƯỚC

```bash
cd video/escbase_template
SLUG=claude-code-<slug của bạn>
BAI=<06|07|08|09|10>

# B1. chép khuôn từ deck bài 05 (bỏ output cho nhẹ)
cp -R slide/claude-code-skill-cam-nang slide/$SLUG && rm -rf slide/$SLUG/output

# B3. đồng bộ lời vào ĐÚNG 3 NƠI (đừng chép tay!)
.venv/bin/python sync_script.py slide/$SLUG ../kichban/escbase_10dong/${BAI}_*.txt
#   -> in bảng "slide | số câu". SỐ CÂU = SỐ THẺ .slide-element phải dựng ở slide đó.
#      Chép bảng này ra giấy, B4 phải khớp từng dòng.

# B5. đổi palette (một lượt, đồng thời, an toàn)
.venv/bin/python remap_palette.py slide/$SLUG $BAI

# B6. validate — PHẢI PASS, cấm dùng --skip-safezone
.venv/bin/python validate_slide.py slide/$SLUG --semantic-report

# B7. chụp rồi SOI TỪNG ẢNH
.venv/bin/python capture_slides.py slide/$SLUG
#   -> /tmp/escbase-qa/$SLUG/slide1..10.png  — phải Read TỪNG file
```

**B4 (nằm giữa B3 và B5) — sửa `index.html`:**
- Đúng **10 slide**, mỗi slide đúng số `.slide-element` theo bảng ở B3.
- Đổi `<title>`, `<meta name="description">`.
- Đổi `?v=claude-code-skill-cam-nang` thành `?v=$SLUG` ở **2 chỗ** (link CSS + thẻ script).
- Giữ nguyên: 2 góc `dungladu.vn`, `<div class="slide-bg slide-bg-N">`, `<canvas ... data-fx="particles">`.
- Slide 1 là HERO: giữ khối `pixelle-hero-orbit`, chỉ thay icon/chữ/chip.

---

## 5. THƯ VIỆN CẢNH CÓ SẴN — dùng lại, ĐỪNG bịa tên lớp

Tất cả đã có CSS trong `style.css`. **Bịa tên lớp mới = hiện ra không có kiểu dáng,
và validate vẫn PASS nên bạn sẽ không biết cho tới lúc soi ảnh.**

```html
<!-- tiêu đề slide: nhãn nhỏ + tiêu đề lớn (chữ trong <em> ăn màu primary) -->
<div class="hk-head hk-row"><span class="hk-kicker">nhãn nhỏ</span><h2 class="hk-title">tiêu đề <em>nhấn</em></h2></div>

<!-- dải chữ tròn 1 dòng (thêm hk-note-cost cho sắc cảnh báo) -->
<div class="hk-note"><i class="fa-solid fa-bolt"></i> chữ ngắn <b>nhấn</b></div>

<!-- thẻ ĐÚNG / SAI -->
<div class="hk-branch">
  <div class="hk-answer hk-answer-ok"><i class="fa-solid fa-check"></i> vế đúng</div>
  <div class="hk-answer hk-answer-no"><i class="fa-solid fa-xmark"></i> vế sai</div>
</div>

<!-- so sánh CŨ -> MỚI -->
<div class="hk-versus">
  <div class="hk-vs-node hk-vs-old"><i class="fa-solid fa-x"></i><b>CŨ</b><span>mô tả</span><div class="hk-strike"></div></div>
  <div class="hk-vs-arrow"><i class="fa-solid fa-arrow-right-long"></i></div>
  <div class="hk-vs-node hk-vs-new"><i class="fa-solid fa-check"></i><b>MỚI</b><span>mô tả</span></div>
</div>

<!-- đường dẫn / tên mã -->
<div class="hk-names cm-names-big"><code class="hk-name-key">.claude/abc/</code></div>

<!-- thẻ file có dòng đánh số -->
<div class="sc-file">
  <div class="sc-file-top"><i class="fa-solid fa-file-lines"></i><code>TÊN.md</code></div>
  <p class="sc-file-line"><span class="sg-num">1</span> dòng một</p>
</div>

<!-- cửa sổ dòng lệnh -->
<div class="mock-terminal hk-term sc-say">
  <div class="terminal-bar"><span class="td red"></span><span class="td yellow"></span><span class="td green"></span><span class="terminal-title">tiêu đề</span></div>
  <div class="terminal-body"><code class="terminal-line"><span class="t-prompt">›</span> lệnh</code></div>
</div>

<!-- thanh chi phí -->
<div class="cm-cost">
  <div class="cm-cost-row"><span class="cm-cost-tag">×9</span><div class="cm-cost-bar"><span></span></div></div>
  <p class="cm-cost-label">nhãn có <b>nhấn</b></p>
</div>

<!-- phiên mới đọc lại -->
<div class="cm-sessions">
  <span class="cm-session">phiên mới</span><i class="fa-solid fa-arrow-right-long"></i><span class="cm-session cm-session-read"><i class="fa-solid fa-file-lines"></i> đọc lại</span>
  <div class="cm-session-pulse"></div>
</div>

<!-- dãy ô bật/tắt (10 phiên, 30 ngày...) -->
<div class="sc-repeat"><span class="sc-day sc-day-on"><i class="fa-solid fa-check"></i></span><span class="sc-day">·</span></div>

<!-- thẻ gạch bỏ -->
<div class="cm-dont-card"><i class="fa-solid fa-code"></i><span>chữ NGẮN</span><div class="hk-strike"></div></div>

<!-- huy hiệu số + mô tả -->
<div class="sg-zero"><span class="sg-zero-badge">0</span><div class="sg-zero-txt"><b>đậm</b><span>mô tả</span></div></div>

<!-- tờ giấy / kết luận -->
<div class="sg-paper"><i class="fa-solid fa-file-lines"></i><div class="sg-paper-txt"><b>đậm</b><span>mô tả</span></div></div>

<!-- hai đầu não / mũi tên -->
<div class="sg-sub">
  <div class="sg-brain sg-brain-main"><i class="fa-solid fa-user"></i><span>bạn</span></div>
  <i class="fa-solid fa-arrow-right-long sg-sub-arrow"></i>
  <div class="sg-brain sg-brain-sub"><i class="fa-solid fa-brain"></i><span>phiên con</span></div>
</div>

<!-- dãy chip kiểm chứng -->
<div class="sg-verify"><span class="sg-verify-head"><i class="fa-solid fa-shield-halved"></i> đầu đề</span><span class="sg-vchip">chip</span></div>

<!-- chồng biểu tượng + đếm -->
<div class="sg-stack"><i class="fa-regular fa-file-lines"></i><span class="sg-count">nhãn</span></div>

<!-- CHỐT bài (slide 10): 2 khối đối xứng -->
<div class="hk-lockup hk-lockup-a"><i class="fa-solid fa-location-dot"></i><span class="hk-lockup-line"><strong>Vế một.</strong></span></div>
<div class="hk-lockup hk-lockup-b"><div class="glowing-orb"></div><i class="fa-solid fa-bolt"></i><strong>Vế hai.</strong></div>
```

Muốn xem thêm: mở `slide/claude-code-hook-cai-khoa`, `...-claude-md-noi-quy`,
`...-slash-command-cai-nut`, `...-subagent-sai-nguoi-di`, `...-skill-cam-nang`.

---

## 6. SÁU CÁI BẪY — đọc kỹ, đây là phần đắt nhất của brief

**1. `<br>` trần LÀM VỠ BỘ ĐẾM REVEAL.** (24/07) Thêm `<br>` vào `index.html` khiến
parser của `validate_slide.py` gộp slide 6→10 thành một, báo *"Slide 10: 3 script
sentences != 15 reveal units"*. **Luôn viết `<br />`** (tự đóng).

**2. `hk-strike` (gạch bỏ) có BỀ NGANG CỐ ĐỊNH.** Chữ dài hơn thì gạch chỉ che được
một phần, nhìn rất lỗi. Giữ chữ trong `cm-dont-card`/`hk-vs-old` **ngắn (~10-12 ký tự)**.

**3. CÒN MÀU HARDCODE NGOÀI BẢNG.** `remap_palette.py` chỉ đổi 8 màu vai trò. Trong
`style.css` vẫn còn mã màu lẻ của template gốc. 24/07 sót `#a5a0ff` (icon hiện ra
TÍM) và `#cdeffd` (chữ hiện ra XANH) giữa deck rose+gold — **validate PASS hoàn toàn**,
chỉ soi ảnh mới thấy. ⇒ Soi ảnh thấy màu lạ thì `grep` mã màu đó trong `style.css` rồi sửa.

**4. DÒNG MÃ KHÔNG ĐƯỢC NGẮT GIỮA CHỪNG.** Khối `hk-name-key` chỉ chứa **~20 ký tự
một dòng**. Đường dẫn dài sẽ tự ngắt giữa từ (`tham-` / `dinh-dn`), đọc rất xấu.
⇒ Rút ngắn, hoặc chủ động xuống dòng **đúng chỗ dấu `/`** bằng `<br />`.

**5. TRÀN SAFEZONE.** Khung 390×693, nội dung phải nằm trong `top>=100px` và chừa
`>=200px` đáy (chỗ của phụ đề). Tràn thì: bớt một dòng chữ dài (hiệu quả nhất, mỗi
dòng ~17px), bỏ bớt một khối phụ, hoặc thêm `hk-content-tight` vào `slide-content`
(⚠️ lớp này nhiều khi **không ăn gì** — đừng trông cậy vào nó).

**6. EXIT CODE 0 KHÔNG CÓ NGHĨA LÀ ĐÚNG.** Cả 4 lỗi trên đều lọt qua validate.
**Bắt buộc `Read` từng file PNG.** Không được báo xong khi chưa mở đủ 10 ảnh.

---

## 7. SOI ẢNH — nhìn những gì

Với **từng** ảnh trong `/tmp/escbase-qa/$SLUG/`:

- [ ] Chữ có bị **cắt / tràn / chồng** lên nhau không?
- [ ] Có **màu nào lạc** khỏi palette bài mình không? (bẫy 3)
- [ ] Gạch `hk-strike` có **che hết chữ** không? (bẫy 2)
- [ ] Dòng mã có **ngắt giữa từ** không? (bẫy 4)
- [ ] Khối chính có **lấp đầy khung** không, hay bé tí lọt thỏm giữa khoảng trống?
- [ ] 2 góc `dungladu.vn` còn nguyên?
- [ ] Slide này có **khác diện mạo** slide trước không, hay lại là cái hộp chữ y hệt?

---

## 8. BÀN GIAO — báo về đúng những mục này

1. Slug deck đã tạo.
2. Bảng `slide | số câu | số .slide-element` — chứng minh khớp 1:1.
3. Kết quả `validate_slide.py`: PASS hay FAIL (dán dòng cuối).
4. Kết quả `remap_palette.py`: tổng số chỗ đổi, có sót không.
5. **Đã Read đủ 10 ảnh chưa** — và liệt kê lỗi đã tìm thấy + đã sửa thế nào.
6. Chỗ nào bạn thấy chưa ưng nhưng chưa sửa được.

⚠️ **Nói thật.** Bỏ bước nào thì khai ra. Thợ 1 sẽ validate + soi lại toàn bộ; báo
cáo đẹp mà ảnh xấu thì chỉ tốn thêm một vòng cho cả hai.
