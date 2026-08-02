# HANDOFF — DỰ ÁN CON `video/` (khởi tạo 23/07/2026, BOSS lệnh tách thư mục riêng)

**Điểm vào của dự án con này.** Luật riêng video: `video/CLAUDE.md` (mở phiên tại
`video/` thì hook trong `video/.claude/` tự nạp 2 khoang sống dưới đây). Luật gốc vẫn
theo `CLAUDE.md` ở gốc repo. Cách chạy + định dạng file kịch bản: `video/README.md`.

**KHUNG FILE NÀY (đừng phá):** 2 khoang `## 📍 TRẠNG THÁI HIỆN TẠI` và
`### 🎯 ĐANG THI CÔNG DỞ` là khoang SỐNG — hook đầu phiên trích đúng 2 khoang này
(trần 7000/5000 ký tự) → giữ GỌN, chi tiết dài đẩy xuống các mục tham khảo phía dưới.

## MỤC ĐÍCH (BOSS đặt 23/07/2026)
Bộ video ngắn dạy **Claude Code**, tiếng Việt, dọc 9:16 để xem trên điện thoại.
Nguyên văn: *"Tôi chỉ xem video là hiểu vấn đề và làm được, chia sẻ lại được."*
Dàn ý gốc: repo `luongnv89/claude-howto` — nhưng **ví dụ thay hết bằng ví dụ THẬT của
dự án này**; repo kia chỉ có ví dụ đồ chơi.

---

## 📍 TRẠNG THÁI HIỆN TẠI (25/07/2026)

> Khoang này CỐ Ý GỌN (hook nạp đầu phiên, trần 7000 ký tự). Diễn biến cũ đã dời xuống
> `## 🗄️ LỊCH SỬ TRẠNG THÁI` cuối file — không mất chữ nào. Chi tiết đầy đủ: `../tri_thuc/patch_history.md`.

### 🆕🎬⭐ 27/07 — `HPD_02_danhgia.mp4` (92,0s): làm lại HPD qua dây chuyền PTBC đầy đủ + góc mới
`thanh_pham/baocao/HPD_02_danhgia.mp4` · deck `headless/deck_hpd02` · lời
`Research copy/PTBC/HPD/31_loi_doc.txt` (4 AI viết mù → phản biện chéo → trọng tài → K5b rà
soát số → **sư phụ Codex duyệt K6 thay BOSS** — lệnh BOSS hôm nay). Góc `thu_giet_dn` lần đầu
dùng ("thứ đủ sức chấm dứt cuộc chơi" — ủy quyền thế chấp TSCĐ 48% tài sản bảo lãnh công ty
mẹ). Đẻ scene `.tgd-chain-content`/`.tgd-tile` (đổ dây chuyền, đặt hàng từ 25/07 chưa ai dựng).
Máy nghiệm thu 7/7. 2 bẫy vá: `<br>` không đóng làm lệch cây validate (tái phát, xem SKILL.md
mục 4) · slide kết tràn safezone 29px. ⛔ **BOSS CHƯA NGHE** — bản `HPD_01` (24/07) đã được
duyệt trước đó, giữ song song để so sánh. Chi tiết đầy đủ: SKILL video-baocao mục 9 (nhật ký).

### 🆕🎬⭐ 26/07 CHIỀU MUỘN — `VFG_01_danhgia.mp4` (106,9s): BÀI ĐẦU LỜI DO **PHÒNG PHÂN TÍCH** VIẾT
`thanh_pham/baocao/VFG_01_danhgia.mp4` · deck `headless/deck_vfg01` · lời
`kichban/escbase_10dong/vfg_01_danhgia.txt` · truy vết `escbase_10dong/README_vfg.md`.
**Xưởng phim KHÔNG viết lời bài này** — lời từ `Research copy/PTBC/VFG/31_loi_doc.txt` (4 AI
viết mù → phản biện chéo → rà soát 23 mệnh đề với nguồn gốc → đọc thẳng BCTC Q2/2026 PDF →
**BOSS duyệt**). Xưởng chỉ dựng hình + tiếng.
- **Góc `nghich_ly_so` lần đầu dùng**, nhịp `[1,1,3,3,2,3,3,3,4,3]` = 26 reveal / 380 từ /
  lời 106,85s. Cặp số chọi: lãi 6T **+171 tỷ** ↔ dòng tiền kinh doanh **−43 tỷ**.
- **3 scene mới** cho kho: `vfg-duel` (hero hai số) · `vfg-jump` (544→878 tỷ) · `vfg-drain`
  (100đ lãi → ~25đ tiền thật). ⭐ **MỞ HÀNG `speed-gauge`** — bản kho tô xanh `#00e676` = "tốt",
  phải recolor về `tc` mới dùng được cho bài bị cấm phán. Kho còn **4 hero** chưa đụng.
- 🔴 **XƯỞNG PHIM SỬA 1 SỐ SO VỚI BẢN BOSS DUYỆT** — dòng 9: *"tiền và tiền gửi hơn sáu trăm
  tỷ, **bằng nửa** giá thị trường"* → **"một phần ba"**. 661,7 tỷ / vốn hóa 1.915 tỷ = **34,6%**;
  con số "54% thị giá" là của **tiền ròng 24.763 đ/cp** (≈1.033 tỷ) — ghép nhầm hai đại lượng.
  Quay lại nguyên văn = sửa 1 dòng txt + chạy lại TTS/render, KHÔNG đụng deck.
- 🐞 **Bẫy mới:** `<br>` không đóng làm `validate_slide` lệch cả cây ⇒ báo sai reveal ở slide
  ĐÚNG, slide cuối báo bằng TỔNG deck. Trong deck luôn viết `<br/>`.
- **Máy: 7/7 ĐẠT** + thước reveal-cuối ≥1,2s sạch + soi 10 ảnh deck (vá 3 chỗ chữ xuống dòng
  xấu) + 3 frame video thật. Render 238,3s = **74,3 ms/khung**.
🔊 **BOSS NGHE BẢN 1 RỒI PHÁN 2 ĐIỀU — ĐÃ SỬA CẢ 2, RENDER LẠI (bản 2, 107,1s):**
1. **`VFG` đọc "Vê Ép Gờ"**, không phải "Vi Ép Gi" (*"nghe quen hơn"*). ⚠️ **Mã cổ phiếu KHÔNG
   mặc định theo phương án C (tên chữ cái tiếng Anh)** như bảng `phat_am.json` ghi — mã nào
   BOSS thấy quen kiểu Việt thì để kiểu Việt. Đây là mã đầu tiên lệch khỏi phương án C.
2. 🔴 **BOSS BẮT LỖI SỐ THỨ HAI:** màn hình *"mua chịu 823 tỷ"* mà tai nghe *"gần bảy trăm
   tỷ"*. Chân tướng: **695,6 tỷ là RIÊNG Syngenta**, còn TỔNG phải trả người bán là
   **823,2 tỷ** (đầu năm 252,2). Lời nay đọc **"hơn tám trăm tỷ"**; đã sửa cả bản gốc
   `PTBC/VFG/31_loi_doc.txt`. Nghiệm thu lại **7/7**, 61,5 ms/khung, soi lại frame 30,5s.
⏳ **BOSS chưa nghe BẢN 2** — còn phán: nhịp 107s · **"một phần ba" thay "bằng nửa"** ở dòng 9.
🔑 **Bài học chung của cả hai lỗi số: SỐ ĐÚNG NHƯNG PHẠM VI SAI** (một nhà cung cấp ≠ tổng ·
tỷ lệ trên mỗi cp ≠ tỷ lệ trên vốn hóa). Đối chiếu từng mệnh đề với nguồn KHÔNG bắt được vì
từng vế đều truy được nguồn — phải tự bấm lại phép chia và ghi kèm **phạm vi** cho mọi số.

### 🎬🎬 25/07 KHUYA — `PNJ_04_hoso.mp4` (128,4s): BẢN **THAY ÁO** CỦA PNJ 03 — CHỜ BOSS CHỌN ÁO
`thanh_pham/baocao/PNJ_04_hoso.mp4` · deck `headless/deck_pnj04` · truy vết
`kichban/escbase_10dong/README_pnj04.md`. **Cùng lời, cùng nhịp, cùng số với PNJ 03** — chỉ khác áo.
- **Lời sửa đúng 1 chỗ (BOSS):** *"tòa chưa tuyên"* → **"cơ quan điều tra chưa kết luận"** (vụ mới
  ở giai đoạn khởi tố/điều tra). Sửa cả 4 nơi: lời đọc · kịch bản gốc · con dấu slide 10 · ô slide 14.
  38 reveal giữ nguyên. ⚠️ Bản **PNJ_03 vẫn mang chữ cũ**.
- **Áo mới = theme 02 "HỒ SƠ ĐIỀU TRA"** (`escbase_template/themes/`, tiền tố `hs-`): xanh thép +
  lưới blueprint + thẻ góc vuông có gáy hồ sơ + tiêu đề Oswald condensed in hoa + nhãn mono.
  **Thư viện theme giờ có 2 áo dùng lại được** — quy trình thay áo ở `themes/README.md`.
- **3 ẢNH THẬT (deck đầu tiên của xưởng có ảnh):** Buffett · Gerald Ratner · thỏi vàng (**CC0**,
  Wikimedia, chú thích "ảnh minh hoạ"). Nguồn+giấy phép: `deck_pnj04/source/links.txt` — 2 ảnh chân
  dung do phiên trước tải **chưa rõ giấy phép**, BOSS đã quyết dùng.
- **Slide 1 = biểu đồ giá THẬT** 31 phiên (12/06→24/07) đọc từ kho giá, vẽ SVG trong DOM.
  **Slide 16** chỉ còn **logo chìa khoá website xoay ngang + 1 dòng `dungladu.vn`** (BOSS lệnh).
- 🆕 **ĐỢT SỬA 2 (BOSS xem bản render rồi phán 7 điều — đã áp hết):** bỏ câu máy móc "máy đo quá
  khứ nói cỗ máy khỏe" → *"Quá khứ sinh lời tốt…"* · "rạn" → **"rạn nứt"** · slide 12 bỏ *"cổ phiếu
  quỹ cũng cần soi"* (BOSS: vô duyên, không nối với đoạn trước) → **"cách công ty xử lý khủng hoảng
  khi cổ đông tới bán"** · **sổ sách lấy đúng Q1/2026 từ `BCTC.db`: 28.128đ/cp** (VCSH 14.401 tỷ ÷
  512,0tr cp sau thưởng 50%; số "26–28k" cũ là ước chừng — P/B 1,09) · *"nhưng chưa phải cho không"* ·
  dòng chốt bỏ "xem thêm tại", còn đúng tên miền · **vá chữ `dungladu.vn` cụt chân `g`**
  (`background-clip:text` + `line-height:1.1` cắt phần dưới đường chân → 1.42 + đệm dưới).
  🔴 **BOSS bắt tiếp LỖI SỰ THẬT ở chính câu này:** không phải "cổ đông tới bán" (tôi đoán sai), mà là
  **KHÁCH TỚI BÁN LẠI NỮ TRANG**. Tra ngược nguồn (`pnj_01_danhgia.txt` · `pnj02_01_hanhdong.txt`, báo
  22/07): PNJ **cam kết mua lại nữ trang của khách bằng 70–90% giá hóa đơn**, sau vụ việc **khách bán lại
  gấp 5 LẦN lượng bán ra**, tiền trả **giãn tới 120 ngày + có hạn mức mỗi ngày**. ⇒ chữ **"5 đợt"** của bản
  PNJ 03 là **đọc nhầm "gấp 5 lần"**, lại gán sang **cổ phiếu quỹ** — chuyện khác hẳn.
  ⚠️ **`PNJ_03_niemtin.mp4` vẫn mang con số sai đó ⇒ ĐỪNG DÙNG BẢN 03.**
- **Máy: 7/7 ĐẠT** + thước reveal-cuối ≥1,2s sạch + soi **11 frame thật** qua 2 vòng render.
  Lời 128,38s · video 128,4s · thước kịch bản `KETLUAN|38|439|DAT`. Render 245,3s.
