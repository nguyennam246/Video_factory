# MÀN HÌNH — sp08_ban_giao (Bài 08 khoá Superpowers)

Khuôn `[1,3,3,2,3,3,3,3,3,3]` = 27 reveal. Mỗi câu lời = 1 reveal.
Ẩn dụ xuyên khoá: **xây một căn nhà** — bài này khép lại bằng **chìa khóa và dây điện
trong nhà mới xây** (bàn giao, kiểm tra trước khi trao chìa).
Vật thể chủ đạo bài này: **chìa khóa**, **công tắc/dây điện**, **cái cân** (mẫu hình mới).
2 mẫu hình MỚI bắt buộc dùng theo brief mục 3: `revenue-balance` (slide 4) và
`glowing-conclusion` (slide 10, KẾ THỪA nguyên khối từ `deck_sp02` — không phải mẫu mới
với riêng bài này, nhưng là mẫu hình chốt của cả khóa).

| Slide | Lời đọc (rút gọn) | Chữ lên màn hình | Hình gì chuyển động |
| :-: | :-- | :-- | :-- |
| 1 | Chìa khóa đã trao, dây điện mới lắp chưa ai bật thử | `Dây điện câm` / `Superpowers, bài 08` | Hero orbit: lõi giữa là chìa khóa xanh, bốn chip bay quanh bật lần lượt `hiểu ý` → `kế hoạch` → `thi công` → `kiểm chứng` (tóm tắt cả 8 bài trước). Dòng thống kê dưới: "chìa đã trao" / "0 công tắc bật thử". |
| 2 | Đến ngày bàn giao, đội thợ báo nhà đã xong · chủ nhà gật đầu nhận chìa · ba hôm sau bật công tắc, không có gì sáng lên | `ĐỘI THỢ` · `CHỦ NHÀ` · `BA HÔM SAU` | Ba ô lưới (tái dùng `workflow-grid` như slide 2 bài 02): "báo: nhà đã xong" → "gật đầu, nhận chìa khóa" → "bật công tắc, không sáng". Reveal 2: dải packet chạy qua ba nhãn "đã xong → gật đầu nhận → không sáng", thể hiện lời tuyên bố trôi thẳng tới thất bại mà không ai chặn lại. Reveal 3: khung ghi chú "không ai bật công tắc trước khi trao chìa khóa". |
| 3 | Lỗi không ở tay nghề thợ điện · dây đấu đúng, ổ cắm lắp chuẩn · lỗi ở chỗ không ai bật thử trước khi trao chìa | `tại thợ điện kém?` (gạch) · `dây đấu đúng, ổ cắm lắp chuẩn` · `không ai bật thử trước khi trao chìa` | Reveal 1: nhãn "tại thợ điện kém?" bị gạch đỏ ngang qua (tái dùng `flow-old`/`flow-strike`). Reveal 2: proof-chip bật sáng "vẫn đấu đúng, vẫn lắp chuẩn". Reveal 3: khung `flow-new` phát sáng hổ phách (KHÔNG xanh lá — đây là nguyên nhân thật, một điều cần chú ý chứ không phải một điều đáng khen) nêu đúng chỗ lỗi. |
| 4 | Đặt câu "đã xong" lên một cái cân, bên kia đặt kết quả vừa đo được · cân nghiêng về bên nào, sự thật nằm ở bên đó | `ĐẶT LÊN CÂN` · `LỜI — ĐÃ XONG — ?` · `SỐ — ĐO ĐƯỢC — ✓` · `lời nói NHẸ CÂN / bằng chứng NẶNG CÂN` | Reveal 1 — ⭐ mẫu MỚI `revenue-balance`: thanh cân hiện ra, hai cột hiện song song. Cột trái (xám, icon bong bóng lời nói) thấp — "LỜI, ĐÃ XONG, dấu hỏi, chưa đo". Cột phải (xanh lá, icon thước đo) cao gần gấp đôi — "SỐ, ĐO ĐƯỢC, dấu tích, vừa đo". Cột phải cao hẳn lên = bằng chứng nặng cân hơn lời nói suông. Reveal 2: dải phán quyết full-width bật sáng "lời nói NHẸ CÂN ⚖ bằng chứng NẶNG CÂN". |
| 5 | Superpowers gọi quy trình này là kiểm chứng trước khi báo xong · luật chỉ một dòng: không nói xong/sửa/test qua nếu chưa đo lại mới nhất · agent không được tự tin thay bạn | `KIỂM CHỨNG` · `không nói đã xong, đã sửa` · `nếu chưa đo lại mới nhất` · `agent phải đưa bằng chứng ra trước` | Reveal 1: tên kỹ thuật "KIỂM CHỨNG" bật sáng dạng huy hiệu, phụ đề "trước khi báo đã xong". Reveal 2: khối luật (tái dùng `sg-verify`) bật 2 chip nêu đúng luật một dòng. Reveal 3: khung ghi chú "agent phải đưa bằng chứng ra trước, không tự tin thay bạn". |
| 6 | Ví dụ thật dự án video này: render sạch, thoát số không · nhưng một dòng lệnh trên slide bị ngắt làm đôi · số không đó không chứng minh gì, hình vẫn sai | `ví dụ thật — dự án video này` · `render_headless.py / exit code 0` · `một dòng lệnh bị ngắt làm đôi` · `số không KHÔNG chứng minh gì` | Reveal 1 — mock-terminal: gõ ra `render_headless.py` rồi `exit code 0` màu xanh (trông như thành công). Reveal 2: proof-chip cảnh báo hổ phách "một dòng lệnh trên slide bị ngắt làm đôi" — mâu thuẫn với vẻ thành công vừa thấy. Reveal 3: khung ghi chú cảnh báo "số không đó không chứng minh gì, hình vẫn sai". |
| 7 | Giờ thử một lần cho đúng quy trình · bước một chạy phép kiểm khớp câu với khung hình và vùng chữ an toàn · bước hai dựng video thật | `GIỜ THỬ MỘT LẦN` · `BƯỚC 1 — kiểm cấu trúc` · `BƯỚC 2 — dựng video thật` | Reveal 1: tiêu đề mở màn "cho đúng quy trình" + phụ đề "đi từng bước, không nhảy cóc". Reveal 2: thẻ số 1 (tái dùng `sc-file`) "kiểm cấu trúc — khớp từng câu với khung hình và vùng chữ an toàn". Reveal 3: thẻ số 2 "dựng video thật — render từ lời đọc và deck vừa kiểm". |
| 8 | Bước ba đo lại khung hình, đúng 1080×1920 và đúng thời lượng · bước bốn chụp ba khung đầu/giữa/cuối · mở từng ảnh, nhìn tận mắt chữ có tràn không | `BƯỚC 3 — đo lại khung hình` · `1080 × 1920 — đúng thời lượng` · `BƯỚC 4 — chụp ba khung` · `mở ảnh và SOI` | Reveal 1 — mock-terminal: `ffprobe output.mp4` → kết quả xanh "1080 × 1920 đúng thời lượng". Reveal 2: proof-chip "BƯỚC 4 — chụp ba khung: đầu · giữa · cuối". Reveal 3: khung ghi chú "mở từng ảnh, nhìn tận mắt chữ có tràn không, có đúng chỗ không". |
| 9 | Bẫy: đọc câu đã xong thấy hợp lý, gật đầu luôn · vì sao sập: không tự đo lại, không tự soi ảnh · cách né: chỉ tin khi chính mắt thấy bằng chứng | `"đã xong" — hợp lý — gật đầu luôn` · `không đo lại · không soi ảnh` · `chỉ tin khi CHÍNH MẮT thấy` | Ba thẻ rủi ro bật lần lượt (`risk-cards-container`): thẻ đỏ (bẫy: tin lời nói suông), thẻ vàng (vì sao: không tự kiểm), thẻ xanh (cách né: chỉ tin bằng chứng tận mắt). Đúng mạch màu: đỏ = phải tránh, xanh = nên làm. |
| 10 | Tám bài một chuyện: hiểu ý, kế hoạch, dựng, kiểm, bàn giao · chìa khóa không phải bằng chứng đã xong · biên bản kiểm tra mới là bằng chứng, như dây điện đã bật thử | `Tám bài, một chuyện` · `hiểu ý → kế hoạch → dựng → kiểm → bàn giao` · `CHÌA KHÓA — không phải bằng chứng` · `BIÊN BẢN — mới là BẰNG CHỨNG` | Dội lại đúng bố cục slide 1 (glowing-conclusion kế thừa từ `deck_sp02`). Reveal 1: icon-badge chìa khóa (cùng icon slide 1, giờ đặt trong khung phát sáng — "đã kiểm chứng xong thật") + dòng tóm tắt 8 bài. Reveal 2: split-panel "CHÌA KHÓA / không phải bằng chứng đã xong" cạnh icon chìa khóa nhỏ. Reveal 3: khung chốt cuối "biên bản kiểm tra mới là bằng chứng, đúng như dây điện đã được bật thử" — icon ổ cắm có dấu tích, callback đúng vật thể "dây điện" của slide 1. |

