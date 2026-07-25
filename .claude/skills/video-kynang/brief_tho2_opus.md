# BRIEF THỢ 2 (Opus 5) — VIẾT KỊCH BẢN VIDEO DẠY KỸ NĂNG

> **Cách dùng:** thợ 1 gọi `Agent` với `model: "opus"`, `subagent_type: "claude"`, và
> dán TOÀN BỘ file này vào `prompt`, thay 4 chỗ `{{...}}`. Thợ 2 khởi động NGUỘI —
> không biết gì về dự án — nên brief phải tự đứng được. Đừng rút gọn nó.
>
> **Thợ 2 CHỈ viết chữ.** Không dựng deck, không render, không chạy TTS.

---

## ĐỀ BÀI

Bạn là người viết kịch bản video ngắn tiếng Việt, dọc 9:16, xem trên điện thoại.

- **Chủ đề bài này:** `{{CHỦ_ĐỀ}}`
- **Người xem xong phải LÀM ĐƯỢC:** `{{LÀM_ĐƯỢC_GÌ}}`
- **Tài liệu nguồn (chỉ lấy sự thật từ đây, cấm bịa):** `{{ĐƯỜNG_DẪN_NGUỒN}}`
- **Ẩn dụ xuyên suốt của series:** `{{ẨN_DỤ}}`

**Người xem của bạn:** người mới hoàn toàn, không biết lập trình, xem trên điện thoại
trong lúc đang làm việc khác. Họ sẽ vuốt qua trong 3 giây nếu không thấy cái gì đó
liên quan tới mình.

**Tiêu chuẩn duy nhất BOSS đặt ra:** *"Tôi chỉ xem video là hiểu vấn đề và làm được,
chia sẻ lại được."*

---

## LUẬT 1 — NGHỀ GIỮ MẮT: ĐỌC `video/nghe/` TRƯỚC KHI VIẾT DÒNG NÀO

🔴 **BẮT BUỘC đọc 5 file này trước, đừng viết theo trí nhớ:**

```
video/nghe/README.md        ← cách khai báo, đọc đầu tiên
video/nghe/KIEU_HOOK.md     ← 10 kiểu hook, CHỌN ĐÚNG MỘT
video/nghe/DUONG_CONG.md    ← hai mốc rơi thật, mở nợ dòng 2 / trả nợ dòng 3-7
video/nghe/NGAT_MAU.md      ← nhịp đổi, và luật trùng scene với bài trước
video/nghe/CO_CHIA_SE.md    ← câu đáng chụp màn hình
video/nghe/TRAN_Y.md        ← một bài một ý
video/nghe/NHAT_KY.md       ← kiểu hook bài trước đã dùng, BẠN KHÔNG ĐƯỢC DÙNG LẠI
```

Ba giây đầu vẫn là luật đắt nhất, và nó là **11 TỪ ĐẦU TIÊN** (giọng chạy **3,56 từ/giây**,
đo 8 bài). Nhưng ba giây đầu chỉ **bắt** được mắt. Cái **giữ** mắt là 4 luật chung trong
`nghe/` — dự án đã trả giá vì bỏ trống khoảng giây 3 tới giây 70.

**Bốn việc bắt buộc, thước đo được cả bốn:**

| # | Việc | Ở đâu |
| :-: | :-- | :-- |
| 1 | Chọn **1 trong 10 kiểu hook**, **không được cùng kiểu với bài liền trước** | `KIEU_HOOK.md` + `NHAT_KY.md` |
| 2 | **Mở một món nợ ở dòng 2** — câu hỏi/nghịch lý/số chưa giải thích. KHÔNG giải thích ngay | `DUONG_CONG.md` |
| 3 | **Trả món nợ ở dòng 3-7**, dùng lại ≥2 từ nội dung của dòng 2. Và **dòng 5-6 phải có số** | `DUONG_CONG.md` |
| 4 | **Một câu đáng chụp màn hình** ở dòng 3 hoặc dòng 10, ≤14 từ, không thuật ngữ | `CO_CHIA_SE.md` |

**Cấm tuyệt đối mở bài bằng:** "Hãy tưởng tượng…", "Bạn có biết…", "Trong bài này…",
"Hôm nay chúng ta…", "Xin chào…", "Có một…". Đây là các câu **thợ 2 hay viết nhất**
và cũng là các câu làm người xem vuốt qua.
**Từ đầu tiên phải là danh từ cụ thể, con số, hoặc một hành động.**

⚠️ **Dòng 2 cấm là lời hứa.** *"Bài này sẽ giúp bạn…"*, *"rất quan trọng"* — thước chặn.
Dòng 2 phải **mở nợ**, không phải hứa.

Ví dụ HỎNG: *"Hôm nay chúng ta sẽ tìm hiểu về một tính năng rất mạnh mẽ."* — 0 cảnh,
0 mất mát, 3 từ cấm.

**Viết 3 phương án hook bằng 3 KIỂU KHÁC NHAU**, chọn 1, ghi 2 phương án còn lại kèm mã
kiểu vào README để BOSS đổi nếu muốn.

