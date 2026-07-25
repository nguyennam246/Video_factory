# CATALOGUE SCENE — 18 mẫu hình có sẵn trong template (lập 25/07/2026)

**Tra bằng ẢNH, không tra bằng chữ.** Ảnh chụp thật từ `template/visual-pattern-gallery`
ở khổ `390×693` (dsf 2), mọi reveal đã bật. Chụp lại bất cứ lúc nào:

```bash
.venv/bin/python capture_slides.py template/visual-pattern-gallery --out docs/assets/catalogue
```

## VÌ SAO CÓ FILE NÀY

Đếm ngày 25/07: **16/18 mẫu hình cờ đầu của template CHƯA DÙNG LẦN NÀO** trong 14+ video
đã dựng. Cả bộ xoay quanh `mock-terminal` (7 deck) + `risk-cards-container` (1 deck) và
một nhúm scene tự chế (`hk-*`, `sc-file`, `sg-*`). Đó là lý do xem 3 bài liền nhau thấy
"cùng một cái khuôn" — không phải vì template nghèo, mà vì mình chưa mở kho ra.

| Trạng thái | Số mẫu |
| :-- | :-- |
| Đã dùng | 2 (`mock-terminal`, `risk-cards-container`) |
| **Chưa dùng lần nào** | **16** |

---

## CÁCH DÙNG

1. Xem ảnh dưới, chọn mẫu diễn đạt ĐÚNG Ý câu voiceover (không chọn vì đẹp).
2. Mở `template/visual-pattern-gallery/index.html`, tìm `data-slide="<N>"`, copy khối DOM.
3. Copy CSS tương ứng từ `template/visual-pattern-gallery/style.css` (tìm theo tên class gốc).
4. Đổi chữ/số/nhãn cho đúng nội dung. **Giữ số `.slide-element` = số câu của dòng script.**
5. `validate_slide.py --semantic-report` → `capture_slides.py` → **Read từng ảnh**.

⚠️ Slide `data-mode="highlight"` thì reveal = `.slide-element` + `.highlightable`.
⚠️ Mẫu có `.lightable` (đèn giao thông) bật theo reveal — ảnh chụp bật CẢ 3 đèn cùng lúc
nên trông xanh hết; lúc chạy thật đỏ/vàng/xanh lên lần lượt.

---

## A. HERO — chỉ dùng cho slide 1

| Ảnh | Mẫu | Class gốc | Dùng khi |
| :-- | :-- | :-- | :-- |
| ![](assets/catalogue/slide1.png) | **Source-image hero** | `vpg-source-hero` · `gia-source-poster` | Ảnh/screenshot là bằng chứng chính. Nguồn: `template/googleaistudio-post-…` |
| ![](assets/catalogue/slide2.png) | **Product-logo hero** | `vpg-logo-hero` · `kimi-logo-orbit` · `kimi-orbit-ring` | Sản phẩm/model/thương hiệu là hook. Nguồn: `template/kimi-moonshot-post-…` |
| ![](assets/catalogue/slide3.png) | **Avatar-person hero** | `addy-orbit-hero` · `orbit-ring` · `orbit-chip` | Tác giả/nhân vật là hook. Nguồn: `template/addyosmani-loop-engineering` |
| ![](assets/catalogue/slide4.png) | **GitHub-repo hero** | `ask-github-mark` · `mtd-hero-halo` · `ask-title` | Repo GitHub / GitHub Trending. Nguồn: `template/openmontage-github-trending` |

Luật cứng của template: slide 1 **copy nguyên**, chỉ thay chữ/logo/media — không đổi
layout, nền, hiệu ứng. Tiêu đề H1 mặc định ~42px trên khung 390.

---

## B. SỐ LIỆU & BẰNG CHỨNG

| Ảnh | Mẫu | Class gốc | Dùng khi |
| :-- | :-- | :-- | :-- |
| ![](assets/catalogue/slide6.png) | **Performance compare bars** ⭐ | `perf-compare` · `perf-bar` · `perf-row` | So sánh trước/sau có SỐ: thời gian, chi phí, điểm. Thanh chạy theo reveal |
| ![](assets/catalogue/slide8.png) | **Speed gauge** | `speed-gauge` · `gauge-arc` · `gauge-needle` | Tốc độ/độ trễ/thông lượng. Kim quét thể hiện chuyển trạng thái |
| ![](assets/catalogue/slide17.png) | **Revenue balance** ⭐ | `revenue-balance-scene` · `balance-beam` · `column-fill` | **Hai số tạo nghịch lý** — rất hợp series tài chính (VD: doanh thu to ↔ lãi bé) |
| ![](assets/catalogue/slide5.png) | **Media-first frame** | `webui-frame` · `vpg-media-full` · `source-tag` | Ảnh/video nguồn full-frame. Chú thích đặt DƯỚI, cấm overlay lên media |

---

## C. QUY TRÌNH & DÒNG CHẢY

