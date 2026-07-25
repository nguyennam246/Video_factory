# MƯỜI KIỂU HOOK — chọn ĐÚNG MỘT (lập 25/07/2026)

**Vì sao có file này:** tới hôm nay dự án dùng **duy nhất một** kiểu mở bài — cảnh sờ được
cộng mất mát. Nó là kiểu tốt, BOSS đã duyệt qua nhiều bài. Nhưng một kiểu duy nhất dùng
cho mọi bài thì **bài nào cũng mở giống nhau**, và đó là một nửa lý do 8 bài Superpowers
xem liền thấy cùng một khuôn (nửa còn lại là `goc/kynang/` rỗng).

## Ràng buộc chung cho MỌI kiểu — không kiểu nào được miễn

| Ràng buộc | Số | Vì sao |
| :-- | :-- | :-- |
| **3 giây đầu = 11 TỪ đầu** | 11 | giọng edge NamMinh `+14%` chạy **3,56 từ/giây**, đo 8 bài |
| Cả dòng 1 | ≤ 18 từ | dài hơn là hook loãng, thước chặn |
| Từ đầu tiên | danh từ cụ thể · con số · một hành động | không được là liên từ, không được là "hãy" |
| Số viết ra chữ | *"ba mươi phần trăm"* | máy đọc chữ số rất xấu. ⚠️ đội từ nhanh, đếm lại 11 từ sau khi viết chữ |
| Cấm mở yếu | "hãy tưởng tượng" · "bạn có biết" · "trong bài này" · "hôm nay chúng ta" · "xin chào" · "có một" | đây là các câu model hay viết nhất, và là các câu làm người xem vuốt qua |

**Luật sổ:** hai bài liền nhau **không được cùng kiểu hook**. Ghi vào `NHAT_KY.md`
trước khi viết lời.

### 🔴 BẪY SỐ MỘT — công thức 2 CÂU đụng khuôn dòng 1 = 1 CÂU
Bắt được khi dựng bài sp07b, lần đầu dùng thư viện này. Bốn kiểu có công thức **hai câu**
(`cau_hoi_gai` · `nghich_ly_so` · `giua_hanh_dong` · `thu_nhan`), nhưng khuôn bài dạy cho
dòng 1 **đúng MỘT câu** — và số câu là ràng buộc **kỹ thuật** (mỗi câu = 1 reveal), không
nới được. **Cách chữa: nén thành một câu, giữ đủ cả dữ kiện lẫn dấu hỏi / nghịch lý.**

| Hai câu (vỡ khuôn) | Nén một câu (đạt) |
| :-- | :-- |
| *"Ba lần thay đồ. Nước vẫn yếu. Vì sao?"* — 3 câu | *"Ba lần thay đồ mà nước vẫn chảy yếu, vì sao?"* — 1 câu, 11 từ |
| *"Doanh thu tăng bốn mươi phần trăm. Dòng tiền âm."* — 2 câu | *"Doanh thu tăng bốn mươi phần trăm, dòng tiền vẫn âm."* — 1 câu, 9 từ |

⚠️ Nén xong **đếm lại 11 từ**, đừng tin bản nháp: dấu phẩy thay dấu chấm không đổi số từ,
nhưng chữ nối thêm vào (*"mà"*, *"vẫn"*) thì có.
⚠️ Góc nào cho dòng 1 **nhiều hơn 1 câu** (xem `nhip` trong `goc/`) thì dùng công thức
hai câu bình thường — bẫy này chỉ dính khuôn có `nhip[0] == 1`.

---

## Bảng chọn nhanh

| Mã | Tên | Chốt ở đâu | Bài dạy | Bài tài chính |
| :-- | :-- | :-- | :-: | :-: |
| `mat_mat` | Mất mát | cảnh có người, có đồ vật, có cái bị mất | ✅ | ✅ |
| `nghich_ly_so` | Nghịch lý số | hai con số đáng lẽ đi cùng lại ngược nhau | ✅ | ✅ |
| `phu_dinh` | Phủ định niềm tin | *"không phải vì X"* — đập một cái ai cũng tin | ✅ | ✅ |
| `giua_hanh_dong` | Vào giữa hành động | mở lúc việc đang xảy ra, không dẫn nhập | ✅ | ✅ |
| `thu_nhan` | Lời thú nhận | người kể tự nhận đã làm sai | ✅ | ⚠️ |
| `mot_moc` | Một cái mốc | *"ngày thứ N"* — mốc mà mọi thứ đổi | ✅ | ✅ |
| `truoc_sau` | Trước và sau | hai trạng thái cạnh nhau, cách nhau đúng một thứ | ✅ | ✅ |
| `cau_hoi_gai` | Câu hỏi có gai | câu hỏi người xem biết là mình không trả lời được | ✅ | ✅ |
| `dung_lam` | Đừng làm | lệnh phủ định — *"đừng X trước khi Y"* | ✅ | ❌ |
| `cai_gia` | Cái giá | cái giá cụ thể của việc không biết | ✅ | ❌ |