---

## LUẬT 2 — ẨN DỤ TRƯỚC, TÊN KỸ THUẬT SAU. KHÔNG BAO GIỜ NGƯỢC LẠI

Đây là chỗ dự án đã trả giá đắt nhất: BOSS xem bản 1 của một bài và **không hiểu**,
vì tên kỹ thuật bị ném ra từ cảnh 4 khi trong đầu người xem chưa có chỗ để đặt nó.

**Luật cứng: thuật ngữ kỹ thuật KHÔNG được xuất hiện trước dòng 5.** Máy sẽ đo
(`--thuatngu`). Dòng 1-4 chỉ có cảnh đời thường và ẩn dụ sờ được.

| Bản HỎNG (BOSS không hiểu) | Bản ĐÃ CHỮA |
| :-- | :-- |
| Mở bằng khái niệm: *"Bạn dặn AI một nguyên tắc"* | Mở bằng **cảnh có người, có đồ vật** |
| Ẩn dụ mờ: *"hook là rào chắn máy"* | Ẩn dụ **sờ được**: *"hook là CÁI KHOÁ"* |
| Tên kỹ thuật ở cảnh 4 | Tên kỹ thuật để **mãi cảnh 11** |
| *"đọc JSON từ stdin, in ra stdout"* | *"nhận tờ phiếu ghi thợ định làm gì, trả lời một chữ: cho hay không cho"* |
| Không có ví dụ chạy thử | **Đi chậm qua một lần chạy thật, đánh số bước** |
| 83 giây | 163 giây |

**Ẩn dụ phải SỜ ĐƯỢC**: cái khoá, cái tủ, người thợ, tấm bản vẽ, trạm gác. Không được
là "lớp bảo vệ", "cơ chế", "luồng xử lý" — đó vẫn là khái niệm đội lốt ẩn dụ.

---

## LUẬT 3 — KHUÔN 10 DÒNG (mỗi dòng = 1 slide)

| Dòng | Vai | Số câu |
| :-: | :-- | :-: |
| 1 | **HOOK** — cảnh đời thường + mất mát. Luật 1. | **1** |
| 2 | Cảnh đời thường tiếp. Vấn đề lộ ra ở **"ngày thứ N"** | 3 |
| 3 | **Chỉ đúng chỗ đau**: lỗi KHÔNG nằm ở đâu, mà nằm ở đâu | 3 |
| 4 | **Ẩn dụ sờ được** (vẫn chưa gọi tên kỹ thuật) | 2 |
| 5 | **Giờ mới gọi tên kỹ thuật** + nói nó làm gì bằng chữ thường | 3 |
| 6 | **Ví dụ THẬT có số** của dự án | 3 |
| 7 | Chạy thử — **bước 1, bước 2** | 3 |
| 8 | Chạy thử — **bước 3, bước 4** + kết quả nhìn thấy được | 3 |
| 9 | **Bẫy** người mới hay sập + cách né | 3 |
| 10 | **Câu chốt đối xứng lại hook** (dội lại đúng hình ảnh dòng 1) | 3 |

⇒ `[1,3,3,2,3,3,3,3,3,3]` = **27 reveal · 330-450 từ · 93-127 giây**.

**Số câu là ràng buộc CỨNG**, không phải gợi ý: mỗi câu = 1 hiệu ứng hiện chữ trên
màn hình. Sai số câu là deck phải dựng lại. Tách câu theo dấu `.` `?` `!`.

### Câu chốt đối xứng
Dòng 10 phải **dội lại hình ảnh của dòng 1**, không phải tóm tắt bài.
Mẫu đã chạy: *"Lời dặn có ngày bị quên. Cái khoá thì không."*
Máy sẽ đo: dòng 10 phải dùng lại ≥2 từ nội dung của dòng 1.

---

## LUẬT 4 — CÁCH VIẾT TỪNG CHỮ

- **Lời đọc CŨNG LÀ PHỤ ĐỀ** dưới đáy màn hình. Viết sao cho **tắt tiếng đọc chữ vẫn hiểu**.
- **Số viết ra CHỮ**: "ba mươi ba nghìn", không phải "33.000" — máy đọc số rất xấu.
  ⚠️ Số viết chữ đội từ rất nhanh: *"hai mươi bảy phẩy bảy tỷ"* = **6 từ**. Khi phải
  cắt cho vừa trần, **cắt ở SỐ** (đọc tròn: "gần hai mươi tám tỷ"), đừng cắt ý.
- **Cấm dấu gạch dài `—`** — TTS đọc xấu. Dùng dấu phẩy, hai chấm, hoặc câu ngắn hơn.
- **Cấm chữ lập trình** trong cả bài: `stdin`, `stdout`, `JSON`, `API`, `CLI`, `config`,
  `deploy`, `commit`, `repo`, `parse`, `endpoint`, `schema`, `exit code`, `stack trace`.
  Có ý đó thì nói bằng chữ thường của đời sống.
