# BỘ SƯU TẬP THEME — dùng lại cho deck sau (lập 25/07/2026, BOSS lệnh)

Mỗi theme = **một khối `<style>` tự chứa** cắm vào `<head>` của `index.html`, dùng **tiền tố
class riêng** nên KHÔNG đụng `style.css` 139 KB dùng chung ⇒ cắm vào deck nào cũng không
làm hỏng deck khác.

## Cách tái dùng
1. `cp -R headless/deck_<gần nhất> headless/deck_<mới>` rồi `rm -rf output*`.
2. Mở `index.html`, **thay trọn khối `<style>…</style>`** bằng nội dung file theme muốn dùng.
3. Đổi tiền tố class trong phần slide cho khớp theme (`nn-` ↔ `hs-` …).
4. Đổi `<title>` / `<meta name="description">` / `?v=` ở 2 thẻ `style.css` + `app.js`.

## Danh sách

| # | File | Tên | Ngôn ngữ thị giác | Tiền tố | Bài đã dùng |
| :-: | :-- | :-- | :-- | :-- | :-- |
| 01 | `theme_01_vet_nut_kim_cuong.css.html` | **VẾT NỨT KIM CƯƠNG** | hộp trang sức tối, nét khắc **vàng** mảnh, mặt cắt kim cương chéo, bo góc tròn 14px, tiêu đề **Playfair Display** serif | `nn-` | `deck_pnj03` → `PNJ_03_niemtin.mp4` |
| 02 | `theme_02_ho_so_dieu_tra.css.html` | **HỒ SƠ ĐIỀU TRA** | phòng hồ sơ tối xanh thép, lưới blueprint mờ, thẻ **góc vuông 3px** viền mảnh, gáy hồ sơ đánh số mono, dấu mộc đỏ, tiêu đề **Oswald condensed in hoa** + nhãn **IBM Plex Mono** | `hs-` | `deck_pnj04` → `PNJ_04_hoso.mp4` |

**Theme 02 có sẵn 3 khuôn mà theme 01 không có** (dùng lại được ngay):
- `.hs-chart` — khung biểu đồ đường vẽ bằng SVG trong DOM (cắm chuỗi giá thật vào là xong).
- `.hs-shot` + `.hs-file-inner` — **ảnh chân dung 76×92 kẹp cạnh chữ trong thẻ hồ sơ**, có
  chú thích mono. 🔴 Đừng đặt ảnh thành dải ngang full-width: `object-fit:cover` cắt mất
  trán/cằm, mà `validate` vẫn PASS — chỉ soi ảnh mới thấy (trả giá 25/07, ca PNJ 04).
- `.hs-key` — logo chìa khoá `dungladu.vn` xoay ngang cho slide chốt thương hiệu.

## Luật giữ theme sạch
- Theme chỉ chứa **class có tiền tố của nó** + `:root` biến của nó. Cấm sửa selector dùng chung
  (`.slide`, `.slide-element`, `.pixelle-slide-content`) trừ 1 ngoại lệ đã có: tắt watermark góc
  ở slide cuối.
- Cỡ chữ trong theme là **cỡ đã soi ảnh thật**; đổi cỡ thì phải capture + soi lại safezone.
- Thêm theme mới ⇒ thêm 1 dòng vào bảng trên **trong cùng phiên**.
