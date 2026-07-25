# README — sp06_thuc_thi (Bài 06 khoá Superpowers)

Người xem xong phải làm được: **giao việc theo từng hạng mục nhỏ**; **nghiệm thu hỏi hai
câu khác nhau theo đúng thứ tự** — "đúng thứ tôi đặt không" trước, "làm có tử tế không" sau.

| File | Vai |
| :-- | :-- |
| `sp06_thuc_thi.txt` | Lời đọc, đúng 10 dòng |
| `sp06_thuc_thi.man_hinh.md` | Chữ + chuyển động từng slide |
| `README_sp06_thuc_thi.md` | File này: truy vết, hook, tự kiểm |

---

## 1. TRUY VẾT TỪNG CHI TIẾT

Không có chi tiết nào ngoài `kichban/superpowers/06_thuc_thi_va_review.md` và
`kichban/superpowers/README.md`. Không bịa số, không bịa bước.

| Dòng | Chi tiết | Nguồn |
| :-: | :-- | :-- |
| 1-2 | Đội xây 8 phòng cùng lúc, cuối tháng mới kiểm, ổ điện sai cao 10 phân ở tất cả | `06_thuc_thi_va_review.md` dòng 5 |
| 2-3 | Sai lệch nhỏ nhân lên 8 lần; sửa thành đục lại cả dãy tường | `06_thuc_thi_va_review.md` dòng 9 |
| 3 | Đóng khung "lỗi không ở đâu / ở đâu" là khuôn MỚI của brief thợ 1 (mục 4 dòng 3), không có sẵn trong nguồn — suy ra hợp lý từ chính hai câu dòng 5+9 (sai không phải do thợ kém, mà do không ai kiểm sớm) |
| 4-5 | "Làm xong 1 nhiệm vụ nhỏ, review, rồi mới chuyển tiếp"; subagent driven development, mỗi nhiệm vụ giao 1 agent mới, chỉ mang phiếu việc + giao diện cần biết; agent tự viết test/làm/kiểm/tự xem lại nhưng chưa thay người nghiệm thu | `06_thuc_thi_va_review.md` dòng 13, 17, 21 |
| 5 | Review hai cổng theo thứ tự: cổng 1 hỏi đúng bản thiết kế chưa, cổng 2 hỏi sạch/an toàn/dễ bảo trì chưa | `06_thuc_thi_va_review.md` dòng 25 (nội dung dồn sang dòng 8 của khuôn mới vì dòng 5 chỉ đủ chỗ gọi tên) |
| 6 | Ví dụ thật: 1 video có 3 yêu cầu đã chốt — thương hiệu `dungladu.vn`, giọng Nam Minh nhanh 14%, màu chính tím Stripe `#635bff` | `06_thuc_thi_va_review.md` dòng 37 |
| 6 | Cổng 1 chỉ kiểm đủ 3 điều đó, video đẹp không có nghĩa đúng đơn | `06_thuc_thi_va_review.md` dòng 41-42 |
| 7-8 | Bốn bước: 1 giao đúng 1 phiếu việc, 2 agent làm + đưa bằng chứng, 3 reviewer kiểm yêu cầu rồi chất lượng, 4 sửa sạch mới đánh dấu hoàn tất | `06_thuc_thi_va_review.md` dòng 51 |
| 8 | Lỗi nghiêm trọng/quan trọng sửa trước khi đi tiếp — gộp vào ý "sửa sạch mới đánh dấu hoàn tất" ở bước 4, không tách thành câu riêng vì khuôn 10 dòng không còn chỗ | `06_thuc_thi_va_review.md` dòng 33 |
| 9 | Bẫy: giao nhiều agent cùng sửa file chồng lên nhau, nhanh trên đồng hồ nhưng đổi lại xung đột + ngữ cảnh rối | `06_thuc_thi_va_review.md` dòng 61 |
| 10 | Nghiệm thu sớm không làm chậm công trình; ngăn 1 lỗi nhỏ thành 8 bức tường phải đục lại | `06_thuc_thi_va_review.md` dòng 65 |
| — | Ẩn dụ "xây một căn nhà", nối mạch với bài 02 ("mang sổ qua cổng") sang cảnh thi công thật (phòng, ổ điện) — không lặp lại hình cuốn sổ/cổng | `superpowers/README.md` dòng 9 |

