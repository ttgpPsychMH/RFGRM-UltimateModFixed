# Campaign V4.1 — búa mạnh hơn, nhặt salvage nhanh và súng dễ kiểm soát

**[Tải V4.1 đầy đủ](../downloads/Ultimate_Mod_Campaign_v4_1.zip)** ·
[Hướng dẫn](../downloads/HUONG_DAN.txt) · [Báo cáo/mã dựng ZIP](../downloads/Ultimate_Mod_Campaign_v4_1_Reports.zip).

V4.1 dùng V4 đã phát hành làm nền. Mọi hệ số búa tính từ **original từng
đòn**, không nhân từ V4. Chỉ sáu bảng mỗi gói thay đổi; các phần khác giữ V4.

| Nhóm | Cấu hình V4.1 |
|---|---|
| Búa NPCDamage | Original ×10 |
| Búa VehicleDamage | Original ×20 |
| Búa StructureDamage | Original ×5 |
| Búa DefaultDamage | Original ×5 theo đề xuất đã chấp thuận; không cộng với nhánh theo mục tiêu |
| HitRange và SecondaryImpact/HitRange | Original ×1,25 |
| HitRadius | Original ×1,25; các đòn chính 0,4 → 0,5 m |
| ImpactForce / RagdollImpulse | Original ×1,5 |
| Nhặt salvage mới sinh | Thời gian chờ 1000 → 250 ms |
| Salvage sau khi chết | Fraction 0,0 → 1: giữ 100% theo mô tả; thử nghiệm, chưa xác minh runtime |
| Độ giật/tản súng | Recoil_Kick và spread thường/fine aim dương ×0,8 original, giảm 20% |

Giữ V4 ở sát thương Alec nhận, hướng/độ cao/away impulse của đòn, hoạt ảnh,
NPC melee, các cờ, camera shake, ngưỡng đứng trên xe, remote limit và unlock.
Chỉ sửa nhánh Player.xtbl của búa, không tăng mọi nhánh NPC cùng lúc.

## Búa: giá trị V4.1

| Bản | NPCDamage ngang/dọc | VehicleDamage | StructureDamage | DefaultDamage |
|---|---:|---:|---:|---:|
| Thường | 6500 / 7500 | 5000 | 7500 | 7500 |
| Nâng cấp 1 | 8500 / 9500 | 7000 | 10000 | 10000 |
| Nâng cấp 2 | 10500 / 11500 | 9000 | 12500 | 12500 |
| Vàng | 21000 / 23000 | 18000 | 25000 | 25000 |

Tầm ngang/dọc 2,5 / 2,75 m; kiểm tra phụ 2,375 / 2,5 m. small có
DefaultDamage 750 và tầm 0,625; các nhánh riêng đang thiếu không được thêm.
[CSV đủ original/V4/V4.1 của mọi đòn](campaign-v4_1-hammer.csv).

Đây là giá trị cấu hình, không phải damage cuối sau giáp/difficulty. Búa vàng
có lực gốc cao nên vẫn có thể hất mạnh. Không sửa tốc độ vung: schema nói
Default_Refire_Delay bị bỏ qua với melee; event/animation timing giữ V4.
Samanya DLC kế thừa Player skeleton trong dữ liệu, nhưng đường chọn melee
runtime chưa được kiểm thử. Các liên kết đòn di chuyển cũ giữ V4.

## Salvage và điều khiển súng

- Thời gian nhặt 250 ms chỉ rút ngắn chờ đối với salvage mới sinh, không mở
  rộng phạm vi hút. Không tìm được trường bán kính nhặt có nghĩa/đơn vị rõ
  trong hai gói; không giả lập bằng cách tăng mesh/collision hoặc coi
  Value=1 của salvage_collector là khoảng cách.
- Player_death_salvage_percent_kept=1 theo mô tả là giữ toàn bộ; cần thử
  chết và load save để xác nhận engine thực hiện. Đây là phép thử được yêu cầu.
- Giảm 20% Recoil_Kick, Spread_Min/Max, Spread_Fine_Aim_Min/Max dương của
  16 định nghĩa súng/launcher cầm tay campaign. Không sửa entry MP/test.
  Recoil_Kick được schema ghi rõ chỉ áp dụng người chơi; không đổi
  RecoilImpulse hoặc preset rung camera của đánh/nổ.
- Ví dụ M16: recoil 0,9 → 0,72; spread 1/2,3 → 0,8/1,84 độ;
  fine aim 0,7/1,1 → 0,56/0,88 độ. NPC_Spread_Min/Max giữ V4.
  Nhánh thiếu NPC spread vẫn có thể dùng fallback; chưa xác nhận engine.
- Không sửa NPC equipment, tốc độ bắn/nạp, recoil vật lý, giới hạn remote,
  điều kiện mở khóa, ngưỡng ragdoll khi đứng trên xe hoặc lượng salvage rơi.

## Kiểm tra

- **406 thay đổi so V4**, mỗi gói 203; tổng **3237** so original.
  Đếm cả bản sao bảng chung giữa hai gói, không phải số hiệu ứng độc lập.
- Giữ tập tên 1208/423 tệp. Chỉ melee.xtbl, weapons.xtbl, tweak_table.xtbl
  và bản DLC tương ứng thay đổi. Mọi payload khác giữ từng byte của V4.
- Đọc VPP độc lập, kiểm tra header/offset/hash tên/padding/chiều dài,
  giải nén đối chiếu toàn bộ 1631 payload; kiểm tra từng đường dẫn XML,
  công thức theo original và toàn bộ giá trị ngoài phạm vi.
- Mọi XML sửa hợp lệ; không có lỗi min/max mới, gồm fine-aim spread.
  credits.xtbl giữ lỗi ký tự có sẵn từ original và không đổi byte.
- **Chưa chạy thử trong game.** Structure damage ×5 và lực hất cao hơn có
  thể phá nhà, hại con tin/mục tiêu hộ tống. Thử trên save phụ trước.

[Delta V4 → V4.1](campaign-v4_1-parameters.csv) ·
[Toàn bộ original → V4.1](campaign-v4_1-parameters-original.csv) ·
[Policy đầy đủ kế thừa V4](campaign-v4_1-policy.json) ·
[Validation](campaign-v4_1-validation.json) · [Cấu hình nền V4](campaign-v4.md).

```text
5440347d5500aeb430b0bfb042e8d0c4a97fd66aae05e89ba8d1d925b4ad0818  misc.vpp_pc
bf8f648e718704e83f5fa8579316ac28e92cacd87358b3b7d117e1552a357590  table.vpp_pc
```
