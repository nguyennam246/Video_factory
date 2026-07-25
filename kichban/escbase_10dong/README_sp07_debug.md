# README — sp07_debug (Bài 07 khoá Superpowers)

Người xem xong phải làm được: **gặp lỗi thì đi bốn pha thay vì đoán rồi sửa bừa**
(bảng "làm được gì" của brief thợ 2, bài 07).

| File | Vai |
| :-- | :-- |
| `sp07_debug.txt` | Lời đọc, đúng 10 dòng |
| `sp07_debug.man_hinh.md` | Chữ + chuyển động từng slide |
| `README_sp07_debug.md` | File này: truy vết, hook, tự kiểm |

---

## 1. TRUY VẾT TỪNG CHI TIẾT

Nguồn duy nhất: `kichban/superpowers/07_debug_co_he_thong.md` (định dạng kịch bản cũ
`LỜI:`/`CHỮ:`/`MÃ:`, 13 khối cách nhau bằng `---`). Không bịa dữ kiện ngoài file này,
trừ 2 chỗ ghi rõ là suy luận ở cuối bảng.

| Dòng | Chi tiết | Nguồn (khối LỜI trong `07_debug_co_he_thong.md`) |
| :-: | :-- | :-- |
| 1 | Vòi chảy yếu → thợ thay vòi mới → nước vẫn yếu | Khối 1: "Vòi nước tầng hai chảy yếu. Người thợ đoán vòi hỏng, thay vòi mới. Nước vẫn yếu." — **bỏ "tầng hai"** để siết trọn nghịch lý vào 11 từ đầu (xem mục 2) |
| 2 | Lần 2 thay bơm, lần 3 thay van, đều vẫn yếu, tốn thêm tiền mỗi lần, không biết mất áp ở đâu | Khối 2: "Anh ta thay tiếp máy bơm, rồi thay van. Mỗi lần tốn thêm tiền, nhưng chưa lần nào biết nước mất áp ở đâu." — chỉ thêm số thứ tự "lần thứ hai / lần thứ ba" cho đúng khuôn "ngày thứ N", thứ tự bơm→van giữ nguyên như nguồn |
| 3 | Lỗi không ở vòi/bơm/van; thợ vẫn làm đúng nghề; lỗi ở đoạn ống khuất trong tường | Khối 3: "Sửa mò là thay đồ ở nơi thấy triệu chứng… nguyên nhân có thể ở nơi khác" — viết lại thành khuôn "chỉ đúng chỗ đau". ⚠️ Câu **"người thợ vẫn làm đúng nghề, đúng thứ tự"** là suy luận hợp lý (nguồn không nói thẳng câu này), xem mục 4 |
| 4 | Sửa mò = thay tại chỗ rỉ nước; đi đúng = lần theo dòng nước ngược vào tường tới đúng chỗ vỡ | Khối 3 gần nguyên văn: "Sửa mò là thay đồ ở nơi thấy triệu chứng. Gỡ lỗi có hệ thống là lần theo dòng nước tới đúng chỗ ống vỡ." |
| 5 | Tên trang sổ "Gỡ Lỗi Có Hệ Thống"; luật: chưa tìm ra chỗ vỡ thì chưa được đề xuất cách sửa; bốn bước, không nhảy cóc | Khối 4: "Skill systematic debugging có luật: chưa điều tra nguyên nhân gốc thì chưa đề xuất cách sửa." + số **bốn** bước suy ra từ cấu trúc pha 1-4 (khối 5-8). ⚠️ **"Gỡ Lỗi Có Hệ Thống" là bản dịch tự đặt** cho `systematic debugging` (nguồn tiếng Anh), xem mục 4 |
| 6 | Ví dụ thật dự án video: có nhạc, mất giọng; giọng thuần −22,4 dB; sau trộn −30,7 dB | Khối 9-10: "giọng thuần khoảng âm hai mươi hai phẩy bốn đề xi ben" (`MÃ: giọng thuần ≈ −22,4 dB`) · "chỉ còn khoảng âm ba mươi phẩy bảy đề xi ben" (`MÃ: sau trộn ≈ −30,7 dB`) — số lấy nguyên, không đổi |
| 7 | Bước 1 thu bằng chứng (đọc lỗi, đo từng chặng); bước 2 so mẫu (đặt cách lỗi cạnh cách chuẩn); điểm khác: bộ trộn tự chia nhỏ mức từng kênh | Khối 5 (pha 1 — bằng chứng: "đọc hết lỗi, tái hiện ổn định… đo đầu vào đầu ra ở từng chặng"), khối 6 (pha 2 — so mẫu: "so chỗ hỏng với chỗ tương tự đang chạy được"), khối 11 (nguyên nhân: "bộ amix mặc định tự chia nhỏ mức của các kênh" — **đổi "amix normalize" thành chữ thường "bộ trộn mặc định tự động chia nhỏ mức của từng kênh âm thanh"**, đúng luật cấm chữ lập trình) |
| 8 | Bước 3 nêu giả thuyết (tắt phép tự chia nhỏ, tự đặt lại mức từng kênh); bước 4 sửa đúng chỗ, đo lại; kết quả −18,8 dB | Khối 12 (giả thuyết: "tắt phép chuẩn hoá ấy và tự đặt mức từng kênh… `MÃ: amix normalize=0`") + khối 7 (pha 4 — sửa gốc) + khối 13 (kết quả: "khoảng âm mười tám phẩy tám đề xi ben") |
| 9 | Bẫy: thấy số đẹp lên liền khen giọng hay hơn; máy chỉ đo to nhỏ không nghe hay dở; đo xong đưa người thật nghe rồi mới phán | **Không có trong `07_debug_co_he_thong.md`** — đây là diễn giải thêm về đúng chính ví dụ thật ở dòng 6-8 (âm lượng đo được không chứng minh chất giọng), nhất quán luật số 1 của `video/CLAUDE.md`: "AI KHÔNG NGHE ĐƯỢC — mọi phán xét giọng để BOSS nghe". Xem mục 4 |
| 10 | Đừng thay vòi vì vòi yếu; đo cả đường ống, tìm đúng chỗ vỡ; sửa đúng 1 chỗ, vòi cũ không phải thay nữa | Khối cuối gần nguyên văn: "Đừng thay vòi vì nước yếu ở vòi. Hãy đo đường ống, tìm đúng chỗ vỡ, rồi chỉ sửa một chỗ đó." + thêm câu dội "vòi cũ không phải thay thêm lần nào nữa" để đối xứng dòng 1 |