## GHI CHÚ CHO NGƯỜI DỰNG DECK
- **Vật thể phải giữ nguyên xuyên bài:** chìa khóa, công tắc/dây điện. Slide 10 phải nhìn
  ra ngay là slide 1 quay lại (cùng icon chìa khóa, cùng khung), nếu không câu chốt mất
  tác dụng — đã dùng đúng kỹ thuật này (xem bài 07 làm mẫu với vòi nước/kính lúp).
- **Slide 1 tuyệt đối không có chữ tiếng Anh/thuật ngữ lập trình nào.** Tên kỹ thuật đầu
  tiên ("Kiểm Chứng") chỉ xuất hiện ở slide 5.
- **Slide 4 dùng `revenue-balance` (mẫu MỚI, lần đầu trong cả dự án ngoài slide gốc của
  gallery)** — CSS gốc (`vpg-revenue-balance`, `.balance-beam`, `.revenue-column`,
  `.column-fill`, `.revenue-verdict`…) KHÔNG có sẵn trong `deck_sp02/style.css`, phải chép
  từ `template/visual-pattern-gallery/style.css` (dòng ~6156-6338), đặt CUỐI file.
  ⚠️ Mẫu gốc dùng 4 `.slide-element` (title+beam / cột A / cột B / verdict) nhưng khuôn
  dòng 4 của bài này chỉ có **2 câu = 2 reveal** ⇒ phải nén: reveal 1 gộp
  title+beam+cả 2 cột trong MỘT `.slide-element` (grid nội bộ tự khai báo lại), reveal 2
  là verdict. **Bẫy đã dính khi dựng lần đầu:** nếu không ép `grid-column: 1 / 3` cho CẢ
  HAI `.slide-element` con ở khung ngoài, verdict (reveal 2) bị lưới 2 cột của
  `.vpg-revenue-balance` đẩy lệch sang phải, nằm cùng hàng với cột dữ liệu thay vì nằm
  full-width bên dưới. `validate` vẫn PASS vì đó là lỗi bố cục thị giác, không phải lỗi
  an toàn khung — chỉ soi ảnh mới thấy. Đã vá bằng cách set `grid-column: 1 / 3` cho cả
  `:nth-child(1)` và `:nth-child(2)` của `.sp08-balance`.
