# ĐƯỜNG CONG GIỮ MẮT — hai mốc rơi, một món nợ (lập 25/07/2026)

**Vấn đề nó giải:** dự án đo và chặn rất chặt **giây 0-3**, rồi bỏ trống **giây 3 tới giây
70**. Bài 93-127 giây mà chỉ có luật cho 3 giây đầu và câu chốt thì khoảng giữa không ai
lo — người xem vuốt qua ở đó chứ không vuốt ở giây đầu.

---

## Mốc rơi TÍNH RA ĐƯỢC, không phải lấy của sách

Sách viral nói "người xem rơi ở giây 8-15 và giây 45-60". Con số đó là của video nói
tiếng Anh, người thật, nhịp khác. Nhưng **quy về dòng nào của khuôn thì tính được**, vì
dự án có đủ ba số đo:

- nhịp giọng edge NamMinh `+14%` = **3,56 từ/giây** (đo 8 bài)
- khuôn bài dạy `[1,3,3,2,3,3,3,3,3,3]` = **27 reveal**
- trần từ **330-450 từ**, mỗi câu xấp xỉ một reveal nên từ chia theo tỉ lệ số câu

Chạy ra:

| Dòng | Câu | Bài 330 từ (92,7 giây) | Bài 450 từ (126,4 giây) |
| :-: | :-: | :-- | :-- |
| 1 | 1 | giây 0,0 → 3,4 | giây 0,0 → 4,7 |
| **2** | 3 | **giây 3,4 → 13,7** 🔴 | **giây 4,7 → 18,7** 🔴 |
| 3 | 3 | giây 13,7 → 24,0 🔴 | giây 18,7 → 32,8 |
| 4 | 2 | giây 24,0 → 30,9 | giây 32,8 → 42,1 |
| 5 | 3 | giây 30,9 → 41,2 | giây 42,1 → 56,2 🔴 |
| **6** | 3 | **giây 41,2 → 51,5** 🔴 | **giây 56,2 → 70,2** 🔴 |
| 7 | 3 | giây 51,5 → 61,8 🔴 | giây 70,2 → 84,3 |
| 8 | 3 | giây 61,8 → 72,1 | giây 84,3 → 98,3 |
| 9 | 3 | giây 72,1 → 82,4 | giây 98,3 → 112,4 |
| 10 | 3 | giây 82,4 → 92,7 | giây 112,4 → 126,4 |

🔴 = dòng chứa mốc rơi. Kết quả:

> **MỐC RƠI 1 (giây 8-15) nằm gọn trong DÒNG 2** — ở cả hai đầu trần độ dài.
> **MỐC RƠI 2 (giây 45-60) nằm ở DÒNG 5-7, tâm là DÒNG 6.**

Tái tính khi đổi nhịp: bảng này dựng cho khuôn bài dạy. Góc tài chính có `nhip` khác thì
chạy lại phép chia — công thức trong `thuoc_nghe.py --moc`.

---

## LUẬT 1 — DÒNG 2 MỞ MÓN NỢ

Dòng 2 là chỗ người xem hỏi *"cái này có phải chuyện của tôi không"*. Hook đã bắt được
mắt, nhưng hook không giữ được mắt.

**Dòng 2 phải làm ĐỦ HAI việc:**

1. **Trả lời "vì sao chuyện này là chuyện của bạn"** — bằng một cảnh người xem nhận ra
   mình, không bằng lời hứa ("bài này sẽ giúp bạn…" là câu chết).
2. **Mở một món nợ** — đặt ra một câu hỏi, một nghịch lý, hoặc một con số chưa giải thích,
   rồi **KHÔNG giải thích ngay**.

Món nợ là cái duy nhất kéo người xem qua dòng 3, 4, 5. Không có nợ thì mỗi dòng phải tự
hấp dẫn một mình — và không dòng nào làm được.

| Đạt | Hỏng |
| :-- | :-- |
| *"Máy báo đạt. Ảnh chụp lại ra bốn lỗi. Ba lượt kiểm không lượt nào thấy."* | *"Trong bài này bạn sẽ học cách kiểm tra kỹ hơn."* |
| *"Chín bài trước đều có phụ đề. Bài này không. Không phép đo nào báo."* | *"Phụ đề rất quan trọng với video ngắn."* |

**Bẫy hay sập nhất:** viết dòng 2 thành *phần mở rộng của hook*. Hook và dòng 2 phải làm
hai việc khác nhau — hook bắt mắt, dòng 2 mở nợ. Nếu xoá dòng 2 mà bài vẫn liền mạch thì
dòng 2 chưa làm gì.

---

## LUẬT 2 — TRẢ MÓN NỢ (dòng 3-7) và ĐỠ MỐC RƠI 2 (dòng 5-6) là HAI VIỆC

