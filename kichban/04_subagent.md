TIÊU ĐỀ: Subagent — sai người đi, chỉ nhận về kết luận
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Bạn nhờ AI một việc: lục hai trăm hồ sơ, tìm xem cái nào thiếu chữ ký.
CHỮ: lục 200 hồ sơ
CHỮ*: tìm cái nào thiếu chữ ký
---
LỜI: Nó làm được. Nhưng để làm, nó phải đọc hết hai trăm hồ sơ.
CHỮ*: phải ĐỌC HẾT 200
---
LỜI: Và đây là chỗ ít người biết. Hai trăm hồ sơ đó nằm lại trong đầu nó, tới hết buổi làm việc.
CHỮ*: 200 hồ sơ NẰM LẠI trong đầu
CHỮ: tới hết buổi
---
LỜI: Mà AI không có trí nhớ. Mỗi lần bạn hỏi thêm một câu, toàn bộ những gì đã đọc được gửi lại từ đầu.
CHỮ: mỗi câu hỏi mới
CHỮ*: gửi lại TẤT CẢ từ đầu
---
LỜI: Bạn hỏi thêm mười câu nữa, là bạn trả tiền cho hai trăm hồ sơ đó mười lần.
CHỮ: hỏi thêm 10 câu
CHỮ*: trả tiền cho 200 hồ sơ × 10
---
LỜI: Giải pháp giống hệt ngoài đời. Bạn không tự lục kho. Bạn sai một người vào kho.
CHỮ: bạn KHÔNG tự lục kho
CHỮ*: sai một người vào
---
LỜI: Người đó lục trong kho, bụi bặm ở lại trong kho. Ra ngoài, anh ta chỉ đưa bạn một tờ giấy: ba hồ sơ này thiếu chữ ký.
CHỮ: bụi ở lại trong kho
CHỮ*: ra ngoài: một tờ giấy kết luận
---
LỜI: Cái người được sai đi đó gọi là subagent. Nó là một phiên làm việc con, có cái đầu riêng.
CHỮ*: SUBAGENT = phiên con
CHỮ: có cái đầu riêng
---
LỜI: Cách tạo: một file khai trong thư mục tác nhân. Khai ba thứ. Tên nó. Khi nào thì gọi nó. Và nó được cầm những công cụ gì.
MÃ: .claude/agents/tho-thi-cong.md
CHỮ: ① tên  ② khi nào gọi  ③ cầm được gì
---
LỜI: Cái thứ ba quan trọng. Người sai đi lục kho thì chỉ cần quyền đọc. Đừng đưa cho anh ta quyền xoá.
CHỮ*: chỉ đưa quyền vừa đủ
CHỮ: đi đọc thì đừng đưa quyền xoá
---
LỜI: Trong dự án của tôi có hai người như vậy. Một anh thợ chuyên chạy việc tay chân. Một anh chuyên đi tra web đối chứng.
MÃ: tho-thi-cong — việc tay chân
MÃ: doi-chung-web — tra web đối chứng
---
LỜI: Nhưng đây là mặt trái, và nhiều người bỏ qua. Người được sai đi bắt đầu từ con số không. Anh ta chưa biết gì về dự án.
CHỮ*: phiên con bắt đầu từ SỐ 0
CHỮ: chưa biết gì về dự án
---
LỜI: Nên trước khi làm, anh ta phải đọc lại bối cảnh mà bạn đã nắm sẵn trong đầu. Đó cũng là thời gian, cũng là tiền.
CHỮ: phải đọc lại bối cảnh
CHỮ*: cũng là tiền
---
LỜI: Từ đó ra một luật rất gọn. Việc chỉ đụng một hai file thì tự làm rẻ hơn. Sai người đi cho việc vặt là lỗ.
CHỮ: 1-2 file → TỰ LÀM
CHỮ*: sai người đi cho việc vặt = lỗ
---
LỜI: Chỉ sai người đi khi việc vừa nặng, vừa máy móc. Nghĩa là bạn nói ra được rõ ràng phải làm gì, từng bước một.
CHỮ: nặng + máy móc
CHỮ*: nói rõ được từng bước
---
LỜI: Và một điều kiện nữa, đây là điều kiện tôi coi là bắt buộc. Phải có cách kiểm tra kết quả mà không cần hỏi lại AI.
CHỮ*: phải có CÁCH KIỂM TRA
CHỮ: kiểm được mà không cần hỏi AI
---
LỜI: Ví dụ: chạy lại bộ kiểm thử. So sánh hai file. Đếm số dòng. Những thứ máy tự trả lời đúng sai, không cần ai phán.
CHỮ: chạy lại bộ kiểm thử
CHỮ: so sánh hai file · đếm dòng
CHỮ*: máy tự trả lời đúng/sai
---
LỜI: Cuối cùng, đừng tin bản báo cáo. Người được sai đi lúc nào cũng báo là xong. Bạn phải tự chạy lại phép kiểm tra đó một lần.
CHỮ*: ĐỪNG tin báo cáo
CHỮ: tự chạy lại phép kiểm tra
---
LỜI: Sai người đi không phải để làm nhanh hơn. Là để cái đầu của bạn còn chỗ mà nghĩ.
CHỮ: Không phải để nhanh hơn.
CHỮ*: Để đầu còn chỗ mà nghĩ.