### Đã CỐ Ý bỏ khỏi bản mới (và vì sao)
- **Review toàn nhánh sau khi cả kế hoạch xong** (`06_thuc_thi_va_review.md` dòng 57, "cần thêm một lượt review toàn nhánh... lỗi chỉ lộ ra khi các phòng nối với nhau"). Đây là ý hay nhưng khuôn 10 dòng đã kín; nội dung này gần với việc "kiểm chứng và bàn giao" của bài 08, để dành cho bài đó thay vì nhồi thêm vào bài 06.
- **Chi tiết "lỗi Critical/Important phải sửa, Minor thì ghi sổ đợi review toàn nhánh"** (dòng 33) — chỉ giữ lại phần "sửa sạch mới đánh dấu hoàn tất" ở bước 4, bỏ phần phân loại 3 mức độ vì dòng 8 chỉ có 3 câu và đã phải cõng cả bước 3 lẫn bước 4.

### Nối mạch với bài 05, không lặp
Bài 05 (theo `README.md`) dạy vòng Đỏ-Xanh-Dọn của một nhiệm vụ đơn. Bài 06 mở rộng ra
**nhiều nhiệm vụ chạy song song** (8 phòng cùng lúc) và trả lời câu hỏi kế tiếp: *xây xong
từng nhiệm vụ rồi thì ai kiểm, kiểm cái gì trước, cái gì sau*. Ẩn dụ "xây nhà" giữ nguyên
nhưng chuyển từ *một bức tường* (bài 05 ngụ ý) sang *nhiều phòng cùng lúc* — đúng quy mô của
chủ đề "thực thi và review nhiều việc song song".

---

## 2. BA PHƯƠNG ÁN HOOK

Trần cứng: 11 từ đầu = 3 giây đầu, phải có **cảnh sờ được** + **mất mát hoặc nghịch lý**,
từ đầu tiên phải là danh từ cụ thể/con số/hành động.

| # | Hook | 11 từ đầu đã đủ chưa | Chọn |
| :-: | :-- | :-- | :-: |
| **A** | *"Tám căn phòng đã xây xong, ổ điện đặt sai y hệt nhau, cuối tháng mới phát hiện."* | `Tám căn phòng đã xây xong, ổ điện đặt sai y` — cảnh (8 phòng, xây xong) ở từ 1-6, mất mát (ổ điện đặt sai) trọn trong từ 7-10. Mở bằng con số "Tám". | ✅ |
| B | *"Người thợ xây xong tám phòng, không ai biết ổ điện đặt sai cho tới cuối tháng."* | `Người thợ xây xong tám phòng, không ai biết ổ điện` — 11 từ đầu mới có cảnh, chữ "sai" (mất mát) rơi ở từ 12-13, ngoài mốc 3 giây. | |
| C | *"Cuối tháng kiểm nhà, tám ổ điện đều đặt sai một kiểu như nhau."* | 11 từ đầu có đủ cả cảnh lẫn mất mát, nhưng **từ đầu tiên là "Cuối"** — một mốc thời gian trừu tượng, không phải danh từ cụ thể/con số/hành động như luật đòi hỏi. | |

**Vì sao chọn A:** A là phương án duy nhất vừa mở bằng một con số cụ thể ("Tám"), vừa nhét
trọn cả hai vế nghịch lý (phòng đã xây xong ↔ ổ điện sai) vào đúng 11 từ đầu. B đúng luật mở
bài nhưng đẩy mất mát ra ngoài mốc 3 giây. C nén được cả hai vế vào 11 từ nhưng vi phạm luật
"từ đầu tiên là danh từ cụ thể/con số/hành động" vì mở bằng trạng từ thời gian.

