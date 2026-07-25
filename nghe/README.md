# NGHỀ GIỮ MẮT — trục thứ hai của việc viết kịch bản (lập 25/07/2026)

**Vấn đề nó giải:** thư viện `video/goc/` cởi trói được *kể chuyện gì*. Nhưng *giữ mắt
bằng cách nào* thì tới hôm nay vẫn chỉ có **hai dòng luật** nằm lẫn trong
`brief_tho2_opus.md`: một luật hook (11 từ đầu phải có mất mát) và một luật câu chốt
(dòng 10 dội lại dòng 1). Hai dòng đó lo được giây 0-3 và giây cuối. **Khoảng giữa
90 giây thì không ai lo.**

## Hai trục, đừng lẫn

| Trục | Thư viện | Trả lời câu | Chọn thế nào |
| :-- | :-- | :-- | :-- |
| **Kể chuyện gì** | `video/goc/` | Điều gây bất ngờ nhất ở đề tài này là gì | chọn 1 góc → ra `nhip` |
| **Giữ mắt bằng cách nào** | `video/nghe/` ← đây | Vì sao người xem không vuốt qua | chọn 1 kiểu hook + tuân 4 luật chung |

Hai trục **độc lập**: cùng một góc `nghich_ly_so` vẫn mở được bằng 4-5 kiểu hook khác
nhau. Góc mà không có nghề giữ mắt thì được sáu cách kể cùng một bài nhạt; nghề giữ
mắt mà không có góc thì được một bài hấp dẫn lặp lại sáu lần.

---

## Năm tầng của thư viện này

| File | Loại luật | Lo khúc nào |
| :-- | :-- | :-- |
| `KIEU_HOOK.md` | **chọn 1 trong 10** | giây 0-3 (dòng 1) |
| `DUONG_CONG.md` | luật chung | giây 3-70 — **hai mốc rơi thật**, mở và trả vòng lặp |
| `NGAT_MAU.md` | luật chung | cả bài — bao nhiêu giây phải đổi một thứ |
| `CO_CHIA_SE.md` | luật chung | 1 câu/bài — cái cớ để người xem gửi cho người khác |
| `TRAN_Y.md` | luật chung | cả bài — trần ý mới, chống loãng |
| `NHAT_KY.md` | sổ | kiểu hook đã dùng · **2 bài liền không cùng kiểu hook** |

---

## Dùng thế nào

**1. Người viết kịch bản** đọc `KIEU_HOOK.md` chọn kiểu, rồi đọc 4 luật chung.

**2. Khai báo một dòng máy đọc được** vào `README_{slug}.md` — đây là cách thước biết
mình đã *cố ý* làm gì, thay vì đoán:

```
NGHE: hook=nghich_ly_so | mo=2 | tra=6 | chia_se=10 | y_moi=1
```

| Trường | Nghĩa | Giá trị hợp lệ |
| :-- | :-- | :-- |
| `hook` | mã kiểu hook đã chọn | 1 trong 10 mã ở `KIEU_HOOK.md` |
| `mo` | dòng **mở món nợ** | phải là **2** — mốc rơi giây 8-15 nằm gọn ở đó |
| `tra` | dòng **trả món nợ** (dùng lại ≥2 từ của dòng `mo`) | **3-7**. Bài sp02 BOSS duyệt trả ở dòng **3** |
| `chia_se` | dòng chứa câu đáng chụp màn hình | **3** hoặc **10** |
| `y_moi` | số ý mới của bài | luôn **1** |

Ngoài 5 trường khai báo, thước còn tự đo **dòng 5-6 phải có số** — đó là chỗ đỡ mốc rơi
thứ hai (giây 45-60), không khai báo được, chỉ đếm được.

**3. Chạy thước — ba chế độ, 0 lượt API, tất định:**