⏳ **BOSS xem rồi phán:** ① chọn áo **03 hay 04** ② 2 cách đọc mới (`dungladu.vn` = "Đúng Là Đủ chấm
vi en"? · `Buffett` = "Ba phét") — vẫn CHƯA ai nghe ③ nhịp ~127s có dài không.

### 🎬 25/07 ĐÊM — ĐÃ DỰNG XONG `PNJ_03_niemtin.mp4` (126,3s) — CHỜ BOSS NGHE
`thanh_pham/baocao/PNJ_03_niemtin.mp4` · deck `headless/deck_pnj03` · lời
`kichban/escbase_10dong/pnj03_01_niemtin.txt` · truy vết `escbase_10dong/README_pnj03.md`.
Dựng từ kịch bản BOSS tự chỉnh 2 vòng, **giữ nguyên văn**; chỉ thêm dòng 16 (slide thương hiệu
`dungladu.vn`, BOSS lệnh giữa phiên) và đổi 2 dấu chấm thành phẩy vì bug reveal dưới đây.
**Góc MỚI `hai_tien_le`** (16 dòng · 38 reveal) · **bộ scene MỚI hoàn toàn**, namespace `nn-*`
viết trong `<style>` của deck ⇒ **trùng deck cũ 0%** · icon **Lucide (ISC)** dán inline 14/14 ·
tiêu đề **serif Playfair** (12 deck cũ toàn Inter). `KETLUAN|38|424|DAT` · `validate` PASS ·
nghiệm thu máy **7/7**.
🔴 **BẪY MỚI:** vòng render 1 **đạt 7/7 mà video vẫn thiếu chữ** — reveal 2 của slide 1 đứng
trên màn **0,00 giây** (`auto_render.py:1014`: slide HOOK đặt reveal 2 đúng lúc dứt giọng;
khuôn cũ slide 1 luôn 1 câu nên chưa từng lộ). **Chỉ soi frame video thật mới thấy.** Thước
mới: *reveal cuối mỗi slide phải còn ≥1,2s trên màn*. Chi tiết: patch_history 25/07 đêm.
⏳ **BOSS nghe rồi phán 3 thứ:** ① 2 cách đọc mới — `dungladu.vn` = *"Đúng Là Đủ chấm vi en"*
(hay là "Dũng"?) và `Buffett` = *"Ba phét"*; sửa = 1 dòng `tts/phat_am.json`, KHÔNG phải dựng
lại · ② nhịp 126s có dài không · ③ slide 16 đã đủ nổi bật chưa.

### 25/07 TỐI — kịch bản nguồn (đã dựng thành video ở mục trên)
`kichban/pnj_dam_chay_kim_cuong.md` — "Vết nứt niềm tin và hai tiền lệ ngành trang sức".
15 cảnh, 420 từ, parser `--loi` pass, CHỮ ≤34 ký tự. Khung kể: vụ P-Lab (khởi tố 03/07,
7 phiên sàn, 68.000đ→30.750đ) đặt giữa HAI tiền lệ trái chiều cùng ngành: Ratners Anh 1991
(niềm tin sụp, khách quay lưng, −500tr bảng, đổi tên Signet) vs Kingold TQ 2020 (giấy giám
định che 83 tấn vàng giả, hủy niêm yết) — chưa phân định PNJ thuộc ca nào; kết trung lập.
**BOSS chỉnh 2 vòng (25/07 tối):** ① P/B 0,79 trong `PNJ_BaoCao.md` SAI — giá sau chia tách
÷ book trên 341tr cp cũ; đúng ~512tr cp, sổ sách ≈26-28k/cp, P/B >1 (kiểm `BCTC.db`: VCSH
13.275 tỷ, vốn điều lệ 3.413 tỷ). DT tháng 7 +20% = số TỰ công bố, 3 tuần chưa phân định;
cổ phiếu quỹ trả 5 đợt/120 ngày khi dòng tiền BÁO ĐỘNG → đều thành điểm NGHI. ② Bỏ ẩn dụ
AmEx 1963 — chọn ca kết cục đẹp làm mỏ neo = ngầm cài kết luận nghiêng mua; thay bằng 2
tiền lệ cùng ngành 2 chiều. Dựng: `python3 lam_video.py kichban/pnj_dam_chay_kim_cuong.md`
(đường dẫn TUYỆT ĐỐI) — BOSS nghe giọng duyệt trước khi render thật.

### 🆕☁️ 25/07 TỐI — 2 REPO ĐÃ LÊN GITHUB PRIVATE (BOSS lệnh)
`video/` → **`nguyennam246/Video_factory`** · `Research copy/` → **`nguyennam246/Research-cp`**.
Push qua SSH (`~/.ssh/id_ed25519`, xác thực sẵn). Đã kiểm `git ls-remote` khớp HEAD cả 3 nhánh;
quét khoá **cả lịch sử** 2 repo = 0 khoá.
🔑 **LUẬT MỚI: commit xong PHẢI `git push`** — git init chỉ chống *sửa hỏng*, remote mới chống
*ổ cứng chết*. Không push thì GitHub đứng lại còn máy chạy tiếp, hụt đúng phần mới nhất.
⚠️ `git push` từng bị cơ chế phê duyệt Claude Code **chặn** (không nhất quán giữa 2 repo) ⇒
đưa lệnh cho BOSS chạy tay, đừng thử lách. Chưa có hook nhắc push.
Kèm: dọn 39 thay đổi treo ở `Research copy/` thành 3 commit — trong đó xoá **bản chụp `video/`
cũ** (35 file thời video còn trong repo Research, lần xoá chưa từng commit; **đã đối chiếu từng
file, 0 file mất**). Chi tiết: patch_history 25/07 tối.

### 🆕⚖️ 25/07 TỐI — DÒNG MIỄN TRỪ TRÁCH NHIỆM (BOSS lệnh) + tra pháp lý
`<p class="mien-tru">` cuối slide 10, **ngoài `.slide-content` và không mang class reveal**
⇒ không đụng safezone, không đổi nhịp, không tốn từ. **Runner đóng thành CỔNG bước 6** cho
`--loai baocao` (thiếu là chặn, mã 10) — quên một dòng chữ thì mọi phép đo khác vẫn sạch,
chỉ lộ khi ĐÃ ĐĂNG. Chi tiết: SKILL mục **4b**.
⚠️ Miễn trừ **không** hợp pháp hoá nội dung khuyến nghị; thứ bảo vệ thật là `CAM_KHUYEN`
trong `thuoc_kichban.py` — **đừng nới danh sách đó để câu cho hay**.
🐞 Vá kèm: `dem_reveal()` đếm chuỗi thô nên chữ "slide-element" trong **bình luận HTML**
cũng bị tính thành reveal (dính thật khi thêm dòng miễn trừ). Nay bỏ bình luận trước, và
chỉ đếm trong thuộc tính `class`.

### 🔊 25/07 CHIỀU MUỘN — BOSS NGHE `PNJ_02` RỒI PHÁN 3 ĐIỀU, ĐÃ SỬA CẢ 3
Bản mới: **`thanh_pham/baocao/PNJ_02_hanhdong.mp4` — 98,8s, nghiệm thu 7/7. BOSS CHƯA NGHE bản này.**
1. **TỪ ĐIỂN PHÁT ÂM** (BOSS chọn sau khi nghe 2 bài thử): mã CP = **"Pi En Giây"** kiểu tên
   chữ cái Anh · tiếng Anh = **viết theo âm Việt** (`superpower`→"su pơ pao ơ").
   `escbase_template/tts/phat_am.json` — **thêm từ = sửa JSON, không sửa code**; `--kiem` 11/11.
   ⚠️ Áp **CHỈ lên đường TTS**: phụ đề lấy `timing.json["text"]` = chữ gốc, nên viết cách đọc
   thẳng vào kịch bản là **phụ đề cũng đổi theo**. Sơ đồ 2 đường: README + SKILL mục 5.
2. **ĐUÔI VIDEO** `TAIL_SECONDS = 1.4` (`tts/common.py`) — đo ra đuôi cũ chỉ **0,024s**, giọng
   chạm khung cuối rồi cắt phựt. **Vá cả 2 nhánh** (`tts/common.py` + `split_voiceover.py` —
   nhánh sau mới là nhánh thực tế chạy). Cổng **⑦** trong thước nghiệm thu.
   ⚠️ Cổng ⑦ **phải đo file GIỌNG**, không đo mp4 — nhạc nền chạy tới khung cuối sẽ che.
   ⚠️ **MSR · HPD · PNJ_01 đều dính bệnh đuôi này**; dựng lại bài nào thì bài đó tự khỏi.
3. **BỎ slide giải thích 127→84.667** (BOSS: không cần thiết). Thay bằng độ sâu + tốc độ +
   **lượng khớp 41,3 triệu cp = phiên lớn nhất trong 4.128 phiên từ 2010**, gấp 24,5 lần TB.

### 25/07 chiều — BOSS BÁC `PNJ_01`, đã dựng lại `PNJ_02_hanhdong.mp4` (bản đầu 97,2s)
1. **LỖI SỐ phải nhớ:** `gia.db` lưu giá **THÔ, không hồi tố chia thưởng**. PNJ thưởng cp **50%
   ngày 23/04/2026** ⇒ đỉnh 30/01 **không phải 127.000đ mà là 84.667đ**, giảm **−63,7%** chứ
   không phải −75,8%. Cách dò 30 giây (3 mỏ neo) đã ghi vào **SKILL `video-baocao` mục 2**.
   ⚠️ Bẫy này áp cho MỌI mã hay chia thưởng, không riêng video.
2. **Góc mới `viec_can_lam`** (`goc/taichinh/viec_can_lam.md`) — BOSS muốn *"nói rõ nhà đầu tư
   nên làm gì lúc này"*. Giải bằng **đổi câu hỏi** (rẻ chưa → cái chưa biết lớn cỡ nào + hiện ở
   đâu) + 3 việc kiểm chứng được ⇒ trả lời đúng ý BOSS mà **không phạm `CAM_KHUYEN`**.
3. **⭐ ĐƯỜNG RẺ (BOSS hỏi "sao tốn thời gian thế?")** — đo ra render KHÔNG tốn (186,9s máy,
   0 token). Tốn ở 3 luật ta tự đặt: b1 spawn Opus nguội · b2 bắt đẻ scene mới + tra catalogue
   bằng ảnh · soi ảnh 10 PNG × 2-3 vòng. Bài này đi đường rẻ: **0 subagent · 0 scene mới ·
   2 lượt đọc ảnh** nhờ 🆕 `escbase_template/contact_sheet.py`. Bảng so 2 đường: **SKILL mục 3b**.
4. **🆕 BOSS lệnh tiếp: "áp đường rẻ đó vào `lam_bai.py` luôn"** ⇒ ĐÃ ĐÓNG THÀNH CỜ:
   ```bash
   python3 video/lam_bai.py --ma pnj03 --ten hanhdong --loai baocao --goc viec_can_lam --duong re
   ```
   `--duong {mo-duong,re}`, **mặc định `mo-duong` = hành vi cũ y nguyên** (có test hồi quy).
   `re` đổi 5 chỗ: b1+b2 bàn giao thẳng thợ 1 · `--mau` tự chọn deck khớp nhịp trong
   `DECK_DA_GO_LOI` (lệch nhịp thì **chặn ngay bước 0**, không đợi render) · dọn `script-90s.txt`
   bài cũ khi chép · b5 bỏ remap khi đo được là không còn gì phải đổi · b7 tự sinh contact sheet.
   **Hồi quy 6/6 đạt, 0 API.** Chi tiết: patch_history 25/07 mục D · README mục `--duong`.
   ⚠️ Deck mới chỉ được thêm vào `DECK_DA_GO_LOI` **SAU KHI** nó ra mp4 nghiệm thu đạt.

### Dây chuyền đang dùng
- **Video báo cáo tài chính** (MSR · HPD · ruiro TCL/SKV/MCF): có **skill riêng, đọc trước khi làm** →
  `/video-baocao` (`.claude/skills/video-baocao/SKILL.md`) — đủ 7 bước, khuôn 10 slide, bảng bẫy, 2 thước chạy được.
- 🆕 **Video DẠY KỸ NĂNG** (Claude Code · Superpowers · khoá học): có **skill riêng** →
  `/video-kynang` (`.claude/skills/video-kynang/`) — khuôn `[1,3,3,2,3,3,3,3,3,3]` = 27 reveal,
  brief giao thợ 2 Opus 5, thước kịch bản riêng, bản đồ scene. Deck `headless/deck_sp0X`.
  ⚠️ **Kho scene: 2/18 → 13/18 đã dùng** (sp02 mở 5, sp03-08 mở thêm 6). Còn 5 chưa đụng:
  `speed-gauge` + 4 hero. Bài sau lấy tiếp mẫu MỚI, đừng quay lại mẫu đã dùng.
  📏 **Nhịp đọc edge NamMinh +14% = 3,56 từ/giây** (đo 8 bài) — ước lượng độ dài trước khi render.
- 🆕🔧 **GIAO VIỆC CHO THỢ 2 / ENGINE NGOÀI: có skill riêng** → `/goi-tho`
  (`.claude/skills/goi-tho/` ở GỐC repo). **"Thợ 2" = tài khoản Claude thứ 2 gọi qua CLI**
  (`CLAUDE_CONFIG_DIR=/Users/simple/.claude-tk2 claude -p …`), KHÔNG phải subagent trong phiên —
  thợ 1 đã hiểu nhầm 2 lần ngày 25/07. Thợ có chạy lệnh thì phải `--permission-mode bypassPermissions`.
- 🆕⭐⭐ **THƯ VIỆN GÓC TIẾP CẬN `video/goc/`** (25/07) — hết khuôn cứng. Engine chỉ ép
  *số câu dòng N = số `.slide-element` slide N*, KHÔNG ép khuôn; khuôn cứng là **thước của
  mình tự trói**. Nay 6 góc tài chính (`nghich_ly_so` · `gia_da_tinh_san` · `thu_giet_dn` ·
  `ho_voi` · `bang_chung` · `dong_ho_chay`), mỗi góc nhịp riêng + bản đồ scene riêng + bẫy riêng.
  Chọn góc bằng câu hỏi *"điều gây bất ngờ nhất ở mã này là gì?"* (đọc Q8 + Q9 trước).
  **2 mã liền nhau không cùng góc** — ghi `video/goc/NHAT_KY.md`. Luật cấm KHÔNG nới theo góc.
  ⭐ Kỷ luật mới: **mỗi bài phải đẻ ≥1 scene mới** (kho chỉ còn 5 mẫu chưa đụng).
- 🆕⭐⭐ **THƯ VIỆN NGHỀ GIỮ MẮT `video/nghe/`** (25/07) — **trục thứ HAI, độc lập với `goc/`**:
  `goc/` = *kể chuyện gì* (ra nhịp) · `nghe/` = *giữ mắt cách nào* (ra kiểu hook + 4 luật chung).
  Trước ngày này dự án chỉ có 2 dòng luật giữ mắt ⇒ lo giây 0-3 và giây cuối, **bỏ trống giây
  3-70**. 5 tầng: `KIEU_HOOK.md` (**10 kiểu**, `dung_lam`+`cai_gia` CẤM bài tài chính) ·
  `DUONG_CONG.md` · `NGAT_MAU.md` · `CO_CHIA_SE.md` · `TRAN_Y.md`. Sổ: `nghe/NHAT_KY.md`.
  📏 **MỐC RƠI tính ra từ nhịp 3,56 từ/giây: mốc 1 nằm gọn DÒNG 2 · mốc 2 ở DÒNG 5-7.**
  ⇒ **mở món nợ dòng 2 · trả nợ dòng 3-7 · dòng 5-6 phải có SỐ.**
  Dùng: `--nghe <mã hook>` trong `lam_bai.py` (bật cổng chặn ở **bước 3**).
  Thước riêng 0 API: `thuoc_nghe.py` — 3 chế độ (kịch bản · `--trung` · `--moc`).
  ⚠️ **2 bài liền nhau không cùng kiểu hook.** Hiện 8 bài sp đều `mat_mat`, 9/10 kiểu chưa dùng.
- 🔴📏 **ĐO 25/07 — VÌ SAO 8 BÀI SUPERPOWERS XEM LIỀN THẤY "CÙNG MỘT KHUÔN"** (dò 12 deck):
  độ trùng scene với bài liền trước **80-88%**, mỗi bài mới chỉ thêm **ĐÚNG MỘT** mẫu; 6 bài
  sp03→sp08 dùng chung lõi 4 mẫu (`mock-terminal` · `workflow-grid` · `flow-diagram` ·
  `glowing-conclusion`). **Số mẫu/bài không thiếu (6-9)** — sai ở chỗ trùng bài trước.
  ⇒ Luật mới: **trùng ≤ 60% + tối thiểu 2 mẫu mới** (sp05→sp06 đạt 57%, nên làm được).
  Đếm thì **BỎ `script-panel`** — nó là khung, có ở cả 12 deck, tính vào là con số nào cũng đẹp.
- 🆕⭐ **MỘT LỆNH RA BÀI: `python3 video/lam_bai.py --ma sp09 --ten X --loai kynang --goc <mã>`** (25/07).
  9 bước, tự dừng ở cổng: `10` thước FAIL · `20` thợ 2 hết quota (đọc `<deck>/_VIEC_CHO_THO1.md`,
  **thợ 1 tự làm nốt**, đừng đổi API free) · `30` chờ soi ảnh · `40` chờ BOSS. Tiếp: `--tu-buoc <n>`.
  Bước THỢ gọi tk 2 qua CLI: **opus cho kịch bản · sonnet cho sửa HTML**. Đã kiểm bước 3/6/9;
  **2 bước THỢ chưa chạy thật lần nào** — bài đầu tiên là lượt thử. Cách dùng đủ: `video/README.md`.