BOSS muốn đổi thì thay nguyên dòng 1 bằng B hoặc C, nhưng **phải chạy lại thước** vì cả hai
đổi tập từ nội dung dòng 1, ảnh hưởng phép đo đối xứng dòng 1 ↔ dòng 10.

---

## 3. KẾT QUẢ TỰ KIỂM

⚠️ **Không chạy được `thuoc_kichban_kynang.py` trong phiên này.** Mọi lệnh gọi trình thông
dịch Python (`python3` hệ thống lẫn `.venv/bin/python` của `escbase_template`) đều bị chặn
với thông báo "This command requires approval" — kể cả lời gọi `--version` trần trụi không
tham số. Đây là hạn chế QUYỀN của phiên Bash hiện tại, không phải lỗi của thước hay của file
lời. Đã thử 3 cách gọi khác nhau (đường tương đối, đường tuyệt đối, venv riêng), cả 3 đều bị
chặn giống nhau; các lệnh Bash không phải Python (`wc`, `sed`, `grep`, `ls`, `cat`) đều chạy
bình thường. `cp -R` và `ditto` (dựng deck) cũng bị chặn cùng lý do.

**Vì vậy tôi đã tự tay dò lại đúng 10 phép đo của thước bằng `wc`/`sed`/`grep`, không đoán:**

```
wc -l  → 10 dòng                                          ✓ đúng "10 dòng"
sed+grep '[.?!]' từng dòng → [1,3,3,2,3,3,3,3,3,3]         ✓ khớp KHUON
wc -w toàn file → 450 từ                                  ✓ trong trần 330-450 (ở biên trên)
wc -w từng dòng → 18,45,53,35,52,55,40,52,55,45            ✓ không dòng nào > 55 (trần DONG)
dòng 1 = 18 từ                                             ✓ không > 18 (trần HOOK)
grep -i 'superpowers|skill|review|codex|agent|subagent|code' dòng 1-4 → rỗng   ✓ sạch thuật ngữ
grep các cụm mở yếu ở dòng 1 → rỗng                        ✓ không mở yếu
grep '—' → 0 lần; grep chữ lập trình/chữ rỗng → rỗng       ✓ sạch
```

Số câu ⇒ tổng = 1+3+3+2+3+3+3+3+3+3 = **27 reveal**. Tổng từ = **450** ⇒ ước lượng
**~126 giây** ở nhịp 3,56 từ/giây (đúng biên trên của trần 93-127 giây — bài này SẼ là bài
dài nhất trong 6 bài nếu không siết thêm).

Số 450 vừa đúng biên trên nghĩa là **không còn chỗ đệm**: nếu thợ 1 chạy lại thước và ra số
khác 450 (kể cả lệch 1 từ do cách đếm dấu câu khác nhau), khả năng cao là do cách `wc -w` và
`re.findall`/`.split()` của Python đếm token hơi khác nhau ở vài chỗ có dấu `:` hoặc dấu `,`
dính liền chữ — **cần thợ 1 chạy lại đúng lệnh Python thật** để có `KETLUAN|...` chính thức,
tôi không thể tự tạo dòng đó vì chưa thực sự chạy được script.

Kiểm tay phép đo còn lại (thước không tự động hoá bằng regex đơn giản, tôi đọc bằng mắt):
- Đối xứng dòng 1 ↔ dòng 10: chung các từ nội dung *phòng, ổ, điện, đặt, sai, cuối, tháng* — dư xa mức trần (2 từ).
- Ví dụ thật có số: rất nhiều số viết chữ (*tám, mười phân, mười bốn phần trăm, ba mươi, bốn bước*...) — đạt.
- Ẩn dụ trước tên kỹ thuật: dòng 1-4 chỉ nói phòng/ổ điện/đội thợ/bản vẽ; `Superpowers`,
  `subagent`, `review` chỉ xuất hiện từ dòng 5 — đạt.

