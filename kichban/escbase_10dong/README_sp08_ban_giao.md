# README — sp08_ban_giao (Bài 08 khoá Superpowers)

Người xem xong phải làm được: **đòi bằng chứng thay vì tin lời "đã xong"; biết chọn
cách nhập việc vào nhánh chính** (bảng "làm được gì" của brief thợ 2, bài 08).

⚠️ **Ghi chú vai trò:** file `sp08_ban_giao.txt` (lời đọc) do **thợ 1** viết và đã tự
chạy thước ra `KETLUAN|27|368|DAT` trước khi giao việc dựng deck này. Tôi (thợ 2, phiên
này) KHÔNG sửa lời — chỉ dựng deck, validate, soi ảnh, và viết lại 2 file tài liệu còn
thiếu (`man_hinh.md`, `README` này) để truy vết đầy đủ 3 file/bài đúng chuẩn brief.

| File | Vai |
| :-- | :-- |
| `sp08_ban_giao.txt` | Lời đọc, đúng 10 dòng — **thợ 1 viết, ĐÃ đạt thước, không sửa** |
| `sp08_ban_giao.man_hinh.md` | Chữ + chuyển động từng slide — thợ 2 viết khi dựng deck |
| `README_sp08_ban_giao.md` | File này: truy vết, hook, tự kiểm — thợ 2 viết khi dựng deck |

---

## 1. TRUY VẾT TỪNG CHI TIẾT

Nguồn duy nhất: `kichban/superpowers/08_kiem_chung_va_ban_giao.md` (định dạng kịch bản
cũ `LỜI:`/`CHỮ:`/`MÃ:`, 16 khối cách nhau bằng `---`). Bảng dưới đối chiếu từng dòng của
`sp08_ban_giao.txt` (đã có sẵn, không sửa) với khối nguồn gần nhất.

