# README — sp04_worktree (Bài 04 khoá Superpowers)

Người xem xong phải làm được: **tách việc mới ra chỗ riêng để không đụng việc đang chạy; nhìn
một bản kế hoạch biết nó chia mấy hạng mục, thứ tự nào** (bảng mục 2 của brief).

| File | Vai |
| :-- | :-- |
| `sp04_worktree.txt` | Lời đọc, đúng 10 dòng — **do thợ 1 viết ở phiên trước, đã đạt thước** |
| `sp04_worktree.man_hinh.md` | Chữ + chuyển động từng slide |
| `README_sp04_worktree.md` | File này: truy vết, hook, kết quả thước |

⚠️ Lời (`sp04_worktree.txt`) đã có sẵn trên đĩa trước khi tôi vào việc, thợ 1 báo đã chạy thước
ra `KETLUAN|27|444|DAT`. **Tôi không sửa lời** — chỉ chạy lại thước để xác nhận, rồi dựng deck.

---

## 1. TRUY VẾT TỪNG CHI TIẾT

Nguồn duy nhất: `kichban/superpowers/04_worktree_va_ke_hoach.md`. Không bịa chi tiết ngoài file
đó, trừ số MINH HOẠ cho ẩn dụ (nêu rõ ở cột cuối, cùng cách bài 02/03 đã làm).

| Dòng | Chi tiết | Nguồn |
| :-: | :-- | :-- |
| 1 | Ẩn dụ thợ đập tường giữa phòng khách đang ở, bụi bay vào bếp | `04_worktree_va_ke_hoach.md` dòng 1 ("Một căn nhà đang ở vẫn cần sửa. Nếu thợ đập ngay giữa phòng khách, bụi và vật liệu sẽ trộn vào cuộc sống đang chạy") — cụ thể hoá "cuộc sống đang chạy" thành hình ảnh sờ được "nồi cơm đang sôi" |
| 2 | Tiến triển 3 ngày: bàn ăn sát tường → vôi vữa lấn → cả nhà đứng ăn | **MINH HOẠ tự đặt** theo đúng khuôn "ngày thứ N" của brief mục 4 dòng 2, dựng cụ thể từ ý gốc dòng 1 nguồn (bụi/vật liệu trộn vào cuộc sống đang chạy) — cùng cách sp02 tự đặt "ba ngày xây tường" |
| 3 | Lỗi không ở thợ vụng, không ở việc khó, mà ở chỗ hai việc chung một khu chưa quây riêng | Diễn giải từ nguồn dòng 1-2 (nguyên nhân là thi công chung chỗ, không phải năng lực) |
| 4 | Ẩn dụ "khung cửa công trường riêng, đi lối khác, nền cũ không suy suyển" + "phiếu việc treo sẵn" | `04_worktree_va_ke_hoach.md` dòng 2 ("Cách an toàn là quây riêng một khu thi công, kiểm tra nền cũ còn tốt, rồi mới mang đồ nghề vào") |
| 5 | Tên `worktree`, "nhánh có thư mục làm việc độc lập, không làm bẩn chỗ đang dùng", skill hỏi trước + ưu tiên công cụ nền tảng | `04_worktree_va_ke_hoach.md` dòng 3-4 nguyên văn |
| 6 | "Kế hoạch thi công" — mỗi nhiệm vụ ghi file/test/lệnh/kết quả; ví dụ thật "tìm cảnh thiếu lời đọc, thử trên file mẫu ba cảnh" | `04_worktree_va_ke_hoach.md` dòng 6-7 nguyên văn ("kiểm tra kịch bản video... phát hiện cảnh thiếu dòng lời") |
| 7 | Bước 1 tạo mẫu 3 cảnh (cảnh 2 thiếu lời), bước 2 chạy kiểm tra đòi lỗi đúng cảnh 2, mỗi bước 2-5 phút | `04_worktree_va_ke_hoach.md` dòng 8 nguyên văn |
| 8 | Bước 3 viết tối thiểu, bước 4 chạy lại thấy đúng 1 lỗi, bước 5 commit/chốt mốc riêng | `04_worktree_va_ke_hoach.md` dòng 8-9 (gộp "commit riêng nhiệm vụ" thành "chốt một mốc riêng... phiếu việc coi như xong một dòng" — tránh chữ cấm "commit") |
| 9 | Bẫy 1: tạo worktree không kiểm tra test nền; bẫy 2: kế hoạch chỉ có tiêu đề, không bằng chứng | `04_worktree_va_ke_hoach.md` dòng 10 nguyên văn |
| 10 | Chốt: khu riêng giữ sạch, kế hoạch giữ đúng, cần cả hai; dội lại hook (bụi vào nồi cơm) | `04_worktree_va_ke_hoach.md` dòng 11 ("Khu riêng giữ công trường sạch. Kế hoạch rõ giữ người thợ đi đúng. Cần cả hai trước khi thi công") + tự thêm vế dội hook cho đối xứng |

### Nối mạch với bài 03, không lặp hình
Bài 03 đóng bằng ẩn dụ **tấm bản vẽ** (bản thiết kế đã duyệt). Bài 04 **không lặp lại** hình bản
vẽ — chuyển sang vật thể mới **khung cửa công trường riêng + phiếu việc**, đúng mạch: bản vẽ đã
duyệt xong ở bài 03, giờ bài 04 là lúc dựng chỗ riêng để thi công đúng bản vẽ đó mà không đụng
nhà đang ở.