- Nhánh Pillow (`lam_video.py`) vẫn chạy được, bộ 10 bài đã xong; escbase headless là đường chính từ 24/07.

### ⭐ ĐÃ RA MP4 — CHỜ BOSS XEM/NGHE (AI không tự phán được, cấm tự khen)
| File `results/video/` | Dài | Giọng | Phán cái gì |
| :-- | :-- | :-- | :-- |
| 🆕⭐⭐ **`pnj_01_danhgia.mp4` — BÀI ĐẦU DÙNG THƯ VIỆN GÓC** (`ho_voi`) | 103,0s | NamMinh +14% | **Phán: ① góc `ho_voi` có thoát được cảm giác "cùng một khuôn" của 5 bài tài chính cũ không** · ② hook *"Giảm 51% mà lợi nhuận vẫn lập đỉnh"* có giữ được người xem không · ③ giọng/nhịp. Bài PNJ: cú rơi **−51% trong 16 phiên** vì vụ kim cương ở công ty con giám định. ⚠️ **Bài duy nhất KHÔNG dựng từ `_HoSo.md`** — PNJ chưa có tài liệu trong `baocao/MD/` nên chuỗi rủi ro bị B0 chặn; BOSS chốt 25/07 dựng từ `BCTC.db` + `gia.db` + web có nguồn. Đẻ 2 scene mới: `đường có hố` · `hai đường chồng lệch pha` |
| 🆕⭐⭐ **`Superpower/superpowers_0{3,4,5,6,7,8}_*.mp4` — 6 BÀI, XONG TRỌN KHOÁ 8 BÀI** ⚠️ BOSS đã dời cả 8 bài vào thư mục con `results/video/Superpower/` | 104,6–121,0s | NamMinh +14% | **Kịch bản+deck do THỢ 2 (tk 2 qua CLI) dựng, thợ 1 kiểm lại + render.** Phán: ① 8 bài xem liền có còn thấy "cùng một khuôn" không (đã mở 13/18 mẫu scene) · ② bài nào chưa hiểu được thì chỉ đúng số bài |
| ✅ `Superpower/superpowers_02_cai_dat.mp4` | 113,2s | NamMinh +14% | **BOSS ĐÃ DUYỆT 25/07: "video tốt"** |
| `hpd_01_danhgia.mp4` | 111,7s | NamMinh +14% | Bài HPD (Thủy điện Đăk Đoa) đạt chưa — **bản render lại sau khi BOSS chê giọng ElevenLabs** |
| `msr_01_danhgia.mp4` | 108,4s | NamMinh +14% | Bài MSR đạt chưa |
| `Superpower/superpowers_01_tong_quan.mp4` | 93,3s | NamMinh +14% | Bài 01 khóa Superpowers đạt chưa |
| `headless_05_skill.mp4` | 93,5s | NamMinh +14% | So `escbase_05_skill.mp4`: hết giật chưa · tiếng đủ to chưa |
| `escbase_05…10_*.mp4` (6 bài) | 84-102s | NamMinh +14% | Duyệt/chê · nội dung có loãng không (nửa dưới khung trống) |
| `ruiro_0{1,2,3}_*.mp4` | 98-105s | NamMinh +14% | 3 bài rủi ro TCL/SKV/MCF đạt chưa |

### 🔒 LUẬT CỨNG CÒN HIỆU LỰC (đừng lật lại, đều đã trả giá)
- 🆕🎙️ **GIỌNG = `edge:vi-VN-NamMinhNeural` `+14%` cho MỌI bài.** BOSS nghe bản HPD dựng bằng
  **ElevenLabs "Nhật"** rồi phán (24/07): *"âm thanh tệ quá, dùng lại mẫu âm thanh ban đầu như các
  video khác đi"* ⇒ đã render lại. **Đừng tự ý dùng ElevenLabs nữa** (tệ hơn theo tai BOSS + tốn tiền).
  Muốn đổi giọng thì dựng **bài thử ngắn** cho BOSS nghe TRƯỚC, đừng đốt cả lượt render.
- 💵 **Cập nhật giá cho video phải chạy CẢ 4 lệnh** (`capnhat_gia` → `fireant_pull` → `q5_calc` →
  `gen_trang_dn`). `capnhat_gia` làm mới giá + P/B nhưng **KHÔNG** làm mới P/E ⇒ chạy một mình là
  hồ sơ lệch mà không cảnh báo gì (đo thật ca MSR: P/E đứng 51,85, chạy `fireant_pull` mới về 48,07).
- 🔴 **`TAB_CAPTURE_WARMUP` giữ 0.8 — ĐỪNG nâng.** Nâng 3.0 làm hụt khung + giãn timeline +17s. Đã hoàn nguyên.
- 🎨 **Palette theo SERIES, không theo bài:** tài chính `tc` vàng `#ffb020` + đỏ `#ef4444` ·
  superpowers `sp` xanh `#38bdf8` + hổ phách `#fbbf24`. ⚠️ `remap_palette.py` chỉ map TỪ bảng rose
  của bài 05 — chép deck đã đổi màu rồi remap tiếp ⇒ **deck lai màu** mà script vẫn báo thành công.
- 🎵 **Nhạc nền:** cả dự án chỉ có **1 file** `meta.mp3` (30 bản cùng md5). BOSS chốt 25/07:
  **`synth_lofi` cho series superpowers**. Chuẩn độ to bằng **LUFS −22,7**, không phải RMS
  (BOSS bắt được lỗi máy không thấy: RMS bằng nhau mà tai vẫn nghe to hơn 3,1 dB).
  ⚠️ 5 preset đều pad + arp chậm, **không có bộ gõ** ⇒ "sôi động" không chữa được bằng âm lượng.
- ✅ **BOSS đã duyệt:** escbase bài **03 + 04** ("2 bài đó đạt") · giọng NamMinh 2 vòng 20 giọng ·
  khuôn tài chính 10 slide. Bài duyệt xong → copy mp4 vào `video/thanh_pham/bai_XX_<tên>/`.

### 🟡 Còn treo, chưa truy ra
- Giật 2-3 giây đầu của nhánh **quay-live** vẫn còn (vá rẻ thất bại). Nhánh **headless** đã trị: 0/120 khung đứng hình.

## ✅ VIỆC CHỜ

### 🎯 ĐANG THI CÔNG DỞ — CHỜ BOSS XEM **2 VIDEO**, rồi mới chạy 7 bài superpowers còn lại
> **🆕⭐⭐ VIỆC 0 — CHỜ BOSS SO HAI BÀI CẠNH NHAU (bài A/B đầu tiên của khâu nghề giữ mắt):**
>
> | Xem 2 file này, **liền nhau, cùng một lượt** | Dài |
> | :-- | :-- |
> | `thanh_pham/kynang/superpowers/superpowers_07_debug.mp4` (BẢN CŨ, BOSS đã duyệt) | 114,6s |
> | 🆕 `…/superpowers_07b_debug_BAN_AB.mp4` (BẢN MỚI) | 109,4s |
>
> **Đổi ĐÚNG MỘT BIẾN** — giữ nguyên giọng · scene · số liệu · nhịp · palette. Chỉ đổi *cách
> giữ mắt*: hook `mat_mat` → **`cau_hoi_gai`** (*"Ba lần thay đồ mà nước vẫn chảy yếu, vì sao?"*)
> · dòng 2 **mở món nợ** (*"chưa ai đo xem nước mất áp ở chỗ nào"*) · dòng 10 có **câu đáng chụp
> màn hình** (*"Ba lần thay đồ không bằng một lần đo đúng."*).
>
> ✅✅ **BOSS ĐÃ PHÁN 25/07: *"Bản mới hút mắt hơn đấy. nhấn mạnh vào 3 lần thay đồ mà vẫn
> yếu, rất hay."*** ⇒ khâu `nghe/` **có ăn thật**, áp `--nghe` cho mọi bài sau.
> Cơ chế đã ghi thành luật (`nghe/KIEU_HOOK.md`, biến thể **"đếm lần thất bại"**): số lần
> thất bại ≥3 (một lần là rủi ro, ba lần là quy luật) + công tăng mà kết quả đứng yên (phá
> nhân quả) + câu hỏi KHÔNG trả lời (để lại món nợ, không phải lời hứa).
> 🔑 Luật lớn: **hook mạnh nhất là hook KỂ CHÍNH CÁI BỆNH bài sẽ chữa** — hỏi *"cảnh nhỏ nhất
> mà cái bệnh này ĐÃ xảy ra rồi là cảnh gì?"*, đừng hỏi *"câu nào giật nhất"*.
> Phép so công bằng: cả 2 bản cùng dây chuyền tiếng (đuôi −36,9 vs −35,9 dB), bản mới không
> thắng nhờ bản vá khác.
>
> ✅ Cổng bước 3 (thước nghề giữ mắt) **đã chạy end-to-end** trong lượt này — hết chỗ chưa kiểm.
>
> ✅ **VIỆC 0b — KHOÁ RENDER: XONG 25/07.** `video/khoa_render.py` (`fcntl.flock` trên
> `state/dang_render.lock`), cắm TRONG `render_headless.py` · `auto_render.py` ·
> `capture_slides.py` (không cắm ở `lam_bai.py` vì còn bị gọi tay). Đã thử chặn thật: giữ khoá
> rồi chạy 2 script THẬT → exit **50**, không quay; nhả xong chạy lại → exit 0, đủ 10 slide.
> Xem ai giữ: `python3 video/khoa_render.py --kiem`. Mã 50 ≠ render hỏng, chỉ là xếp hàng.
>
> ✅ **VIỆC 0c — HỢP NHẤT `tri_thuc/` + `video/` VÀO GIT: XONG 25/07.**
> Gốc bệnh: `Cloud/` KHÔNG phải repo (repo là `Research copy/`), mà `video/` nằm NGOÀI repo ⇒
> `../tri_thuc/` trỏ ra một bản sao ngoài git. Đã gộp **311 mục, 0 mất 0 lặp** (+68 gạch đầu
> dòng `kinh_nghiem`), rồi `Cloud/tri_thuc` → **symlink** vào `Research copy/tri_thuc`.
> **Chỉ còn MỘT sổ, nằm trong git.** ⚠️ Thứ tự tương đối trong 24-25/07 không tin được.
> `video/` giờ là **repo git riêng** (`main`, commit `dfe6e01`, 325 file/31,4 MB, `.git` 6,3 MB).
> Đã quét khoá: `.env` · `key.rtf` · `config/tts.json` đều KHÔNG vào git. Rollback đã thử thật.
>
> **VIỆC 1 — ✅ BOSS ĐÃ DUYỆT HẾT 25/07** (*"những video đó làm đều đạt cả"*): 8 bài Superpowers
> + `hpd_01_danhgia` + `headless_05_skill`. Đã cất vào `thanh_pham/` (superpowers vào ngăn
> riêng `kynang/superpowers/`, headless_05 thành `bai_05_skill_nghe_tu_bat/`).
> ⚠️ Duyệt = **đạt**, không phải *không cần khá hơn*: số đo vẫn cho 6 bài trùng scene 80-88%
> và 8 bài cùng một kiểu hook. Chưa duyệt: `msr_01` · `ruiro_0{1,2,3}` · `PNJ_02`.
>
> **VIỆC 2 — 6 LỖI HEADLESS ĐÃ VÁ HẾT** (thợ 2 soi 5, thợ 1 bắt thêm lỗi thứ 6 khi dựng deck mới):
> highlight/traffic-light + đếm reveal · hạt bùng nổ · chiều trượt slide · 20 SFX + nhạc nền 0.3 ·
> thẻ màu bt709 · **phụ đề (lỗi IM LẶNG: chỉ đọc cache, deck mới ra video không phụ đề mà vẫn PASS
> mọi phép đo)**. Chi tiết + cách vá: patch_history 24/07 khuya.
>
> **VIỆC 3 — dựng bài superpowers tiếp theo thì làm đúng đường này** (đã chạy trơn 1 lượt):
> ```bash
> cd video/escbase_template
> cp -R headless/deck_thu headless/deck_sp0X && rm -rf headless/deck_sp0X/output*
> # viết script-90s.txt 10 dòng, ÉP số câu = [1,3,3,2,3,3,3,3,3,3] để tái dùng scene deck 05
> .venv/bin/python sync_script.py headless/deck_sp0X headless/deck_sp0X/script-90s.txt
> .venv/bin/python generate_tts.py headless/deck_sp0X --engine edge --voice vi-VN-NamMinhNeural --rate "+14%"
> .venv/bin/python remap_palette.py headless/deck_sp0X sp    # palette CHUNG của series
> # sửa index.html (thay chữ, giữ scene) + <title>/<meta>/?v=
> .venv/bin/python validate_slide.py headless/deck_sp0X --semantic-report   # phải PASS
> .venv/bin/python capture_slides.py headless/deck_sp0X    # rồi Read TỪNG ảnh
> .venv/bin/python headless/render_headless.py headless/deck_sp0X          # CHẠY NỀN, ~3 phút
> ```
> ⚠️ **Deck MỚI thì phải ĐO PHỤ ĐỀ** (đếm pixel vùng y≈1330-1520), đừng tin "video trông ổn".
> 🟡 Còn 6 rủi ro nhỏ chưa vá, chỉ dính deck có tính năng đó: `slideLights` từng slide đứng ở slide 0 ·
> `data-count-to` không đếm lên · `<video>` nhúng đứng khung đầu · thiếu `ensure_voiceover_matches_timing` ·
> nhánh `'slide'` từng thiếu `{subtree:true}` (đã thêm) · font/icon nạp từ mạng chỉ chờ `load`.
>
> --- (dưới đây là việc CŨ của nhánh escbase quay-live, vẫn treo) ---

