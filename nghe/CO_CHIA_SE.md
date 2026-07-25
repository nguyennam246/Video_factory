# CỚ ĐỂ CHIA SẺ — một câu mỗi bài (lập 25/07/2026)

**Vấn đề nó giải:** tiêu chuẩn BOSS đặt cho cả bộ là *"chỉ xem video là hiểu vấn đề và
làm được, **chia sẻ lại được**"*. Hai phần đầu có luật và có thước. Phần thứ ba —
**chia sẻ lại được** — tới hôm nay **không khâu nào lo**.

Không ai chia sẻ "một video hay". Người ta chia sẻ **một câu**. Video chỉ là chỗ đựng câu đó.

---

## Câu đáng chụp màn hình — năm điều kiện

Mỗi bài phải có **đúng một** câu như thế. Không phải hai (loãng), không phải không có.

| # | Điều kiện | Vì sao |
| :-: | :-- | :-- |
| 1 | **Tự đứng được** — tách khỏi video vẫn hiểu | người chia sẻ dán câu đó ra chỗ khác, không dán cả bài |
| 2 | **≤ 14 từ** | dài hơn thì không ai nhớ, không ai gõ lại. Bằng 4 giây đọc |
| 3 | **Không có tên kỹ thuật** | người nhận chưa xem video, thuật ngữ là bức tường |
| 4 | **Có một cặp đối** hoặc **một con số thật** | đối làm nó nhớ được; số làm nó đáng tin |
| 5 | **Không hứa hẹn gì** | "bạn sẽ giỏi hơn" là quảng cáo, không ai chia sẻ quảng cáo |

---

## Đặt ở đâu — dòng 3 hoặc dòng 10, không đặt chỗ khác

| Chỗ đặt | Dùng khi | Cơ chế |
| :-- | :-- | :-- |
| **Dòng 3** | câu chốt là một **nhận định** — chỉ đúng chỗ đau | người xem gặp nó sớm, còn 70 giây để hiểu tại sao đúng, nên tin nó rồi mới chia sẻ |
| **Dòng 10** | câu chốt là một **kết luận** — đối xứng lại hook | người xem vừa hiểu xong, câu chốt là chỗ dồn hết bài lại |

**Đừng đặt ở dòng 5-8.** Đó là khúc thân bài, chỗ giải thích và chạy thử — một câu đẹp
đặt giữa mớ chi tiết thì bị chi tiết nuốt.

Nếu đặt ở dòng 10 thì nó phải **đồng thời** thoả luật câu chốt đối xứng (dội lại ≥2 từ
của dòng 1). Hai luật này cộng được, không xung nhau.

---

## Mẫu đã chạy trong bộ

| Câu | Từ | Đối / số | Đặt ở |
| :-- | :-: | :-- | :-- |
| *"Lời dặn có ngày bị quên. Cái khoá thì không."* | 10 | đối: lời dặn ↔ cái khoá | dòng 10 |
| *"Máy báo đạt không có nghĩa là đúng."* | 8 | đối: báo đạt ↔ đúng | dòng 3 |

Cả hai đều: tự đứng được, không tên kỹ thuật, có cặp đối, không hứa gì.

---

## Khuôn dựng câu — ba công thức

**① Đối lập hai vế** — mạnh nhất, dùng được cho cả bài dạy và bài tài chính.
> `{Cái người ta tin}. {Cái thật} thì không.`
> *"Lời dặn có ngày bị quên. Cái khoá thì không."*

**② Phủ định một tương đương** — dùng khi bài sửa một niềm tin.
> `{A} không có nghĩa là {B}.`
> *"Máy báo đạt không có nghĩa là đúng."*

**③ Số đặt cạnh số** — dùng cho bài tài chính, an toàn nhất vì không phán gì.
> `{Số A}. {Số B}. Cùng một {kỳ}.`
> *"Doanh thu tăng bốn mươi phần trăm. Dòng tiền âm. Cùng một năm."*

⚠️ Công thức ③ trùng với hook `nghich_ly_so`. Nếu đã dùng nó làm hook thì **đừng dùng lại
làm câu chia sẻ** — chọn ① hoặc ②, không thì bài chỉ có một câu nói hai lần.

---

## Bẫy

- **Câu đẹp mà rỗng.** *"Chất lượng là thứ không thể thoả hiệp."* — thoả cả 5 điều kiện
  hình thức, nhưng không dạy gì và ai cũng viết được. Phép thử: **câu đó chỉ đúng với bài
  này, hay đúng với mọi bài?** Đúng với mọi bài thì bỏ.
- **Nhét thuật ngữ vì nó "chính xác hơn".** Chính xác cho người đã xem, tường chắn cho
  người chưa xem. Người chưa xem mới là người nhận được câu chia sẻ.
- **Bài tài chính:** câu này bị người ta chia sẻ ra khỏi ngữ cảnh — nên nó phải chịu luật
  `CAM_KHUYEN` **nghiêm hơn cả bài**. Một câu tách khỏi video mà đọc lên như lời khuyên
  mua bán là câu hỏng, kể cả khi trong video nó vô can.

---

## Khai báo

Khai vào `README_{slug}.md`:

```
NGHE: hook=nghich_ly_so | mo=2 | tra=6 | chia_se=10 | y_moi=1
CAU_CHIA_SE: Lời dặn có ngày bị quên. Cái khoá thì không.
```

Thước kiểm: câu khai báo phải **có thật trong dòng đã khai**, ≤14 từ, không chứa thuật
ngữ trong `--thuatngu`, không chứa từ cấm.
