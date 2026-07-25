# README — sp02_cai_dat (Bài 02 khoá Superpowers)

Người xem xong phải làm được: **cài Superpowers vào Codex** (cả bản App lẫn bản dòng lệnh),
và hiểu **skill tự bật theo tình huống**, không phải thuộc tên skill nào.

| File | Vai |
| :-- | :-- |
| `sp02_cai_dat.txt` | Lời đọc, đúng 10 dòng |
| `sp02_cai_dat.man_hinh.md` | Chữ + chuyển động từng slide |
| `README_sp02_cai_dat.md` | File này: truy vết, hook, tự kiểm |

---

## 1. TRUY VẾT TỪNG CHI TIẾT

Không có chi tiết nào ngoài ba nguồn dưới. Không bịa bước cài, không bịa số.

| Dòng | Chi tiết | Nguồn |
| :-: | :-- | :-- |
| 1-4 | Ẩn dụ đội thợ / công trường / sổ tay thi công | `superpowers/README.md` dòng 9 ("Ẩn dụ xuyên suốt: **xây một căn nhà**") + `01_tong_quan.md` (thợ, xây nhà, đập đi làm lại) |
| 1, 4 | "sổ tay nằm ngoài cổng" | `02_cai_dat_va_skill.md` cảnh 1 ("cuốn sổ nằm ngoài cổng thì chẳng giúp được ai") — giữ ý, viết lại câu |
| 4 | Mỗi trang có nhãn, gặp việc nào tự lật trang đó | `02_cai_dat_va_skill.md` cảnh 6 ("mỗi skill là một trang sổ tay có nhãn") |
| 5 | Tên Superpowers, mỗi trang = một skill, cài vào Codex | `02_cai_dat_va_skill.md` cảnh 2 |
| 5 | "không phải thuộc tên trang nào" | `02_cai_dat_va_skill.md` cảnh 5 ("không có nghĩa là bạn phải nhớ và gọi từng skill bằng tay") |
| 6 | "thêm chức năng xuất phụ đề" → brainstorming (việc xây mới) | `02_cai_dat_va_skill.md` cảnh 8 |
| 6 | "có nhạc nhưng mất tiếng đọc" → systematic debugging (lỗi bất ngờ) | `02_cai_dat_va_skill.md` cảnh 9 (nguyên văn "video có nhạc nhưng mất giọng") |
| 6 | Số **tám bài** | `superpowers/README.md` bảng 8 bài + `01_tong_quan.md` cảnh 12 ("chạy cả tám bài ngay") |
| 7 | Codex App: thanh bên → `Plugins` → nhóm `Coding` → `Superpowers` → dấu cộng | `02_cai_dat_va_skill.md` cảnh 3 |
| 8 | Codex dòng lệnh: gõ gạch chéo `plugins` → tìm `Superpowers` → `Install Plugin` | `02_cai_dat_va_skill.md` cảnh 4 |
| 8 | "làm theo màn hình" | `02_cai_dat_va_skill.md` cảnh 3 ("rồi làm theo màn hình") |
| 9 | Bẫy "việc này nhỏ, bỏ qua quy trình" | `02_cai_dat_va_skill.md` cảnh 14 |
| 9 | "để nó hỏi hết rồi mới gật đầu" | `02_cai_dat_va_skill.md` cảnh 13 ("chỉ gật đầu khi bạn hiểu sản phẩm sẽ làm gì") |
| 10 | "cài = đưa sổ vào, làm theo = đổi cách xây" | `02_cai_dat_va_skill.md` cảnh 15 |

### Đã CỐ Ý bỏ khỏi bản mới (và vì sao)
- **Cổng bắt buộc của skill** (cảnh 10 bản cũ: chưa duyệt thiết kế thì chưa viết mã). Đây là nội dung của bài 03 và bài 05; nhét vào đây sẽ ăn mất chỗ của hai đường cài. Người xem bài 02 chỉ cần **cài được** và **biết skill tự bật**.
- **Ví dụ chạy thử bốn bước của bản cũ** (mở dự án → đưa yêu cầu → trả lời câu hỏi → duyệt). Dòng 7-8 của khuôn mới đã dùng cho **bốn bước CÀI**, vì cài mới là việc người xem phải làm ngay sau video. Phần "để nó hỏi hết rồi mới gật" được giữ lại, gói vào dòng 9.
- **Phiên bản manifest `6.2.0`** (`superpowers/README.md` dòng 4). Số thật nhưng vô nghĩa với người mới, và số phiên bản sẽ cũ đi trước cả video.

### Nối mạch với bài 01, không lặp
Bài 01 đóng bằng *"quy trình mới giúp bức tường đứng đúng chỗ"*. Bài 02 mở bằng **cuốn sổ nằm ngoài cổng** — tức là bài 01 đã cho người xem biết quy trình tồn tại, bài 02 trả lời câu hỏi kế tiếp: *quy trình đó hiện đang ở đâu, và làm sao đưa nó vào máy mình*. Sáu trạm kiểm soát của bài 01 **không nhắc lại**; hai skill nêu ở dòng 6 (`brainstorming`, `systematic-debugging`) là hai cái bài 01 chưa mô tả cách kích hoạt.

---

## 2. BA PHƯƠNG ÁN HOOK

Trần cứng: 11 từ đầu = 3 giây đầu, phải có **cảnh sờ được** + **mất mát hoặc nghịch lý**.

