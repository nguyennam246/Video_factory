---
name: video-baocao
description: >
  Dây chuyền dựng VIDEO BÁO CÁO TÀI CHÍNH dọc 9:16 từ hồ sơ doanh nghiệp trong
  `Research copy/baocao/hoso/{MÃ}_HoSo.md` ra mp4 hoàn chỉnh. Dùng skill này bất cứ khi
  nào BOSS bảo "dựng video báo cáo {MÃ}", "làm video {MÃ}", "ra video {MÃ}", hoặc muốn
  làm video đánh giá/phân tích một mã cổ phiếu. Bao gồm: cập nhật giá trước khi viết lời,
  khuôn kịch bản 10 slide, thước tự kiểm 0 API, dựng deck escbase headless, sinh giọng,
  soi ảnh, nghiệm thu bằng máy, và ghi 4 sổ. Cũng kích hoạt khi nhắc "deck tài chính",
  "kịch bản 10 dòng", "khuôn [1,2,3,3,3,3,2,2,3,3]", "nghiệm thu video", hay khi cần
  rút kinh nghiệm/cập nhật quy trình làm video sau mỗi bài.
---

# LÀM VIDEO BÁO CÁO TÀI CHÍNH

**Mục đích bộ video** (BOSS đặt): *"Tôi chỉ xem video là hiểu vấn đề và làm được, chia sẻ
lại được."* Dọc 9:16, tiếng Việt, xem trên điện thoại.

**Vai khi viết lời** (3 phẩm chất KHÔNG đánh đổi cho nhau): nhà phân tích **sắc bén** +
**trung thực tuyệt đối** + **hấp dẫn dễ hiểu với người mới**.

**⭐ Chạy một lệnh (25/07/2026):**
`python3 video/lam_bai.py --ma msr02 --ten danhgia --loai baocao --goc nghich_ly_so`
— runner giữ đúng thứ tự 9 bước, lấy nhịp từ **góc tiếp cận** (bỏ `--goc` thì về khuôn
`[1,2,3,3,3,3,2,2,3,3]`), palette `tc`, đóng cổng
chặn ở thước/soi ảnh/nghiệm thu. Mã thoát: `10` thước FAIL · `20` cần thợ 1 · `30` chờ soi ảnh ·
`40` chờ BOSS. ⚠️ **Runner KHÔNG cập nhật giá** — phải chạy đủ 4 lệnh giá TRƯỚC (mục dưới).

---

## 0. BA LUẬT SỐNG CÒN — đọc lại mỗi lần, đây là chỗ trả giá đắt nhất

1. **AI KHÔNG NGHE ĐƯỢC.** Cấm viết "giọng nghe tự nhiên", "nhạc vừa phải", "đọc mượt" —
   đó là bịa. Mọi phán xét *giọng · nhịp · mức nhạc · mượt hay giật* phải để **BOSS nghe
   rồi phán**. Số đo của máy chỉ chứng minh "không còn nguyên nhân kỹ thuật", không thay
   được tai người.
2. **Đầu ra là ẢNH/VIDEO thì phải MỞ RA SOI.** `validate` PASS **không** có nghĩa slide
   đúng. Ca HPD: PASS cả 2 lượt mà soi ảnh vẫn ra 4 lỗi, trong đó 1 lỗi NGHĨA. `Read`
   từng file PNG, và soi vài frame của video thật.
3. **Chỉ từ FACTS trong hồ sơ. Không bịa, không bóp méo. Đúng là đủ.** Không suy diễn,
   không tự tính hộ con số mà tài liệu không đưa ra, không kết luận đắt/rẻ, không khuyến
   nghị mua bán dưới mọi hình thức.

**BOSS chốt về độ dài:** *"không cần làm quá ngắn — đúng là đủ."* Bài 100-165 giây là bình
thường. Nhưng khuôn tài chính vẫn giữ trần 380 từ (xem mục 3).

---

## 1. NGUỒN SỰ THẬT — đọc đúng những file này, đừng đọc lan man

| File | Lấy gì |
| :-- | :-- |
| `Research copy/baocao/hoso/{MÃ}_HoSo.md` | **NGUỒN SỐ 1.** Mục ① 8 khoang · ② SỔ RỦI RO · ③ ĐỊNH GIÁ & SỐ |
| `Research copy/baocao/{MÃ}_BaoCao.md` | **NGUỒN SỐ 2** — phán quyết + số Ratio/Thể trạng |
| `video/kichban/escbase_10dong/hpd_01_danhgia.txt` | **MẪU giọng văn + nhịp câu đích.** Nội dung không liên quan, đừng chép ý |
| `video/kichban/escbase_10dong/README_hpd.md` | mẫu báo cáo truy vết |

Cần tra sâu thì đọc thẳng `baocao/MD/{BCTC,BCTN,NQ}/{MÃ}_*.md` (rất dài, chỉ khi thật cần).

