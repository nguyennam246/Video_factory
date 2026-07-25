# README — sp07b_debug (BẢN A/B của bài 07 khoá Superpowers)

NGHE: hook=cau_hoi_gai | mo=2 | tra=3 | chia_se=10 | y_moi=1
CAU_CHIA_SE: Ba lần thay đồ không bằng một lần đo đúng.
Y_MOI: gặp lỗi thì lần theo bằng chứng tới đúng chỗ vỡ, chưa tìm ra chỗ vỡ thì chưa được đề xuất cách sửa

---

## Bài này để làm gì — KHÔNG phải bài mới

Đây là **bản thứ hai của cùng một bài** (`sp07_debug`, BOSS đã duyệt 25/07), dựng để BOSS
**so trực tiếp bản cũ ↔ bản mới** và phán khâu `video/nghe/` có ăn thật hay không.
Nội dung, nguồn, con số **giữ y nguyên** bản cũ — truy vết đầy đủ ở
`README_sp07_debug.md`, không lặp lại ở đây. Chỉ đổi **cách giữ mắt**.

## Đổi đúng bốn thứ, ghi rõ để BOSS biết mình đang so cái gì

| # | Bản cũ (`sp07_debug`) | Bản mới (`sp07b_debug`) |
| :-: | :-- | :-- |
| 1 | Hook kiểu `mat_mat`: *"Vòi chảy yếu, thợ thay vòi mới, nước vẫn yếu như cũ."* — kể một cảnh | Hook kiểu **`cau_hoi_gai`**: *"Ba lần thay đồ mà nước vẫn chảy yếu, vì sao?"* — mở bằng **số** rồi **đặt câu hỏi người xem biết là mình không trả lời được** |
| 2 | Dòng 2 kể tiếp cảnh, không để lại món nợ | Dòng 2 **mở món nợ**: *"chưa ai đo xem nước mất áp ở chỗ nào"* — câu hỏi treo |
| 3 | Không có câu nào thiết kế để chụp màn hình | Dòng 10 có **câu đáng chụp màn hình**: *"Ba lần thay đồ không bằng một lần đo đúng."* — 10 từ, cặp đối *ba lần thay ↔ một lần đo*, không thuật ngữ |
| 4 | Scene trùng bài liền trước **83%**, chỉ thêm 1 mẫu | Bắt buộc **≥2 mẫu mới, trùng ≤60%** (thước `--trung` chặn) |

**Giữ nguyên có ý:** giọng · nhịp `[1,3,3,2,3,3,3,3,3,3]` · palette `sp` · ẩn dụ đường ống ·
mọi con số (−22,4 · −30,7 · −18,8 đề xi ben) · bốn bước. Đổi nhiều thứ một lúc thì BOSS
không biết cái gì làm nên khác biệt.

## Hook — ba phương án, ba KIỂU khác nhau

| Kiểu | Phương án | Từ | Chọn? |
| :-- | :-- | :-: | :-: |
| `cau_hoi_gai` | *"Ba lần thay đồ mà nước vẫn chảy yếu, vì sao?"* | 11 | ✅ **chọn** — có số ngay từ đầu, câu hỏi có dữ kiện đứng trước nên là câu hỏi thật, và nó dựng sẵn câu chốt đối xứng ở dòng 10 |
| `giua_hanh_dong` | *"Thợ vừa siết xong cái van thứ ba, nước vẫn chảy nhỏ giọt."* | 12 | vào giữa việc rất tốt, nhưng mất con số "ba lần" ở vị trí mở |
| `mot_moc` | *"Hai lần thay đồ đều êm, lần thứ ba mới lộ ra vô ích."* | 12 | sai sự thật của bài: cả **ba** lần đều vô ích, không phải hai lần đầu êm |

## Bẫy phát hiện khi dùng thư viện lần đầu — ĐÃ VÁ VÀO `KIEU_HOOK.md`

Công thức gốc của `cau_hoi_gai` là **hai câu** (`{tình huống có số}. {câu hỏi}?`) nhưng khuôn
bài dạy cho dòng 1 **đúng MỘT câu**. Hai luật đụng nhau. Cách chữa: nén thành một câu, giữ cả
dữ kiện lẫn dấu hỏi (*"Ba lần thay đồ mà nước vẫn chảy yếu, vì sao?"*). Đã ghi luật này vào
`video/nghe/KIEU_HOOK.md` để bài sau không sập lại.

## Tự kiểm

```bash
cd /Users/simple/Desktop/Cloud/video
TN="gỡ lỗi có hệ thống,superpowers,skill,plugin,codex"
python3 .claude/skills/video-kynang/thuoc/thuoc_kichban_kynang.py \
        kichban/escbase_10dong/sp07b_debug.txt --thuatngu "$TN"
python3 .claude/skills/video-kynang/thuoc/thuoc_nghe.py \
        kichban/escbase_10dong/sp07b_debug.txt \
        kichban/escbase_10dong/README_sp07b_debug.md --thuatngu "$TN"
```