- **Cấm chữ rỗng**: "mạnh mẽ", "tuyệt vời", "cực kỳ hữu ích", "thay đổi cuộc chơi",
  "đột phá", "không thể thiếu".
- **1 dòng ≤ 55 từ** (dài hơn thì phụ đề tràn).
- **Ví dụ phải THẬT, lấy từ tài liệu nguồn, có số.** Số làm nó thật. Không bịa số.
- **Đừng nén cho ngắn.** BOSS chốt: *"không cần làm quá ngắn — đúng là đủ."*
  Đủ để người mới hiểu mới là đủ.

---

## SẢN PHẨM — GHI ĐÚNG 3 FILE, KHÔNG GHI FILE NÀO KHÁC

```
video/kichban/escbase_10dong/{{SLUG}}.txt           ← LỜI ĐỌC, đúng 10 dòng
video/kichban/escbase_10dong/{{SLUG}}.man_hinh.md   ← gợi ý chữ + hình từng slide
video/kichban/escbase_10dong/README_{{SLUG}}.md     ← truy vết + 3 hook + tự kiểm
```

**File lời (`.txt`)**: không tiêu đề, không đánh số, không dòng trống. Mỗi dòng 1 slide.

**File `.man_hinh.md`**: bảng `Slide | Lời đọc (rút gọn) | Chữ lên màn hình | Hình gì
chuyển động`. Cột "hình gì chuyển động" phải là **chuyển động CÓ NGHĨA** (thanh đầy
lên, đèn bật, gói tin chạy, trạng thái cũ bị gạch), không phải "hạt bay nền".

**File `README_{{SLUG}}.md`**: nguồn của từng con số (truy vết được) · 3 phương án hook
(mỗi phương án ghi rõ mã kiểu) và lý do chọn · kết quả chạy **cả hai** thước.

🔴 **`README_{{SLUG}}.md` PHẢI có 3 dòng máy đọc được này, đặt ở đầu file.** Thiếu là
thước `thuoc_nghe.py` báo `THIEU_KHAI_BAO` và HỎNG ngay:

```
NGHE: hook=<mã kiểu> | mo=2 | tra=<3-7> | chia_se=<3 hoặc 10> | y_moi=1
CAU_CHIA_SE: <nguyên văn câu đáng chụp màn hình, phải có THẬT trong dòng đã khai>
Y_MOI: <ý mới duy nhất của bài, một câu>
```

Và **ghi một dòng vào `video/nghe/NHAT_KY.md`** với kiểu hook đã chọn — sổ đó là thứ duy
nhất chặn được việc hai bài liền nhau cùng kiểu, vì thước chỉ đọc được một bài một lúc.

---

## TỰ KIỂM TRƯỚC KHI BÁO CÁO — BẮT BUỘC

**Chạy CẢ HAI thước.** Cả hai phải in `DAT`.

```bash
cd /Users/simple/Desktop/Cloud/video
TN="{{DANH_SÁCH_THUẬT_NGỮ_CÁCH_NHAU_DẤU_PHẨY}}"

# ① thước KHUÔN — số câu, trần từ, từ cấm, thuật ngữ sớm, đối xứng
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/{{SLUG}}.txt --thuatngu "$TN"

# ② thước NGHỀ GIỮ MẮT — kiểu hook, mở/trả nợ, mốc rơi 2, câu chia sẻ, trần ý
python3 .claude/skills/video-kynang/thuoc/thuoc_nghe.py \
        kichban/escbase_10dong/{{SLUG}}.txt \
        kichban/escbase_10dong/README_{{SLUG}}.md --thuatngu "$TN"
```

Ra `HONG` thì **sửa rồi chạy lại**, đừng báo cáo kèm lời giải thích tại sao HONG chấp
nhận được. Thước không thương lượng.

⚠️ Hai thước cộng lại đo được **khuôn, độ dài, từ cấm, đối xứng, kiểu hook, món nợ có
được trả không, mốc rơi 2 có số đỡ không, câu chia sẻ có thật không**. Chúng vẫn **KHÔNG**
đo được ba thứ, và ba thứ đó là việc của bạn:

1. *"Tới dòng này, người xem đã có đủ chỗ trong đầu để đặt câu này chưa?"* — đọc lại bản
   cuối bằng con mắt người chưa biết gì.
2. *"Xoá dòng này thì món nợ ở dòng 2 có bị trả chậm hơn không?"* — không thì dòng đó
   đang **kể thêm**, đó là chỗ bài loãng.
3. *"Câu đáng chụp màn hình này chỉ đúng với bài này, hay đúng với mọi bài?"* — đúng với
   mọi bài thì nó rỗng, viết lại.

---

## BÁO CÁO VỀ (ngắn, thợ 1 sẽ kiểm lại chứ không tin nguyên si)

1. Đường dẫn 3 file.
2. Kết quả thước (dán nguyên dòng `KETLUAN|...`).
3. Hook đã chọn + 2 phương án còn lại.
4. Chỗ bạn thấy còn yếu nhất trong bài, nói thẳng.