❌ = **cấm dùng cho bài tài chính**: `dung_lam` là khuyến nghị đội lốt, `cai_gia` là dọa
dẫm đội lốt. Cả hai đụng thẳng `CAM_KHUYEN` / `CAM_DOA`.
⚠️ `thu_nhan` dùng được cho tài chính **chỉ khi** cái thú nhận là về *cách đọc số liệu*,
không phải về *lãi lỗ của người kể*.

---

## `mat_mat` — MẤT MÁT

**Dùng khi** đề tài là một thói quen sai gây hậu quả tích luỹ. Kiểu mặc định của bộ dạy,
đã chạy nhiều bài BOSS duyệt.

**Công thức 11 từ:** `{Mốc thời gian}, {người} {làm việc thường}, {mất luôn cái quan trọng}.`

**Ví dụ đạt:** *"Ngày thứ ba mươi, người thợ mới quên lời dặn, dọn luôn cái tủ hồ sơ."*
→ có người, có đồ vật, có mất mát, có số. 13 từ, sát trần.

**Vì sao ăn:** mất mát cụ thể kích hoạt nhanh hơn lợi ích cụ thể. Người xem tự hỏi *"tôi
có đang mất cái đó không"*.

**Bẫy:** mất mát trừu tượng ("mất thời gian", "mất hiệu quả") là **không có mất mát** —
phải mất một **đồ vật hoặc một con số**. Và đừng dùng lại kiểu này hai bài liền, vì nó
đang là kiểu bị lạm dụng nhất trong dự án.

---

## `nghich_ly_so` — NGHỊCH LÝ SỐ

**Dùng khi** có hai con số thật đáng lẽ đi cùng chiều mà lại ngược nhau.

**Công thức 11 từ:** `{Số A} {tăng}. {Số B} {giảm}. Cùng một {kỳ / người / máy}.`

**Ví dụ đạt:** *"Doanh thu tăng bốn mươi phần trăm. Dòng tiền âm. Cùng một năm."*
→ 12 từ, hai số thật, nghịch lý lộ ngay, không một tính từ nào.

**Vì sao ăn:** không hứa hẹn gì mà vẫn căng, vì người xem tự thấy có cái không khớp. Đây
là kiểu hook **an toàn nhất cho bài tài chính** — sức hút đến từ số, không từ lời.

**Bẫy:** hai số phải **cùng kỳ, cùng đơn vị so sánh được**. So doanh thu năm nay với dòng
tiền năm khác là bịa nghịch lý. Và đừng giải thích nghịch lý ngay dòng 2 — đó là món nợ
phải giữ tới dòng 6 (xem `DUONG_CONG.md`).

---

## `phu_dinh` — PHỦ ĐỊNH NIỀM TIN

**Dùng khi** người mới có một niềm tin phổ biến mà sai, và cả bài là để sửa niềm tin đó.

**Công thức 11 từ:** `{Hiện tượng} không phải vì {lý do ai cũng tin}.`

**Ví dụ đạt:** *"Phiên làm việc đắt lên không phải vì bạn hỏi nhiều."*
→ 10 từ. Đập trực diện cái người xem đang tin.

**Vì sao ăn:** phủ định tạo khoảng trống trong đầu, và khoảng trống thì phải lấp. Người
xem ở lại để biết *"thế thì vì cái gì"*.

**Bẫy:** phải phủ định niềm tin **thật sự phổ biến**, không phải một niềm tin bạn tự dựng
lên để đập. Nếu người xem không tin điều đó từ đầu thì hook rỗng. Và phủ định rồi **bắt
buộc phải trả lời** ở dòng 6 — mở mà không trả là hook lừa.

---

## `giua_hanh_dong` — VÀO GIỮA HÀNH ĐỘNG

**Dùng khi** bài có một lần chạy thử / một sự việc kể được, và phần dẫn nhập là phần nhạt nhất.

**Công thức 11 từ:** `{Hành động đang diễn ra}. {Kết quả bất thường hiện ra}.`

**Ví dụ đạt:** *"Gõ xong lệnh, màn hình dừng lại. Ba mươi hai lỗi cùng lúc."*
→ 12 từ. Không giới thiệu gì, vào thẳng giữa việc.

**Vì sao ăn:** bỏ hẳn khúc dẫn nhập — chỗ rơi người xem nhiều nhất. Người xem bị đặt vào
giữa một việc đang xảy ra và phải ở lại để hiểu đầu đuôi.

