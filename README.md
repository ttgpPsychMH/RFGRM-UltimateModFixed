# RFGRM Ultimate Mod Fixed

Bản mod cho **Red Faction Guerrilla Re-Mars-tered**, dùng để chơi offline.

## Tải bản mới nhất — Campaign V4

**[Tải V4 — khoảng 16,0 MiB](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4.zip)** — gồm `misc.vpp_pc`, `table.vpp_pc`, hướng dẫn và SHA-256.

[Báo cáo thay đổi và mã dựng](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4_Reports.zip) · [Chi tiết cấu hình V4](reports/campaign-v4.md) · [Mọi giá trị original → V4](reports/campaign-v4-parameters.csv) · [Kết quả kiểm tra](reports/campaign-v4-validation.json) · [SHA-256](downloads/SHA256SUMS.txt).

[Toàn bộ thông số búa: original/V4, giải thích, animation và hướng tinh chỉnh](reports/hammer-reference.md).

V4 được dựng lại từ **hai file BACKUP gốc đã xác minh**, chỉ giữ cấu hình xe từ V3 theo yêu cầu. Trang bị NPC, tên đội quân, loại xe spawn, liên kết vũ khí và điều kiện mở khóa lấy từ original.

| Nhóm | Cấu hình V4 |
|---|---|
| Alec | HP 5500, giới hạn tốc độ 10 m/s, giảm sát thương và hồi phục mạnh kiểu V3 |
| NPC campaign chính | HP đồng minh/dân thường ×3; EDF/Marauder ×2; trang bị gốc |
| Búa | Sát thương của người chơi ×3; phá công trình ×2; tầm và lực hất gốc |
| Súng cầm tay không có mẫu nổ | Damage NPC/xe ×3; nhịp bắn, nạp, độ giật gốc |
| Vũ khí nổ được chọn | Damage NPC/xe ×2; phá công trình và bán kính tác động ×1,5 |
| Thermobaric | Damage ×1,5; bán kính gốc 6,5 m |
| Xe | Đúng giá trị V3 theo từng gói; các trường tốc độ/động cơ được chọn ×1,5 |
| Tiếp viện | Delay ÷2; số quân và đội hình gốc |
| Hoạt động/kinh tế | Timer mục tiêu ×3; courier Escape_Speed ÷3; salvage reward ×3; đạn ×5; giá mua/nâng cấp ÷2 |

Vũ khí có mẫu nổ dùng hệ số nổ thấp hơn, không nhân thêm damage súng ×3. Gauss/nano/grinder thuộc nhóm này. Cỡ băng đạn, giới hạn gắn remote cùng lúc, morale và EDF control giữ gốc; xem [phạm vi và ngoại lệ](reports/campaign-v4.md) để biết chi tiết DLC, timer, phần thưởng và mẫu nổ dùng chung.

## Cài đặt

1. Thoát game và sao lưu hai file `misc.vpp_pc`, `table.vpp_pc` đang dùng.
2. Giải nén ZIP V4; chép **cả hai file VPP** vào thư mục game chứa các file cùng tên và thay thế.
3. V4 là bản đầy đủ, không cần cài chồng V2/V3. Muốn hoàn tác thì chép lại bản sao lưu.

[Hướng dẫn đầy đủ và các điểm cần biết khi chơi](downloads/HUONG_DAN.txt).

Đã kiểm tra 2.947 giá trị thay đổi, cấu trúc VPP, giải nén đối chiếu toàn bộ 1.631 tệp và các cặp min/max; mọi XML sửa đều hợp lệ. Lỗi ký tự có sẵn trong `credits.xtbl` giữ nguyên từng byte. **Chưa chạy thử trong game.**

V4 giảm mạnh khả năng phá hủy so với V3, nhưng nổ/búa vẫn có thể làm chết con tin hoặc sập công trình cần bảo vệ. Súng dùng chung cũng ảnh hưởng NPC cầm cùng loại; một số turret dùng chung mẫu nổ rocket/remote. Cần thử nhiệm vụ giải cứu, hộ tống và demolitions trên save phụ trước khi dùng làm bản chơi chính.

## Tiện ích nhảy cao riêng

[Tiện ích nhảy cao ×2/×3 qua RSL — thử nghiệm](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/RFGRM_Jump_RSL_Experimental.zip) · [Hướng dẫn](jump-addon/README.md).

V4 không chứa hoặc sửa tiện ích này. Tiện ích cần RSL tương thích; đã kiểm tra logic bằng mô phỏng, chưa xác nhận độ cao thực tế trong game.

## Bản và tài liệu cũ

- [Campaign V3 — xe ×1,5](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Vehicle_1_5x.zip) · [Báo cáo V3](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Reports.zip).
- [Campaign V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2.zip) · [Báo cáo V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2_Reports.zip).
- [Đánh giá rủi ro V3](reports/campaign-balance-review.md), [tốc độ xe V3](reports/vehicle-speeds.md), [kiểm tra chuyển động](reports/player-movement.md), [cơ chế và thông số nổ gốc](reports/explosives-reference.md).

Các bảng mang nhãn V3 mô tả V3; dùng báo cáo V4 để đối chiếu bản mới. Cấu hình xe V4 giữ đúng giá trị V3 nên báo cáo xe vẫn có giá trị tham khảo.

Mod Nexus ban đầu: [Ultimate Mod](https://www.nexusmods.com/redfactionguerrillaremarstered/mods/16?tab=description).
