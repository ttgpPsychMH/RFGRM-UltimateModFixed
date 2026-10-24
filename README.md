# RFGRM Ultimate Mod Fixed

Bản mod cho **Red Faction Guerrilla Re-Mars-tered**, dùng để chơi offline.

## Tải bản mới nhất — Campaign V4.1

**[Tải V4.1 — khoảng 16,0 MiB](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4_1.zip)** — gồm `misc.vpp_pc`, `table.vpp_pc`, hướng dẫn và SHA-256.

[Báo cáo và mã dựng](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4_1_Reports.zip) · [Chi tiết V4.1](reports/campaign-v4_1.md) · [Delta V4 → V4.1](reports/campaign-v4_1-parameters.csv) · [Mọi giá trị original → V4.1](reports/campaign-v4_1-parameters-original.csv) · [Kiểm tra](reports/campaign-v4_1-validation.json) · [SHA-256](downloads/SHA256SUMS.txt).

V4.1 cập nhật búa và tiện ích salvage trên nền V4 đã dựng từ original. Các hệ số bên dưới tính từ **original từng đòn**, không nhân từ V4.

| Nhóm | V4.1 |
|---|---|
| Búa: NPC / xe / công trình | Damage ×10 / ×20 / ×5 |
| Búa: DefaultDamage | ×5, nhánh chung riêng với damage từng loại mục tiêu |
| Búa: tầm chính/phụ và bán kính xét trúng | ×1,25; tầm ngang/dọc 2,5/2,75 m, bán kính chính 0,5 m |
| Búa: lực va chạm / ragdoll | ×1,5; giữ hướng/độ cao/away impulse và animation timing |
| Nhặt salvage mới sinh | Chờ 250 ms thay cho 1000 ms |
| Salvage sau khi chết | Đặt mức giữ 100% theo mô tả trường; cần thử runtime |
| Giật/tản súng | Các trường dương recoil camera và spread thường/fine aim giảm 20% |
| Camera shake, đứng trên xe, giới hạn remote | Giữ V4 theo lựa chọn của người dùng |

Chỉ sửa sáu bảng trong mỗi gói: melee, weapons, tweak_table và các bản DLC. Không tìm được trường bán kính nhặt salvage có nghĩa rõ trong hai gói nên giữ phần đó; không đổi kích thước mesh/va chạm để giả lập hút đồ.

Cấu hình nền [V4](reports/campaign-v4.md) giữ lại: Alec HP 5500 và giới hạn tốc độ 10 m/s; NPC đồng minh ×3/địch ×2 với trang bị gốc; damage súng thường ×3, nhóm nổ được chọn ×1,5–×2; xe theo V3; tiếp viện delay ÷2; timer mục tiêu ×3, courier Escape_Speed ÷3, salvage reward ×3, đạn ×5 và giá mua/nâng cấp ÷2 trong phạm vi đã chọn. Xem [policy đầy đủ V4.1](reports/campaign-v4_1-policy.json) và hướng dẫn để biết ngoại lệ.

## Cài đặt

1. Thoát game và sao lưu `misc.vpp_pc`, `table.vpp_pc` đang dùng.
2. Giải nén ZIP V4.1; chép **cả hai file VPP** vào thư mục game chứa các file cùng tên và thay thế.
3. Đây là bản đầy đủ, không cần cài V4 trước. Hoàn tác bằng bản sao lưu.

[Hướng dẫn đầy đủ](downloads/HUONG_DAN.txt) · [Toàn bộ đòn búa original/V4/V4.1](reports/campaign-v4_1-hammer.csv).

Đã kiểm tra **406 giá trị đổi so V4**, toàn bộ **3.237 giá trị so original**, cấu trúc VPP, giải nén đối chiếu 1.631 tệp và min/max, gồm fine-aim spread. Mọi XML sửa hợp lệ; lỗi ký tự có sẵn trong `credits.xtbl` giữ nguyên từng byte. Hai ZIP V4 cũ giữ nguyên.

**Chưa chạy thử trong game.** Búa phá công trình ×5 và lực hất cao hơn có thể làm sập nhà hoặc hại con tin/mục tiêu hộ tống. Giữ salvage sau khi chết được đặt theo mô tả trong bảng, cần xác nhận khi chơi. Nên thử giải cứu/hộ tống/demolitions và chết/load save trên save phụ.

## Tiện ích nhảy cao riêng

[Tiện ích nhảy cao ×2/×3 qua RSL — thử nghiệm](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/RFGRM_Jump_RSL_Experimental.zip) · [Hướng dẫn](jump-addon/README.md).

V4.1 không chứa hoặc sửa tiện ích này. Tiện ích cần RSL tương thích; đã kiểm tra logic bằng mô phỏng, chưa xác nhận độ cao thực tế trong game.

## Bản và tài liệu cũ

- [Campaign V4](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4.zip) · [Báo cáo V4](reports/campaign-v4.md) · [Thông số búa original/V4](reports/hammer-reference.md).
- [Campaign V3 — xe ×1,5](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Vehicle_1_5x.zip) · [Báo cáo V3](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Reports.zip).
- [Campaign V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2.zip) · [Báo cáo V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2_Reports.zip).
- [Đánh giá rủi ro V3](reports/campaign-balance-review.md), [tốc độ xe V3](reports/vehicle-speeds.md), [kiểm tra chuyển động](reports/player-movement.md), [cơ chế và thông số nổ gốc](reports/explosives-reference.md).

Các báo cáo mang tên V4 hoặc cũ hơn mô tả đúng phiên bản đó; dùng báo cáo V4.1 để đối chiếu bản mới. Cấu hình xe V4.1 vẫn giữ V3 theo từng gói.

Mod Nexus ban đầu: [Ultimate Mod](https://www.nexusmods.com/redfactionguerrillaremarstered/mods/16?tab=description).