### Đã CỐ Ý bỏ khỏi bản mới (và vì sao)
- **Khối gần cuối nguồn**: "Nếu ba cách sửa liên tiếp đều thất bại và mỗi cách lộ một lỗi ở
  chỗ khác, Superpowers yêu cầu dừng để xem lại kiến trúc." Đây là luật thật nhưng là một
  nhánh hiếm (leo thang kiến trúc), không phải đường chính bốn pha — khuôn 10 dòng không có
  chỗ cho nhánh phụ này mà không đá văng phần ví dụ thật (dòng 6-8), vốn là phần giúp người
  xem THẤY được bốn pha chạy trên một lỗi có thật.
- **Thuật ngữ `amix`, `normalize`** (khối 11-12 nguồn): giữ nguyên sẽ phạm luật cấm chữ
  lập trình. Viết lại bằng chữ thường "bộ trộn tự động chia nhỏ mức từng kênh".

### Nối mạch với các bài trước, không lặp
Ẩn dụ "xây một căn nhà" của cả khoá được mở rộng sang **đường ống nước trong nhà** (vòi,
tường, ống) — vẫn là một phần của căn nhà, không phải ẩn dụ mới. Bài 02 đóng bằng "sổ
ngoài cổng thì tường vẫn mọc, mọc sai"; bài 07 không lặp lại hình sổ tay/cổng, mà đi tiếp
với vật thể riêng của bài này.

---

## 2. BA PHƯƠNG ÁN HOOK