### 🎯 (cũ) ĐÃ RENDER XONG 03→10, **CHỜ BOSS DUYỆT 05→10**
> **TRẠNG THÁI 24/07 cuối ngày: escbase 03→10 ĐỦ 8/8 BÀI ĐÃ RA MP4.** 03+04 BOSS duyệt rồi
> (đã cất `video/thanh_pham/`). **05→10 render xong, CHỜ BOSS NGHE/XEM.** Tất cả ở `results/video/`:
>
> | Bài | File | Dài | Cỡ | Tiếng | Palette |
> | :-- | :-- | :-- | :-- | :-- | :-- |
> | 05 skill | `escbase_05_skill.mp4` | 94,1s | 19,5 MB | −17,4 dB | rose + gold |
> | 06 MCP | `escbase_06_mcp.mp4` | 101,8s | 22,1 MB | −17,3 dB | sky + lime |
> | 07 plan mode | `escbase_07_plan_mode.mp4` | 83,9s | 18,3 MB | −17,4 dB | teal + cam |
> | 08 checkpoint | `escbase_08_checkpoint.mp4` | 92,1s | 20,4 MB | −17,5 dB | tím + lục |
> | 09 token | `escbase_09_token.mp4` | 100,2s | 22,7 MB | −17,3 dB | cam + sky |
> | 10 kết | `escbase_10_ket.mp4` | 91,4s | 20,6 MB | −17,2 dB | lục + vàng |
>
> Cả 6: 1080×1920 · validate PASS (thợ 1 chạy lại độc lập) · quét màu sạch · **đo hụt khung sạch**
> · tiếng khớp hình (lệch +0,49…+0,71s). Bài 06→10 do **5 subagent Sonnet dựng song song** (B1–B7),
> thợ 1 kiểm lại + render tuần tự.
>
> **3 VIỆC CHỜ BOSS PHÁN (AI không tự quyết được):**
> 1. **Duyệt/chê 05→10.** ⚠️ Giật 2-3s đầu VẪN CÒN (vá rẻ đã thất bại, xem mục 📍 trên).
> 2. **Độ dày nội dung:** cả 6 bài để trống nửa dưới khung (vùng phụ đề). 3/5 thợ tự nêu là "hơi
>    thưa" so với bài 03/04. BOSS phán loãng thì dựng dày lại đồng loạt.
> 3. **Bài 09:** thợ rút tiêu đề mở bài "BÀI QUAN TRỌNG NHẤT" → "Quan trọng nhất" cho vừa khung.
>
> **Duyệt xong thì:** copy mp4 vào `video/thanh_pham/bai_XX_<tên>/` (quy ước BOSS đặt 24/07).
>
> --- (bên dưới là CÔNG THỨC RENDER escbase cũ — vẫn dùng, chỉ đổi giọng sang NamMinh) ---
> **Bản `escbase_01_hooks_NHAT.mp4` (23/07) từng là chuẩn 3 mảnh** (giờ thay giọng):
> 1. **Giọng:** ElevenLabs "Nhật - Narrative & Compelling" qua `config/tts.json` (đã cấu
>    hình sẵn: key 2 PAYG + voice `6adFm46eyy74snVn6YrT` + model `eleven_turbo_v2_5`).
> 2. **Render NÉT:** `RENDER_DSF=2.769230769230769 .venv/bin/python
>    render_elevenlabs_tts.py slide/<deck> --size 390x693` (ra 1080×1918, nhịp đúng).
> 3. **Trộn tiếng + pad 1920:** ffmpeg `voice ×2,0 + bgm ×0,9 + amix normalize=0 +
>    alimiter=0.95` + `pad=1080:1920` (lệnh nguyên văn: patch_history mục 23/07 ĐÊM
>    video/escbase, hoặc chép từ lượt gần nhất).
> **VIỆC KẾ TIẾP PHIÊN SAU:** (a) BOSS chọn đường chính thức escbase vs Pillow (bản Nhật
> đã là ứng viên mạnh); (b) nếu escbase → dựng deck HTML/CSS cho 9 bài còn lại theo đúng
> WORKFLOW template (mỗi bài phải viết deck riêng, ~1 buổi/vài bài); (c) quota ElevenLabs
> 23.736 ký tự/tháng ≈ đủ ~12-13 bài — render cả bộ thì vừa khít, hỏi BOSS trước khi vượt.
> ⚠️ Nhắc BOSS mỗi lần render: trình duyệt tự mở = MÁY QUAY, đừng tắt.

#### Hồ sơ 4 nút đã đóng (tra khi cần, đừng mở lại)
1. 🔴 **BOSS không nghe thấy giọng — mâu thuẫn chưa gỡ, HỎI BOSS TRƯỚC KHI LÀM GÌ.**
   🆕 23/07 ~21:00 (Fable đo thêm, đừng đo lại): lượt render 20:34 SẬP giữa chừng —
   `tab_capture_raw.webm` **0 byte**, KHÔNG có video mới nào sau bản v2 (20:22); nếu BOSS
   mở "bản dựng lại" sau 20:22 thì đang mở file hỏng/không tồn tại. Đã cắt 2 file thử 15s
   cho BOSS nghe chốt bệnh: `results/video/kiemtra_15s_GIONG_THUAN.mp3` (giọng thuần) +
   `kiemtra_15s_TU_BAN_V2.m4a` (trích từ v2). Nghe được mp3 mà không nghe được m4a → lỗi
   trộn/file; cả 2 đều câm → lỗi máy phát/loa.
   BOSS 20:15: "giọng rõ, nhạc nhỏ quá" (bản `_v2`) → 20:40: "có nhạc nhưng không nghe
   thấy giọng". Máy đã đo (ĐỪNG đo lại): Whisper nghe ra 22-28 đoạn khớp kịch bản trong
   CẢ 2 file; giọng −20 dB, nhạc −34 dB; 2 kênh cùng pha (KHÔNG phải triệt pha);
   `_CHI_GIONG.mp4` là mono 0 nhạc. ⇒ Nếu BOSS nghe thấy NHẠC trong `_CHI_GIONG` thì
   BOSS mở KHÔNG PHẢI file đó. **Việc đầu tiên phiên sau: hỏi BOSS đang mở đúng TÊN FILE
   nào** + cho nghe 1 đoạn 15 giây chỉ giọng để chốt lỗi ở file hay máy phát.
   ⚠️ AI KHÔNG NGHE ĐƯỢC — cấm tự kết luận "giọng ổn".
2. ✅ **Trộn tiếng — ĐÃ GIẢI 23/07 ~21:20 (bản NHẬT).** Đo ra gốc bệnh: `amix` mặc định
   của template CHIA ĐÔI mọi kênh (normalize) ⇒ bản final mặc định chỉ −30,7 dB dù giọng
   thuần −22,4 · nhạc −33,1 ⇒ cả video bé tiếng — đây là lý do BOSS "không nghe thấy
   giọng". Bản `escbase_01_hooks_NHAT.mp4` trộn lại: `voice ×2,0 + bgm ×0,9 +
   amix normalize=0 + alimiter=0.95` ⇒ mean −18,8 dB, đỉnh −0,1 dB. Số này BOSS nghe rồi
   mới chốt làm chuẩn cho các bài sau.
3. ✅ **Video mờ — GIẢI XONG 23/07 đêm (vá `RENDER_DSF` trong `auto_render.py`).**
   Chân tướng: "sập" hôm trước là **BOSS tự tắt cửa sổ Chromium** (xác nhận miệng) — 2 bản
   vá bị oan. Đo loại trừ: native 1080 GIÃN timeline (180,6s vs giọng 112,9s) ⇒ cấm đường
   đó; probe chụp màn hình cho thấy `zoom` thật ra vẫn ăn — chẩn đoán cũ sai. Cách chạy
   NÉT chuẩn từ nay:
   `RENDER_DSF=2.769230769230769 .venv/bin/python render_elevenlabs_tts.py slide/<deck> --size 390x693`
   (layout 390 không giãn, GPU raster 1080×1918 nét, pad 1920 lúc trộn tiếng; RENDER_DSF
   không đặt = hành vi gốc). ⚠️ Dặn BOSS: trình duyệt tự mở lúc render là MÁY QUAY — đừng tắt.
4. ✅ **Key ElevenLabs + giọng "Nhật" — ĐÃ THÔNG (23/07 ~21:05).** `key.rtf` có **2 key**;
   key thứ 2 (`sk_7b2c…`) là key mới, gói **PAYG active** (hạn mức 23.736 ký tự, đã dùng
   ~250). Đã: tìm thấy giọng **"Nhật - Narrative & Compelling"** (`6adFm46eyy74snVn6YrT`,
   nam Bắc, chuyên narration, verified vi với `eleven_turbo_v2_5`) → thêm vào My Voices →
   tạo `config/tts.json` (key 2 + voice + model turbo_v2_5; file nằm trong `.gitignore`).
   **Mẫu thử chờ BOSS nghe: `results/video/thu_giong_NHAT.mp3`** (14s, lời mở bài Hook).
   **BOSS đã GẬT giọng (23/07 ~21:10) → ĐÃ RENDER CẢ BÀI: `results/video/
   escbase_01_hooks_NHAT.mp4`** (1080×1920 · 113,6s · 12,5 MB · trộn tiếng theo nút 2;
   đường render `--size 390x693` + phóng ffmpeg chạy sạch, KHÔNG sập trình duyệt lần này).
   Verify: meta 9/9 line `engine=elevenlabs` đúng voice_id · frame 6s+60s soi mắt đạt ·
   volumedetect đạt. Quota sau render báo 288/23.736 — billing ElevenLabs cập nhật TRỄ,
   đừng tin số đọc ngay sau lượt gọi. Cache TTS đã là giọng Nhật nên render lại 0 tốn quota
   (ĐỪNG `--force` — luật escbase). ⚠️ Lúc quay, trình duyệt chỉ phát nhạc nền — giọng trộn
   SAU bằng ffmpeg; xem giữa chừng không nghe giọng là ĐÚNG thiết kế. ⚠️ key 1 cũ trong
   `.env` (`elevenlap_api`) vẫn là key thiếu quyền — script escbase KHÔNG đọc `.env` nên
   không sao, nhưng đừng nhầm. Hồ sơ tường 402 cũ (đã hết hiệu lực): gói free chặn cứng
   `402 — Free users cannot use library voices via the API` (đã đo bằng key thật;
   `.env` vẫn key cũ, `config/tts.json` chưa tồn tại). 2 đường: (a) BOSS dán tay trên
   web ElevenLabs → tải mp3 → `render_elevenlabs.py` tự cắt 9 đoạn; (b) nâng Starter
   ~$5/tháng. BOSS đã nói giọng edge "cũng được" nếu bí. ⚠️ ĐÃ TỪ CHỐI: clone giọng
   "Nhật" bằng viXTTS/F5-TTS — giọng người thật đóng góp, vấn đề quyền. Chi tiết ④.

### Chờ BOSS
1. Xem nội dung khóa mới tại `kichban/superpowers/README.md`; nếu duyệt mới render
   thử bài 01 (không chạy cả 8 bài trước khi duyệt mẫu).
2. **Chọn đường đi tiếp**: xem `results/video/escbase_01_hooks.mp4` so với
   `results/video/01_hooks.mp4` (Pillow) — theo escbase hay theo Pillow?
3. Có commit cả thư mục template 199k (`video/escbase_template/`) vào repo không?
4. Xem `01_hooks.mp4` bản viết lại — chỗ nào còn khựng thì chỉ đúng số cảnh; sửa 1 cảnh
   render lại chỉ ~1 phút (cache giữ phần còn lại).
5. Có muốn thêm truyện không? BOSS thích dạng truyện; bài học nào cũng gói được.

### Việc AI làm tiếp
- Ngoài 4 nút escbase trên: không còn việc treo. Bộ 10 bài Pillow đã xong.
- Chưa làm, chưa ai yêu cầu: nhạc nền (dây chuyền Pillow) · hiệu ứng chuyển cảnh ·
  phụ đề động kiểu Reels · ảnh bìa từng bài.

---
# THAM KHẢO (hook KHÔNG nạp — tự đọc khi cần)

# ⭐ CÔNG THỨC LÀM VIDEO ESCBASE CHUẨN (chốt 24/07 — làm theo, ĐỪNG mò lại)
Dựng 1 bài video escbase từ đầu tới mp4 nét. Bài 03 (`slash-command-cai-nut`) +
bài 04 (`subagent-sai-nguoi-di`) làm đúng quy trình này — chép khuôn của chúng.

**Vị trí:** dây chuyền `video/escbase_template/`, chạy `.venv/bin/python` TRONG đó.
Nội dung dạy: `video/kichban/0X_*.md` (BOSS đã viết theo 7 nhịp — chỉ reformat, đừng bịa lại).

**B1. Copy scaffold** (chép bài GẦN NHẤT đã sạch màu, KHÔNG chép bài 02 vì dính indigo):
```bash
cp -R video/escbase_template/slide/claude-code-<bài trước> \
      video/escbase_template/slide/claude-code-<slug bài mới>
```
**B2. Viết `script-90s.txt`**: mỗi DÒNG = 1 slide (~10 slide). Slide 1 = 1 câu hook. Slide sau
2-4 câu. **Số câu (tách theo . ? !) = số reveal**. KHÔNG dùng dấu gạch dài `—` (TTS đọc xấu).
Giữ ẩn dụ "người thợ" + ví dụ THẬT của dự án + câu chốt đối xứng (kiểu bài 01).
**B3. Đồng bộ LỜI ở 3 NƠI — khớp từng chữ** (validator so): `script-90s.txt` · mảng
`const slideScripts=[…]` trong `app.js` · `slides.scriptLines` trong `preview-settings.json`.
**B4. Sửa `index.html`**: 10 slide, tái dùng scene bài trước (hero orbit · hk-head/kicker/title ·
mock-terminal · hk-funnel · hk-vs-node so sánh · hk-lockup chốt · hk-strike) + scene riêng cho nội
dung mới. Reveal = số `.slide-element`; slide `data-mode="highlight"` thì reveal = `.slide-element`
+ `.highlightable`. Đổi `<title>`/`<meta>`. Giữ 2 góc `dungladu.vn`.
**B5. ĐỔI PALETTE (mỗi bài 1 màu khác: 01 xanh·02 indigo·03 amber·04 cyan·…):** sửa 4 chỗ +
remap: (a) `:root` trong style.css; (b) `defaultPreviewSettings` trong `app.js` = **NGUỒN MÀU LÚC
CHẠY**; (c) theme trong `preview-settings.json`; (d) **REMAP hex+rgba màu cũ còn hardcode** trong
style.css VÀ app.js (viết script Python `re.sub` map cả `#hex` lẫn `rgba(r,g,b` — cả có/không space,
giữ alpha). Sửa mỗi `:root` là KHÔNG đủ — phải capture soi mới biết đúng màu.
**B6. Validate** (PASS, không `--skip-safezone`):
`.venv/bin/python validate_slide.py slide/<slug> --semantic-report`
(lỗi hay gặp: câu≠reveal → thêm/bớt `.slide-element`; tràn đáy → giảm margin/font hoặc `hk-content-tight`).
**B7. Capture + SOI MẮT** (Read TỪNG ảnh, không tin exit code):
`.venv/bin/python capture_slides.py slide/<slug>` → `/tmp/escbase-qa/<slug>/slideN.png`.
**B8. Render NÉT (BẮT BUỘC `RENDER_DSF`, nếu không sẽ NHOÈ):**
```bash
cd video/escbase_template
RENDER_DSF=2.769230769230769 .venv/bin/python render_edgetts.py slide/<slug> \
  --voice vi-VN-NamMinhNeural --speed 1.14 --size 390x693
```
(ra `slide/<slug>/output/final_video.mp4` ~1080×1918 native nét · edge free, cache sẵn ·
⚠️ trình duyệt tự mở = MÁY QUAY, đừng tắt).
**B9. Phóng 1080×1920 + nâng tiếng** (template trộn ra ~−28 dB, quá nhỏ):
```bash
ffmpeg -y -i <output>/final_video.mp4 \
  -vf "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p" \
  -af "volume=11dB,alimiter=limit=0.95" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k \
  results/video/escbase_0X_<slug>.mp4
```
CHỈ `pad`, **KHÔNG `scale`** (scale = nhoè lại). Kiểm cuối: ffprobe (1080×1920) · volumedetect
(mean ~−17 dB, max<0) · trích 2-3 frame rồi **Read** (nét + màu đúng).
**B10.** ⚠️ **Giọng để BOSS nghe** — AI cấm tự phán hay/dở. Báo BOSS duyệt.