| Ảnh | Mẫu | Class gốc | Dùng khi |
| :-- | :-- | :-- | :-- |
| ![](assets/catalogue/slide7.png) | **Flow diagram** ⭐ | `flow-diagram` · `flow-old` · `flow-strike` · `flow-new` | Cũ → mới, có gạch bỏ trạng thái cũ. Hợp bài dạy "trước khi có X / sau khi có X" |
| ![](assets/catalogue/slide10.png) | **Data stream** | `stream-visual` · `stream-pipe` · `stream-data` | Pipeline, packet chạy, API streaming |
| ![](assets/catalogue/slide12.png) | **Workflow grid** ⭐ | `workflow-grid` · `workflow-step` · `packet` | Quy trình nhiều bước đánh số. **Rất hợp khóa Superpowers 6 trạm kiểm soát** |
| ![](assets/catalogue/slide11.png) | **Mock terminal** ✅đang dùng | `mock-terminal` · `terminal-bar` · `terminal-title` | CLI, cài đặt, output test |

---

## D. CƠ CHẾ BÊN TRONG

| Ảnh | Mẫu | Class gốc | Dùng khi |
| :-- | :-- | :-- | :-- |
| ![](assets/catalogue/slide9.png) | **CPU / chip scan** | `cpu-chip` · `chip-body` · `chip-core` · `chip-pins` | Ruột máy: cache, model internals, tối ưu. Scanner quét qua từng layer |
| ![](assets/catalogue/slide13.png) | **Highlight mode** ⭐ | `core-module-grid` · `core-module` · `highlightable` | Nhấn LẦN LƯỢT từng phần trong CÙNG một scene — thay cho việc đổi slide |

---

## E. RỦI RO & PHẢN ỨNG

| Ảnh | Mẫu | Class gốc | Dùng khi |
| :-- | :-- | :-- | :-- |
| ![](assets/catalogue/slide14.png) | **Risk cards** ✅đang dùng | `risk-cards-container` · `risk-card` · `lightable` | Đỏ = rủi ro · vàng = cần kiểm chứng · xanh = tín hiệu tốt |
| ![](assets/catalogue/slide15.png) | **Traffic-light pole** | `vpg-traffic-pole` · `vpg-lamp` · `lightable` | Khi muốn tín hiệu đỏ/vàng/xanh RÕ như cột đèn thật |
| ![](assets/catalogue/slide16.png) | **Chat bubbles** | `vpg-chat-message` · `msg-bubble` · `msg-avatar` | Hội thoại, phản ứng cộng đồng, hỏi–đáp |

---

## F. KẾT BÀI

| Ảnh | Mẫu | Class gốc | Dùng khi |
| :-- | :-- | :-- | :-- |
| ![](assets/catalogue/slide18.png) | **Final lockup** ⭐ | `glowing-conclusion` · `glowing-orb` · `icon-badge` | Câu chốt + nguồn/CTA. Hợp câu chốt đối xứng của bộ dạy |

---

## ⭐ 6 MẪU NÊN LẤY TRƯỚC (hợp nội dung đang dựng)

| Mẫu | Vào bài nào | Vì sao |
| :-- | :-- | :-- |
| `workflow-grid` | Superpowers 01-08 | Cả khóa là **6 trạm kiểm soát** — đúng nghĩa quy trình đánh số |
| `flow-diagram` | Bài dạy có "trước/sau" | Gạch trạng thái cũ, sáng trạng thái mới: thấy được sự thay đổi |
| `core-module-grid` (highlight) | Bài liệt kê nhiều phần | Nhấn từng phần trong 1 scene, đỡ phải tách slide, đỡ thưa |
| `revenue-balance` | Series tài chính | Khuôn tài chính slide 1 là **nghịch lý bằng số** — mẫu này sinh ra cho việc đó |
| `perf-compare` | Bài có số đo | Số của dự án (`2.700 token`, `93 giây`…) thành thanh so sánh |
| `glowing-conclusion` | Slide 10 mọi bài | Câu chốt đối xứng đang chỉ là chữ |

---

## RÀNG BUỘC KHÔNG ĐƯỢC PHÁ (rút từ TEMPLATE_RULES của gallery)

- Safezone `100px 28px 200px` — nửa dưới là chỗ của phụ đề, đừng đặt chữ quan trọng.
- Nhãn tối thiểu 11-12px · kicker 13-20px · số chính 42-51px (đo trên khung 390).
- Visual chính phải **lấp gần đủ safezone**; scene lọt thỏm giữa slide là lỗi.
- **Hai slide liền nhau không được cùng một dạng hộp** — đổi hình, đổi chuyển động,
  hoặc đổi vai màu.
- Animation nền (hạt, shimmer, glow) **không tính** là animation có nghĩa. Phải có:
  scanner quét, packet chạy, thanh đầy lên, đèn bật, trạng thái cũ bị gạch.