---

## 4. CHỖ CÒN YẾU NHẤT — NÓI THẲNG

1. **Tổng từ đúng 450, chạm trần trên (450).** Không còn biên độ an toàn nào — nếu thước
   thật (chạy bằng Python) đếm ra một con số cao hơn dù chỉ 1 từ do khác cách tách token,
   bài sẽ HONG ngay. Thợ 1 nên chạy lại bằng chính script gốc trước khi dựng deck, và nếu
   HONG thì chỗ dễ cắt nhất là dòng 6 (55 từ, đã cắt "một", "chính", "đọc là", "đủ" — cắt
   thêm sẽ mất chữ "Cổng nghiệm thu thứ nhất" đang neo cho dòng 8 nhắc lại "cổng 1").
2. **Dòng 3 dùng khuôn "lỗi không ở đâu / không ở đâu / mà ở đâu" (hai lần phủ định liên
   tiếp) trong khi nguồn gốc chỉ có MỘT phủ định rõ ("không phải tay nghề").** Vế thứ hai
   ("không phải vì đợi cuối tháng là chậm") là tôi tự suy ra để khớp khuôn 3 câu của brief,
   không có nguyên văn trong `06_thuc_thi_va_review.md`. Ý này hợp lý (đang bảo vệ luôn cả
   nhịp độ, không riêng tay nghề) nhưng là suy luận thêm, cần thợ 1 xác nhận có đúng ý BOSS
   muốn dạy không.
3. **Dòng 5 dồn ba khái niệm vào một lúc (tên cách làm, subagent, và ý "tự xem lại chưa
   thay được nghiệm thu")** vì nguồn gốc (3 câu liên tiếp trong `06_thuc_thi_va_review.md`)
   vốn đã dày đặc thuật ngữ. Đây là dòng nặng nghĩa nhất bài — người xem chưa quen từ
   "subagent" có thể cần tua lại đúng dòng này.
4. **`perf-compare` ở dòng 4 dùng nhãn `NGAY` (chữ, không phải số) cho vế "giao từng
   phòng"** vì nguồn không cho một con số thời gian cụ thể cho việc nghiệm thu từng phòng —
   tôi cố tình không bịa số để giữ đúng luật "không bịa số". Nếu để cạnh nhãn số `NGÀY 30`
   của vế kia, sự bất cân xứng số-chữ có thể khiến hình trông chưa "chốt" bằng các mẫu
   `perf-compare` gốc (vốn cả hai vế đều là số). Cần soi ảnh thật mới biết có ổn không.

---

## 5. VIỆC CHƯA LÀM ĐƯỢC TRONG PHIÊN NÀY — báo rõ, không giấu

Theo brief mục 0, việc của thợ 2 là: viết lời → chạy thước → dựng deck → validate → capture
→ soi ảnh → vá → validate/capture/soi lại. **Chỉ làm được bước đầu (viết lời + 3 file).**
Mọi bước sau đều cần chạy Python (`sync_script.py`, `validate_slide.py`, `capture_slides.py`)
hoặc copy thư mục deck (`cp -R`, `ditto`) — **cả hai loại lệnh này đều bị Bash của phiên này
chặn với "requires approval"**, thử nhiều cách gọi khác nhau đều bị chặn giống hệt, kể cả
`python --version` không tham số. Đây không phải tôi từ chối làm, mà là quyền Bash của phiên
không cho phép — cần thợ 1 hoặc BOSS gỡ giới hạn quyền, hoặc tự chạy các bước dựng deck ở
phiên có quyền đầy đủ, dùng đúng 3 file lời đã viết ở đây làm đầu vào.
