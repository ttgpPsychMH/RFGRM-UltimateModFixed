# RFGRM Ultimate Mod Fixed

Bản điều chỉnh Ultimate Mod cho **Red Faction Guerrilla Re-Mars-tered**, dùng để chơi offline.

## Tải bản mới nhất — Campaign v3, tốc độ/động cơ xe ×1,5

- **[Tải bản mod mới nhất (khoảng 16,5 MiB)](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Vehicle_1_5x.zip)** — chứa cả `misc.vpp_pc`, `table.vpp_pc` và hướng dẫn.
- [Tải báo cáo thay đổi và kiểm tra V3](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Reports.zip).
- [Đọc hướng dẫn đầy đủ](downloads/HUONG_DAN.txt) · [SHA-256](downloads/SHA256SUMS.txt).
- [Bảng tốc độ toàn bộ 146 cấu hình xe: original và từng gói hiện tại](reports/vehicle-speeds.md) · [CSV](reports/vehicle-speeds.csv).
- [Kiểm tra walking / running / sprinting của nhân vật chính](reports/player-movement.md).

V3 chỉ giảm các giới hạn tốc độ tiến/lùi và mô-men xoắn/RPM đã được chọn từ ×3 xuống **×1,5 original**. Giữ nguyên các thiết lập khác, kể cả HP xe ×5. Có 349 giá trị đổi trong `vehicles.xtbl` của `misc.vpp_pc`; toàn bộ `table.vpp_pc` giữ nguyên từng byte từ V2. Hai gói giữ phạm vi sửa riêng như đã thống nhất.

Ví dụ giới hạn cấu hình của Bluecrab: gốc 52 mph → V2 156 mph → **V3 78 mph (125,53 km/h)**; HeavyTank `EDF_HeavyTank-A_1`: 20 → 60 → **30 mph (48,28 km/h)**. Tốc độ đo thực tế còn tùy engine và điều kiện lái; chưa xác nhận thứ tự game ưu tiên nạp các bảng trùng giữa hai VPP.

## Tiện ích nhảy cao ×2 / ×3 (thử nghiệm)

**[Tải tiện ích nhảy cao](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/RFGRM_Jump_RSL_Experimental.zip)** · [Hướng dẫn cài và sử dụng](jump-addon/README.md).

Cần cài thêm **RSL 1** tương thích với game. Mặc định nhân trường độ cao nhảy của người chơi ×2; có thể chọn ×3 hoặc trả về mốc đã lưu. Dùng cùng Campaign v2 hoặc v3. Đã kiểm tra logic Lua bằng mô phỏng; **chưa xác nhận độ cao thực tế trong game**.

## Thiết lập chính

Các hệ số đều tính từ dữ liệu game gốc, chỉ áp dụng trong phạm vi tham số đã được chọn của từng gói cùng các ngoại lệ liên quan.

| Nhóm | Thiết lập |
|---|---|
| Thời gian spawn đã được mod sửa | Gốc ÷3; 30 giây → 10 giây; số nguyên làm tròn lên |
| Tốc độ tối đa nhân vật chính | 10 m/s, gấp đôi gốc |
| Bảo vệ nhân vật chính | Giữ HP và các hệ số giảm sát thương/hồi phục đã chốt |
| Giới hạn tốc độ xe, mô-men xoắn, RPM | Các trường được chọn ×1,5 |
| Bán kính nổ | Các trường được chọn ×3 |
| HP xe, sát thương súng/nổ, lượng đạn | Các trường được chọn ×5; sát thương tới người chơi giữ giảm riêng |
| Thời gian bắn lại/nạp đạn | Các trường được chọn ÷3 |
| HP NPC | Đồng minh/dân thường ×5; EDF/Marauder ×3 |
| Búa | Thường ×50; nâng cấp ×20 chỉ số gốc riêng; vàng ×100 |

## Cài đặt

1. Thoát game và sao lưu hai file `misc.vpp_pc`, `table.vpp_pc` đang dùng.
2. Giải nén ZIP bản mod; chép **cả hai file VPP** vào thư mục game chứa các file cùng tên và thay thế.
3. Đây là hai gói đầy đủ, không cần cài chồng các ZIP trước đó. Muốn hoàn tác thì chép lại bản sao lưu.

Đã kiểm tra cấu trúc VPP, giải nén đối chiếu toàn bộ tệp, công thức thay đổi và các cặp min/max liên quan. **Chưa chạy thử trong game.** Spawn nhanh có thể tăng mật độ quân/tải CPU; búa và phá hủy vẫn rất mạnh. Bảo vệ nhân vật chính không bảo vệ mọi đồng minh hay mục tiêu nhiệm vụ.

Mỗi gói có một lỗi ký tự XML trong `credits.xtbl` đã tồn tại ở bản gốc, được giữ nguyên từng byte. Tất cả tài liệu sửa trong bản này đều qua kiểm tra XML; xem ZIP báo cáo để biết chi tiết.

## Bản cũ

[Campaign v2 — tốc độ/động cơ xe được chọn ×3](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2.zip) · [Báo cáo V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2_Reports.zip).

Mod ban đầu: [Ultimate Mod trên Nexus Mods](https://www.nexusmods.com/redfactionguerrillaremarstered/mods/16?tab=description).