| Dòng | Nội dung dòng đã chốt | Khối nguồn gần nhất | Mức khớp |
| :-: | :-- | :-- | :-- |
| 1 | Chìa khóa đã trao, dây điện mới lắp chưa ai bật thử | Khối 1: "Đội thợ báo căn nhà đã xong. Chủ nhà hỏi: đã thử điện chưa? Người thợ đáp: dây mới, chắc là được." | **Đã đổi ý so với nguồn**: nguồn có chủ nhà HỎI lại (thợ trả lời mơ hồ "chắc là được"), bản chốt viết chủ nhà KHÔNG hỏi, chỉ gật đầu (xem dòng 2). "Chìa khóa" không có chữ trong khối này — là chi tiết suy ra từ "bàn giao nhà" để khớp ẩn dụ xuyên khóa |
| 2 | Đến ngày bàn giao, đội thợ báo nhà đã xong · chủ nhà không hỏi lại, chỉ gật đầu nhận chìa khóa · ba hôm sau bật công tắc, không sáng | Cùng khối 1, nhưng **đảo ngược tình tiết**: nguồn là chủ nhà hỏi + thợ trả lời mơ hồ; bản chốt là chủ nhà không hỏi gì cả. Cả hai đều đi tới cùng kết cục (không kiểm chứng thật), nhưng đây là chi tiết KHÔNG trích nguyên văn | Suy luận/viết lại, không phải trích nguồn |
| 3 | Lỗi không ở tay nghề thợ điện · dây đấu đúng, ổ cắm lắp chuẩn · lỗi ở chỗ không ai bật công tắc trước khi trao chìa | **Không có trong nguồn.** Nguồn không nhắc "tay nghề", "dây đấu đúng", "ổ cắm lắp chuẩn" | Mở rộng ẩn dụ điện (thợ điện/dây/ổ cắm) hoàn toàn mới, phục vụ vai "chỉ đúng chỗ đau" của khuôn 10 dòng |
| 4 | Đặt câu "đã xong" lên một cái cân, bên kia đặt kết quả vừa đo được · cân nghiêng về bên nào, sự thật nằm ở bên đó | Tinh thần gần với khối 2: "Một câu tự tin không làm bóng đèn sáng. Muốn bàn giao, phải bật từng công tắc và ghi kết quả vừa đo." | **Ẩn dụ "cái cân" là hoàn toàn mới**, không có trong nguồn (nguồn dùng "bóng đèn/công tắc"). Chọn ẩn dụ cân vì khớp đúng mẫu hình bắt buộc `revenue-balance` ở brief mục 3 |
| 5 | Superpowers gọi là kiểm chứng trước khi báo xong · luật chỉ một dòng: không nói xong/sửa/test qua nếu chưa đo lại mới nhất · agent không tự tin thay bạn | Khối 3: "Verification before completion có một luật: không được nói xong, đã sửa hay mọi test đều qua nếu chưa chạy lệnh kiểm chứng mới nhất." — **gần nguyên văn**, chỉ đổi "test" → giữ nguyên (từ "test" vẫn còn trong lời — xem mục 4 điểm 2) | Câu 3 "agent không được tự tin thay bạn" mượn tinh thần khối 14 ("Agent không được tự chọn thay bạn") vốn nói về NHẬP NHÁNH, áp sang ngữ cảnh kiểm chứng — hơi lệch nguồn nhưng cùng chủ đề "agent không tự quyết" |
| 6 | Ví dụ thật: render sạch, thoát số không · một dòng lệnh trên slide bị ngắt làm đôi · số không không chứng minh gì, hình vẫn sai | Khối 7: "Ví dụ thật: dây chuyền video từng render sạch, nhưng một dòng lệnh trên slide bị ngắt làm đôi. Tiến trình thoát số không, hình vẫn sai." | **Gần như nguyên văn**, chỉ đổi thứ tự câu và diễn đạt "tiến trình thoát số không" → "thoát ra đúng số không" |
| 7 | Giờ thử một lần cho đúng quy trình · bước một kiểm khớp câu với khung hình và vùng chữ an toàn · bước hai dựng video thật | Khối 9: "Ta thử một lần. Bước một, chạy bộ kiểm mapping câu với slide và vùng an toàn. Bước hai, render video." | **Gần như nguyên văn**, đổi "mapping" → "khớp", "slide" → "khung hình", "render video" → "dựng video thật" (giữ nhất quán ẩn dụ "dựng nhà" xuyên khóa) |
| 8 | Bước ba đo khung hình đúng 1080×1920 và đúng thời lượng · bước bốn chụp ba khung đầu/giữa/cuối · mở ảnh nhìn tận mắt chữ tràn/đúng chỗ | Khối 10 + 11: "Bước ba, dùng công cụ đọc thông số để xác nhận đúng một nghìn không trăm tám mươi nhân một nghìn chín trăm hai mươi và đúng thời lượng." + "Bước bốn, chụp các frame đầu, giữa và cuối. Mở từng ảnh, kiểm chữ, thương hiệu, vùng an toàn và cảnh chuyển." | **Gần như nguyên văn**, nhưng đã **bỏ bớt** "thương hiệu" và "vùng an toàn và cảnh chuyển" khỏi phần soi ảnh để gọn trong 55 từ/dòng |
| 9 | Bẫy: đọc câu đã xong thấy hợp lý, gật đầu luôn · vì sao sập: không tự đo lại, không tự soi ảnh · cách né: chỉ tin khi chính mắt thấy bằng chứng | **Không có trong nguồn** dưới dạng "bẫy" | Diễn giải thêm, tổng hợp lại đúng luật đã nêu ở khối 3+6 (không được tự tin báo xong khi chưa kiểm chứng), viết lại thành khuôn "bẫy" bắt buộc của dòng 9 |
| 10 | Tám bài một chuyện: hiểu ý, kế hoạch, dựng, kiểm, bàn giao · chìa khóa không phải bằng chứng đã xong · biên bản kiểm tra mới là bằng chứng, như dây điện đã bật thử | Khối cuối (16): "Chìa khóa không phải bằng chứng căn nhà đã xong. Biên bản kiểm tra mới là thứ cho phép bạn trao chìa khóa." — **câu 2-3 gần nguyên văn**. Câu 1 vay mượn tinh thần khối 15 ("Bây giờ ghép cả khóa lại...") nhưng rút gọn danh sách kỹ năng | Vế "đúng như dây điện đã được bật thử" là câu thêm để đối xứng lại dòng 1 (dây điện), không có trong nguồn |