⚠️ **Luật này đã bị số đo sửa một lần — đọc kỹ, đừng gộp lại.**

Bản đầu của luật ép *"trả nợ ở dòng 6"*. Đo thử trên bài **sp02 — bài BOSS đã duyệt
"video tốt"** thì thước báo HỎNG. Soi ra: **bài không sai, luật sai.** Bài sp02 làm thế này:

| Dòng | Bài sp02 làm gì |
| :-: | :-- |
| 2 | mở nợ: *"Ngày thứ ba, hai bức tường không khớp, phải đập bỏ một bức."* |
| **3** | **trả nợ**: *"Lỗi nằm ở chỗ cuốn sổ chung chưa bao giờ được mang vào công trường."* — dùng lại 3 từ của dòng 2 (*chưa · làm · thợ*) |
| **5-6** | **đỡ mốc rơi 2**: ví dụ THẬT có số của chính dự án video |

Tức là **hai việc khác nhau, đặt ở hai chỗ khác nhau**:

### 2a. Trả món nợ — dòng 3 tới 7
Phải **dùng lại ≥2 từ nội dung của dòng 2** (thước đo được, cùng cơ chế phép đo đối xứng
dòng 1/dòng 10). Mở mà không trả là hook lừa — người xem nhớ, và lần sau vuốt qua ngay
từ giây đầu.

> dòng 2: *"Máy báo đạt. Ảnh chụp lại ra bốn lỗi."*
> dòng 3-7: *"Bốn lỗi đó là: khung đỏ bọc câu tích cực, hai dòng lệnh ngắt đôi…"*

### 2b. Đỡ mốc rơi 2 — dòng 5 hoặc 6 PHẢI CÓ SỐ
Giây 45-60 là chỗ rơi thứ hai, và nó rơi vào dòng 5-6. Chỗ đó phải có **vật liệu nặng
nhất của bài** — ví dụ thật có số. Thước đo: dòng 5 hoặc dòng 6 phải chứa một con số
(chữ số hoặc số viết ra chữ).

Khuôn bài dạy đặt *"ví dụ THẬT có số"* ở dòng 6 sẵn rồi. Cái phải cố ý làm là **đừng để
dòng 5-6 thành hai dòng giải thích suông** — đó là lúc mốc rơi 2 không ai đỡ.

**Cho phép lệch:** góc nào đổi `nhip` thì khai `tra` trong khoảng 3-7 ở
`README_{slug}.md`. Ngoài khoảng đó là thước chặn.

---

## LUẬT 3 — MỖI DÒNG PHẢI ĐẨY, KHÔNG ĐƯỢC KỂ THÊM

Sau khi có nợ, mỗi dòng còn lại phải **đẩy về phía trả nợ**. Thử bằng câu hỏi:

> *"Xoá dòng này thì món nợ ở dòng 2 có bị trả chậm hơn không?"*

- **Có** → dòng đó đang đẩy, giữ.
- **Không** → dòng đó đang kể thêm. Đây chính là chỗ bài loãng.

Đây là phép thử **của người viết, không phải của thước**. Thước đếm được số câu, không
đếm được một dòng có đẩy hay không.

---

## LUẬT 4 — DÒNG 10 KHÉP CẢ HAI VÒNG

Dòng 10 đã có một luật (dội lại hình ảnh dòng 1, thước đo ≥2 từ chung). Thêm:

**Dòng 10 phải khép cả vòng hình ảnh (dòng 1) LẪN vòng nhận thức (dòng 2).** Người xem
phải rời video với cảm giác *món nợ đã trả xong*, không phải *bài đã hết*.

Mẫu đã chạy: *"Lời dặn có ngày bị quên. Cái khoá thì không."* — khép vòng hình ảnh.
Bản đầy đủ còn phải trả lời luôn câu hỏi đã mở ở dòng 2.

---

## Tóm một câu

| Dòng | Việc | Ai chặn |
| :-: | :-- | :-- |
| 1 | bắt mắt — 11 từ, 1 trong 10 kiểu hook | thước |
| **2** | **mở món nợ** + nói vì sao là chuyện của người xem | thước (`mo=2`, chặn lời hứa rỗng) |
| **3-7** | **trả món nợ** — dùng lại ≥2 từ của dòng 2 | thước (`tra=<dòng>`) |
| **5-6** | **đỡ mốc rơi 2** — phải có số | thước (đếm số ở dòng 5-6) |
| 3-9 | mỗi dòng phải ĐẨY, không kể thêm | **người viết** — thước không đo được |
| 10 | khép cả vòng hình ảnh lẫn vòng nhận thức | thước (≥2 từ chung với dòng 1) |