| # | Hook | 11 từ đầu đã đủ chưa | Chọn |
| :-: | :-- | :-- | :-: |
| **A** | *"Sổ tay thi công còn ngoài cổng, tường đã xây xong ba ngày."* | `Sổ tay thi công còn ngoài cổng, tường đã xây xong` — nghịch lý **trọn vẹn trong 11 từ**: sách hướng dẫn còn ngoài hàng rào mà tường đã dựng xong. Cảnh có 3 vật sờ được: sổ, cổng, tường. | ✅ |
| B | *"Sổ tay thi công khoá ngoài cổng, đội thợ vẫn xây, ba tầng lệch nhau."* | Mất mát cụ thể hơn (ba tầng lệch) nhưng rơi ở từ 12-15, ngoài 3 giây. 11 từ đầu mới chỉ có cảnh. | |
| C | *"Ngày thứ ba, tường xây xong, sổ tay thi công vẫn nằm ngoài cổng."* | Có "ngày thứ N" và có số ngay từ đầu, nhưng "ngoài cổng" rơi ở từ 14-15; 3 giây đầu chưa lộ nghịch lý. | |

**Vì sao chọn A:** chỉ A đưa được **cả hai vế của nghịch lý vào trong 11 từ**. B và C đều đẩy vế mất mát ra sau mốc 3 giây, tức là người vuốt nhanh chỉ nghe được nửa đầu vô hại. A cũng cho câu chốt dòng 10 dội lại sạch nhất: cùng ba vật *sổ · cổng · tường*.

**Hook bản cũ bị loại:** *"Một đội thợ giỏi vẫn cần sổ tay thi công. Nhưng cuốn sổ nằm ngoài cổng thì chẳng giúp được ai."* — hai câu (khuôn chỉ cho một), và 11 từ đầu là một mệnh đề chung chung, không có gì mất.

BOSS muốn đổi thì thay nguyên dòng 1 bằng B hoặc C, nhưng **phải chạy lại thước**: cả B và C đều đổi tập từ nội dung của dòng 1, nên phép đo đối xứng dòng 1 ↔ dòng 10 phải kiểm lại.

---

## 3. KẾT QUẢ CHẠY THƯỚC

```
cd /Users/simple/Desktop/Cloud/video
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/sp02_cai_dat.txt \
        --thuatngu "superpowers,skill,plugin,codex,agent,brainstorming,debugging"
```

```
SACH   | khong loi, khong canh bao
KETLUAN|27|387|DAT
```

- **27 reveal**, khuôn `[1,3,3,2,3,3,3,3,3,3]` khớp.
- **387 từ** ≈ **109 giây** ở nhịp 3,56 từ/giây (trong trần 330-450).
- Dòng dài nhất: dòng 6, 53 từ (trần 55).
- Thuật ngữ đầu tiên xuất hiện ở **dòng 5** (`Superpowers`, `skill`, `Codex`) — dòng 1-4 sạch.
- Đối xứng dòng 1 ↔ dòng 10: chung 7 từ nội dung (*sổ, cổng, công, tường, xây, xong, ngoài*), trần là 2.
- Không dấu gạch dài, không chữ lập trình, không chữ rỗng.

---

## 4. CHỖ CÒN YẾU NHẤT — NÓI THẲNG

1. **Dòng 6 là dòng nặng nhất bài (53 từ, sát trần 55) và cũng là dòng khó nhất.** Nó phải cõng cả hai ví dụ tự-bật, kèm hai tên tiếng Anh (`brainstorming`, `systematic debugging`) đọc lên nghe khó với người Việt không biết tiếng Anh. Nếu BOSS nghe thử thấy vấp, cách chữa rẻ nhất là **bỏ hẳn ví dụ thứ hai** và để dòng 6 chỉ còn một ví dụ chạy chậm hơn — nhưng như thế mất đối xứng "xây mới / gặp lỗi", là đúng cái làm người xem hiểu skill bật theo *loại việc*. Tôi chọn giữ hai ví dụ. Đây là chỗ tôi ít chắc nhất.

2. **Kết quả cài ở dòng 8 chỉ mô tả bằng lời, tôi không xác minh được màn hình thật.** Câu *"thấy Superpowers nằm trong danh sách đã cài là xong"* là suy ra hợp lý từ cảnh 3-4 bản cũ, **không** có trong nguồn nguyên văn. Nếu giao diện Codex hiện trạng thái khác, dòng 8 sai và phải sửa. Cần người có Codex mở ra soi một lần trước khi dựng deck.

3. **Hai đường cài bị ép vào hai dòng, mỗi đường chỉ còn hai câu.** Người dùng Codex App nghe dòng 8 (dòng lệnh) sẽ thấy thừa và ngược lại — nửa số người xem sẽ "trôi" mất một slide. Đã bù bằng câu mở dòng 7 (*"chọn đúng bản Codex bạn đang dùng"*) và bằng cách để slide 7 nền sáng / slide 8 nền tối, nhưng đây là nhược điểm cấu trúc chứ không phải nhược điểm câu chữ; khuôn 10 dòng không cho chỗ để làm tốt hơn.

4. **Dòng 9 nói bẫy bằng chữ, chưa có số.** Ba dòng còn lại đều có vật hoặc số neo vào; dòng 9 là dòng trừu tượng nhất bài. Slide 9 phải gánh phần này bằng hình (viên gạch lệch làm nghiêng cả tường) — nếu người dựng deck làm nhạt, dòng 9 sẽ là chỗ người xem vuốt qua.
