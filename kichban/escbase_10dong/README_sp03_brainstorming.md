# README — sp03_brainstorming (Bài 03 khoá Superpowers)

Người xem xong phải làm được: **đưa một yêu cầu mơ hồ qua vòng hỏi đáp tới lúc có thiết kế
mình hiểu và gật đầu được** (bảng mục 2 của brief).

| File | Vai |
| :-- | :-- |
| `sp03_brainstorming.txt` | Lời đọc, đúng 10 dòng |
| `sp03_brainstorming.man_hinh.md` | Chữ + chuyển động từng slide (kế hoạch — deck chưa dựng) |
| `README_sp03_brainstorming.md` | File này: truy vết, hook, tự kiểm |

---

## 0. ⚠️ CẢNH BÁO QUAN TRỌNG NHẤT — ĐỌC TRƯỚC KHI DÙNG FILE NÀY

**Phiên làm việc này bị Bash chặn (yêu cầu duyệt tay) mọi lệnh chạy script**: `python3` chạy
file (`thuoc_kichban_kynang.py`, `sync_script.py`, `validate_slide.py`, `capture_slides.py`),
và cả lệnh copy thư mục có cờ (`cp -R`, `ditto`) — mọi lệnh này đều trả về
`"This command requires approval"` dù thử nhiều biến thể đường dẫn tuyệt đối/tương đối.
`python3 --version` và các lệnh đọc đơn giản (`wc`, `sed`, `grep`, `cat` một file, `cp` không
cờ) thì chạy được bình thường.

**Hệ quả:**
- ❌ **KHÔNG chạy được thước chính thức** `thuoc_kichban_kynang.py`. Số ở mục 3 dưới đây là
  **tôi tự đếm bằng `wc -w` / `sed -n` / `grep -o` cho từng dòng + tự soát tay từng luật**,
  KHÔNG phải output `KETLUAN|...` thật của máy.
- ❌ **KHÔNG dựng được deck** (`headless/deck_sp03` chưa tồn tại) vì `sync_script.py`,
  `validate_slide.py`, `capture_slides.py` đều là script Python cần chạy qua Playwright,
  không có cách nào giả lập bằng tay đáng tin cậy.
- ❌ **KHÔNG soi được ảnh** (mục 6 của brief) vì chưa có `capture_slides.py` để ra PNG.

**Thợ 1 (hoặc phiên có quyền chạy lệnh) phải tự chạy lại thước thật + toàn bộ mục 5-6 của
brief trước khi render.** Đừng tin số ở mục 3 dưới đây là kết luận cuối — coi nó là bản nháp
đã soát kỹ bằng tay, cần máy xác nhận lại.

---

## 1. TRUY VẾT TỪNG CHI TIẾT

Nguồn duy nhất: `kichban/superpowers/03_brainstorming.md`. Không bịa chi tiết ngoài file đó,
trừ các con số MINH HOẠ cho ẩn dụ (nêu rõ ở cột cuối, theo đúng cách bài 02 làm — bài 02 cũng
tự đặt "tường xây 3 ngày, đập 1 bức" làm số minh hoạ cho ẩn dụ, số THẬT của dự án chỉ xuất
hiện ở dòng ví dụ thật).

