# RFGRM Ultimate Mod Fixed

Bản điều chỉnh Ultimate Mod cho **Red Faction Guerrilla Re-Mars-tered**, dùng để chơi offline.

## Tải bản mới nhất — Campaign v2

- **[Tải bản mod (16,5 MiB)](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2.zip)** — chứa cả `misc.vpp_pc`, `table.vpp_pc` và hướng dẫn.
- [Tải báo cáo thay đổi và kiểm tra](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2_Reports.zip).
- [Đọc hướng dẫn đầy đủ](downloads/HUONG_DAN.txt) · [SHA-256](downloads/SHA256SUMS.txt).

## Thiết lập chính

Các hệ số đều tính từ dữ liệu game gốc, chỉ áp dụng trong phạm vi tham số đã được chọn của từng gói cùng các ngoại lệ liên quan.

| Nhóm | Thiết lập |
|---|---|
| Thời gian spawn đã được mod sửa | Gốc ÷3; 30 giây → 10 giây; số nguyên làm tròn lên |
| Tốc độ tối đa nhân vật chính | 10 m/s, gấp đôi gốc |
| Bảo vệ nhân vật chính | Giữ HP và các hệ số giảm sát thương/hồi phục đã chốt |
| Động lực xe, tốc độ xe, RPM, bán kính nổ | Các trường được chọn ×3 |
| HP xe, sát thương súng/nổ, lượng đạn | Các trường được chọn ×5; sát thương tới người chơi giữ giảm riêng |
| Thời gian bắn lại/nạp đạn | Các trường được chọn ÷3 |
| HP NPC | Đồng minh/dân thường ×5; EDF/Marauder ×3 |
| Búa | Thường ×50; nâng cấp ×20 chỉ số gốc riêng; vàng ×100 |

## Cài đặt

1. Thoát game và sao lưu hai file `misc.vpp_pc`, `table.vpp_pc` đang dùng.
2. Giải nén ZIP bản mod; chép **cả hai file VPP** vào thư mục game chứa các file cùng tên và thay thế.
3. Đây là hai gói đầy đủ, không cần cài chồng các ZIP trước đó. Muốn hoàn tác thì chép lại bản sao lưu.

Đã kiểm tra cấu trúc VPP, giải nén đối chiếu toàn bộ tệp, công thức thay đổi và các cặp min/max liên quan. **Chưa chạy thử trong game.** Spawn nhanh có thể tăng mật độ quân/tải CPU; xe ×3 vẫn nhanh; búa và phá hủy vẫn rất mạnh. Bảo vệ nhân vật chính không bảo vệ mọi đồng minh hay mục tiêu nhiệm vụ.

Mỗi gói có một lỗi ký tự XML trong `credits.xtbl` đã tồn tại ở bản gốc, được giữ nguyên từng byte. Tất cả tài liệu sửa trong bản này đều qua kiểm tra XML; xem ZIP báo cáo để biết chi tiết.

Mod ban đầu: [Ultimate Mod trên Nexus Mods](https://www.nexusmods.com/redfactionguerrillaremarstered/mods/16?tab=description).
