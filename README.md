# RFGRM Ultimate Mod Fixed

Bản mod cho **Red Faction Guerrilla Re-Mars-tered**, dùng để chơi offline.

## Tải bản mới nhất — Campaign V4.2 Backpacks

**[Tải V4.2 đầy đủ — khoảng 16,0 MiB](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4_2.zip)** — chứa `misc.vpp_pc`, `table.vpp_pc`, hướng dẫn và SHA-256.

[Chi tiết V4.2](reports/campaign-v4_2.md) · [Báo cáo và mã dựng ZIP](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4_2_Reports.zip) · [Từng thay đổi V4.1 → V4.2](reports/campaign-v4_2-parameters.csv) · [Validation](reports/campaign-v4_2-validation.json) · [SHA-256](downloads/SHA256SUMS.txt).

V4.2 điều chỉnh đủ 10 backpack trên nền V4.1. Các thiết lập Alec, búa, súng, NPC, nhiệm vụ, kinh tế, xe và salvage ngoài phạm vi backpack giữ nguyên V4.1.

| Backpack | Cấu hình mới chính |
|---|---|
| Jetpack | Tiêu hao 0,075/s, hồi 0,5/s; chưa xác minh trần độ cao/lực nâng |
| Fleetfoot | Hệ số active ×2; tiêu hao thấp hơn; bỏ chặn fine aim của backpack |
| Heal | 900 HP/s, radius 10; tắt cờ hồi địch; thời lượng dài hơn theo mô hình fuel |
| Rhino | Tốc độ cấu hình 14 m/s, tiêu hao thấp hơn, hồi nhanh hơn, cho chủ động hủy |
| Thrust | Boost vận tốc dọc 10 → 15; hồi nhanh hơn và bật được khi chưa đầy |
| Tremor | Đợt ngắn, hồi nhanh; damage công trình mỗi xung ×1,5; giữ bán kính/nhịp xung |
| Concussion | Tầm đẩy 8, lực hất nhân vật ×1,5; damage công trình của mẫu nổ giảm 80% |
| Firepower | Direct damage factor 2; reload factor 0,7; area damage factor 1 |
| Vision | Dùng lâu hơn theo fuel, hiệu ứng chuyển nhanh hơn |
| Stealth | Dùng lâu hơn theo fuel, vào/tái ngụy trang nhanh hơn |

**Thời gian trong [bảng fuel](reports/campaign-v4_2-fuel-model.csv) là mô hình, chưa đo trong game.** Jetpack bay lâu hơn không bảo đảm tăng trần độ cao; Fleetfoot chưa xác nhận đạt 20 m/s thực tế. Heal lên NPC và Stealth/Vision với AI campaign cần thử riêng. Tham số nằm trong các bảng dùng chung MP/Wrecking Crew; không có cam kết chỉ ảnh hưởng riêng Alec trong mọi chế độ.

## Cài đặt

1. Thoát game, sao lưu `misc.vpp_pc` và `table.vpp_pc` đang dùng.
2. Giải nén ZIP V4.2; thay **cả hai VPP** trong thư mục game chứa các file cùng tên.
3. Đây là gói đầy đủ, không cần cài bản trước. Hoàn tác bằng bản sao lưu hoặc ZIP V4.1 cũ.

[Hướng dẫn đầy đủ và cách thử từng backpack](downloads/HUONG_DAN.txt).

Đã kiểm tra **128 thay đổi so V4.1**, gồm 14 trường fuel optional thêm vào override của hai gói. Chỉ ba bảng mỗi gói đổi. Validator riêng kiểm tra header/offset/hash/padding, toàn bộ 1.631 payload, từng đường dẫn XML, ID, schema/type và 24 đối chiếu fuel giữa bảng chính/ghi đè. Không có lỗi min/max mới. Mọi XML sửa hợp lệ; `credits.xtbl` giữ lỗi ký tự có sẵn từ original.

**Chưa chạy thử trong game.** Nên thử trên save phụ ở khu vực trống; các backpack phá hủy vẫn có thể hại con tin hoặc công trình nhiệm vụ. Hai ZIP V4 và hai ZIP V4.1 cũ giữ nguyên để hoàn tác.

Nền [V4.1](reports/campaign-v4_1.md): Alec HP 5500 / giới hạn tốc độ 10 m/s; búa NPC ×10, xe ×20, công trình ×5; NPC đồng minh ×3/địch ×2; đạn ×5; cải thiện salvage và giảm giật/tản súng. Xem báo cáo phiên bản để biết đầy đủ phạm vi và ngoại lệ.

## Tiện ích nhảy cao riêng

[Tiện ích nhảy cao ×2/×3 qua RSL — thử nghiệm](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/RFGRM_Jump_RSL_Experimental.zip) · [Hướng dẫn](jump-addon/README.md).

V4.2 không chứa hoặc sửa tiện ích này. Tiện ích cần RSL tương thích; đã kiểm tra logic bằng mô phỏng, chưa xác nhận độ cao thực tế trong game.

## Bản và tài liệu cũ

- [Campaign V4.1 — búa và tiện ích salvage/súng](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4_1.zip) · [Cấu hình V4.1](reports/campaign-v4_1.md) · [Hướng dẫn V4.1](downloads/HUONG_DAN_V4_1.txt).
- [Campaign V4](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v4.zip) · [Báo cáo V4](reports/campaign-v4.md) · [Thông số búa original/V4](reports/hammer-reference.md).
- [Campaign V3 — xe ×1,5](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Vehicle_1_5x.zip) · [Báo cáo V3](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v3_Reports.zip).
- [Campaign V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2.zip) · [Báo cáo V2](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/raw/refs/heads/main/downloads/Ultimate_Mod_Campaign_v2_Reports.zip).
- [Đánh giá rủi ro V3](reports/campaign-balance-review.md), [tốc độ xe V3](reports/vehicle-speeds.md), [kiểm tra chuyển động](reports/player-movement.md), [cơ chế và thông số nổ gốc](reports/explosives-reference.md).

Các báo cáo có nhãn phiên bản mô tả đúng phiên bản đó; dùng báo cáo V4.2 để đối chiếu bản mới. Cấu hình xe V4.2 vẫn giữ V3 theo từng gói.

Mod Nexus ban đầu: [Ultimate Mod](https://www.nexusmods.com/redfactionguerrillaremarstered/mods/16?tab=description).