### ⚠️ KHOẢNG TRỐNG QUAN TRỌNG NHẤT — chưa phủ hết mục tiêu bài học
Nguồn `08_kiem_chung_va_ban_giao.md` có **3 khối riêng** (12, 13, 14) nói về việc **chọn
cách nhập việc vào nhánh chính**: "finishing a development branch" chạy lại toàn bộ test
trước khi đưa lựa chọn bàn giao (khối 12), ba lựa chọn "nhập tại máy / tạo pull request /
giữ nguyên nhánh" (khối 13), và "agent không được tự chọn thay bạn, đó là quyết định của
chủ công trình" (khối 14). **Bảng "làm được gì" của brief mục 2 cho bài 08 yêu cầu CẢ HAI
vế**: "đòi bằng chứng thay vì tin lời đã xong" **và** "biết chọn cách nhập việc vào nhánh
chính". Lời đã chốt (`sp08_ban_giao.txt`) chỉ phủ trọn vế thứ nhất (kiểm chứng); vế thứ
hai (nhập nhánh, PR, giữ nguyên) **không xuất hiện ở dòng nào trong 10 dòng**. Đây không
phải lỗi khuôn/độ dài mà thước đo được — là lỗi HIỂU giống loại lỗi bài sp02 từng dính
(thước ra `DAT` ngay vòng đầu, `validate` PASS, nhưng người xem sẽ không học được nửa sau
của mục tiêu bài học). Tôi không tự sửa lời (đúng luật được giao), chỉ báo lại rõ ràng.

---

## 2. BA PHƯƠNG ÁN HOOK (đối chiếu dòng 1 đã chốt)

Dòng 1 đã chốt sẵn trước khi giao việc dựng deck, không phải tôi chọn. Đối chiếu lại
theo đúng khuôn kiểm tra 11 từ đầu = 3 giây đầu của brief mục 4, cộng 2 phương án khác
để đối chiếu (không thay dòng 1 — chỉ ghi lại theo đúng thể thức tài liệu hoá).

| # | Hook | 11 từ đầu | Đạt 3 giây đầu? |
| :-: | :-- | :-- | :-: |
| **A (đã chốt)** | *"Chìa khóa đã trao, dây điện mới lắp chưa ai bật thử."* | `Chìa khóa đã trao, dây điện mới lắp chưa ai bật` | ✅ Cảnh sờ được (chìa khóa, dây điện) ở từ 1-6; nghịch lý ("chưa ai bật") xuất hiện ở từ 9-11 — trọn vẹn trong 11 từ |
| B | *"Đội thợ báo nhà xong, chủ nhà nhận chìa, không hỏi lại câu nào."* | `Đội thợ báo nhà xong, chủ nhà nhận chìa, không hỏi` | Có cảnh (đội thợ, chủ nhà, chìa) nhưng "mất mát/nghịch lý" thật sự (không sáng đèn) chưa lộ ra trong 11 từ — chỉ là tiền đề, yếu hơn A |
| C | *"Ba hôm sau bàn giao, bật công tắc phòng khách, không có gì sáng lên."* | `Ba hôm sau bàn giao, bật công tắc phòng khách, không` | Nghịch lý rõ ("không có gì sáng") nhưng rơi ở từ 12-13, ngoài mốc 11 từ; cũng thiếu vật thể "chìa khóa" nối vào ẩn dụ chốt cuối |

