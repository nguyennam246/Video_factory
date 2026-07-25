TIÊU ĐỀ: Thi công và review — làm xong một phòng, nghiệm thu một phòng
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Một đội xây cùng lúc tám căn phòng. Cuối tháng mới kiểm. Lúc đó mới phát hiện mọi ổ điện đều đặt cao sai mười phân.
CHỮ: xây 8 phòng
CHỮ*: cuối tháng mới kiểm
---
LỜI: Một sai lệch nhỏ đã được nhân lên tám lần. Sửa không còn là dời một ổ điện, mà là đục lại cả dãy tường.
CHỮ: sai 1 lần
CHỮ*: nhân lên × 8
---
LỜI: Superpowers ưu tiên làm xong một nhiệm vụ nhỏ, review nó, rồi mới chuyển sang nhiệm vụ kế tiếp.
CHỮ: làm 1 nhiệm vụ
CHỮ*: review rồi mới đi tiếp
---
LỜI: Với subagent driven development, mỗi nhiệm vụ được giao cho một agent mới, chỉ mang theo phiếu việc và những giao diện cần biết.
CHỮ*: MỖI VIỆC — MỘT AGENT MỚI
CHỮ: ngữ cảnh vừa đủ
---
LỜI: Agent đó viết test, làm mã, chạy kiểm tra, commit và tự xem lại. Nhưng tự xem lại chưa thay cho người nghiệm thu.
CHỮ: làm · test · commit
CHỮ*: vẫn cần review độc lập
---
LỜI: Review có hai cổng theo thứ tự. Cổng một hỏi: có làm đúng bản thiết kế không? Cổng hai hỏi: cách làm có sạch, an toàn và dễ bảo trì không?
CHỮ: cổng 1 — ĐÚNG YÊU CẦU?
CHỮ*: cổng 2 — CHẤT LƯỢNG TỐT?
---
LỜI: Hai câu này khác nhau. Một căn phòng có thể đúng ba cửa sổ như bản vẽ, nhưng dây điện đi ẩu. Hoặc xây rất đẹp nhưng chỉ có hai cửa sổ.
CHỮ: đúng yêu cầu nhưng làm ẩu
CHỮ*: làm đẹp nhưng SAI yêu cầu
---
LỜI: Lỗi nghiêm trọng và lỗi quan trọng phải sửa trước khi đi tiếp. Lỗi nhỏ được ghi lại để đợt review toàn nhánh quyết định.
CHỮ: Critical · Important → sửa
CHỮ*: Minor → ghi sổ
---
LỜI: Ví dụ thật: bài video mẫu có ba yêu cầu đã chốt. Thương hiệu là dungladu chấm vi, giọng Nam Minh nhanh mười bốn phần trăm, và màu chính là tím Stripe.
MÃ: dungladu.vn
MÃ: NamMinhNeural +14%
MÃ: #635bff
---
LỜI: Review cổng một kiểm đủ ba điều ấy trên sản phẩm. Chỉ thấy video đẹp không có nghĩa là đúng đơn đặt hàng.
CHỮ: đẹp mắt
CHỮ*: chưa chắc ĐÚNG ĐƠN
---
LỜI: Review cổng hai mới xem chữ có lọt vùng an toàn không, ánh xạ câu với slide có một đối một không, và mã có lặp khó sửa không.
CHỮ: vùng an toàn
CHỮ: câu ↔ slide 1:1
CHỮ*: chất lượng bên trong
---
LỜI: Ta đi qua bốn bước. Một, giao đúng một phiếu việc. Hai, agent làm và đưa bằng chứng. Ba, reviewer kiểm yêu cầu rồi chất lượng. Bốn, sửa sạch mới đánh dấu hoàn tất.
CHỮ: 1 — giao
CHỮ: 2 — làm
CHỮ: 3 — review
CHỮ*: 4 — sửa sạch
---
LỜI: Khi cả kế hoạch xong, cần thêm một lượt review toàn nhánh. Nó tìm những lỗi chỉ lộ ra khi các phòng nối với nhau.
CHỮ: review từng nhiệm vụ
CHỮ*: rồi review TOÀN NHÁNH
---
LỜI: Bẫy là giao nhiều agent cùng sửa các file chồng lên nhau. Nhanh trên đồng hồ, nhưng đổi lại là xung đột và ngữ cảnh rối.
CHỮ: nhiều agent · cùng một chỗ
CHỮ*: nhanh giả, rối thật
---
LỜI: Nghiệm thu sớm không làm chậm công trình. Nó ngăn một lỗi nhỏ trở thành tám bức tường phải đục lại.
CHỮ: review SỚM
CHỮ*: để khỏi sửa LỚN