```bash
T=video/.claude/skills/video-kynang/thuoc/thuoc_nghe.py

# ① đo kịch bản + khai báo  (thêm --taichinh cho bài tài chính để bật luật cấm hook)
python3 $T video/kichban/escbase_10dong/<slug>.txt \
           video/kichban/escbase_10dong/README_<slug>.md \
           --thuatngu "tên,thuật,ngữ"

# ② đo TRÙNG SCENE với bài liền trước  (ngưỡng 60%, tối thiểu 2 mẫu mới)
python3 $T --trung video/escbase_template/headless/deck_sp09 \
                   video/escbase_template/headless/deck_sp08

# ③ tính lại MỐC RƠI khi góc đổi nhịp
python3 $T --moc "1,2,3,2,3,3,3,3,3,4"
```

**Đã kiểm chạy 25/07:** bài `sp02_cai_dat` (bài BOSS duyệt *"video tốt"*) ra **DAT** ·
ca âm 9 lỗi cùng lúc ra **HONG** đủ 9 dòng · `--trung sp08 sp07` ra **HONG** (83%, 1 mẫu mới).

---

## BA TẦNG RÀNG BUỘC — giống `goc/`, đừng lẫn

| Tầng | Gồm | Xử lý |
| :-- | :-- | :-- |
| **Kỹ thuật** — vỡ là video hỏng | số câu = số reveal · ≤55 từ/dòng · không dấu `—` | **giữ tuyệt đối** |
| **Nghề giữ mắt** — bỏ là người xem vuốt qua | 5 tầng trong thư mục này | **giữ — đây là cái đang thiếu** |
| **Sở thích** | kiểu hook nào *đẹp hơn* | BOSS phán, không phải thước |

---

## 🔴 LUẬT CẤM KHÔNG NỚI THEO KIỂU HOOK

Nghề giữ mắt là để **hấp dẫn**, không phải để giật gân. Mọi kiểu hook vẫn chịu nguyên:

- Bài tài chính: **cấm kết luận đắt/rẻ, cấm khuyến nghị mua bán, cấm ngôn ngữ dọa dẫm.**
  Ba kiểu hook có mã ❌ trong `KIEU_HOOK.md` **không được dùng cho bài tài chính** vì
  bản chất của chúng là hô hào hoặc dọa.
- Cả bộ: **cấm chữ rỗng** ("mạnh mẽ", "đột phá"), **cấm chữ lập trình**, **cấm dấu `—`**.
- **Cấm bịa số.** Hook mạnh nhất trong bộ này luôn là hook có số thật.

Sức hút phải đến từ **nghịch lý có thật trong dữ liệu**, không từ tính từ mạnh. Đó cũng
là cách duy nhất vừa hút vừa không hứa hẹn gì.

---

## Vì sao KHÔNG nhập nguyên si skill viral ngoài GitHub

Khảo 25/07: có 6 skill đáng đọc (`claude-youtube`, `viral-short-form-video-master`,
`viral-reel-generator`, `ai-video-generator-claude`, `short-drama-scriptwriter`,
`create-viral-content`). **Không cái nào cắm thẳng vào được**, vì chúng không biết:

- ràng buộc engine: *số câu dòng N = số `.slide-element` slide N*;
- nhịp đọc thật của giọng đã chốt: **3,56 từ/giây** ⇒ "hook 3 giây" ở đây là **11 từ**,
  không phải "một câu ngắn";
- luật cấm khuyến nghị mua bán của bài tài chính.

Và chúng tối ưu cho **lượt xem**, còn tiêu chuẩn của xưởng là *"chỉ xem video là hiểu
vấn đề và làm được, chia sẻ lại được"*. Cái lấy được từ chúng là **tầng phân loại hook**
và **ý niệm đường cong giữ mắt** — đã mổ ra và dịch sang số của dự án trong hai file
`KIEU_HOOK.md` + `DUONG_CONG.md`.

---

## Thêm kiểu hook mới

Thêm một khối vào `KIEU_HOOK.md` theo đúng 6 mục có sẵn (mã · dùng khi · công thức 11 từ ·
ví dụ đạt · vì sao ăn · bẫy), rồi thêm mã vào danh sách `MA_HOOK` trong `thuoc_nghe.py`.
Không thêm vào thước thì thước báo mã lạ.