**Chia việc với subagent (thợ 2):** thợ 2 chỉ làm **B1–B7** (dựng deck + validate + capture soi);
**phần render B8–B9 để thợ 1/phiên chính làm** — vì render nền trong subagent hay TREO mồ côi khi
phiên con kết thúc (đã dính 24/07). Nhận deck của thợ 2 thì tự validate + soi lại, đừng tin báo cáo.

**Số ĐO thật (24/07):** render escbase ~2-3 phút/bài · bài dạy ra 80-105s · file 1080 nét ~17-20 MB.

# ⭐ CÔNG THỨC VIẾT KỊCH BẢN (phần quan trọng nhất — trả giá mới có)

**BOSS xem bản 1 của bài Hook và KHÔNG HIỂU.** Đó là thất bại đắt nhất của dự án con này.
Nguyên nhân mổ ra được, và cách chữa đã kiểm chứng bằng bản viết lại:

| Bản 1 (BOSS không hiểu) | Bản 2 (đã chữa) |
| :-- | :-- |
| Mở bằng khái niệm: *"Bạn dặn AI một nguyên tắc"* | Mở bằng **cảnh đời thường có người, có đồ vật**: *sáng nào cũng một người thợ mới; bạn dặn đừng đụng tủ hồ sơ; ngày thứ 30 một người quên, dọn luôn cái tủ* |
| Ẩn dụ mờ: "hook là rào chắn máy" | Ẩn dụ **sờ được**: "hook là **CÁI KHOÁ**" — chặn bàn tay ngay lúc tay chạm tủ |
| Tên kỹ thuật ném ra từ cảnh 4 | Tên kỹ thuật để **mãi cảnh 11**, sau khi đã có "lúc vào cửa / lúc cầm đồ nghề / lúc ra về" |
| Cách làm nói bằng chữ lập trình: *"đọc JSON từ stdin, in ra stdout"* | Nói bằng chữ thường: *"nhận **tờ phiếu ghi thợ định làm gì**, trả lời một chữ: cho hay không cho"* |
| Không có ví dụ chạy thử | **6 cảnh đi chậm qua một lần chặn thật, bốn bước**, có cả câu chốt vì sao khoá phải đứng TRƯỚC |
| 83 giây | 163 giây |

**BOSS chốt 23/07: *"không cần làm quá ngắn đâu. Đúng là đủ."*** ⇒ Đủ để hiểu mới là đủ.
Đừng nén cho ngắn. Bài dạy 100-165 giây là bình thường.

### Khuôn 7 nhịp — viết bài mới thì bám cái này
1. **Cảnh đời thường** (2-3 cảnh): có người, có đồ vật, KHÔNG một chữ kỹ thuật nào.
2. **Vấn đề lộ ra** — thường ở "ngày thứ N" khi cái sai cuối cùng cũng xảy ra.
3. **Chỉ đúng chỗ đau** — lỗi không nằm ở đâu, mà nằm ở đâu.
4. **Ẩn dụ sờ được** → rồi mới tới **tên kỹ thuật**. KHÔNG BAO GIỜ ngược lại.
5. **Ví dụ THẬT của dự án, có số** (`134 KB`, `2.700 token`, `ngày thứ 30`). Số làm nó thật.
6. **Đi chậm qua một lần chạy thử**, đánh số bước 1-2-3-4.
7. **Bẫy** rồi **câu chốt đối xứng** ("Lời dặn có ngày bị quên. Cái khoá thì không.").

### Luật nhỏ đã kiểm
- Người thợ mới mỗi sáng = **ẩn dụ xuyên suốt cả 10 bài**. Đừng đổi ẩn dụ giữa bộ.
- Dòng `MÃ:` không được ngắt giữa chừng → script tự thu chữ cho vừa 1 dòng (đã vá).
- Lời đọc **cũng là phụ đề** dưới đáy ⇒ viết lời sao cho đọc chữ cũng hiểu, tắt tiếng vẫn theo được.
- Truyện kể (`truyen_*.md`) là dạng BOSS thích nhất. Bài học nào gói được thành truyện thì gói.

## CÁCH CHẠY (chép thẳng)
```bash
# 1 bài
.venv/bin/python video/lam_video.py video/kichban/01_hooks.md
# render thử vài cảnh (nhanh, để soi bố cục)
.venv/bin/python video/lam_video.py video/kichban/01_hooks.md --canh 1-3
# cả bộ — ⚠️ CHẠY NỀN, mỗi bài ~2-4 phút, quá 10 phút là Bash tool cắt
for f in video/kichban/0[1-9]_*.md video/kichban/10_*.md; do
  .venv/bin/python video/lam_video.py "$f" 2>&1 | tail -1; done
```
Ra `results/video/{tên}.mp4`. Xem: `open results/video/01_hooks.mp4`.

## ĐO THẬT (đừng đoán lại)
| Việc | Số đo | Ngày |
| :-- | :-- | :-- |
| Render 1 bài ~15 cảnh | **2-4 phút** (quá 10 phút thì Bash tool cắt → chạy nền) | 23/07 |
| Bài dạy sau viết lại | 108-163 giây · 2,8-4,4 MB | 23/07 |
| Edge TTS | **không hạn mức, không cần key** — render bao nhiêu lần cũng được | 23/07 |
| Gemini TTS `2.5-flash-preview-tts` | 5-10 giây/cảnh · **~11-12 lượt/key/ngày** ⇒ 5 key ≈ 5 video/ngày | 23/07 |
| Gemini TTS `3.1-flash-tts-preview` | 17,4 giây — **chậm gấp 3, đừng dùng** | 23/07 |
| Cache TTS | hash (lời + giọng + model + NGHỈ) ở `state/video_tts/` ⇒ **sửa slide, render lại: 0 lượt API** | 23/07 |
| Render escbase 1 bài | ~3 phút (Chromium 93 MB + 45 gói) | 23/07 |

## HAI ENGINE GIỌNG + ĐƯỜNG THỨ BA
| Cách khai `GIỌNG:` | Được gì | Mất gì |
| :-- | :-- | :-- |
| **`edge:vi-VN-NamMinhNeural:+14%`** ⭐ đang dùng | Giọng nam **người Việt bản địa**. Free, không key, không hạn mức. Chỉnh được tốc độ | Đường **không chính thức** (dịch vụ đọc-to của Edge); **endpoint CHẬP CHỜN** → đã vá thử lại 4 lần |
| `Iapetus`, `Charon`… (30 giọng Gemini) | Chính thức, dặn được lối đọc (`KIỂU:`) | Giọng đa ngữ đọc tiếng Việt; ~11-12 lượt/key/ngày |
| **`TIẾNG: <file>`** trong cảnh | Dùng **CapCut · ElevenLabs · Vbee · giọng người thật** | Làm tay, mất cache |

**Đường CapCut đã gỡ được nút thắt** (`--tach-tieng`): dán 1 lần, xuất 1 file, máy dò khoảng
lặng cắt ra đúng N cảnh. Chi tiết 3 bước: `video/README.md`. Giọng BOSS khen: **"Thanh niên
tự tin"** — CapCut không có API nên chỉ lấy được bằng đường này.

## NGUỒN GIỌNG NAM KHÁC (Antigravity khảo sát — Opus ĐÃ KIỂM, đừng tin nguyên si)
| Nguồn | Giọng nam | Free thật | Rào cản |
| :-- | :-- | :-- | :-- |
| **FPT.AI** | `leminh` (bản địa) | 100k ký tự/tháng | đăng ký, **không cần thẻ** — đáng thử nếu bỏ edge |
| Google Cloud TTS | `vi-VN-Neural2-D` | 1 triệu ký tự/tháng | **phải khai thẻ** |
| Piper / sherpa-onnx | `vi_VN-vais1000-medium`… | vô hạn, offline | tải model, **giới tính chưa rõ** |
| EraX viF5TTS | bản địa | vô hạn, offline | giấy phép **CC-BY-NC: cấm thương mại** |
| gTTS | — | — | **chỉ có giọng nữ** |

**2 lỗi Antigravity bịa, Opus bắt được** (chi tiết `tri_thuc/api_free.md` mục 2b): bịa ID giọng
Piper `vi_VN-nam-medium` (không tồn tại) · khai Microsoft "cấm" edge-tts thương mại trong khi
**Microsoft không có tài liệu công khai nào** — chỉ là *không rõ*. ⇒ Với mục đích dạy học,
chia sẻ, không kiếm tiền thì edge-tts rủi ro thấp.

## ⚠️ GIỚI HẠN CỦA AI TRONG DỰ ÁN NÀY (đọc trước khi hứa với BOSS)
**AI KHÔNG NGHE ĐƯỢC.** Không nghe được file mình vừa tạo, không mở được video mạng xã hội
(Facebook/TikTok đòi đăng nhập). Mọi phán xét về *giọng hay dở, đọc sai dấu, nhịp nhanh chậm*
**bắt buộc để BOSS nghe rồi phán**. Đừng bao giờ viết "giọng nghe tự nhiên" — đó là bịa.
Cách làm đúng: **dựng bài thử nhiều phương án cho BOSS chọn** (`00_thu_giong.md`).

**Đầu ra là ẢNH thì phải MỞ RA SOI.** Script chạy exit 0 không có nghĩa slide đúng: đã từng
render sạch mà dòng lệnh bị ngắt làm đôi. Luôn `Read` file PNG trước khi báo xong.

## CHI TIẾT ESCBASE (bổ trợ cho 🎯 4 nút — 23/07 tối)

### Bối cảnh: thử nghiệm template (BOSS mua 199k, lệnh "thử làm 1 video hoàn toàn bằng công cụ của họ")
- Deck: `video/escbase_template/slide/claude-code-hook-cai-khoa/` — **9 slide, 26 câu = 26 reveal**,
  nội dung là bài Hook (lời giữ nguyên từ `kichban/01_hooks.md`, gói lại theo khuôn của họ).
  Đi đủ 6 bước WORKFLOW: script chốt → visual-plan `AUTO-APPROVED` → DOM/CSS → validate →
  capture → soi mắt. `validate_slide.py` **PASS** (mapping 1:1 + safezone 9/9).
- Giọng vẫn là giọng BOSS đã chốt: `--voice vi-VN-NamMinhNeural --speed 1.14`. **0 đồng.**
- ⚠️ **BẮT BUỘC render `--size 390x693` rồi tự phóng lên 1080×1920 bằng ffmpeg** — cỡ mặc định
  1080×1920 và cỡ 720×1280 đều VỠ trên máy này (lỗi `zoom` CSS với Chromium mới; chi tiết +
  cách né đã ghi `tri_thuc/kinh_nghiem.md`). Lệnh đã chạy được:
  ```bash
  cd video/escbase_template
  .venv/bin/python render_edgetts.py slide/claude-code-hook-cai-khoa \
      --voice vi-VN-NamMinhNeural --speed 1.14 --size 390x693
  ffmpeg -i slide/claude-code-hook-cai-khoa/output/final_video.mp4 \
    -vf "scale=-2:1920:flags=lanczos,pad=1080:1920:(ow-iw)/2:0:black" \
    -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a copy final_1080.mp4
  ```
- **Được so với dây chuyền Pillow:** slide hiện DẦN theo từng câu · phụ đề karaoke tô chữ đang đọc ·
  nhạc nền + tiếng chuyển slide · animation có nghĩa (đường chạy, gate chặn, đèn đỏ/vàng/xanh).
- **Mất:** nặng hơn (Chromium 93 MB + 45 gói), render ~3 phút/bài, và mỗi bài phải viết HTML/CSS.

### ② Lệnh mẫu bản v3 trộn nhạc (đổi số rồi chạy lại)
```bash
cd video/escbase_template/slide/claude-code-hook-cai-khoa/output
ffmpeg -ss 0.8 -i tab-capture-video/tab_capture_raw.webm -i voiceover_concat.mp3 -i slide_audio.webm \
 -filter_complex "[0:v]fps=30,scale=-2:1920:flags=lanczos,pad=1080:1920:(ow-iw)/2:0:black,format=yuv420p[v];\
[1:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,volume=2.0[tts];\
[2:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,aresample=async=1:first_pts=0,volume=0.55[bgm];\
[tts][bgm]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.95[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k out_v3.mp4 -y
```

### ③ Video mờ — hồ sơ đầy đủ
- **Gốc:** `auto_render.py` phóng slide bằng `zoom: <W/390>` CSS bake vào `_recording.html`.
  Trên **Chromium 149 + Playwright 1.61** (template ghim `playwright>=1.40`, đời cũ hơn nhiều)
  `zoom` KHÔNG ăn ⇒ nội dung chỉ nở ~1,05× thay vì đúng hệ số. Hệ quả: `1080x1920` ra video
  **175 giây trong khi giọng 107 giây**; `720x1280` **vỡ khung** (slide chiếm 57% bề ngang,
  đen viền phải, cắt đáy). Né bằng `--size 390x693` (zoom=1) rồi phóng bằng ffmpeg ⇒ **đúng
  khung, đúng sync, nhưng MỜ vì phóng ảnh 2,77 lần** — đây chính là cái BOSS chê.
- **Đã thử, ĐỀU SẬP TRÌNH DUYỆT** (`TargetClosedError: browser has been closed`, chết giữa
  chừng quanh giây 52 của lượt quay; không phải OOM — đã kiểm 0 tiến trình mồ côi):
  1. `new_context(viewport=390x693, device_scale_factor=W/390)` + `RENDER_ZOOM=1` — sập ở cả
     scale 2,77 lẫn scale 2,0.
  2. Giữ viewport `WxH`, đổi CSS `zoom` → `transform: scale(...)` + `transform-origin: top left` — cũng sập.
  - ⚠️ Lưu ý: lượt render `1080x1920` **đầu tiên** (bản gốc chưa vá) KHÔNG sập, chỉ sai timing.
    Nên chưa loại trừ khả năng sập là do máy/lượt chạy chứ không do bản vá. **Phiên sau nên
    chạy lại 1080 bằng bản GỐC 1 lượt để tách bạch** trước khi vá tiếp.
- **Hướng chưa thử:** cờ Chromium `--force-device-scale-factor=N` (cấp trình duyệt, không qua
  Playwright context) · hoặc hạ Playwright/Chromium về đời template ngắm (`playwright==1.40`).

### ④ Key ElevenLabs — hồ sơ đầy đủ
- Key trong `.env` tên **`elevenlap_api`** (51 ký tự, `sk_`). BOSS nói đã nạp key mới nhưng
  **file `.env` vẫn là key cũ** (sửa lúc 20:10, trước lần thử) và `config/tts.json` **chưa tồn tại**.