- **Màu cột KHÔNG dùng alex-cyan/alex-pink gốc của gallery** (đó là màu cho ví dụ tài
  chính). Đổi thành: cột "LỜI, đã xong" → xám trung tính (`rgba(203,213,225,.92)`, chưa
  kiểm chứng, KHÔNG phải "xấu" nên không dùng đỏ); cột "SỐ, đo được" → `var(--success)`
  xanh lá (đã kiểm chứng, đáng tin). Cả hai đều nằm trong palette gốc của deck (root đã
  có sẵn biến `--success`), không cần thêm màu ngoài palette `sp`.
- **Slide 3 dùng `flow-new` cho câu nêu NGUYÊN NHÂN THẬT** ("không ai bật thử trước khi
  trao chìa") — patch màu hổ phách kế thừa từ `deck_sp02` (`.sp-flow-two .flow-node.flow-new`)
  áp dụng đúng ở đây vì đây cũng là "nguyên nhân gây lỗi", không phải trạng thái mới tốt.
  Không cần vá gì thêm, patch cũ tự động đúng nghĩa cho nội dung mới.
- Màu vai: xanh dương = brand/trung tính, hổ phách = chỗ cần chú ý (nguyên nhân, cảnh
  báo nhẹ), xanh lá (`--success`) = đã kiểm chứng/đáng tin (CHỈ dùng ở slide 4 cho mẫu
  cân), đỏ = điều phải tránh (slide 9 thẻ bẫy). Giữ nhất quán cả bài.
- ⚠️ Slide 6 và 8 đều dùng `mock-terminal` — không liền kề nhau (cách bởi slide 7 dùng
  `sc-file`), nên không phạm luật "hai slide liền nhau không cùng dạng hộp".
