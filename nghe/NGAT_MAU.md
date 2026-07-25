# NHỊP NGẮT MẪU — bao nhiêu giây phải đổi một thứ (lập 25/07/2026)

**Vấn đề nó giải:** kho có 18 mẫu scene và 20 tiếng động. Có **vật liệu**, nhưng **không
có nhịp** — không luật nào nói bao lâu phải đổi một thứ, và không luật nào chặn hai bài
liền nhau dùng chung một bộ hình.

---

## ⭐ ĐO THẬT 25/07/2026 — vì sao 8 bài Superpowers xem liền thấy cùng một khuôn

Dò `class` scene trong 12 deck (bỏ `script-panel` vì nó là **khung**, deck nào cũng có):

| Cặp bài liền nhau | Trùng / tổng scene bài sau | Độ trùng | Mẫu MỚI thêm được |
| :-- | :-: | :-: | :-- |
| sp01 → sp02 | 0 / 7 | **0%** | 7 mẫu (mở kho lần đầu) |
| sp02 → sp03 | 7 / 8 | **88%** | `stream-visual` |
| sp03 → sp04 | 5 / 6 | **83%** | `webui-frame` |
| sp04 → sp05 | 4 / 5 | **80%** | `vpg-traffic-pole` |
| sp05 → sp06 | 4 / 7 | **57%** | `core-module-grid` · `perf-compare` · `risk-cards-container` |
| sp06 → sp07 | 5 / 6 | **83%** | `cpu-chip` |
| sp07 → sp08 | 5 / 6 | **83%** | `revenue-balance` |

> **Lõi dùng chung của sp03→sp08 — 6 bài liền, 4 mẫu y nguyên:**
> `mock-terminal` · `workflow-grid` · `flow-diagram` · `glowing-conclusion`

Kết luận: **số mẫu mỗi bài không thiếu** (6-9 mẫu/bài, đủ nhiều). Cái sai là **mỗi bài
mới chỉ thêm ĐÚNG MỘT mẫu** rồi giữ nguyên 4-5 mẫu của bài trước. Xem một bài thì thấy
phong phú; xem sáu bài liền thì thấy một khuôn.

Và bài sp05→sp06 đạt 57% — chứng minh **ngưỡng dưới đây là làm được, không phải lý tưởng**.

---

## LUẬT 1 — TRÙNG VỚI BÀI LIỀN TRƯỚC ≤ 60%

**Mỗi deck phải có ≥ 40% scene mà bài liền trước KHÔNG có**, và tối thiểu **2 mẫu mới**.

Cách né sai: đừng đếm `script-panel` — nó là khung chứa chữ, không phải scene. Đếm nó vào
là con số nào cũng đẹp mà bài vẫn giống nhau.

**Đo bằng máy:**
```bash
python3 video/.claude/skills/video-kynang/thuoc/thuoc_nghe.py --trung <deck_moi> <deck_truoc>
```

🔴 **Luật này là cho BÀI KẾ TIẾP TRONG SERIES, không cho BẢN LÀM LẠI.** Khi dựng bản A/B của
cùng một bài (ví dụ `deck_sp07b` so `deck_sp07`) thì **giữ scene y nguyên mới đúng** — đổi
nhiều thứ một lúc thì BOSS không biết cái gì làm nên khác biệt. Lúc đó `--trung` báo 100%
HỎNG là **báo oan**, bỏ qua có ý thức và ghi rõ trong README của bản đó. Đo trùng thì đo với
**bài liền trước trong series**, đừng đo với bản mình đang làm lại.

Ba mẫu **chưa dùng lần nào** trong 12 deck: `speed-gauge` + bộ hero
(`ask-github-mark` · `vpg-source-hero` · `vpg-logo-hero`). Bài sau mở hàng chỗ này trước
khi quay lại lõi 4 mẫu cũ.

---

## LUẬT 2 — TRONG MỘT BÀI: ≤ 11 GIÂY PHẢI ĐỔI MỘT THỨ

10 slide trên 93-127 giây ⇒ **một slide ≈ 9-13 giây**. Reveal thì dày hơn nhiều
(27 reveal ⇒ một reveal mỗi 3,4-4,7 giây) nên **chữ hiện ra không phải là ngắt mẫu** —
nó là nhịp nền, người xem quen sau 15 giây.

**Mỗi lần sang slide phải đổi ÍT NHẤT MỘT trong bốn thứ:**

| Đổi cái gì | Đổi thế nào |
| :-- | :-- |
| **Loại scene** | slide này khác loại slide trước (mạnh nhất) |
| **Màu nhấn** | đổi màu nhấn trong bảng của series — không đổi bảng, chỉ đổi cái đang được nhấn |
| **Hướng trượt** | slide vào từ hướng khác slide trước |
| **Tiếng động** | có / không có tiếng ở nhịp reveal đầu của slide |

**Luật cứng:** **không được hai slide liền nhau cùng loại scene.** Đây là chỗ dễ vỡ nhất
khi chép deck cũ rồi chỉ thay chữ — chép xong là có ngay 3-4 slide liền cùng loại.

---

## LUẬT 3 — ĐỔI PHẢI CÓ NGHĨA, KHÔNG ĐỔI ĐỂ CHO KHÁC

Ngắt mẫu là để **đánh dấu một chuyển ý**, không phải để trang trí. Quy tắc:

- Đổi **loại scene** ở chỗ bài chuyển vai: hết cảnh đời thường sang gọi tên kỹ thuật
  (dòng 4→5), hết giải thích sang chạy thử (dòng 6→7).
- Đổi **màu nhấn** ở chỗ trạng thái đổi: cái cũ bị gạch, cái mới sáng lên.
- **Tiếng động** dành cho chỗ có kết quả nhìn thấy được, không rải đều.

⚠️ Bẫy đã trả giá: khung màu cảnh báo (`sg-warn`, đỏ) từng bọc quanh một câu **tích cực**
trong bài HPD — thước PASS cả hai lượt, chỉ soi mắt mới bắt. **Màu là nghĩa, không phải
trang trí.** Đổi màu cho khác thì sẽ đổi luôn nghĩa mà không ai báo.

---

## LUẬT 4 — CHUYỂN ĐỘNG PHẢI CÓ NGHĨA

Cột *"hình gì chuyển động"* trong `.man_hinh.md` phải là chuyển động **mang thông tin**:

| Đạt | Hỏng |
| :-- | :-- |
| thanh đầy dần lên tới mức thật | hạt bay nền |
| đèn bật lần lượt theo thứ tự bước | chữ nảy lên cho vui |
| trạng thái cũ bị gạch, cái mới sáng | scene xoay 360 độ |
| gói tin chạy từ ô này sang ô kia | mờ dần rồi rõ dần không lý do |

Phép thử: *"tắt tiếng, xem riêng chuyển động này, có hiểu thêm được gì không?"* Không thì bỏ.

---

## Tóm bảng chặn

| Luật | Ngưỡng | Ai chặn |
| :-- | :-- | :-- |
| Trùng scene với bài trước | ≤ 60%, và ≥ 2 mẫu mới | thước `--trung` |
| Hai slide liền cùng loại scene | cấm | thước `--trung` (trong 1 deck) |
| Đổi một thứ mỗi ≤ 11 giây | bắt buộc | **người dựng deck** |
| Đổi có nghĩa, màu đúng nghĩa | bắt buộc | **soi mắt từng PNG** — máy không bắt được |