- Đo thật bằng API: quyền `text_to_speech` **CÓ**; nhưng thiếu `voices_read`, `models_read`,
  `user_read`. Và chặn cứng: **`402 — Free users cannot use library voices via the API`**.
  ⇒ **Gói free KHÔNG dùng được giọng Voice Library qua API**, bất kể key.
- **2 đường đi:** (a) BOSS vào web ElevenLabs (free được dùng giọng library trên web), dán
  1.795 ký tự trong `script-90s.txt`, tải mp3 về → chạy
  `render_elevenlabs.py slide/claude-code-hook-cai-khoa <file.mp3> --size 390x693`
  (máy tự dò khoảng lặng cắt đúng 9 đoạn); (b) nâng **Starter ~$5/tháng** + tạo lại key đủ quyền
  ⇒ AI làm tự động trọn gói. BOSS đã nói **giọng edge hiện tại "cũng được"** nếu bí.
- ⚠️ ĐÃ TỪ CHỐI, đừng làm lại: clone giọng "Nhật" bằng viXTTS/F5-TTS để né phí — đó là giọng
  của người thật đóng góp, vấn đề quyền. Muốn free thì clone **giọng của chính BOSS**.

## 🗄️ LỊCH SỬ TRẠNG THÁI (tra khi cần — hook KHÔNG nạp khoang này)

> Nguyên văn khoang 📍 TRẠNG THÁI trước lần dọn 25/07/2026. Giữ đủ, không cắt chữ nào.

- 🆕📊✅ **[24/07] ⭐ BÀI **HPD** ĐÃ RA MP4 — `results/video/hpd_01_danhgia.mp4` · CHỜ BOSS XEM/NGHE.**
  Bài tài chính thứ 2 dựng bằng headless, và là bài ĐẦU TIÊN dùng **giọng ElevenLabs "Nhật"**
  (BOSS lệnh giữa phiên, thay edge NamMinh). 1080×1920 · **114,53s** · 24,6 MB · mean **−17,2** /
  max −0,0 dB · bt709 đủ bộ · 30fps · 35 SFX · nhạc nền 0.3 · render 563,8s (164,1 ms/khung,
  **chậm ~2,4× ca MSR — chưa truy nguyên nhân**). 💰 **KHÔNG còn 0 đồng** (ElevenLabs tính theo
  ký tự, lời ~1.900 ký tự) ⇒ **không tự render lại tiếng, không `--force`**, trừ khi BOSS bảo.
  **Nghiệm thu bằng máy:** lệch giọng **0,375 khung** · hụt khung sạch (9 mốc, thấp nhất 34.799,
  không mốc nào =0) · **4s đầu 0/119 khung đứng hình** · **phụ đề có thật** (pixel y1330-1520:
  7.493-14.227, đo đủ 9 mốc) · validate PASS · soi mắt 10 ảnh deck + 3 frame video.
  ⚠️ **Mượt + giọng Nhật PHẢI BOSS PHÁN** — AI không nghe được.
  - **Giá đã làm mới trước khi viết lời:** hồ sơ cũ ghi 16.400đ (10/07). Chạy đủ **cả 4 bước**
    (`capnhat_gia` + `fireant_pull` + `q5_calc` + `gen_trang_dn`) → **16.200đ ngày 24/07/2026**.
  - **Lời:** `kichban/escbase_10dong/hpd_01_danhgia.txt` · `.man_hinh.md` · `README_hpd.md`.
    10 dòng · `[1,2,3,3,3,3,2,2,3,3]` · 25 câu · **380 từ** · hook 16 từ · 0 dấu `—` · 0 từ cấm.
    Nội dung: biên lãi sau thuế **48%**, nhưng ưu đãi thuế 10% (2011→hết 2025) vừa kết thúc, từ
    2026 nộp **20%**; và **bảng kế hoạch 2026 chỉ ghi lãi TRƯỚC thuế, bỏ trống dòng SAU thuế**
    (bảng 2025 ngay trên đó có đủ cả hai). MẶT KIA: vay dài hạn về 0, nợ vay/vốn chủ 0,25→0,11,
    dòng tiền 38,87 tỷ > lãi 24,92 tỷ, kiểm toán chấp nhận toàn phần.
  - **Deck: `escbase_template/headless/deck_hpd01`**, chép từ **`deck_msr01`** — đúng đường cho bài
    tài chính: khuôn reveal khớp sẵn, palette `tc` đã đúng ⇒ **không phải chạy `remap_palette`**.
  - 🔴 **SOI ẢNH BẮT 4 LỖI MÀ `validate` PASS CẢ 2 LƯỢT** — ① *(lỗi NGHĨA, nặng nhất)* slide 10
    dùng khung **cảnh báo ĐỎ** `sg-warn` bọc câu **tích cực** "nhà máy chạy tốt, dòng tiền thật"
    ⇒ đã đổi `hk-note` · ② slide 6 giá trị sổ sách bị tô đỏ `hk-vs-old` ⇒ ngầm phán "xấu" trong
    khi bài CẤM kết luận đắt/rẻ, đã cho cùng màu trung tính · ③ slide 5 nhét `"KH 2026"` vào
    `sg-num` (huy hiệu 1 ký tự) ⇒ chữ tràn thành bóng mờ · ④ slide 7 thiếu ý "vay dài hạn về 0".
    **Chép deck cũ là thừa kế cả NGHĨA của style — phải duyệt lại từng class mang màu/nghĩa.**
- 🆕🎵 **[25/07] MỞ KHO NHẠC NỀN + CATALOGUE SCENE — CHỜ BOSS NGHE 6 BÀI THỬ NHẠC.**
  Đo mở màn: nhạc nền cả dự án là **1 file duy nhất** (`meta.mp3`, md5 giống hệt mọi deck, 60,0s,
  lặp vòng) · bài sp01 **10/10 slide cùng `particles`** · **16/18 mẫu hình của template CHƯA
  DÙNG LẦN NÀO**. Đã làm: ① `render_headless.py` hết ghi cứng `meta.mp3` — thêm `resolve_bgm()`
  đọc `preview-settings.json` (custom · preset · none), sai đường dẫn thì quay về meta.mp3 (thử
  6/6 nhánh đúng); ② `dung_nhac_synth.py` dựng **5 preset nhạc synth** của template thành WAV
  (có sẵn từ đầu mà chưa bao giờ dùng được) — cả 5 chuẩn về **mean −24,1 dB** = đúng mức
  meta.mp3, giữ nguyên tương quan nhạc/giọng đã duyệt; ③ `thu_nhac.py` dựng bài thử **không
  render lại khung nào** (tái dùng `silent.mp4`+giọng+SFX, ~5s/phương án); ④
  `docs/CATALOGUE_SCENE.md` — catalogue **tra bằng ẢNH THẬT**, 18 mẫu đã soi từng cái; ⑤
  `remap_palette.py` nhận hex trực tiếp (`--mau "#38bdf8,#fbbf24"`), khoá cũ giữ nguyên;
  ⑥ vá lỗi ngủ `drain_err` (`readline()` chết vì ffmpeg in tiến độ bằng `\r` — xem kinh_nghiem).
  ✅ **BOSS ĐÃ NGHE VÀ CHỐT (25/07): `synth_lofi` cho SERIES SUPERPOWERS** — đã áp vào
  `deck_sp01/preview-settings.json` (`"bgm": {"mode":"preset","preset":"lofi"}`); deck sp02→08
  chép theo. ⭐ **BOSS bắt được lỗi máy không thấy: "bản đang lồng vào to hơn các bản khác".**
  Đúng — chuẩn RMS ra bằng nhau (−24,1 dB) nhưng **LUFS** (độ to cảm nhận) thì meta −22,7 vs
  synth −24,5…−25,8, lệch tới 3,1 dB. **Đã đổi thước sang LUFS**, 5 bản giờ đều −22,7 LUFS.
  ⚠️ **"Sôi động" thì KHÔNG chữa được bằng âm lượng** — 5 preset đều là pad + arp chậm,
  **không có bộ gõ, không có nhịp** (`playChord` giữ 8s, `playArpNote` 1 nốt/2s).
  ⚠️ **"Còn nhạc nào khác không": KHÔNG** — quét cả dự án, **30 bản `meta.mp3` CÙNG md5**;
  template chỉ ship 1 bản 60s.
  🔒 **BOSS CHỐT CUỐI (25/07): *"chốt nhạc cũ đi, nhạc mới để tôi đi tìm, các video tạm thời
  dùng bộ nhạc lofi sẵn có"*.** ⇒ **AI KHÔNG tự đi tải nhạc nữa.** Phân nhạc hiện tại:
  **superpowers → `synth_lofi`** · **tài chính + bộ dạy 01→10 → `meta.mp3` (giữ nguyên)**.
  BOSS mang bản mới về thì làm theo mục "KHI THÊM BẢN NHẠC MỚI" trong `nhac/NGUON.md`
  (⚠️ chuẩn độ to phải đo **LUFS −22,7**, KHÔNG dùng RMS — xem kinh_nghiem 25/07).
- 🆕📊✅ **[24/07 tối] ⭐ BÀI **MSR** ĐÃ RA MP4 — `results/video/msr_01_danhgia.mp4` · CHỜ BOSS XEM/NGHE.**
  Bài tài chính ĐẦU TIÊN dựng bằng dây chuyền **headless**. 1080×1920 · **108,4s** · 22,9 MB ·
  mean **−17,0** / max −0,9 dB · bt709 đủ bộ · 30fps · 35 SFX · nhạc nền 0.3 · giọng NamMinh +14% ·
  **0 đồng** · render 224,7s (69,1 ms/khung). **(Bản 2 — đã cập nhật giá mới, xem gạch đầu dòng
  💰 dưới; bản 1 giá cũ đã bị đè.)**
  - 💰 **BOSS lệnh cập nhật giá (24/07 tối):** video ban đầu ghi **36.300đ ngày 10/07** (cũ 2 tuần).
    Đã chạy `capnhat_gia.py --symbols MSR` (nguồn công khai VNDirect) **+ `fireant_pull.py pull MSR
    --update`** (BOSS chỉ định) → **2 nguồn khớp tuyệt đối: 33.500đ ngày 24/07/2026** (giảm 7,7%).
    Rồi `q5_calc.py MSR` + `gen_trang_dn.py MSR` dựng lại hồ sơ, sửa lời + deck + man_hinh + README,
    render lại. Lời sau sửa: **381 từ**, khuôn vẫn `[1,2,3,3,3,3,2,2,3,3]`, hook 16 từ.
  - 🔴 **LỖI DỮ LIỆU ĐÀO RA (BOSS nhắm trúng khi bảo "dùng fireant_pull"): `capnhat_gia.py` cập nhật
    giá và **P/B** nhưng KHÔNG cập nhật **P/E**.** `pb_raw` tính từ `gia_hien_tai`, còn `pe_raw` đọc
    từ `raw.fundamentals` (ảnh chụp FireAnt trong DB) — chỉ `fireant_pull` làm mới. Chạy `capnhat_gia`
    một mình ⇒ hồ sơ có **P/B đứng trên giá mới, P/E đứng trên giá cũ** mà không cảnh báo gì.
    Đo thật ca MSR: sau `capnhat_gia` P/B 3,28→3,02 (đúng) nhưng P/E vẫn y nguyên **51,85**; chạy
    thêm `fireant_pull` mới về **48,07** (khớp số FireAnt trả trực tiếp 47,93).
    ⇒ **Từ nay cập nhật giá cho video/hồ sơ phải chạy CẢ HAI**, hoặc vá `q5_calc` tính pe_raw từ
    `gia_hien_tai ÷ EPS` thay vì đọc snapshot (chưa làm, cần BOSS duyệt vì đụng chân ③).
  **Nghiệm thu bằng máy (thợ 1 tự đo, không tin exit code):** thời lượng lệch **0,005s = 0,15 khung**
  so với giọng · **hụt khung sạch** (max dải phải 133-255 ở 6 mốc, không mốc nào =0) · **3s đầu
  6/6 mốc CÓ chuyển động** (không đứng hình) · **phụ đề có thật** (đếm pixel vùng y1330-1520:
  9.404-11.424) · validate PASS · soi mắt 10 ảnh deck + 3 frame video.
  ⚠️ **Mượt/giọng PHẢI BOSS PHÁN** — số trên chỉ chứng minh không còn nguyên nhân kỹ thuật gây giật.
  - **Deck: `escbase_template/headless/deck_msr01`.** Dựng từ **`slide/ruiro-tcl-xuong-ham-ma-soi`**
    (cùng khuôn tài chính ⇒ số reveal `[1,2,3,3,3,3,2,2,3,3]` KHỚP SẴN, palette đã đúng) rồi ghép
    **`app.js` headless của `deck_sp01`** + đổi màu app.js sp→tc. **Đây là đường ĐÚNG cho bài tài
    chính tiếp theo** — đừng chép từ `deck_sp01` như thợ 1 làm hụt lần đầu (xem bẫy dưới).
  - 🔴 **BẪY VỪA DÍNH — `remap_palette.py` CHỈ MAP TỪ BẢNG ROSE CỦA BÀI 05.** Chép `deck_sp01`
    (đã là xanh `#38bdf8`) rồi chạy `remap_palette … tc` thì **primary KHÔNG đổi** (nguồn rose không
    còn tồn tại) trong khi accent lại đổi ⇒ deck **lai màu**, script vẫn báo "đã đổi 728 chỗ" nghe
    như thành công. Phát hiện bằng cách **đếm hex trong style.css sau khi remap**, không phải bằng
    validate. ⇒ Đã thêm khoá **`tc`** (vàng `#ffb020` + đỏ `#ef4444`, `success` giữ lục `#34d399`
    cố ý để slide 7 MẶT KIA tách tông) vào `remap_palette.py`.
  - 🔴 **3 LỖI CHỈ LỘ RA KHI SOI ẢNH (validate PASS cả 3 lần):** ① icon thẻ giá **tím `#a5a0ff`**
    (đúng màu chính docstring `remap_palette.py` ghi là "đã sót 24/07"; deck TCL cũng chưa vá) ·
    ② `.hk-answer-ok` **lime `#a3e635`** chói ở slide 7 · ③ **NẶNG NHẤT, lỗi NGHĨA:** câu chốt
    *"Giá lên là một chuyện."* bị **gạch ngang** (`hk-strike` kế thừa từ deck TCL, chỗ đó vốn để
    PHỦ ĐỊNH) ⇒ màn hình đang phủ nhận một sự thật. Đã vá cả 3 (thêm `#cdeffd`→kem, `#ff8a95`→
    `#fca5a5`). **Bài học: chép deck cũ thì phải soi TỪNG ảnh, lỗi nghĩa không thước nào bắt.**