Trần cứng: 11 từ đầu = 3 giây đầu, phải có **cảnh sờ được** + **mất mát hoặc nghịch lý**
**trọn vẹn trong 11 từ**, không phải trong cả dòng hook (rút kinh nghiệm sp02: chỉ phương
án đưa được cả hai vế vào 11 từ mới đạt).

| # | Hook | 11 từ đầu | Chọn |
| :-: | :-- | :-- | :-: |
| A (bản lượt trước) | *"Vòi nước tầng hai chảy yếu, thợ thay vòi mới, nước vẫn yếu như cũ."* | `Vòi nước tầng hai chảy yếu, thợ thay vòi mới, nước` — có cảnh (vòi, tầng hai, thợ) nhưng chữ **"yếu" xác nhận lại** (vế nghịch lý: thay rồi vẫn yếu) rơi ở từ thứ 12-13, ngoài mốc 3 giây | |
| **B** | *"Vòi chảy yếu, thợ thay vòi mới, nước vẫn yếu như cũ."* | `Vòi chảy yếu, thợ thay vòi mới, nước vẫn yếu như` — nghịch lý **trọn vẹn trong 11 từ**: chữ "yếu" xuất hiện cả ở từ 3 (vấn đề) lẫn từ 10 (đã sửa mà vẫn vậy). Bỏ "tầng hai" để đổi lấy trọn nghịch lý nằm trong khung 3 giây | ✅ |
| C | *"Thợ thay vòi nước mới, ba ngày sau nước vẫn chảy yếu như cũ."* | `Thợ thay vòi nước mới, ba ngày sau nước vẫn chảy` — có mốc "ba ngày sau" giống khuôn dòng 2, nhưng chữ "yếu" (vế mất mát) rơi ở từ 12, ngoài mốc; đảo thứ tự "thợ thay" lên đầu cũng làm mất tính "cảnh" (đồ vật vòi nước) ở ngay từ đầu tiên | |

**Vì sao chọn B:** chỉ B đưa được cả hai vế của nghịch lý (chảy yếu → đã thay → vẫn yếu)
vào trong 11 từ đầu. A giữ được chi tiết "tầng hai" (cụ thể hơn) nhưng đánh đổi bằng việc
đẩy vế "vẫn yếu" ra ngoài khung 3 giây — đúng lỗi mà sp02 đã từng tránh (xem
`README_sp02_cai_dat.md` mục 2). Chi tiết "tầng hai" không mất hẳn: dòng 2 vẫn giữ được
không khí nhiều lần thử liên tiếp qua "lần thứ hai, lần thứ ba".

BOSS muốn đổi thì thay nguyên dòng 1 bằng A hoặc C, nhưng **phải chạy lại thước**: cả ba
phương án đổi tập từ nội dung dòng 1, phép đo đối xứng dòng 1 ↔ dòng 10 phải kiểm lại.

---

## 3. KẾT QUẢ CHẠY THƯỚC

```
cd /Users/simple/Desktop/Cloud/video
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/sp07_debug.txt \
        --thuatngu "superpowers,skill,debug,debugging,codex,agent,log"
```

```
SACH   | khong loi, khong canh bao
KETLUAN|27|424|DAT
```

- **27 reveal**, khuôn `[1,3,3,2,3,3,3,3,3,3]` khớp.
- **424 từ** ≈ **119 giây** ở nhịp 3,56 từ/giây (trong trần 330-450).
- Dòng dài nhất sau khi siết lại: dòng 2 (đo được từ thước, không vượt trần 55).
  ⚠️ Bản nháp đầu tiên (lượt trước) bị `HONG`: tổng 451 từ (vượt trần 1 từ) và **ba dòng
  cùng lúc vượt trần 55 từ/dòng** — dòng 6 (59), dòng 7 (63), dòng 8 (59). Đã cắt lại cả
  ba dòng (bỏ chữ đệm, giữ nguyên số liệu và ý), còn 53/52/52 từ, chạy lại ra `DAT` ngay.