---

## 2. BA PHƯƠNG ÁN HOOK (thợ 1 đã chọn ở lượt trước)

Trần cứng: 11 từ đầu = 3 giây đầu, phải có **cảnh sờ được** + **mất mát hoặc nghịch lý**.

| # | Hook | 11 từ đầu đã đủ chưa | Chọn |
| :-: | :-- | :-- | :-: |
| **A** | *"Thợ đập tường giữa phòng khách, bụi bay thẳng vào nồi cơm đang sôi trên bếp."* | `Thợ đập tường giữa phòng khách, bụi bay thẳng vào nồi cơm` — cảnh (thợ, tường, bụi, nồi cơm) và mất mát (bụi bay thẳng vào bữa ăn đang nấu) **trọn trong 11 từ đầu**. | ✅ |
| B | *"Bạn giao việc mới, đội thợ mở luôn ngay giữa phòng khách đang ở."* | Có cảnh nhưng mất mát chưa lộ trong 11 từ đầu — phải đợi câu sau mới thấy hậu quả. | |
| C | *"Hai việc chạy chung một chỗ, việc mới vừa bắt đầu thì việc cũ đã lem luốc."* | Nghịch lý có nhưng thiếu vật cụ thể sờ được (không có tường/bụi/nồi cơm), trừu tượng hơn A. | |

**Vì sao chọn A:** duy nhất A đặt được cảnh cụ thể (thợ, tường, bụi, nồi cơm) VÀ mất mát (bụi
lấn vào bữa ăn) trọn trong 11 từ đầu — không phải đợi vế sau. A cũng cho dòng 10 dội lại sạch:
đúng cụm "bụi vẫn bay thẳng vào nồi cơm đang sôi" được lặp lại nguyên văn ở câu chốt.

*(Ghi chú: 3 phương án này là suy luận lại từ hook đã chọn trên đĩa — thợ 1 phiên trước không để
lại bảng 3 phương án, tôi dựng lại B/C để đúng khuôn brief mục 4, không đổi lời dòng 1 đã có.)*

---

## 3. KẾT QUẢ THƯỚC (chạy lại xác nhận, phiên có quyền chạy lệnh)

```
$ python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/sp04_worktree.txt --thuatngu "superpowers,skill,worktree,codex,agent,plugin,branch"

SACH   | khong loi, khong canh bao
KETLUAN|27|444|DAT
```

Khớp đúng số thợ 1 đã báo trước khi bị chặn quyền (`KETLUAN|27|444|DAT`) — xác nhận không có
sửa lời nào giữa hai lượt.

---

## 4. DỰNG DECK — tóm tắt (chi tiết xem `sp04_worktree.man_hinh.md`)

Chép nền từ `deck_sp02`. 2 mẫu MỚI bắt buộc theo brief mục 3: `webui-frame`/`vpg-media-full`/
`source-tag` ở slide 4 (khung cửa sổ đôi, không có ảnh thật nên không nhét `<img>`, dùng icon +
nhãn tự dựng bên trong khung) và `workflow-grid` lưới 2×2 đánh số ở slide 6. Các slide còn lại
tái dùng nguyên cấu trúc slide tương ứng của `deck_sp02` (flow-diagram, hk-names, sc-file,
mock-terminal, risk-cards, glowing-conclusion).

---

## 5. CHỖ CÒN YẾU NHẤT — NÓI THẲNG

1. **Slide 4 không có ảnh chụp thật.** Bài 03 dùng `stream-visual` (không cần ảnh thật) nhưng bài
   04 được giao đúng mẫu `webui-frame`/`vpg-media-full` — mẫu này SINH RA để bọc ảnh/video nguồn
   thật. Ở đây không có screenshot worktree thật nào để nhét, nên tôi giữ đúng CLASS (đúng khung,
   đúng kích thước) nhưng thay `<img>` bằng icon + nhãn tự dựng. Đây là cách diễn giải hợp lý
   nhất tôi tìm được, nhưng khác tinh thần gốc của mẫu (media-first). Nếu BOSS thấy chưa ổn, cách
   khác là đổi hẳn sang scene khác — nhưng brief mục 3 ghi rõ "không tự đổi mẫu hình được giao".
2. **Dòng 2 (ngày 1/2/3) là số MINH HOẠ tôi tự đặt**, không truy được nguyên văn về
   `04_worktree_va_ke_hoach.md` (nguồn chỉ có 1 câu mô tả chung, không có tiến triển 3 ngày cụ
   thể) — cùng logic bài 02/03 tự đặt số minh hoạ cho ẩn dụ, nhưng nếu BOSS soi kỹ nguồn sẽ thấy
   đây là hư cấu thêm cho sinh động, không phải trích nguyên văn.
3. **Dòng 8 gộp "bước năm — commit riêng"** thành "chốt một mốc riêng... phiếu việc coi như xong
   một dòng" để tránh chữ cấm `commit`. Nghĩa gần đúng nhưng không còn cụ thể là thao tác git —
   người xem có thể không nối được "chốt mốc" với hành động thực tế "git commit".
4. Tôi **chưa nghe/xem gì** — mọi thứ trên đây chỉ là số máy đo được (thước, `grep`) và suy luận
   chữ nghĩa. Giọng, nhịp, mượt hay giật để BOSS nghe rồi phán.