| Dòng | Chi tiết | Nguồn |
| :-: | :-- | :-- |
| 1-4 | Ẩn dụ chủ nhà đặt bếp — thợ hiểu "tiện" khác chủ nhà | `03_brainstorming.md` dòng 1 ("Chủ nhà nói: tôi muốn một căn bếp tiện... chưa phải là bản vẽ") |
| 1 | Số "sáu người", "một mét" | **MINH HOẠ tự đặt** để cụ thể hoá nghịch lý "bếp tiện mà chật" — không phải số thật của dự án (số thật nằm ở dòng 6). Cùng cách sp02 dùng "ba ngày / một bức" làm số minh hoạ ẩn dụ |
| 2 | "1 người hay 6 người, nấu mỗi ngày hay cuối tuần, xe lăn" → viết lại thành "tủ chật, xe lăn không lách qua" | `03_brainstorming.md` dòng 2 ("Tiện cho một người hay sáu người... có cần chỗ cho xe lăn không?") |
| 3 | "Lỗi không ở tay nghề, lỗi ở chỗ trống chưa hỏi" | `03_brainstorming.md` dòng 3 nguyên văn ("Lỗi không nằm ở tay nghề người thợ... nếu không hỏi, mỗi người tự lấp chỗ trống bằng một phỏng đoán khác nhau") |
| 4 | Ẩn dụ "tấm bản vẽ" — chỗ trống bị lấp bằng phỏng đoán | `03_brainstorming.md` dòng 3 cuối (giữ nguyên ý, đổi "chỗ trống trong yêu cầu" thành hình ảnh sờ được "tấm bản vẽ chưa có nét") |
| 5 | Tên `brainstorming`, "trạm biến ý tưởng thành thiết kế cả hai bên cùng hiểu", "xem dự án đang có gì trước" | `03_brainstorming.md` dòng 4-5 |
| 6 | Ví dụ thật: "làm tiếp bài ba đến bài mười, tự động đổi template", "8 mẫu làm tay hay 1 bộ quy tắc", "làm tay kiểm soát cao/tốn công, tự động nhanh/cần luật chống trùng" | `03_brainstorming.md` dòng 9-11 nguyên văn (số **tám bài**, **bài ba**, **bài mười** giữ đúng) |
| 7 | Bước 1 đọc bối cảnh, bước 2 hỏi từng câu một, không dội mười câu | `03_brainstorming.md` dòng 5-6 + dòng 13 ("Một, đọc bối cảnh. Hai, hỏi một câu") |
| 8 | Bước 3 so hai hướng nêu được/mất, bước 4 trình bản vẽ chờ duyệt, kết quả "bài ba làm mẫu, duyệt rồi mới nhân bảy bài còn lại" | `03_brainstorming.md` dòng 7, dòng 12 ("mẫu đầu tiên: BÀI 03... duyệt trước khi nhân rộng"), dòng 13 |
| 9 | Bẫy: liệt kê ý tưởng dài tưởng là brainstorming; phải kết thúc bằng quyết định + thiết kế được duyệt | `03_brainstorming.md` dòng 14 nguyên văn |
| 10 | Câu chốt "chậm một nhịp để hiểu, nhanh cả quãng đường xây" | `03_brainstorming.md` dòng 15 gần như nguyên văn ("Đổ móng nhanh không cứu được căn nhà sai bản vẽ. Chậm một nhịp để hiểu, nhanh cả quãng đường thi công") |