**Bẫy:** phải là hành động **sờ được, thấy được**, không phải hành động trong đầu ("bạn
đang suy nghĩ về…"). Và đừng để dòng 2 quay lại giải thích từ đầu — như thế là vẫn có
khúc dẫn nhập, chỉ dời xuống chỗ khác.

---

## `thu_nhan` — LỜI THÚ NHẬN

**Dùng khi** chính dự án đã trả giá cho cái bẫy mà bài này dạy. Bộ này có sẵn nhiều ca thật.

**Công thức 11 từ:** `{Tôi/Chúng tôi} đã {làm sai}. {Hậu quả có số}.`

**Ví dụ đạt:** *"Tôi tin máy báo xong. Bốn lỗi lọt tới tay người xem."*
→ 12 từ. Thú nhận có số, không xin lỗi vòng vo.

**Vì sao ăn:** người xem hạ phòng bị. Một lời thú nhận đáng tin hơn mười lời khuyên, và
nó cho phép cả bài nói thẳng về cái bẫy mà không có giọng dạy đời.

**Bẫy:** thú nhận phải **thật, có số, truy vết được**. Thú nhận bịa là kiểu hook hỏng
nhất trong mười kiểu, vì nó vừa nhạt vừa mất tin. Với bài tài chính chỉ được thú nhận
về *cách đọc số*, không được thú nhận về lãi lỗ — chạm `CAM_KHUYEN` ngay.

---

## `mot_moc` — MỘT CÁI MỐC

**Dùng khi** vấn đề chỉ lộ ra sau khi tích luỹ, và cái mốc chính là bằng chứng.

**Công thức 11 từ:** `{Chín} {lần / ngày / kỳ} {vẫn ổn}. {Lần thứ mười} {đổ}.`

**Ví dụ đạt:** *"Chín lần chạy đều sạch. Lần thứ mười, không có phụ đề."*
→ 12 từ. Cái mốc làm cả bài có mốc neo.

**Vì sao ăn:** con số thứ tự tạo cảm giác đếm — người xem chờ tới chỗ vỡ. Nó cũng cho
dòng 10 một chỗ dội lại rất chắc.

**Bẫy:** đừng lẫn với `mat_mat` — `mat_mat` chốt vào **cái bị mất**, `mot_moc` chốt vào
**cái mốc**. Nếu viết ra mà thấy trọng tâm rơi vào đồ vật bị mất thì khai báo là
`mat_mat`, đừng khai báo sai để lách luật hai bài liền.

---

## `truoc_sau` — TRƯỚC VÀ SAU

**Dùng khi** dạy một thao tác mà hiệu quả thấy ngay, hoặc so hai kỳ của một doanh nghiệp.

**Công thức 11 từ:** `{Trạng thái A}. {Trạng thái B}. Cách nhau đúng {một thứ}.`

**Ví dụ đạt:** *"Tám mươi ba giây, không ai hiểu. Trăm sáu ba giây, hiểu hết."*
→ 13 từ. Hai trạng thái có số, cách nhau đúng một thay đổi.

**Vì sao ăn:** so sánh cạnh nhau là hình ảnh rẻ nhất mà rõ nhất, và nó hứa sẵn phần
thân bài: *cái "một thứ" đó là gì*.

**Bẫy:** cái "một thứ" phải **đúng là một thứ**. Nếu giữa A và B đổi ba thứ thì hook nói
dối, và người xem thấy ngay ở dòng 6. Với bài tài chính, tuyệt đối không để A/B thành
"giá lúc rẻ / giá lúc đắt" — đó là khuyến nghị.

---

## `cau_hoi_gai` — CÂU HỎI CÓ GAI

**Dùng khi** câu trả lời chính là cả bài, và câu hỏi đủ cụ thể để người xem *biết là mình
không trả lời được*.

**Công thức 11 từ:** `{Tình huống cụ thể có số}. {Câu hỏi ngắn}?`

**Ví dụ đạt:** *"Máy báo đạt cả hai lượt. Vì sao vẫn ra bốn lỗi?"*
→ 11 từ, sát trần. Người xem không đoán được, và biết là không đoán được.

**Vì sao ăn:** khoảng trống nhận thức. Khác với câu hỏi rỗng ("bạn có biết…"), câu hỏi
này có **dữ kiện trước** nên nó là câu hỏi thật.

**Bẫy:** đây là kiểu **dễ hỏng nhất** — hỏi một câu người xem trả lời được ngay là hook
chết, hỏi một câu quá xa là hook rỗng. Bắt buộc phải có **dữ kiện có số đứng trước** dấu
hỏi. Và cấm hỏi câu tu từ kiểu "bạn có muốn giỏi hơn không".

### ⭐⭐ BIẾN THỂ "ĐẾM LẦN THẤT BẠI" — BOSS DUYỆT 25/07/2026
BOSS xem bản A/B `sp07b` cạnh bản cũ rồi phán: *"Bản mới hút mắt hơn đấy. **Nhấn mạnh vào
3 lần thay đồ mà vẫn yếu**, rất hay."* Đây là **phán quyết của tai/mắt người**, không phải
suy luận của máy — ghi thành luật, đừng lật lại.

> *"**Ba lần** thay đồ **mà** nước **vẫn** chảy yếu, **vì sao?**"*

**Ba bộ phận, thiếu một là yếu hẳn:**

| Bộ phận | Trong ví dụ | Nó làm gì |
| :-- | :-- | :-- |
| **Số lần thất bại ≥ 3** | *"Ba lần"* | Một lần là rủi ro. **Ba lần là một QUY LUẬT.** Con số làm thay việc của cả đoạn giải thích, người xem tự hiểu "đây không phải xui" |
| **Công tăng, kết quả đứng yên** | *"thay đồ… mà vẫn yếu"* | Phá quan hệ nhân quả người xem mặc định (làm nhiều hơn thì phải khá hơn). Cái gì phá nhân quả thì **bắt buộc phải có lời giải** |
| **Câu hỏi KHÔNG được trả lời** | *"vì sao?"* | Để lại **món nợ**, không phải lời hứa. Người xem ở lại vì trong đầu còn một chỗ chưa khớp, chứ không vì được hứa hẹn gì |

**Vì sao ăn hơn `mat_mat` ở đúng bài này:** bản cũ mở bằng *"Vòi chảy yếu, thợ thay vòi mới,
nước vẫn yếu như cũ"* — cùng cảnh, cùng sự việc, nhưng **kể** chứ không **hỏi**, và không có
số đếm. Người xem nhận được một mẩu chuyện; bản mới nhận được một **câu đố dở dang**.

### 🔑 LUẬT RÚT RA — HOOK MẠNH NHẤT LÀ HOOK KỂ CHÍNH CÁI BỆNH BÀI SẼ CHỮA
Bài 07 dạy *"đừng sửa mò, hãy lần theo bằng chứng tới đúng chỗ vỡ"*. Hook *"ba lần thay đồ
mà vẫn yếu"* **chính là một ca sửa mò** — không phải cái móc câu gắn ngoài, mà là **bản thu
nhỏ của vấn đề**. Vì thế nó không có mùi chiêu trò, và dòng 10 dội lại được tự nhiên
(*"Ba lần thay đồ không bằng một lần đo đúng."*).

⇒ **Chọn hook cho bài sau đừng hỏi *"câu nào giật nhất"*.** Hỏi:
> ***"Cảnh nhỏ nhất mà trong đó cái bệnh này ĐÃ xảy ra rồi là cảnh gì?"***

Nén cảnh đó vào 11 từ, thêm con số đếm và một dấu hỏi. Đó là công thức.

⚠️ Đếm lần thất bại **chỉ dùng khi có thật**. Bài nào không có chuỗi thất bại lặp lại thì
đừng bịa "ba lần" — bịa số là bẫy nặng nhất của cả thư viện này.

---

## `dung_lam` — ĐỪNG LÀM ❌ *(cấm cho bài tài chính)*

**Dùng khi** có một thao tác mà người mới hay làm sai thứ tự, và làm sai thì mất công dựng lại.

**Công thức 11 từ:** `Đừng {làm X} trước khi {làm Y}. {Hậu quả có số}.`

**Ví dụ đạt:** *"Đừng đổi màu deck hai lần. Lần thứ hai ra deck lai màu."*
→ 12 từ.

**Vì sao ăn:** câu lệnh phủ định đọc nhanh hơn câu khuyên, và nó đánh vào cái sợ làm lại.

**Bẫy:** **cấm tuyệt đối cho bài tài chính** — bất cứ câu "đừng mua / đừng bán / đừng
vào" nào cũng là khuyến nghị, thước `CAM_KHUYEN` chặn ngay. Với bài dạy thì "đừng" phải
nhắm vào **thao tác**, không nhắm vào người xem ("đừng ngu").

---

## `cai_gia` — CÁI GIÁ ❌ *(cấm cho bài tài chính)*

**Dùng khi** cái giá của việc không biết đo được bằng giờ, bằng lượt làm lại, bằng tiền.

**Công thức 11 từ:** `{Không biết cái này} tốn {con số cụ thể}.`

**Ví dụ đạt:** *"Không biết cache giọng, mỗi lần sửa slide tốn thêm mười một lượt."*
→ 12 từ.

**Vì sao ăn:** cái giá có số làm người xem tự quy ra trường hợp của mình.

**Bẫy:** **cấm cho bài tài chính** — nói cái giá của việc không biết một mã cổ phiếu là
dọa dẫm, chạm `CAM_DOA`. Với bài dạy thì con số phải là **con số đo được của dự án**,
không được là con số hù ("tốn hàng trăm giờ").