- Thuật ngữ cấm (`superpowers,skill,debug,debugging,codex,agent,log`) không xuất hiện ở
  dòng 1-4 — bài này còn tự tránh cả ở dòng 5 vì dùng tên dịch "Gỡ Lỗi Có Hệ Thống" thay
  vì "debugging".
- Đối xứng dòng 1 ↔ dòng 10: chung các từ nội dung *vòi, nước, chảy, yếu, thay* — vượt
  trần tối thiểu (2).
- Không dấu gạch dài `—`, không chữ lập trình (`amix`, `normalize`, `dB` viết tắt đều đã
  đổi sang chữ Việt/số đọc được), không chữ rỗng.

---

## 4. CHỖ CÒN YẾU NHẤT — NÓI THẲNG

1. **Dòng 9 (bẫy) không truy vết được tới nguồn `07_debug_co_he_thong.md`.** Tài liệu gốc
   không nói tới việc "thấy số đo đẹp lên liền khen giọng hay hơn" — đây là diễn giải
   thêm, rút ra từ đúng ví dụ thật đã dùng ở dòng 6-8 (đo dB không chứng minh chất giọng
   hay dở), và nhất quán với luật số 1 của `video/CLAUDE.md` ("AI KHÔNG NGHE ĐƯỢC"). Nhưng
   nói đúng thì đây là suy luận của người viết kịch bản, không phải trích nguyên văn từ
   tài liệu skill. Nếu BOSS muốn bẫy bám sát nguồn hơn, nguồn có sẵn một bẫy khác ở khối
   gần cuối ("ba cách sửa liên tiếp thất bại mà không dừng lại xem kiến trúc") nhưng khuôn
   10 dòng không đủ chỗ cho cả hai.

2. **Tên trang sổ "Gỡ Lỗi Có Hệ Thống" (dòng 5) là bản dịch tự đặt** cho `systematic
   debugging`. Tôi chọn dịch hẳn sang tiếng Việt để giữ đúng luật "ẩn dụ trước, tên kỹ
   thuật sau" theo tinh thần Việt hoá toàn bài (không có từ tiếng Anh nào lọt vào trước
   dòng 5, và ngay ở dòng 5 cũng không cần thiết phải bật tiếng Anh). Nhược điểm: người
   đã quen gọi skill này bằng tên gốc `systematic-debugging` trong Codex sẽ không thấy
   tên quen thuộc xuất hiện trên màn hình. Nếu BOSS muốn giữ tên gốc tiếng Anh, cần đổi cả
   dòng 5 và slide 5 (deck), rồi chạy lại thước.

3. **Câu "người thợ vẫn làm đúng nghề, đúng thứ tự" ở dòng 3 là suy luận hợp lý**, không
   trích nguyên văn từ nguồn (nguồn chỉ nói "triệu chứng ở vòi, nguyên nhân có thể ở nơi
   khác", không nói thẳng thợ có làm đúng nghề hay không). Suy luận này cần thiết để dòng
   3 làm đúng vai "chỉ đúng chỗ đau" (loại trừ nguyên nhân sai trước khi chỉ nguyên nhân
   đúng), nhưng đây là chỗ tôi thêm ý ngoài câu chữ gốc, cần nói thẳng.

4. **Dòng 7-8 gộp lại ranh giới pha 2/pha 3 hơi mờ so với nguồn.** Nguồn tách rất rõ bốn
   pha (khối 5-8), nhưng khi áp cả bốn pha lên MỘT ví dụ thật xuyên suốt hai dòng, câu
   cuối dòng 7 ("điểm khác lộ ra: bộ trộn tự chia nhỏ mức từng kênh") thực chất vẫn là kết
   quả của pha 2 (so mẫu), còn pha 3 (giả thuyết) chỉ thật sự bắt đầu ở câu đầu dòng 8.
   Người xem lần đầu có thể không tách rạch được ranh giới hai pha này nếu chỉ nghe lời
   đọc mà không nhìn nhãn "PHA 02" / "PHA 03" trên màn hình — deck phải gánh phần làm rõ
   này bằng chữ trên màn hình (xem `sp07_debug.man_hinh.md` slide 7-8).