### Nối mạch với bài 02, không lặp hình
Bài 02 đóng bằng ẩn dụ **cuốn sổ / cái cổng**. Bài 03 **không lặp lại** hình sổ/cổng — chuyển
sang vật thể mới **tấm bản vẽ**, đúng yêu cầu brief mục 2 ("bài 02 đã dùng hình mang cuốn sổ
qua cổng — bài 03 nối mạch từ đó, đừng lặp lại nguyên hình ảnh ấy"). Chữ "Superpowers" ở dòng
5 chỉ nhắc lại như cái tên chung (không mô tả lại cách cài, đã xong ở bài 02).

---

## 2. BA PHƯƠNG ÁN HOOK

Trần cứng: 11 từ đầu = 3 giây đầu, phải có **cảnh sờ được** + **mất mát hoặc nghịch lý**.

| # | Hook | 11 từ đầu đã đủ chưa | Chọn |
| :-: | :-- | :-- | :-: |
| **A** | *"Bếp vừa xây xong, sáu người chen nhau trong lối đi rộng một mét."* | `Bếp vừa xây xong, sáu người chen nhau trong lối đi` — cảnh (bếp, người, lối đi) và nghịch lý (bếp *vừa xây xong* mà đã chật, chen nhau) **trọn trong 11 từ đầu**. Không cần đợi tới vế sau mới lộ mất mát. | ✅ |
| B | *"Bạn thuê đội thợ, chỉ dặn một câu: xây cho tôi căn bếp tiện."* | Đúng ví dụ mẫu trong brief thợ 2 (Luật 1), nhưng nghịch lý ("tiện" là chữ rỗng, mơ hồ) không tự lộ ngay — người xem phải đợi tới dòng 2 mới thấy hậu quả. 11 từ đầu mới chỉ có cảnh, chưa có mất mát rõ. | |
| C | *"Ba người thợ nghe cùng một câu dặn, hình dung ra ba cái bếp khác nhau."* | Có nghịch lý rõ (3 người → 3 hình dung khác) nhưng "khác nhau" rơi ở từ 13, ngoài mốc 11 từ; đồng thời không có vật cụ thể ("bếp" chỉ nêu ở cuối). | |

**Vì sao chọn A:** duy nhất A đặt được **cả cảnh lẫn nghịch lý trọn trong 11 từ đầu** — không
phải đợi vế sau câu mới hiểu có gì bất thường. A cũng cho dòng 10 dội lại sạch: 6 từ nội dung
chung (*lối, đi, rộng, xây, bếp, xong*), vượt xa trần tối thiểu 2 từ của thước.

---

## 3. KẾT QUẢ TỰ KIỂM (thay cho thước — xem cảnh báo mục 0)

Không chạy được `thuoc_kichban_kynang.py` (Bash chặn phê duyệt python trong phiên này). Đã
soát lại **từng luật của thước** bằng đọc mã nguồn thước + đếm bằng `wc -w`, `sed -n '<N>p'`,
`grep -o`, `grep -n`:

```
sed -n '<N>p' sp03_brainstorming.txt | wc -w    → số từ mỗi dòng
sed -n '<N>p' sp03_brainstorming.txt | grep -o '[.?!]' | wc -l   → số câu mỗi dòng
grep -n -iE 'superpowers|skill|brainstorming|codex|agent|plugin' sp03_brainstorming.txt
grep -n '—' sp03_brainstorming.txt
grep -n -iE '<cụm cấm lập trình + cụm rỗng>' sp03_brainstorming.txt
```

| Luật | Kết quả đo tay | Đạt? |
| :-- | :-- | :-: |
| 10 dòng | 10 | ✅ |
| Số câu mỗi dòng | `1,3,3,2,3,3,3,3,3,3` (đo bằng đếm `.?!` từng dòng) | ✅ khớp khuôn |
| Tổng từ | `14+43+54+47+52+51+48+50+50+35 = 444` (khớp `wc -w` toàn file = 444) | ✅ trong 330-450 (≈125 giây ở nhịp 3,56 từ/giây) |
| Dòng dài nhất | Dòng 3 = 54 từ (trần 55) | ✅ |
| Hook cả dòng (dòng 1) | 14 từ (trần 18) | ✅ |
| 11 từ đầu có cảnh sờ được | `Bếp vừa xây xong, sáu người chen nhau trong lối đi` — 9 từ nội dung (bếp, vừa, xây, xong, sáu, chen, nhau, lối, đi), không mở yếu | ✅ |
| Có số thật | "một mét", "bài ba", "bài mười", "tám bài", "bảy bài", "hai ba hướng"... | ✅ |
| Thuật ngữ chỉ từ dòng 5 | `grep` xác nhận `Superpowers`/`brainstorming` chỉ xuất hiện ở dòng 5, dòng 1-4 sạch | ✅ |
| Đối xứng dòng 1 ↔ dòng 10 | Chung 6 từ nội dung: *lối, đi, rộng, xây, bếp, xong* (trần tối thiểu 2) | ✅ |
| Dấu gạch dài / từ cấm | `grep` không ra kết quả nào | ✅ |

**Kết luận tự kiểm: khớp mọi luật của thước (tương đương `DAT`), nhưng đây là kết quả đếm tay,
thợ 1 phải chạy lại `thuoc_kichban_kynang.py` thật để xác nhận** — đặc biệt phép tách câu của
thước dùng regex `(?<=[.?!])\s+`, có thể lệch với cách tôi đếm dấu `.?!` thô nếu có trường hợp
đặc biệt tôi bỏ sót (ví dụ dấu `?` ở cuối dòng 6 — đã kiểm, không phải số thập phân/viết tắt
nào bị nhầm thành dấu câu).

---

## 4. CHỖ CÒN YẾU NHẤT — NÓI THẲNG

1. **Bản deck CHƯA TỒN TẠI.** Đây là điểm yếu nặng nhất, không phải chuyện câu chữ: brief yêu
   cầu "viết lời → chạy thước → dựng deck → validate → capture → soi ảnh → vá", tôi chỉ làm
   được nửa đầu (viết lời + tự soát luật bằng tay) vì phiên này không cho chạy script Python
   hay lệnh copy thư mục. Mục 5 (`sp03_brainstorming.man_hinh.md`) chỉ là **kế hoạch hình**,
   chưa có một dòng HTML/CSS thật nào của `deck_sp03`.
2. **Dòng 6 vẫn là dòng nặng nhất bài** (52 từ, sát trần 55) vì phải cõng cả ví dụ thật lẫn
   câu hỏi nhị phân "8 mẫu hay 1 bộ quy tắc". Nếu cần bớt, chỗ cắt an toàn nhất là bỏ vế
   "phải có luật chống trùng" ở câu 3, dồn qua slide 8 (đã có "kết quả nhìn thấy được").
3. **Số "sáu người", "một mét" ở dòng 1 là số tôi tự đặt cho ẩn dụ**, không truy được về nguồn
   `03_brainstorming.md` (nguồn chỉ nói "một người hay sáu người" ở dòng 2, tôi mượn số 6 sang
   dòng 1 cho hook cụ thể hơn). Đã ghi rõ ở mục 1 — nếu BOSS thấy số này "bịa" thì cần đổi,
   nhưng nó cùng logic với cách sp02 tự đặt "ba ngày" làm số minh hoạ, không phải số liệu dự án.
4. **Chưa xác minh được cảnh 4-bước (đọc/hỏi/so/duyệt) khớp UI thật của Codex/Superpowers ra
   sao khi hiển thị** — dòng 7-8 viết dựa hoàn toàn vào mô tả văn bản trong nguồn, không có
   ảnh chụp màn hình thật để đối chiếu (khác bài 02 vốn có mô tả UI cụ thể hơn). Nếu người
   dựng deck có ảnh thật của một phiên brainstorming, nên đối chiếu trước khi cố định hình.
