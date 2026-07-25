TIÊU ĐỀ: Worktree và kế hoạch — chia khu rồi mới giao việc
GIỌNG: edge:vi-VN-NamMinhNeural:+14%
NGHỈ: 0.9
---
LỜI: Một căn nhà đang ở vẫn cần sửa. Nếu thợ đập ngay giữa phòng khách, bụi và vật liệu sẽ trộn vào cuộc sống đang chạy.
CHỮ: nhà vẫn đang dùng
CHỮ*: thợ sửa ngay giữa phòng khách
---
LỜI: Cách an toàn là quây riêng một khu thi công, kiểm tra nền cũ còn tốt, rồi mới mang đồ nghề vào.
CHỮ: quây khu riêng
CHỮ: kiểm tra nền cũ
CHỮ*: rồi mới thi công
---
LỜI: Trong Git, worktree là khu thi công riêng. Nó cho một nhánh có thư mục làm việc độc lập mà không làm bẩn chỗ đang dùng.
CHỮ*: WORKTREE = KHU THI CÔNG RIÊNG
CHỮ: nhánh riêng · thư mục riêng
---
LỜI: Skill using git worktrees luôn kiểm tra trước xem bạn đã ở khu riêng chưa. Có công cụ worktree của nền tảng thì dùng công cụ đó trước.
CHỮ: kiểm tra nơi đang đứng
CHỮ*: ưu tiên công cụ của nền tảng
---
LỜI: Sau khi tạo khu riêng, nó cài phụ thuộc phù hợp và chạy bộ test gốc. Nếu test đã đỏ từ đầu, phải báo lại trước khi xây tiếp.
CHỮ: cài phụ thuộc
CHỮ: chạy test nền
CHỮ*: nền đỏ thì DỪNG hỏi
---
LỜI: Nhưng có khu riêng vẫn chưa đủ. Đội thợ cần một phiếu việc đủ chi tiết để người chưa từng thấy căn nhà cũng làm đúng.
CHỮ: khu riêng ≠ biết phải làm gì
CHỮ*: cần PHIẾU VIỆC
---
LỜI: Writing plans biến bản thiết kế đã duyệt thành các nhiệm vụ nhỏ. Mỗi nhiệm vụ ghi đúng file, giao diện, phép thử, lệnh chạy và kết quả mong đợi.
CHỮ*: WRITING PLANS
CHỮ: file · test · lệnh · kết quả
---
LỜI: Mỗi bước chỉ nên là một hành động dài khoảng hai đến năm phút: viết test thất bại, chạy để thấy đỏ, viết phần tối thiểu, chạy lại, rồi commit.
CHỮ: mỗi bước 2–5 phút
CHỮ*: một bước = một hành động
---
LỜI: Kế hoạch tốt không có câu kiểu thêm xử lý lỗi phù hợp. Nó phải nói lỗi nào, đầu vào nào, thông báo nào và test nào chứng minh.
CHỮ: "xử lý lỗi phù hợp"
CHỮ*: quá mơ hồ
---
LỜI: Ví dụ thật: thêm kiểm tra kịch bản video. Nhiệm vụ một có thể là phát hiện cảnh thiếu dòng lời.
CHỮ: việc thật
MÃ: kiểm tra cảnh thiếu LỜI:
---
LỜI: Bước một, tạo một file mẫu có ba cảnh, trong đó cảnh hai thiếu lời. Bước hai, chạy trình kiểm tra và đòi nó thất bại đúng ở cảnh hai.
CHỮ: mẫu có 3 cảnh
CHỮ*: cảnh 2 thiếu LỜI
---
LỜI: Bước ba, viết phần đọc file tối thiểu. Bước bốn, chạy lại thấy một lỗi đúng như yêu cầu. Bước năm, commit riêng nhiệm vụ đó.
CHỮ: viết tối thiểu
CHỮ: chạy lại
CHỮ*: commit riêng
---
LỜI: Đó là mức chi tiết để một người thợ mới nhận phiếu vẫn biết chạm file nào và chứng minh ra sao.
CHỮ: người mới vẫn làm được
CHỮ*: vì phiếu không để chỗ đoán
---
LỜI: Bẫy thứ nhất là tạo worktree mà không kiểm tra test nền. Bẫy thứ hai là viết kế hoạch chỉ có tiêu đề lớn, không có bằng chứng cho từng bước.
CHỮ: bẫy 1 — không test nền
CHỮ*: bẫy 2 — kế hoạch mơ hồ
---
LỜI: Khu riêng giữ công trường sạch. Kế hoạch rõ giữ người thợ đi đúng. Cần cả hai trước khi thi công.
CHỮ: worktree giữ chỗ SẠCH
CHỮ*: plan giữ việc ĐÚNG