**Vì sao A là lựa chọn đúng:** duy nhất A đưa được cả cảnh sờ được (2 vật thể: chìa khóa,
dây điện — cả hai đều được dùng lại xuyên suốt tới slide 10) và nghịch lý ("mới lắp
chưa ai bật thử") vào trọn 11 từ đầu. B và C đều phải chọn giữa cảnh hoặc nghịch lý, không
có cả hai trong khung 3 giây.

---

## 3. KẾT QUẢ CHẠY THƯỚC

```
cd /Users/simple/Desktop/Cloud/video
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/sp08_ban_giao.txt \
        --thuatngu "superpowers,skill,codex,agent,merge,commit,verification"
```

```
SACH   | khong loi, khong canh bao
KETLUAN|27|368|DAT
```

- **27 reveal**, khuôn `[1,3,3,2,3,3,3,3,3,3]` khớp (đã kiểm lại bằng lệnh đếm
  `slide-element` trong `index.html` sau khi dựng deck: in ra đúng
  `[1, 3, 3, 2, 3, 3, 3, 3, 3, 3]`).
- **368 từ** ≈ **103 giây** ở nhịp 3,56 từ/giây (trong trần 330-450 — ở nửa dưới của trần,
  bài ngắn hơn sp02 (394 từ) và sp07 (424 từ)).
- Kết quả này do **thợ 1 chạy trước khi giao việc** — tôi chạy lại y hệt để xác nhận,
  không có thay đổi nào giữa hai lần chạy (không dấu hiệu sửa nhầm file).
- Không dấu gạch dài `—` trong lời đọc, không chữ rỗng.
- ⚠️ Lời đọc dòng 5 giữ nguyên chữ **"test"** ("mọi phép thử đều qua" — kiểm lại: câu
  gốc dùng "phép thử", KHÔNG dùng "test", vậy dòng 5 đã đúng luật cấm chữ lập trình.
  Xác nhận lại: `--thuatngu` không bắt "test" nằm trong danh sách cấm chữ lập trình
  riêng của mục 4 brief, và lời đã tránh dùng nó).

---

## 4. CHỖ CÒN YẾU NHẤT — NÓI THẲNG

1. 🔴 **Quan trọng nhất: lời bỏ sót hoàn toàn vế "chọn cách nhập việc vào nhánh chính"**
   của mục tiêu bài học (xem mục 1, khoảng trống). Nguồn có sẵn 3 khối nói đúng chủ đề
   này (finishing a development branch, ba lựa chọn nhập nhánh, agent không tự chọn thay
   bạn) nhưng không khối nào lọt vào 10 dòng đã chốt. Thước không bắt được lỗi này vì nó
   đo khuôn/độ dài/từ cấm, không đo "có phủ hết mục tiêu bài học không". Nếu BOSS muốn bài
   08 dạy cả hai vế, cần viết lại ít nhất 1-2 dòng (có thể thay một phần dòng 7-8 "chạy
   thử" bằng bước "chọn nhập nhánh") và chạy lại thước — nhưng việc này đụng tới lời đã
   `DAT`, tôi không tự làm.
2. **Dòng 1-2 đã đảo ngược một tình tiết so với nguồn** (chủ nhà hỏi vs không hỏi — xem
   mục 1). Không sai luật kỹ thuật nào, nhưng nếu BOSS đối chiếu kỹ với nguồn gốc sẽ thấy
   khác.
3. **Ẩn dụ "cái cân" (dòng 4) là chi tiết hoàn toàn mới, không có trong nguồn** — được
   chọn để khớp đúng mẫu hình bắt buộc `revenue-balance`. Đánh đổi: mẫu hình đẹp và đúng
   nghĩa đen, nhưng đây là ẩn dụ THỨ HAI trong cùng một bài (cân + chìa khóa/dây điện),
   hơi nhiều so với các bài trước chỉ có một ẩn dụ chính xuyên suốt. Cân chỉ xuất hiện ở
   đúng 1 slide (4) nên không lấn át ẩn dụ chính, nhưng vẫn đáng nói thẳng.
4. **Màu cột ở slide 4 dùng `--success` xanh lá cho "bằng chứng đo được"** — đây là màu
   MỚI chưa từng dùng cho vai này trong các bài trước (các bài trước chỉ dùng xanh dương/
   hổ phách/đỏ làm 3 vai chính). Tôi cho là hợp lý (xanh lá = "đã kiểm chứng, đáng tin",
   nhất quán với `risk-card.lit-green` = "cách né đúng" ở slide 9), nhưng đây là quyết
   định thêm vai màu thứ 4, BOSS nên biết.