- 🗄️ **(bản cũ, giữ để tra) Kịch bản MSR — chờ duyệt lời trước khi dựng.**
  - Lời: `kichban/escbase_10dong/msr_01_danhgia.txt` · chữ màn hình `.man_hinh.md` · truy vết
    `README_msr.md`. Codex viết, Opus nghiệm thu ĐỘC LẬP: **10 dòng · `[1,2,3,3,3,3,2,2,3,3]` ·
    25 câu · 378 từ · hook 15 từ · 0 dấu `—` · 0 từ cấm** (quét 33 từ) · 6 số chính tra ngược khớp
    `Research copy/baocao/hoso/MSR_HoSo.md`.
  - Nội dung bài: MSR khai thác vonfram/fluorit/đồng/bismut. Doanh thu **7.442,7 tỷ** → lợi nhuận
    gộp **1.375,3 tỷ** → **lãi vay 1.020,1 tỷ** → LNST **11,29 tỷ**; EPS 10đ (2024 lỗ 1.491đ/cp);
    dòng tiền kinh doanh 1.054,5 tỷ nhưng **657,7 tỷ (62,4%) đến từ chậm trả người bán**;
    5 năm cổ tức 0; giá 36.300đ (10/07/2026).
  - **Lệnh Codex nâng cấp — DÙNG LẠI cho mọi bài tài chính sau:** `Research copy/results/codex/
    lenh_kichban_video_msr.md`. Hơn bản v2 ba thứ: **mục 0 VAI** (nhà phân tích sắc bén + trung
    thực tuyệt đối + hấp dẫn dễ hiểu, 3 phẩm chất KHÔNG đánh đổi cho nhau) · **mục 6 LUẬT HOOK**
    (câu 1 nói thẳng vấn đề, từ đầu tiên phải là SỐ hoặc danh từ cụ thể, cấm mở bằng "có một…/hãy
    tưởng tượng…", bắt viết 3 phương án hook) · **mục 5b MỎ DỮ KIỆN** + rào cấm lấy mục "chờ
    soi/tranh chấp" làm kết luận (lớp đó đo chỉ đúng 8%).
  - ✅ **HOOK ĐÃ CHỐT (BOSS lệnh đổi 24/07 tối):** *"**Giá vonfram tăng một trăm sáu mươi mốt phần
    trăm, lãi cả năm mười một tỷ.**"* (16 từ, 1 câu — số 161% ở `MSR_HoSo.md` ① Khoang 1 dòng 16,
    nguồn BCTN trang Commodity Prices). Bỏ hook cũ của Codex (*"…tỷ tiền lãi…"* — chữ "tiền lãi"
    dễ nghe nhầm thành *lãi lời*, và nói luôn nguyên nhân nên hết tò mò). Kèm sửa câu đối xứng
    slide 10 cho vọng lại hook mới: "Bán nhiều là một chuyện…" → **"Giá lên là một chuyện, giữ lại
    bao nhiêu là chuyện khác."** Thước chạy lại sau khi đổi: **379 từ · hook 16 từ · vẫn đạt hết.**
  - ✅ **VÁ HOOK KHÓA DỮ LIỆU THÔ (BOSS lệnh 24/07 tối):** `video/.claude/settings.json` trỏ tới
    `Cloud/.claude/hooks/khoa_dulieu_tho.py` nhưng file đó không tồn tại (sót từ vụ gom về Cloud)
    ⇒ chốt an toàn ĐANG MỞ, `rm BCTC.db` gọi từ `video/` không bị chặn. Đã copy từ
    `Research copy/.claude/hooks/`; thước `_thu_hook.py` từ **2 LỖI → ✅ SẠCH**.
  - Palette: dùng CHUNG bộ nhận diện series tài chính (vàng `#ffb020` + đỏ `#ef4444`).
- 🆕⭐ **BÀI 01 KHÓA SUPERPOWERS ĐÃ RA MP4 (24/07 khuya) — `results/video/superpowers_01_tong_quan.mp4`.**
  Bài ĐẦU TIÊN dựng trọn bằng dây chuyền headless mới. 1080×1920 · 93,33s · 21,2 MB ·
  mean −17,0 / max −0,3 dB · bt709 đủ bộ · **0/120 khung đứng hình 4s đầu** · hụt khung sạch ·
  phụ đề karaoke · 37 SFX · thanh tiến trình đúng 10/10 slide · giọng NamMinh +14% · **0 đồng**.
  Nội dung: `kichban/superpowers/01_tong_quan.md`, ẩn dụ **xây một căn nhà → 6 trạm kiểm soát**.
  Deck: `escbase_template/headless/deck_sp01` · **palette CHUNG cho cả series superpowers**
  (xanh bản vẽ `#38bdf8` + hổ phách `#fbbf24`, khoá `sp` trong `remap_palette.py`).
  **6 lỗi headless đã vá hết** (5 do thợ 2 soi + lỗi PHỤ ĐỀ im lặng thợ 1 bắt khi dựng deck mới).
  ⚠️ CHỜ BOSS XEM/PHÁN — xem mục 🎯 ngay dưới.
- 🆕✅ **NHÁNH HEADLESS ĐÃ RENDER CẢ BÀI + VÁ 3 LỖI — CHỜ BOSS XEM/PHÁN (24/07 đêm, cuối).**
  Bản để BOSS xem: **`results/video/headless_05_skill.mp4`** (đặt cạnh `escbase_05_skill.mp4`
  để so đôi CÙNG bài 05). 1080×1920 · 93,533s · 20,7 MB · mean −17,1 / max −0,3 dB · render 2'51.
  **TRỊ ĐÚNG BỆNH GIẬT (đo bằng máy): 4s đầu 0/120 khung đứng hình, bản cũ 76/120 = 63,9%.**
  Nghiệm thu 6 bước: thời lượng lệch 0,8 khung · hụt khung sạch · **nét gấp 1,8-2,3× bản cũ** ·
  determinism chỉ lệch viền chữ đang transform (nền hạt trùng bit tuyệt đối) · tiếng đạt đích.
  ⚠️ **Mượt hay chưa PHẢI BOSS XEM** — AI không phán được, số trên chỉ chứng minh nguyên nhân
  kỹ thuật gây giật đã hết. Toàn bộ vẫn cách ly trong `escbase_template/headless/` (nhánh cũ 0
  file bị sửa; rollback = xoá folder). Chi tiết + 3 bản vá: patch_history 24/07 đêm (tiếp).
  🔴 **CHƯA ĐỦ ĐỂ NHÂN RA CẢ BỘ — thợ 2 soi ra 5 lỗi còn lại** (thợ 1 kiểm lại 4/4 điểm nặng đều
  đúng), xem mục 🎯 ĐANG THI CÔNG DỞ ngay dưới.