⚠️ **KIỂM ĐƠN VỊ.** Nhiều BCTC in bằng **nghìn VND** (thuyết minh ghi "làm tròn đến hàng
nghìn"); số trong bảng ×1.000 mới ra đồng. Đọc nhầm đơn vị là sai cả bài.

⛔ **CẤM lấy mục "chờ soi / tranh chấp" của hồ sơ làm kết luận** — lớp đó đo chỉ đúng 8%.
Chỉ dùng dữ kiện đã xác nhận.

---

## 2. BƯỚC 1 — LÀM MỚI GIÁ TRƯỚC KHI VIẾT LỜI (đừng bỏ qua)

Hồ sơ "đã có sẵn" **không** có nghĩa dùng được ngay: giá trong đó thường cũ hàng tuần, mà
video thì đọc to ngày tháng lên màn hình. Xem ngày ở mục ③ trước.

```bash
cd "/Users/simple/Desktop/Cloud/Research copy"
python3 scripts/capnhat_gia.py --symbols {MÃ}
python3 scripts/fireant_pull.py pull {MÃ} --update
python3 scripts/q5_calc.py {MÃ}
python3 scripts/gen_trang_dn.py {MÃ}
```

🔴 **PHẢI CHẠY CẢ 4, đặc biệt là 2 lệnh đầu.** `capnhat_gia.py` làm mới giá và **P/B**
nhưng **KHÔNG** làm mới **P/E** (`pb_raw` tính từ giá hiện tại, còn `pe_raw` đọc ảnh chụp
FireAnt trong DB — chỉ `fireant_pull` làm mới). Chạy `capnhat_gia` một mình ⇒ hồ sơ có
**P/B đứng trên giá mới, P/E đứng trên giá cũ**, không cảnh báo gì. Đo thật ca MSR: P/B
3,28→3,02 (đúng) nhưng P/E vẫn y nguyên 51,85; chạy thêm `fireant_pull` mới về 48,07.

### 🔴🔴 NÓI "GIẢM X% TỪ ĐỈNH" THÌ PHẢI KIỂM CHIA THƯỞNG TRƯỚC (BOSS bắt được 25/07, ca PNJ)

`dulieu/gia.db` lưu giá **THÔ, KHÔNG hồi tố corporate action**. Cột `adj_close` **không cứu**
(không phải chuỗi back-adjust chuẩn — có ngày `adj_close > close`). Bài PNJ 01 đọc thẳng
127.000đ làm đỉnh ⇒ nói **"−76%"**, đúng phải là **"−64% từ 84.667đ"** vì PNJ thưởng cổ phiếu
**50% ngày 23/04/2026**. Sai 12 điểm phần trăm, ngay con số TO NHẤT của bài.

**Dò 30 giây, làm TRƯỚC khi viết bất kỳ câu nào có chữ "từ đỉnh":**
```bash
cd "/Users/simple/Desktop/Cloud/Research copy"
# ① có chia thưởng / chia tách năm nào không
sqlite3 dulieu/BCTC.db "SELECT year,cash_dividend,stock_dividend FROM dividends WHERE symbol='PNJ' ORDER BY year DESC LIMIT 6;"
# ② mỏ neo RẺ NHẤT: nhà cung cấp đã điều chỉnh sẵn -> đọc high52Week
sqlite3 dulieu/BCTC.db "SELECT json FROM fundamentals WHERE symbol='PNJ';"
# ③ soi đứt gãy >15% qua 1 phiên trong chuỗi close (ngày đứt = ngày GDKHQ)
```
**Ba cái khớp nhau mới tin.** Ca PNJ: `stock_dividend=50.0` · `high52Week=84666.67` ·
đứt gãy 110,0 → 75,1 đúng ngày 23/04 — cả ba chỉ về **127.000 ÷ 1,5 = 84.667**.

⚠️ Cùng bẫy này áp cho mọi mã hay chia thưởng (PNJ chia 2026·2022·2019·2018·2015·2012).

---

## 3. BƯỚC 2 — VIẾT LỜI THEO KHUÔN TÀI CHÍNH 10 SLIDE

Khuôn này BOSS chốt sau khi xem bản 1 và phán 4 điều: ① 3 giây đầu phải là HOOK, vào thẳng
· ② không giải thích ví dụ lan man · ③ **CẤM nói về hệ thống phân tích của dự án** ·
④ chỉ từ facts.

| Slide | Vai | Câu |
| :-- | :-- | :-: |
| 1 | **HOOK** ≤16 từ, nghịch lý bằng SỐ | 1 |
| 2 | đặt bài: công ty gì + con số đẹp | 2 |
| 3-6 | mỗi slide **1 fact + 1 câu giải nghĩa thuật ngữ cho người mới** | 3 |
| 7 | **MẶT KIA** — cái tốt có thật / cái chưa xác nhận (BẮT BUỘC, chống bóp méo) | 2 |
| 8 | **điều báo cáo KHÔNG trả lời được** | 2 |
| 9 | **dạy nghề: 3 câu hỏi tự hỏi khi cầm báo cáo** | 3 |
| 10 | chốt + câu miễn trừ, **đối xứng lại hook** | 3 |

⇒ `[1,2,3,3,3,3,2,2,3,3]` = **25 reveal · 300-380 từ**.

### 🆕⭐ 25/07: KHUÔN TRÊN LÀ **MẶC ĐỊNH**, KHÔNG CÒN BẮT BUỘC — chọn GÓC trước đã

Khuôn cứng làm MSR · HPD · TCL · SKV · MCF **cùng một nhịp thở**, xem 3 bài liền là
thấy chung một khung. Sự thật kỹ thuật: engine chỉ ép `số câu dòng N == số
.slide-element slide N` ([auto_render.py:951](../../../escbase_template/auto_render.py:951)),
**không ép khuôn nào cả**. Cái khuôn là ta tự trói cho tiện tái dùng deck.

**Từ nay: đọc hồ sơ + Q8 (`/valuation-check`) + Q9 (`/devil-advocate`), hỏi *"điều gây
bất ngờ nhất ở mã này là gì?"*, rồi chọn góc trong `video/goc/README.md`.** Mỗi góc có
nhịp câu riêng, cách mở 11 từ riêng, bản đồ scene riêng, bẫy riêng.

| Điều bất ngờ nhất | Góc |
| :-- | :-- |
| hai số đáng lẽ đi cùng nhau lại ngược nhau | `nghich_ly_so` |
| giá đang ngầm giả định một điều khó xảy ra | `gia_da_tinh_san` |
| có một thứ đủ sức chấm dứt cuộc chơi | `thu_giet_dn` |
| vừa rơi rất sâu — rơi vì cái gì | `ho_voi` |
| lời kể và con số không khớp | `bang_chung` |
| vị trí trong chu kỳ mới là chuyện chính | `dong_ho_chay` |

**Hai mã liền nhau không được cùng góc** — ghi vào `video/goc/NHAT_KY.md` trước khi viết lời.
⚠️ Luật cấm **không** nới theo góc: vẫn cấm kết luận đắt/rẻ, cấm khuyến nghị, cấm dọa dẫm.
Sức hút đến từ **nghịch lý có thật trong số liệu**, không từ tính từ mạnh.

💡 **BOSS hỏi "nhà đầu tư nên làm gì lúc này?" thì KHÔNG phải xin miễn `CAM_KHUYEN`.** Góc
`viec_can_lam` (25/07) giải bằng cách **đổi câu hỏi**: từ *"rẻ chưa / có nên mua"* sang
*"cái chưa biết lớn cỡ nào, và nó sẽ hiện ra ở đâu"*, rồi giao **3 việc kiểm chứng được**
(mở đúng tên thuyết minh · đếm đúng kỳ báo cáo · viết ra trước con số khiến bạn đổi ý).
Vừa trả lời đúng thứ BOSS muốn, vừa không câu nào phán mua/bán.

### 🆕⭐ 25/07 chiều: **HAI ĐƯỜNG ĐI — chọn TRƯỚC khi bắt đầu, đừng mặc định đường đắt**

BOSS hỏi *"quy trình chuẩn rồi, render cũng nhanh, sao tổng thể tốn thời gian thế?"* — đo ra
thì **render đúng là không tốn** (186,9s máy chạy, 0 token). Tốn nằm ở 3 luật ta TỰ đặt:

| | **Đường MỞ ĐƯỜNG** (mặc định của `lam_bai.py`) | **Đường RẺ** (bài làm lại · bài gấp · nhịp trùng deck cũ) |
| :-- | :-- | :-- |
| Kịch bản | `b1` spawn **subagent Opus NGUỘI**, đề bài bảo *"tự tra tài liệu trong repo"* | **Opus phiên chính tự viết** — số liệu đã nằm sẵn trong ngữ cảnh, không việc gì re-derive |
| Deck | `b2` spawn Sonnet + **bắt đẻ ≥1 scene mới** + tra catalogue **bằng ảnh** (12 MB / 18 ảnh) | **chép deck tài chính đã gỡ lỗi, CHỈ THAY CHỮ.** Đảo chiều: *viết lời VỪA nhịp deck sẵn có* thay vì bẻ deck theo lời |
| Soi ảnh | `Read` slide1..10 × 2-3 vòng = **20-30 lượt đọc ảnh** (kho 1 bài 7,8 MB) | **`contact_sheet.py`** → lướt **1 tấm 2,0 MB**, chỉ zoom slide nghi ngờ |
| Được | kho scene lớn dần, deck không lặp | nhanh, ít lỗi (deck cũ đã trả giá rồi) |
| Mất | thời gian + token + vòng vá scene mới chưa ai test | bài trùng nhịp bài cũ |

🔴 **Đường rẻ KHÔNG được cắt 3 thứ:** thước kịch bản · `validate --semantic-report` · soi ảnh
(chỉ đổi thứ tự **LƯỚT → ZOOM**, không bỏ). Đó là 3 cổng bắt lỗi thật.

### ⭐ ĐÃ ĐÓNG THÀNH CỜ `--duong re` TRONG RUNNER (25/07 chiều, BOSS lệnh "áp vào lam_bai.py")

Không phải gõ tay từng bước nữa — runner tự đi đường rẻ:
```bash
python3 video/lam_bai.py --ma pnj03 --ten hanhdong --loai baocao \
        --goc viec_can_lam --duong re
```
Runner tự làm 5 việc: ① b1 và b2 **bàn giao thẳng thợ 1** (mã 20), brief đã nhét sẵn bảng
class mang màu/nghĩa · ② `--mau` **tự chọn** deck trong `DECK_DA_GO_LOI` có nhịp **trùng**
nhịp góc; không deck nào khớp thì **dừng và gợi ý 3 cách sửa** · ③ chép deck thì **dọn
`script-90s.txt` của bài cũ** (không dọn thì b1 tưởng đã có lời, bài mới chạy bằng lời bài
cũ) · ④ b5 đo `style.css` còn mã **cần đổi thật** không, 0 thì bỏ qua remap · ⑤ b7 tự sinh
contact sheet và in **LƯỚT → ZOOM**.

⚠️ **Nhịp là ràng buộc cứng ở đường rẻ:** deck lệch nhịp ⇒ runner chặn ngay bước 0, không
đợi tới render. Muốn đi rẻ mà nhịp không khớp thì đổi `--goc`, sửa `nhip:` trong file góc,
hoặc chấp nhận `--duong mo-duong`.

```bash
# contact sheet chạy riêng cũng được (tự đếm số slide, nhận tên deck hoặc đường dẫn)
cd /Users/simple/Desktop/Cloud/video/escbase_template
.venv/bin/python contact_sheet.py deck_{mã}01   # -> /tmp/escbase-qa/deck_{mã}01/_contact_sheet.png
```
**Đo thật bài PNJ 02 đi đường rẻ:** 1 lượt thước (ĐẠT ngay vòng 1) · 2 lượt validate · 2 lượt
capture · **2 lượt đọc ảnh** · **0 subagent** · 0 API trả phí.
So bài PNJ 01 cùng ngày đi đường mặc định: 2 subagent + 2 scene tự dựng + **4 lỗi chỉ soi ảnh
mới thấy**.

### Luật hook
Câu 1 nói thẳng vấn đề. **Từ đầu tiên phải là SỐ hoặc danh từ cụ thể.** Cấm mở bằng
"có một…", "hãy tưởng tượng…". Hook phải đặt ra **nghịch lý người xem không tự trả lời
được**, rồi slide 3-6 mới trả lời — đừng nói luôn nguyên nhân, nói ra là hết tò mò.
**Viết 3 phương án hook**, chọn 1, ghi lý do vào README, để BOSS đổi nếu muốn.

### Sản phẩm bước này — 3 file, không ghi file nào khác
```
video/kichban/escbase_10dong/{mã}_01_danhgia.txt          ← LỜI ĐỌC, đúng 10 dòng
video/kichban/escbase_10dong/{mã}_01_danhgia.man_hinh.md  ← gợi ý chữ màn hình
video/kichban/escbase_10dong/README_{mã}.md               ← truy vết + 3 hook + tự kiểm
```
File lời: không tiêu đề, không đánh số, không dòng trống. Mỗi dòng = 1 slide.
**Số viết ra CHỮ** ("ba mươi ba nghìn năm trăm"), vì máy đọc số rất xấu.

### Chạy thước NGAY sau bản nháp đầu
```bash
cd /Users/simple/Desktop/Cloud/video
python3 .claude/skills/video-baocao/thuoc/thuoc_kichban.py \
        kichban/escbase_10dong/{mã}_01_danhgia.txt --goc nghich_ly_so
```
`--goc` thì thước đo theo nhịp của góc; bỏ `--goc` thì quay về khuôn cũ (bài cũ vẫn chạy).
Phải ra `DAT`. **Đừng ước lượng độ dài bằng cảm giác**: bản nháp HPD viết "đúng ý" ra
**521 từ**, vượt trần 37%, siết 3 vòng mới về 380 — một số như *"hai mươi bảy phẩy bảy tỷ"*
là **6 từ**. Khi siết, **cắt ở SỐ** (đọc tròn: "gần hai mươi tám tỷ") chứ đừng cắt ý.

---

## 4. BƯỚC 3 — DỰNG DECK

**Luôn chép từ một deck TÀI CHÍNH đã ra video** (`deck_hpd01` hoặc `deck_msr01`): khuôn
reveal `[1,2,3,3,3,3,2,2,3,3]` khớp sẵn, palette `tc` (vàng `#ffb020` + đỏ `#ef4444`) đã
đúng ⇒ **không phải chạy `remap_palette.py`**.

```bash
cd video/escbase_template
cp -R headless/deck_hpd01 headless/deck_{mã}01
rm -rf headless/deck_{mã}01/output headless/deck_{mã}01/output_headless
cp ../kichban/escbase_10dong/{mã}_01_danhgia.txt headless/deck_{mã}01/script-90s.txt
.venv/bin/python sync_script.py headless/deck_{mã}01 headless/deck_{mã}01/script-90s.txt
# sửa index.html: thay chữ, GIỮ NGUYÊN cấu trúc scene + số .slide-element mỗi slide
# đổi <title>, <meta name="description">, và cả hai ?v=… (style.css và app.js)
.venv/bin/python validate_slide.py headless/deck_{mã}01 --semantic-report   # phải PASS
```

Kiểm số reveal sau khi sửa HTML:
```bash
python3 -c "import re;s=open('headless/deck_{mã}01/index.html',encoding='utf-8').read();\
print([p.count('slide-element') for p in re.split(r'<div class=\"slide[ \"]',s)[1:]])"
# phải in ra [1, 2, 3, 3, 3, 3, 2, 2, 3, 3]
```

🔴 **CHÉP DECK CŨ LÀ THỪA KẾ CẢ *NGHĨA* CỦA STYLE, KHÔNG CHỈ HÌNH.**
Sau khi thay chữ, **duyệt lại từng class mang MÀU/NGHĨA** và hỏi *"câu MỚI nằm trong đó có
đúng sắc thái đó không":*

| Class | Sắc thái nó áp | Lỗi đã dính thật |
| :-- | :-- | :-- |
| `sg-warn` | khung **cảnh báo đỏ** | HPD slide 10: bọc câu **tích cực** "nhà máy chạy tốt, dòng tiền thật" ⇒ màn hình cảnh báo một điều tốt. Vá: `hk-note` |
| `hk-strike` | **gạch ngang = phủ định** | MSR slide 10: gạch ngang câu chốt ĐÚNG ⇒ màn hình phủ nhận một sự thật |
| `hk-vs-old` | đỏ = vế **xấu** | HPD slide 6: tô đỏ "giá trị sổ sách" ⇒ ngầm phán "xấu", trong khi bài **bị cấm kết luận đắt/rẻ**. Vá: cho hai vế **cùng màu trung tính** |
| `hk-answer-no` / `hk-answer-ok` | xấu / tốt | kiểm câu bên trong có đúng cực đó không |
| `sg-num` | huy hiệu **1 KÝ TỰ** | HPD slide 5: nhét `"KH 2026"` ⇒ chữ tràn, "2026" lòi ra sau thành bóng mờ |
| `core-module` | 🔴 **MẶC ĐỊNH TẮT ĐÈN** — kho đặt `opacity:.3 + grayscale(100%)`, chỉ sáng khi app.js gắn `.highlighted` (cần `data-mode="highlight"`), mà lúc sáng lại thành **XANH** `rgba(0,230,118)` = "tốt" | PNJ slide 8: dùng grid để nói *"những thứ KHÔNG đổi vẫn còn nguyên"* ⇒ 3 ô mờ **gần như vô hình**, màn hình nói NGƯỢC lời đọc. Vá: tự bật `opacity:1; filter:none`, giữ trung tính, **không** lấy màu xanh phán "tốt" |
| `cm-names-big code` | huy hiệu **KEY NGẮN** — 24px/900, thẻ `code` ⇒ monospace | PNJ slide 3·4·6: nhồi cả câu định nghĩa (*"giấy kiểm định = thứ khiến viên đá có giá"*) ⇒ vỡ **3-4 dòng chữ khổng lồ**, ăn hết slide. Vá: hạ 14px + `font-family: inherit` khi nội dung là CÂU chứ không phải KEY |
| `speed-gauge` (+ `gauge-arc`/`gauge-needle`/`gauge-center`) | 🔴 cung **conic quét ĐỎ → CAM → XANH** `rgba(0,230,118)` và tâm kim `var(--primary)` glow xanh ⇒ kim đứng bên phải = màn hình đang nói **"tốt"** | VFG slide 8 (mở hàng mẫu này): dùng để chỉ *chỉ số cần theo dõi*, mà bài **bị cấm phán tốt/xấu**. Vá: bọc `.vfg-gauge` rồi đổi conic sang đỏ→hổ phách→**trắng**, kim + tâm về `--primary` của palette `tc`; kim đứng vùng trắng = **chưa phân định** |
| ⚠️ thẻ rỗng `<br>` | không phải màu — nhưng `validate_slide.py` parse bằng **stack thẻ**, `<br>` không pop ⇒ **lệch cả cây** | VFG: báo "x câu != y reveal" cho 5 slide ĐÚNG, slide 10 báo `26 reveal units` (= tổng deck). Vá: viết `<br/>` |
| `glowing-orb` | quầng sáng **XANH** `rgba(0,230,118)` | PNJ slide 10: deck tài chính palette `tc` (vàng+đỏ) ⇒ lòi quầng xanh lạ sau câu chốt. Vá: `rgba(255,176,32,…)` |

**Bài không được phép kết luận thì MÀU cũng không được kết luận hộ.** Hai vế chỉ để đặt
cạnh nhau ⇒ cùng một màu; màu tương phản chỉ dùng khi lời đọc thật sự đang phán một bên.

---

## 4b. 🆕⚖️ DÒNG MIỄN TRỪ TRÁCH NHIỆM — BẮT BUỘC với mọi video tài chính (BOSS lệnh 25/07/2026)

Nguyên văn BOSS: **"Video này không phải là khuyến nghị mua bán. Chỉ là tổng hợp thông tin."**

```html
<!-- đặt CUỐI slide 10, NGOÀI .slide-content, KHÔNG mang class reveal -->
<p class="mien-tru">Video này không phải là khuyến nghị mua bán. Chỉ là tổng hợp thông tin.</p>
```
Hai điều kiện đặt chỗ, cả hai đều cần:
- **Ngoài `.slide-content`** ⇒ không lọt hộp bố cục mà `validate_slide` đo ⇒ không đẩy slide 10 tràn safezone.
- **Không mang class reveal** ⇒ engine không đếm là reveal ⇒ nhịp vẫn `[…,3]`, không phải sửa kịch bản, không tốn từ nào trong trần 380.

CSS `.mien-tru` chép từ cuối `headless/deck_pnj02/style.css`: đáy giữa, `bottom: 46px`,
9,5px, mờ 50% — **dưới vùng phụ đề** (y480-549 quy về khung 390×693) và trên watermark.

**Runner đóng thành CỔNG ở bước 6** (`--loai baocao`): thiếu `mien-tru` là chặn, mã 10.
Vì sao phải là cổng: quên một dòng chữ thì video vẫn render sạch, vẫn qua mọi phép đo
khác, và chỉ phát hiện ra khi **đã đăng**.

⚠️ **Dòng miễn trừ KHÔNG hợp pháp hoá nội dung khuyến nghị.** Nó chỉ nói rõ ý định. Thứ
thật sự bảo vệ là **danh sách `CAM_KHUYEN`** trong `thuoc_kichban.py` (cổng bước 3) —
đừng bao giờ nới danh sách đó để "câu cho hay".

**Bối cảnh pháp lý** (tra 25/07/2026, KHÔNG phải ý kiến luật sư): khoản 4 Điều 12 Luật
Chứng khoán 2019 nghiêm cấm cung cấp dịch vụ chứng khoán khi chưa được UBCKNN cấp phép;
chỉ công ty chứng khoán / công ty quản lý quỹ được cấp phép mới được **tư vấn đầu tư**.
UBCKNN cảnh báo 17/04/2026 nhắm vào tài khoản mạng xã hội **"đưa ra khuyến nghị liên quan
đến việc mua, bán, nắm giữ cổ phiếu"** — ranh giới nằm ở chữ **KHUYẾN NGHỊ**, không ở chữ
phân tích. Đó đúng là ranh giới mà `CAM_KHUYEN` + góc `viec_can_lam` đang giữ.

---

## 5. BƯỚC 4 — GIỌNG

### 🆕🔴 25/07 chiều — TỪ ĐIỂN PHÁT ÂM: mã CP và chữ tiếng Anh đọc ĐÚNG

BOSS nghe PNJ 02 rồi phán: *"AI đọc chữ tiếng Anh hay bị lỗi, như superpower, hoặc mã cổ
phiếu PNJ đọc lỗi"*. Dựng 2 bài thử cho BOSS nghe (`kichban/00c_*`, `00d_*`), **BOSS chốt**:

| | Chọn | Ví dụ |
| :-- | :-- | :-- |
| Mã cổ phiếu | **phương án C** — tên chữ cái kiểu tiếng Anh | `PNJ` → "Pi En Giây" · `MSR` → "Em Ét Rờ" |
| Chữ tiếng Anh | **phương án B** — viết lại theo âm tiếng Việt | `superpower` → "su pơ pao ơ" · `hook` → "húc" · `Claude Code` → "Clốt Cốt" |

⚠️ **KHÔNG viết cách đọc thẳng vào `script-90s.txt`.** Phụ đề lấy từ `timing.json["text"]`,
mà chuỗi đó CHÍNH LÀ dòng thô trong kịch bản ⇒ viết "Pi En Giây" vào kịch bản thì **phụ đề
cũng hiện "Pi En Giây"**. Hai đường phải tách:

```
script-90s.txt ──┬──> timing.json["text"] ──> PHỤ ĐỀ        (chữ GỐC "PNJ")
                 └──> doc_am() ──> engine  ──> GIỌNG ĐỌC    (chữ đọc "Pi En Giây")
```

**Thêm từ mới = sửa `escbase_template/tts/phat_am.json`, KHÔNG sửa code.** Mã mới vào nhóm
`ma_cophieu`, từ tiếng Anh vào `tieng_anh`. Khớp theo biên từ, không phân biệt hoa thường,
khoá dài thắng khoá ngắn (`Claude Code` trước `Claude`).

```bash
cd /Users/simple/Desktop/Cloud/video/escbase_template
.venv/bin/python tts/phat_am.py --kiem                    # thước 0 API, 11 ca
.venv/bin/python tts/phat_am.py "PNJ và hook trong Claude Code"   # thử 1 câu
```
Cache tiếng khoá theo **chữ ĐỌC**, nên sửa `phat_am.json` là tự sinh lại giọng — không phải
xoá cache tay.

### 🆕🔴 25/07 chiều — ĐUÔI VIDEO (`TAIL_SECONDS`)

BOSS: *"video hình như chưa hết mà đã dừng rồi"*. Đo ra đúng: tổng lời 97,176s / video
97,200s ⇒ **đuôi 0,024s**, một giây cuối vẫn còn tiếng ở max **−4,8 dB**. Giọng chạm đúng
khung cuối rồi cắt phựt. **Bệnh có ở MỌI bài trước** (MSR · HPD · PNJ 01) mà 6 phép đo cũ
không cái nào bắt.

`TAIL_SECONDS = 1.4` trong `escbase_template/tts/common.py`. **Phải vá CẢ HAI nhánh** —
`tts/common.py` (per-slide) và `split_voiceover.py` (edge "full rồi cắt", nhánh THỰC TẾ đang
chạy). Vá một chỗ là lỗi im lặng. Thước nghiệm thu nay có **cổng ⑦**: 0,8s cuối phải ≤ −45 dB.

⛔ **Đừng vá bằng cách nối im lặng vào mp4 sau khi render** — làm vậy lệch `timing.json`.

---

🔴 **GIỌNG MẶC ĐỊNH CHO VIDEO BÁO CÁO TÀI CHÍNH: `edge:vi-VN-NamMinhNeural` `+14%`.**
BOSS nghe bản HPD dựng bằng ElevenLabs "Nhật" rồi phán **"âm thanh tệ quá, dùng lại mẫu âm
thanh ban đầu như các video khác đi"** (24/07/2026) ⇒ đã render lại bằng NamMinh.
**Đừng tự ý dùng ElevenLabs cho bài tài chính nữa** — vừa tệ hơn theo tai BOSS, vừa tốn tiền.
Chỉ đổi khi BOSS nói thẳng, và đổi thì dựng bài thử nhiều phương án cho BOSS chọn
(khuôn: `kichban/00*_thu_giong.md`). **KHÔNG tự đổi giọng/tốc độ/nghỉ.**

```bash
# ⭐ MẶC ĐỊNH — edge NamMinh, MIỄN PHÍ vô hạn, render thoải mái
.venv/bin/python generate_tts.py headless/deck_{mã}01 \
    --engine edge --voice vi-VN-NamMinhNeural --rate "+14%"

# CHỈ khi BOSS bảo — ElevenLabs "Nhật", TÍNH TIỀN theo ký tự, đọc config/tts.json
.venv/bin/python generate_tts.py headless/deck_{mã}01 --engine elevenlabs
```
Đổi engine cho deck đã có tiếng thì thêm `--force` (đè file cũ). Đổi **sang edge** thì
`--force` vô hại vì miễn phí; nhưng **đã sinh tiếng ElevenLabs rồi thì KHÔNG tự render lại,
KHÔNG `--force`** — trừ khi BOSS bảo. Sửa slide, render lại hình: **không** tốn tiền tiếng.

---

## 6. BƯỚC 5 — SOI ẢNH (không bỏ được)

```bash
.venv/bin/python capture_slides.py headless/deck_{mã}01     # ra /tmp/escbase-qa/deck_{mã}01/
```
Rồi **`Read` TỪNG file `slide1.png` … `slide10.png`**. Soi: chữ tràn/đè · nhãn quá nhỏ ·
khoảng trống chết · **màu có mâu thuẫn với nghĩa của câu không** (mục 4) · số trên màn hình
có khớp lời đọc không.

Vá xong thì **`validate` lại + `capture` lại + soi lại đúng những slide đã sửa**.

---

## 7. BƯỚC 6 — RENDER + NGHIỆM THU BẰNG MÁY

```bash
.venv/bin/python headless/render_headless.py headless/deck_{mã}01   # CHẠY NỀN, 4-10 phút
```
⚠️ File đích là **`output_headless/final_headless.mp4`**. `silent.mp4` xuất hiện trước
vài phút là bản **chưa có tiếng** — đừng tưởng xong (tôi đã bắt nhầm file này).

```bash
cp headless/deck_{mã}01/output_headless/final_headless.mp4 \
   /Users/simple/Desktop/Cloud/results/video/{mã}_01_danhgia.mp4

.venv/bin/python ../.claude/skills/video-baocao/thuoc/nghiem_thu_video.py \
   /Users/simple/Desktop/Cloud/results/video/{mã}_01_danhgia.mp4 \
   headless/deck_{mã}01/output/voiceover_concat.mp3
```

🔴 **NGHIỆM THU ĐẠT RỒI THÌ COPY NGAY VỀ CHỖ CỐ ĐỊNH** (BOSS chốt 25/07/2026 — `results/video/`
là **bãi làm việc** 95 file lộn xộn, BOSS không tìm video ở đó):
```bash
cp /Users/simple/Desktop/Cloud/results/video/{mã}_01_danhgia.mp4 \
   /Users/simple/Desktop/Cloud/video/thanh_pham/baocao/{MÃ}_01_danhgia.mp4
```
Rồi **thêm 1 dòng vào bảng `baocao/` trong `thanh_pham/README.md`** (mã · dài · ngày · trạng
thái). Trạng thái chỉ được ghi cái MÁY đo; **cấm ghi "duyệt"** — AI không nghe được.
Thước đo 6 việc: khổ hình/bt709 · dB · lệch giọng theo khung · hụt khung · **đứng hình 4
giây đầu** · **phụ đề có thật**.

🔴 **PHỤ ĐỀ LÀ PHÉP ĐO BẮT BUỘC VỚI DECK MỚI.** Lỗi 24/07/2026 là lỗi **IM LẶNG**: dây
chuyền chỉ đọc cache, deck mới ra video **không có phụ đề** mà vẫn PASS mọi phép đo khác.

Cuối cùng **soi mắt 2-3 frame của video thật** (không chỉ tin ảnh deck).

**Mốc tham chiếu đã đo:** MSR 108,4s / 69,1 ms-khung · superpowers-01 93,3s · HPD 114,5s /
164,1 ms-khung (chậm ~2,4×, **chưa truy được nguyên nhân — nếu bài sau vẫn chậm thì đào**).

---

## 7b. 🔴🔴 THƯỚC BẮT BUỘC MỚI — "REVEAL CUỐI CÒN LẠI BAO NHIÊU GIÂY TRÊN MÀN" (25/07/2026)

**Ca PNJ 03: `validate` PASS · ảnh deck đúng · `nghiem_thu_video` ĐẠT CẢ 7 CỔNG — mà reveal 2
của slide 1 đứng trên màn 0,00 giây.** Cả dải giá `68.000đ → 30.750đ` **không bao giờ hiện**.
Sáu phép đo cũ không cái nào bắt được, vì chúng đo *khung hình có sáng không*, không đo
*chữ có kịp lên không*.

Hai nguyên nhân, đều nằm trong `auto_render.build_click_timeline`:
1. Lịch reveal chia theo **vị trí ký tự** của câu trong dòng ⇒ **câu chót NGẮN đứng cuối dòng
   DÀI** hiện ở ~95% thời lượng slide (ca slide 10: `"Tòa chưa tuyên."` chỉ 0,52s).
2. **Slide HOOK có luật riêng** ([auto_render.py:1014](../../../escbase_template/auto_render.py:1014)):
   reveal 2 đặt **đúng lúc dứt giọng đọc** ⇒ trùng khít mốc chuyển slide. Vô hại suốt 12 deck cũ
   vì khuôn cũ slide 1 luôn **1 câu / 1 reveal**; bài đầu tiên viết hook 2 câu là lộ.

**Chạy TRƯỚC khi render** (0 API, tất định — sửa `ru=` cho khớp nhịp bài):
```bash
cd /Users/simple/Desktop/Cloud/video/escbase_template
.venv/bin/python -c "
import json, re, auto_render as ar
t=json.load(open('headless/deck_XXX/output/timing.json'))
ru=[1,1,2,3,2,3,3,2,3,3,3,2,4,2,3,1]
cum=0; starts=[]
for x in t: starts.append(cum); cum+=x['duration']
last={}
for e in ar.build_click_timeline(t,ru):
    m=re.match(r'Slide (\d+): reveal (\d+)/(\d+)', e['desc'])
    if m and m.group(2)==m.group(3): last[int(m.group(1))-1]=e['time']
xau=[(s+1, round(starts[s]+t[s]['duration']-last[s],2)) for s in last
     if starts[s]+t[s]['duration']-last[s] < 1.2]
print('slide có reveal cuối <1,2s:', xau or 'KHÔNG CÒN')"
```

**Hai luật rút ra:**
- 🔴 **DÒNG 1 PHẢI LÀ MỘT CÂU.** Muốn hook 2 vế thì nối bằng dấu phẩy, đừng dùng dấu chấm.
- Dòng khác có câu chót ngắn ⇒ gộp vào câu trước bằng dấu phẩy. **Vá bằng dấu câu, đừng sửa
  `auto_render.py`** — đó là code dùng chung cho mọi deck, sửa nó là đổi luật cả xưởng.
- Và: **luôn soi frame video THẬT ở vài mốc**, không chỉ ảnh deck. Ảnh deck bật sẵn mọi reveal
  nên nó **không thể** phát hiện lỗi loại này.

## 8. BƯỚC 7 — BÁO BOSS + GHI 4 SỔ

Báo BOSS phải **tách bạch**: cái gì máy đo được (nêu số), cái gì cần BOSS nghe rồi phán
(mượt · giọng). Cấm tự khen.

Ghi sổ **VỀ GỐC REPO** (không mở sổ riêng trong `video/`):
1. `tri_thuc/patch_history.md` — mục mới **LÊN ĐẦU**: đã làm gì, số nghiệm thu, lỗi đã vá.
2. `tri_thuc/kinh_nghiem.md` — bẫy mới, 1-3 dòng kèm **ngày**, đúng nhóm.
3. `video/HANDOFF.md` — 2 khoang sống, **GIỮ GỌN** (hook cắt ở 7000/5000 ký tự; mục mới
   đặt lên ĐẦU để chắc chắn lọt vào cửa sổ hook).
4. **CẬP NHẬT CHÍNH SKILL NÀY** — xem mục 9.

---

## 9. ⭐ MỖI LẦN LÀM VIDEO XONG PHẢI CẬP NHẬT SKILL NÀY

BOSS lệnh: *"mỗi lần làm video thì cập nhật skill này"*, để lần sau không phải mò lại và
để video ngày càng tốt hơn. Sau mỗi bài, làm đúng 3 việc:

1. **Thêm 1 dòng vào bảng NHẬT KÝ** dưới đây (số đo thật, đừng đoán).
2. **Lỗi mới soi ra mà thước không bắt được** ⇒ thêm dòng vào bảng class ở **mục 4**.
   Đây là bảng quý nhất của skill: nó lớn dần theo từng bài.
3. **Luật/khuôn mới BOSS chốt** ⇒ sửa thẳng vào mục tương ứng, ghi ngày BOSS chốt.
   Cải tiến dây chuyền có số đo ⇒ cập nhật mốc tham chiếu ở mục 7.

### NHẬT KÝ BÀI ĐÃ LÀM

| Ngày | Mã | Video | Dài | Giọng | Từ | Ghi chú / lỗi soi ra |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 26/07/2026 | VFG | `VFG_01_danhgia.mp4` | **106,9s** | edge NamMinh +14% | 380 | ⭐ **BÀI ĐẦU XƯỞNG PHIM KHÔNG VIẾT LỜI** — lời đến từ **phòng phân tích PTBC** (`Research copy/PTBC/VFG/31_loi_doc.txt`, BOSS đã duyệt). ⇒ **bước 2 của skill này chuyển thành: KIỂM lời, đừng viết lại.** Góc `nghich_ly_so` lần đầu dùng, nhịp `[1,1,3,3,2,3,3,3,4,3]`. 3 scene mới + **mở hàng `speed-gauge`** (phải recolor: bản kho xanh #00e676 = "tốt"). 🔴 **Bắt được 1 lỗi số trong lời BOSS đã duyệt**: "600 tỷ **bằng nửa** giá thị trường" — thật ra 34,6% (661,7/1.915 tỷ); "54%" là của *tiền ròng 24.763 đ/cp*. **Loại lỗi ghép-hai-đại-lượng: rà soát từng mệnh đề KHÔNG bắt được, phải tự bấm lại phép chia.** 🐞 Bẫy `<br>` không đóng ⇒ `validate_slide` lệch cả cây. Máy 7/7 · 74,3 ms/khung |
| 25/07/2026 | PNJ | `PNJ_03_niemtin.mp4` | **126,3s** | edge NamMinh +14% | 424 | ⭐ **BÀI ĐẦU DỰNG TỪ KỊCH BẢN BOSS TỰ VIẾT/CHỈNH** (`kichban/pnj_dam_chay_kim_cuong.md`) và **bài đầu 16 slide** — góc mới `hai_tien_le`, bộ scene mới hoàn toàn (`nn-*` trong `<style>` của deck, **trùng deck cũ 0%**), icon **Lucide ISC** dán inline, tiêu đề **serif Playfair**. Thêm **slide 16 quảng bá `dungladu.vn`** (BOSS lệnh). 🔴 **LỖI QUAN TRỌNG NHẤT TỪ TRƯỚC TỚI NAY: nghiệm thu 7/7 mà video vẫn thiếu chữ** — xem mục **7b**. Thước kịch bản nay đọc `tran_tu:`/`tran_hook:` từ file góc (góc dài hơn 10 dòng thì khai báo, mặc định KHÔNG đổi) |
| 25/07/2026 | PNJ | `PNJ_02_hanhdong.mp4` **(02b)** | **98,8s** | edge NamMinh +14% | 380 | 🔊 **BOSS NGHE RỒI PHÁN 3 ĐIỀU, sửa cả 3:** ① bỏ slide giải thích 127→84.667 (thay bằng độ sâu/tốc độ/**lượng khớp 41,3tr = lớn nhất 4.128 phiên từ 2010**) · ② `PNJ` đọc lỗi ⇒ dựng 2 bài thử cho BOSS chọn ⇒ **từ điển phát âm** `tts/phat_am.json` (mục 5) · ③ *"chưa hết mà đã dừng"* ⇒ `TAIL_SECONDS=1.4` + **cổng ⑦**. Nghiệm thu **7/7**. Bẫy mới: cổng ⑦ đo mp4 ra −19 dB (tưởng hỏng) vì **nhạc nền** che — phải đo file GIỌNG (−91 dB) |
| 25/07/2026 | PNJ | ~~`PNJ_02` bản đầu~~ | 97,2s | edge NamMinh +14% | 380 | ⭐ **DỰNG LẠI SAU KHI BOSS BÁC BÀI PNJ 01.** Góc mới `viec_can_lam`. 🔴 Lỗi bị bác: **giá đỉnh không chia lại theo thưởng cổ phiếu** (xem cảnh báo đỏ mục 2). Bài đầu đi **ĐƯỜNG RẺ**: 0 subagent, 0 scene mới, chép `deck_msr01` chỉ thay chữ, soi bằng `contact_sheet.py` ⇒ **2 lượt đọc ảnh** thay vì 20-30. Thước kịch bản ĐẠT **ngay vòng 1**. Chỉ 1 lỗi soi ảnh: `hk-lockup-a` đỏ bọc câu dạy nghề đứng vững (3 bẫy còn lại chặn trước bằng CSS `.vcl-flat`). Render **64,1 ms/khung** — mốc nhanh nhất tới nay |
| 24/07/2026 | MSR | `msr_01_danhgia.mp4` | 108,4s | edge NamMinh +14% | 379 | Bài tài chính đầu bằng headless. 3 lỗi chỉ lộ khi soi ảnh, nặng nhất: `hk-strike` gạch ngang câu chốt ĐÚNG. Bẫy `remap_palette` chỉ map từ bảng rose ⇒ deck lai màu |
| 25/07/2026 | PNJ | `pnj_01_danhgia.mp4` | 103,0s | edge NamMinh +14% | 380 | ⭐ **BÀI ĐẦU DÙNG THƯ VIỆN GÓC** (`ho_voi`, nhịp `[1,2,3,2,3,3,3,3,3,4]` = 27 reveal) và **bài đầu KHÔNG có `_HoSo.md`** — PNJ chưa có tài liệu trong `baocao/MD/` nên chuỗi rủi ro bị B0 chặn; BOSS chốt dựng từ `BCTC.db` + `gia.db` + web có nguồn, mọi số web đều đối chứng lại bằng DB nội bộ. Đẻ 2 scene mới (`đường có hố`, `hai đường chồng lệch pha`). **4 lỗi chỉ soi ảnh mới thấy**, nặng nhất `core-module` mặc định tắt đèn ⇒ màn hình nói NGƯỢC lời đọc (xem bảng mục 4). Render ~4 phút ≈ **78 ms-khung** ⇒ bệnh chậm 164 ms của HPD **KHÔNG tái diễn** |
| 24/07/2026 | HPD | `hpd_01_danhgia.mp4` | 111,7s | edge NamMinh +14% | 380 | 🔴 **BOSS BÁC GIỌNG ELEVENLABS**: dựng lần 1 bằng ElevenLabs "Nhật" (BOSS lệnh giữa phiên) → BOSS nghe rồi phán *"âm thanh tệ quá, dùng lại mẫu âm thanh ban đầu như các video khác đi"* ⇒ render lại bằng NamMinh. **Bài học: giọng là thứ chỉ tai BOSS quyết được — đừng đầu tư cả lượt render vào giọng mới khi chưa cho BOSS nghe THỬ trước.** 4 lỗi soi ảnh bắt được, nặng nhất `sg-warn` đỏ bọc câu tích cực. Nháp đầu 521 từ, siết 3 vòng |

---

## 10. TRA NHANH

| Cần gì | Ở đâu |
| :-- | :-- |
| Thước kịch bản (0 API) | `video/.claude/skills/video-baocao/thuoc/thuoc_kichban.py` |
| Thước nghiệm thu video | `video/.claude/skills/video-baocao/thuoc/nghiem_thu_video.py` |
| Luật riêng dự án video | `video/CLAUDE.md` |
| Trạng thái + việc chờ | `video/HANDOFF.md` (2 khoang sống) |
| Cách chạy + định dạng kịch bản | `video/README.md` |
| Bẫy kỹ thuật toàn dự án | `tri_thuc/kinh_nghiem.md` |
| Đề bài Codex đầy đủ + danh sách từ cấm | `Research copy/results/codex/lenh_kichban_video_msr.md` |
| Luật deck escbase (visual, QA) | `video/escbase_template/CLAUDE.md` · `WORKFLOW.md` |

**Phụ thuộc ngoài:** `ffmpeg` (brew) · `.venv` trong `escbase_template/` (Pillow, playwright,
edge-tts) · font macOS có sẵn.