- 🆕🎬🔁 **[24/07 chiều muộn, VÒNG 2 — BOSS xem bản 1: "video làm tốt lắm. Nhưng kịch bản cần
  format riêng cho tài chính"] ⭐ ĐÃ CÓ **KHUÔN TÀI CHÍNH** + BÀI 01 RENDER LẠI.**
  BOSS phán 4 điều (ràng buộc cứng từ nay cho mọi video tài chính):
  ① **3 giây đầu phải là HOOK**, vào thẳng · ② **không giải thích ví dụ lan man** (bản 1 đốt 2
  slide dựng cảnh "đi xem nhà" mới vào việc) · ③ **CẤM nói về hệ thống phân tích của dự án**
  (bản 1 có "hội tụ 2/2", "hai máy soi độc lập" — người xem không cần biết) · ④ **chỉ từ facts,
  không bịa không bóp méo, đúng là đủ, chất lượng quan trọng nhất**. Phong cách giảng giải của
  bản 1 BOSS khen là hợp người mới ⇒ GIỮ, chỉ bỏ phần lan man.
  - **KHUÔN TÀI CHÍNH 10 SLIDE (dùng cho cả series):** `1` hook ≤16 từ, nghịch lý bằng SỐ ·
    `2` đặt bài (công ty gì + con số đẹp) · `3-6` mỗi slide 1 fact + **1 câu giải nghĩa thuật
    ngữ cho người mới** · `7` **MẶT KIA** (cái tốt / cái chưa xác nhận — chống bóp méo, BẮT
    BUỘC) · `8` **điều báo cáo KHÔNG trả lời được** · `9` **dạy nghề: 3 câu hỏi tự hỏi khi cầm
    báo cáo** · `10` chốt + câu miễn trừ. Số câu chuẩn `[1,2,3,3,3,3,2,2,3,3]` = 25 reveal,
    300-380 từ, ra 85-100 giây. Đề bài đầy đủ + **danh sách từ CẤM**:
    `Research copy/results/codex/lenh_kichban_video_ruiro_v2.md`.
  - **Lời mới:** `kichban/escbase_10dong/ruiro_0{1,2,3}_*.txt` (+ `.man_hinh.md` gợi ý chữ màn
    hình). Codex viết, `KETLUAN|3|75|3`; **Fable soát tay bài 01** cho mượt khi đọc và cắt
    416→370 từ (bản Codex hơi telegraphic). Bản v1 giữ nguyên ở `kichban/ruiro/` để tra.
  - **Ra lại `results/video/ruiro_01_TCL.mp4`** (ĐÈ bản cũ): 1080×1920 · **98,4s** · 20,9 MB ·
    mean −17,5 dB · validate PASS · capture soi + 4 frame · **đo hụt khung sạch** (150-255).
    Deck cùng chỗ `slide/ruiro-tcl-xuong-ham-ma-soi`, index.html dựng lại theo khuôn mới.
  - **✅ ĐỦ 3/3 BÀI ĐÃ RA MP4 (BOSS "dựng luôn 2 video còn lại"), CHỜ BOSS NGHE/XEM:**

    | Bài | File `results/video/` | Dài | Cỡ | Tiếng | Deck |
    | :-- | :-- | :-- | :-- | :-- | :-- |
    | 01 TCL | `ruiro_01_TCL.mp4` | 98,4s | 20,9 MB | −17,5 dB | `slide/ruiro-tcl-xuong-ham-ma-soi` |
    | 02 SKV | `ruiro_02_SKV.mp4` | 100,3s | 21 MB | −17,3 dB | `slide/ruiro-skv-mot-khach-la-chu` |
    | 03 MCF | `ruiro_03_MCF.mp4` | 105,3s | 22 MB | −17,3 dB | `slide/ruiro-mcf-re-ma-khong-lon` |

    Cả 3: 1080×1920 · validate PASS · capture soi 10 ảnh/bài · **đo hụt khung sạch** (129-255) ·
    giọng edge NamMinh +14% · **0 đồng**. **Palette DÙNG CHUNG cho cả series** (vàng #ffb020 +
    đỏ #ef4444) — cố ý khác luật "mỗi bài 1 màu" của bộ dạy Claude Code, vì đây là **nhận diện
    của một series**, xem 3 bài phải thấy cùng một bộ.
  - Lời 3 bài: `kichban/escbase_10dong/ruiro_0{1,2,3}_*.txt` — cả 3 qua thước: 10 dòng ·
    `[1,2,3,3,3,3,2,2,3,3]` · 25 câu · 376/389/411 từ · hook 16 từ · **0 từ trong danh sách cấm**.
  - ⚠️ Bẫy vừa dính: chạy `render_edgetts.py` mà **cwd bị reset về repo khác** ⇒ `can't open file`
    nhưng log lại nối sau dòng "All done" của lượt TRƯỚC ⇒ tưởng đã render. **Luôn `cd` tuyệt đối
    trong CÙNG lệnh render, và kiểm `output/final_video.mp4` tồn tại trước khi ffmpeg.**
- 🆕🎬 **(vòng 1, giữ để tra) SERIES "PHÂN TÍCH RỦI RO" — BÀI 01 (TCL) BẢN ĐẦU
  (24/07 chiều, BOSS lệnh "cho codex đọc kết quả 3 mã rồi dựng kịch bản, dùng dây chuyền
  escbase").** Nội dung lấy từ dự án đầu tư `Research copy/baocao/hoso/{MCF,TCL,SKV}_HoSo.md`
  (chuỗi rủi ro 5 bước chạy 24/07).
  - **3 kịch bản do Codex viết** (lệnh tự-chứa: `Research copy/results/codex/
    lenh_kichban_video_ruiro.md`): `kichban/ruiro/ruiro_0{1,2,3}_{TCL,SKV,MCF}.md`,
    mỗi bài 15 cảnh · 357-391 từ · `KETLUAN|3|45|3`. **Ẩn dụ xuyên series: ĐI XEM NHÀ TRƯỚC
    KHI MUA** (mặt tiền đẹp → phải xuống hầm soi móng, soi đường ống). Luật đã ép trong lệnh:
    chỉ dùng số CÓ TRONG hồ sơ · cấm mọi câu khuyến nghị mua bán · cảnh chốt bắt buộc có câu
    "không phải lời khuyên mua bán".
  - **Deck escbase bài 01:** `escbase_template/slide/ruiro-tcl-xuong-ham-ma-soi` — 10 slide /
    27 reveal · **palette riêng của series: vàng đèn pin `#ffb020` + đỏ `#ef4444`**
    (kicker `--info` đổi `#818cf8`→`#ffcf8a` cho khỏi lạc tông) · validate **PASS** ·
    capture soi 10 ảnh.
  - **Ra: `results/video/ruiro_01_TCL.mp4`** — 1080×1920 · **105,7s** · 21,8 MB ·
    mean **−17,4 dB** / max −0,4 dB · giọng edge NamMinh +14% · **đo hụt khung SẠCH**
    (dải 200px sát phải max 186-255, không đen) · 4 frame soi mắt nét, màu đúng. **0 đồng.**
  - ⚠️ **AI KHÔNG NGHE ĐƯỢC** — giọng/nhịp phải để BOSS phán. Duyệt xong thì copy vào
    `video/thanh_pham/`. Chưa dựng bài 02 (SKV) + 03 (MCF) — **chờ BOSS gật bài 01 trước**.
  - 🔧 Tiện ích dùng lại: `escbase_template/sync_script.py` đồng bộ LỜI vào đúng 3 nơi
    (script-90s.txt · `slideScripts` app.js · `scriptLines` preview-settings.json) và in luôn
    bảng "số câu = số .slide-element phải dựng" — **đừng chép tay 3 nơi nữa**.
- 🆕 **ĐÃ VIẾT KHÓA SUPERPOWERS CHO CODEX — 8/8 KỊCH BẢN, CHƯA RENDER:**
  `kichban/superpowers/` gồm lộ trình + 8 bài (tổng quan; cài/skill; brainstorming;
  worktree/kế hoạch; TDD; thực thi/review; debugging; kiểm chứng/bàn giao). Ẩn dụ
  xuyên khóa: **xây một căn nhà** (BOSS cho phép đổi 24/07). Mỗi bài 14–16 cảnh,
  334–400 từ; 8/8 đã qua parser thật bằng `lam_video.py --loi`. Nguồn khảo sát:
  `obra/superpowers`, manifest Codex v6.2.0 ngày 24/07/2026. **Chưa gọi TTS, chưa
  render, chưa thể phán giọng/nhịp/hình.**
- 🎙️ **GIỌNG ĐÃ CHỐT LẠI (24/07, sau cả buổi thử giọng): quay về `edge:vi-VN-NamMinhNeural`
  (+14%)** — đúng giọng nam ban đầu, đã dùng bài 02 + bộ 10 Pillow. Free, tức thì, 0 quota.
  BOSS đã **loại**: (a) clone giọng chính BOSS (F5-TTS + OmniVoice) — "không hay lắm", chậm;
  (b) Chirp3-HD/Neural2 — hay nhưng không cần. ⇒ Từ nay dùng NamMinh cho cả escbase lẫn Pillow.
- 🧪 **Đã dựng hạ tầng thử giọng (giữ lại, KHÔNG cần nữa nhưng đừng xoá vội):**
  · **Google Cloud TTS THÔNG** qua key `google_console_nicolas_api` trong `.env` (BOSS tự bật
    API + tạo key trên project Nicolas `1048392419235`). vi-VN có: Neural2 A(nữ)/D(nam),
    Wavenet A-D, **Chirp3-HD 30 giọng**. Gọi bằng `escbase_template/.venv` (f5venv lỗi SSL).
  · **OmniVoice-Studio** cài trên **ổ ngoài Trancend** qua **ảnh đĩa APFS** `/Volumes/Trancend/
    ovs.sparsebundle` → mount `/Volumes/OVS` (venv + model ở đó, máy trong nhẹ). Clone chạy
    được trên MPS (`omnivoice-infer --model k2-fsa/OmniVoice`). repo ở `/Volumes/Trancend/
    OmniVoice-Studio`. F5-TTS thì TREO trên MPS → phải CPU (chậm), venv `scratchpad/f5venv`.
  · ~30 file mẫu `results/video/thu_*·PA1_*·PA2_*·GIONG_CHUAN_*·baiday_ChirpNAM_*` để đối chiếu.
- ⚠️ **exFAT làm hỏng venv/HF cache** (symlink + file rác `._`): cài Python nặng lên ổ ngoài
  phải qua ảnh đĩa APFS (sparsebundle) hoặc để cache build ở ổ trong. (→ ghi kinh_nghiem.md.)
- ✅ **BÀI 03 + 04 ESCBASE — BOSS ĐÃ DUYỆT (24/07): "2 bài đó đạt".** Đã copy bản cuối vào
  folder thành phẩm mới `video/thanh_pham/bai_0X_<tên>/` (quy ước từ nay: bài duyệt xong → copy
  mp4 vào đây; `results/video/` giữ bản thô). ⚠️ **GÓP Ý CHO BÀI TỚI (không sửa 03/04):** bài 04
  BOSS thấy **2–3s ĐẦU hơi giật nhẹ**. Gốc: render = quay live 1 tab Chromium (`getDisplayMedia`,
  `headless=False` ghim cứng) → 2–3s đầu trình duyệt nặng nhất (load+font+particles+anim slide1 +
  mã hoá) → rớt frame, giật nướng vào pixel; template chỉ trim 0.8s (`TAB_CAPTURE_WARMUP` dòng 42
  `auto_render.py`). 🔴 **VÁ RẺ ĐÃ THẤT BẠI — ĐÃ HOÀN NGUYÊN (24/07). ĐỪNG THỬ LẠI.** Nâng `TAB_CAPTURE_WARMUP`
  0.8 → 3.0 tưởng vô hại (vì `trim_start` cũng = warmup) nhưng render bài 05 ra **HỎNG NẶNG 2 mặt**:
  (a) **HỤT KHUNG** từ ~giây 20 — dải ~230px mép phải đen tuyệt đối (đo: `max=0` dải 200px sát phải),
  cắt cả thanh tiến trình; (b) **GIÃN TIMELINE +17 giây** (video 110,5s trong khi giọng 93,5s) ⇒ lệch
  tiếng. Đối chứng: bài 03+04 (warmup 0.8) đo lại **sạch mọi mốc**; render lại bài 05 với 0.8 → sạch,
  dài 94,1s (lệch giọng chỉ +0,56s). ⇒ **Đã trả về 0.8 + ghi cảnh báo ngay trong `auto_render.py`.**
  **Cái giật 2-3s đầu VẪN CÒN, chưa có cách chữa rẻ** — chỉ còn đường triệt để bên dưới.
  📏 **Cách ĐO hụt khung (0 API, dùng lại được):** trích frame rồi lấy `max` độ sáng dải 200px sát mép
  phải bằng PIL; `max<=2` là đen tuyệt đối = hụt khung. `ffprobe pkt_pts_time` và `cropdetect` ĐỀU
  KHÔNG bắt được lỗi này (nền tối làm cropdetect nhiễu).
  🔧 **DỰ ÁN NÂNG CẤP (để dành, làm khi rảnh — BOSS lệnh 24/07):** viết lại lõi render sang **headless
  chụp-từng-frame** — Playwright ẩn + `document.getAnimations()` set `currentTime` từng frame +
  particles gieo PRNG cố định (`renderAt(t)`) + audio làm chuẩn thời lượng (`N=ceil(D×fps)`) + ghép
  ffmpeg. Bỏ hẳn cửa sổ + hết rớt frame. codex đã web-search XÁC NHẬN đúng hướng này (Playwright
  per-frame > Remotion/puppeteer-recorder/CDP-screencast/getDisplayMedia). qwen chưa hỏi được: key
  `qwen_api_key_2` trong `.env` chết 401 (endpoint đúng là `<host>/compatible-mode/v1`, chỉ sai key).
- 🗄️ **(bản cũ, giữ để tra) BÀI 03 + 04 ESCBASE ĐÃ RA (24/07):**
  · Bài 03 `results/video/escbase_03_slash_command.mp4` (1080×1920 · 81s · 17,3 MB · mean −17,2 dB ·
    palette **amber #ff9d2e + magenta #ff4d8d**). Deck `slide/claude-code-slash-command-cai-nut`.
  · Bài 04 `results/video/escbase_04_subagent.mp4` (1080×1920 · 103s · 20,3 MB · mean −17,3 dB ·
    palette **cyan #22d3ee + violet #a855f7**). Deck `slide/claude-code-subagent-sai-nguoi-di`
    (thợ 2/subagent dựng deck, thợ 1 render+chốt). Cả 2: giọng edge NamMinh +14% · validate PASS ·
    soi 10 ảnh + 3 frame. Mỗi bài đổi palette khác nhau (01 xanh lá · 02 indigo · 03 amber · 04 cyan).
  · ⚠️ 3 BẪY ĐÃ TRẢ GIÁ (ghi kỹ ở kinh_nghiem): (1) **NÉT**: PHẢI render với
    `RENDER_DSF=2.769230769230769 render_edgetts.py … --size 390x693` (raster thẳng 1080 native);
    quên là ra 388×692 rồi bị phóng 2,77× = NHOÈ (BOSS bắt lỗi bài 03 bản đầu). (2) **MÀU**: đổi
    palette phải remap hex+rgba trong style.css VÀ `defaultPreviewSettings` của app.js (nguồn màu
    lúc chạy), rồi capture soi — sửa mỗi `:root`/preview-settings KHÔNG đủ. (3) **TIẾNG**: template
    trộn ra ~−28 dB, phóng 1080 nhớ `pad` (KHÔNG scale) + `volume=11dB,alimiter=0.95` → ~−17 dB.
  · ⚠️ **BẪY SUBAGENT RENDER TREO:** giao render cho subagent (thợ 2) → nó chạy render nền qua
    `| tail` rồi kết thúc phiên ⇒ tiến trình render MỒ CÔI, treo (0% CPU, không chromium). Lần sau:
    subagent chỉ DỰNG deck + validate + capture soi; để **thợ 1 (phiên chính) render + phóng + chốt**.
- 🎯 **VIỆC CHÍNH CÒN TREO:** escbase **05→10** (mỗi bài đổi palette + giọng NamMinh).
  **Chờ BOSS duyệt bài 03+04 rồi mới chạy loạt** (luật: báo trước việc lớn). Nội dung dạy có sẵn
  `kichban/05_skill.md`…`10_ket.md`. Khuôn chuẩn: xem bài 03/04 (script-90s.txt 3 nơi khớp lời +
  remap màu + validate + capture soi + `RENDER_DSF` render + pad 1080 nâng tiếng).
- 🆕 **BÀI 02 ESCBASE ĐÃ RA — CHỜ BOSS NGHE/XEM:**
  `results/video/escbase_02_claude_md.mp4` (1080×1920 · 95,3s · 12,9 MB · mean −16,7 dB).
  3 điểm BOSS đặt hàng phiên này đều đã làm: (a) bỏ `@escbase` → **`dungladu.vn`** 2 góc;
  (b) **giọng nam BOSS chốt ban đầu** `edge:vi-VN-NamMinhNeural +14%` (KHÔNG dùng giọng Nhật
  ElevenLabs ⇒ 0 đồng, 0 quota); (c) **BOSS chọn template Stripe indigo** trong `template/`
  (blurple `#635bff` + cyan `#00d4ff` + nền đen), hiệu ứng nền hạ về 1 loại nhẹ.
  Deck: `escbase_template/slide/claude-code-claude-md-noi-quy/` — 10 slide · 29 câu ·
  validate PASS (mapping 1:1 + safezone) · đã chụp + soi mắt 10 ảnh + 5 frame video.
- ✅ **VỤ "2 BẢN SAO" ĐÃ XONG (24/07, BOSS lệnh gom về Cloud):** gốc dự án video giờ là
  `/Users/simple/Desktop/Cloud/` (= BASE_DIR của `lam_video.py`). Đã COPY từ `Research copy/`
  (repo ĐẦU TƯ, giữ nguyên) sang cho Cloud tự đủ: `.env` · `.venv` (Pillow+edge-tts) ·
  `state/video_tts`+`tieng_tach` · `results/video` (đủ 39 media) · `tri_thuc/` (21 sổ). Đã
  **XOÁ `Research copy/video/`** (bản trùng, Cloud trội hơn). Escbase tự đủ (venv riêng trong
  `video/escbase_template/`). Render thử 2 cảnh từ Cloud → PASS. ⚠️ Giờ có 2 bản `tri_thuc/`
  (Cloud = của video · Research copy = của đầu tư) → từ nay là 2 DỰ ÁN riêng, ghi sổ ai nấy giữ.
  Git cho Cloud: CHƯA có, BOSS làm mới sau.
- **BOSS DUYỆT BẢN ESCBASE GIỌNG NHẬT (23/07 đêm): "nét rồi, giọng cũng ổn"** —
  `results/video/escbase_01_hooks_NHAT.mp4` (1080×1920 · 113,8s). Công thức chuẩn 3 mảnh
  + việc kế tiếp: xem 🎯 ĐANG THI CÔNG DỞ ngay dưới.
- ✅ **Dây chuyền Pillow 0 đồng, không đăng ký tool nào** (`video/lam_video.py`).
- ✅ **Giọng: 2 chuẩn song song** — dây chuyền Pillow: `edge:vi-VN-NamMinhNeural:+14%` +
  `NGHỈ: 0.9` (BOSS duyệt 2 vòng 20 giọng); escbase: **ElevenLabs "Nhật - Narrative &
  Compelling"** (BOSS duyệt 23/07 đêm). KHÔNG tự đổi giọng nào (luật video/CLAUDE.md).
- ✅ 10/10 kịch bản **viết lại theo công thức 7 nhịp** (mục ⭐ dưới) + 2 truyện + 2 bài thử giọng.
- ✅ **ĐÃ RENDER ĐỦ 10/10 BÀI**, tổng **21 phút 17 giây**, ~32 MB: `01` 168s · `02` 111s ·
  `03` 111s · `04` 153s · `05` 120s · `06` 131s · `07` 106s · `08` 119s · `09` 126s ·
  `10` 112s. Cộng 2 truyện: `truyen_01` 96s · `truyen_02` 51s. Kiểm bằng `ffprobe`
  từng file + soi mắt slide, không tin exit code.
- 🆕 **Thử nghiệm ESCBASE template** (BOSS mua 199k): đã ra `results/video/escbase_01_hooks.mp4`
  (108s) bằng trọn dây chuyền của họ — slide hiện dần theo câu, phụ đề karaoke, nhạc nền,
  animation có nghĩa. Đổi lại: nặng (Chromium 93 MB), ~3 phút/bài, mỗi bài phải viết
  HTML/CSS. **4 nút đang dở** → xem 🎯 ĐANG THI CÔNG DỞ. Chi tiết đầy đủ: mục
  "CHI TIẾT ESCBASE" dưới.
- 🛠️ **23/07: dựng bộ thiết lập chuẩn cho video/**: `video/CLAUDE.md` (luật riêng) +
  `video/.claude/` (hook nạp HANDOFF · nhắc nghi thức · khóa dữ liệu thô gốc ·
  `/dauphien` `/cuoiphien`); thước: `python3 video/.claude/hooks/_thu_hook.py`.

### File đang có (`results/video/`)
| File | Trộn | Ghi chú |
| :-- | :-- | :-- |
| `escbase_01_hooks.mp4` | template mặc định | bản BOSS xem đầu tiên |
| `escbase_01_hooks_v2.mp4` | giọng ×2 · nhạc ×0,25 | BOSS: giọng rõ, **nhạc bé quá** |
| `escbase_01_hooks_CHI_GIONG.mp4` | chỉ giọng, mono, 0 nhạc | file đối chứng |
| **`escbase_01_hooks_NHAT.mp4`** ⭐ | giọng Nhật ElevenLabs · NÉT (RENDER_DSF) · giọng ×2 + bgm ×0,9 | bản mới nhất 23/07 đêm — chờ BOSS nghe |
| `01_hooks.mp4` … `10_*.mp4` | dây chuyền Pillow | bộ 10 bài + 2 truyện |


## BẢN ĐỒ
| Đường dẫn | Là gì |
| :-- | :-- |
| `video/CLAUDE.md` | Luật riêng video + nghi thức + bản đồ |
| `video/.claude/` | Hook (nạp HANDOFF · nhắc nghi thức · khóa dữ liệu gốc) + `/dauphien` `/cuoiphien` + thước `_thu_hook.py` |
| `video/lam_video.py` | Dây chuyền kịch bản → mp4 (neo `BASE_DIR` = gốc repo) |
| `video/kichban/01`…`10` | 10 bài dạy Claude Code |
| `video/kichban/truyen_*.md` | Truyện kể (BOSS thích dạng này) |
| `video/kichban/00*_thu_giong.md` | 2 bài thử giọng — khuôn mẫu khi cần chọn giọng mới |
| `video/escbase_template/` | Template mua 199k — dây chuyền HTML/CSS (đang thử nghiệm) |
| `video/README.md` | Cách chạy + định dạng kịch bản đầy đủ |
| `video/key.rtf` | Key tay của BOSS — gitignore, KHÔNG commit |
| `results/video/*.mp4` | Video ra (gitignore — dựng lại được) |
| `state/video_tts/` · `state/tieng_tach/` | Cache giọng · tiếng đã cắt từ CapCut (gitignore) |

Phụ thuộc ngoài: `ffmpeg` (brew) · `Pillow` + `edge-tts` (trong `.venv`) · font
`/System/Library/Fonts/Supplemental/Arial Unicode.ttf` + `Menlo.ttc` (macOS có sẵn).
