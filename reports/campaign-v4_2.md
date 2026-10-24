# Campaign V4.2 — cải thiện đủ 10 backpacks

**[Tải V4.2 đầy đủ](../downloads/Ultimate_Mod_Campaign_v4_2.zip)** ·
[Hướng dẫn và cách thử](../downloads/HUONG_DAN.txt) ·
[Báo cáo/mã dựng ZIP](../downloads/Ultimate_Mod_Campaign_v4_2_Reports.zip).

V4.2 dùng **V4.1 đã phát hành** làm nền. Chỉ ba bảng trong mỗi VPP thay đổi:
mp_backpacks.xtbl, mp_backpack_overrides.xtbl và hai trường trong explosions.xtbl.
Tất cả búa, súng, Alec, NPC, nhiệm vụ, kinh tế, xe, salvage và camera-shake
ngoài các trường này giữ nguyên V4.1. Không thêm backpack, ID, asset, unlock
hoặc trang bị cho NPC. Các profile là định nghĩa dùng chung với MP/Wrecking Crew;
đây là bản dành cho chơi offline.

## Cấu hình đã áp dụng

| Backpack | Thay đổi chính |
|---|---|
| Jetpack | Tiêu hao 0,3 → 0,075; hồi 0,15 → 0,5; không thêm tham số độ cao/lực nâng chưa xác minh |
| Fleetfoot | Hệ số active 1,45 → 2; tiêu hao/hồi 0,04/0,4; phí/ngưỡng 0,02/0,1; bỏ chặn fine aim của backpack |
| Heal | 450 → 900 HP/s; radius 5,8 → 10; tắt cờ hồi địch ở nhánh active; fuel 0,05/0,4, phí/ngưỡng 0,02/0,1 |
| Rhino | charge_top_speed và trường tốc độ cũ cùng 14; fuel 0,5/0,5, ngưỡng 0,25; cho phép chủ động hủy |
| Thrust | Boost vận tốc dọc 10 → 15; hồi 0,2 → 0,5; ngưỡng 1 → 0,25; damage và delay giữ V4.1 |
| Tremor | Đợt ngắn: tiêu hao 0,5, hồi 0,4, ngưỡng 0,5; damage công trình mp_quake 2500 → 3750/xung; giữ nhịp 300 ms và bán kính |
| Concussion / Shockwave | Tầm ripple 6 → 8; tốc độ hất nhân vật 12 → 18; phí/ngưỡng 0,5/0,5, hồi 0,25; structure blast 15000 → 3000 |
| Firepower / Commando | Direct damage factor 1,25 → 2; area factor 1,25 → 1; reload factor 1 → 0,7; fuel 0,05/0,4, ngưỡng 0,25 |
| Vision | Fuel 0,035/0,4, phí/ngưỡng 0,02/0,1; ramp hiệu ứng vào/ra 250 → 100 ms |
| Stealth | Fuel 0,033/0,4, phí/ngưỡng 0,02/0,1; vào ngụy trang 1000 → 250 ms, tái ngụy trang 1000 → 500 ms |

`fuel` trong bảng viết theo thứ tự tiêu hao/hồi mỗi giây. Chỉ Rhino được đổi
quyền hủy chủ động mới; các điều khiển khác giữ V4.1. Nhịp bắn, unlimited_ammo,
hướng/độ cao va chạm và preset rung camera không được tự tăng/đổi.

Firepower direct factor=2 là bonus trên damage hiện tại; súng nền ×3 có thể
thành ×6 original nếu engine nhân theo nhánh này. Area factor=1 giữ nổ nền
V4.1, không thêm bonus ×1,25 của Firepower cũ. Chưa xác nhận đường tính melee.

## Mô hình năng lượng, không phải kết quả đo trong game

Giả định bình tối đa=1, regen dừng khi active, không có modifier engine/nâng
cấp. Các giá trị sau là phép tính từ cấu hình; nếu giả định sai thì phải đo
và hiệu chỉnh. Kích hoạt trước khi đầy cho thời lượng ngắn hơn.

| Backpack | Thời lượng active từ đầy (s) | Rỗng → đầy (s) | Ghi chú |
|---|---:|---:|---|
| Fleetfoot | 24.5 | 2.5 |  |
| Jetpack | 13.333 | 2 |  |
| Thrust | 1.25 | 2 | Cửa sổ fuel, không phải độ cao/thời lượng quỹ đạo |
| Rhino | 2 | 2 | 14 m/s × 2 s = 28 m chỉ khi không bị cản theo mô hình |
| Concussion | — | 4 | Mô hình 2 lần từ đầy; hồi phí một lần 2 s; nhịp action chưa đo |
| Tremor | 2 | 2.5 |  |
| Firepower | 20 | 2.5 |  |
| Heal | 19.6 | 2.5 |  |
| Vision | 28 | 2.5 |  |
| Stealth | 29.697 | 2.5 |  |

Các giới hạn còn cần thử:

- Jetpack: giảm tiêu hao không bảo đảm tăng trần độ cao hoặc lực nâng.
- Fleetfoot: hệ số 2 chưa chứng minh tốc độ đo được là 20 m/s; engine có thể cap.
- Heal: schema nói players. Hồi NPC/đồng đội/con tin campaign chưa xác nhận;
  đặt cờ heal_enemies=False không tự tạo khả năng hồi NPC.
- Stealth: thay timing ngụy trang chưa chứng minh AI campaign mất dấu.
- Vision: tập đối tượng hiển thị trong campaign chưa kiểm thử.
- Rhino: quãng lao và hủy phụ thuộc input, collision và logic engine.
- Concussion/Tremor vẫn có thể gây sập nhà, va chạm phụ hoặc hại con tin.
  Không có cam kết mọi nhiệm vụ an toàn từ kiểm tra cấu hình.

## Rà soát bảng ghi đè và schema

Commando, Vision và Stealth có override fuel riêng. V4.2 ghi đủ bốn trường
tiêu hao, hồi, phí kích hoạt, ngưỡng kích hoạt trong cả ba override, khớp bảng
chính. Có **7 trường optional thêm mỗi gói**, đều có trong TableDescription;
không thêm tag đoán tên. Không nhân dồn hai profile.

Đã cập nhật cả charge_top_speed có trong schema và rhino_top_speed cũ có sẵn
theo phương án được chấp thuận. Các giá trị legacy khác ở cấp ngoài giữ
nguyên; không tự coi mọi trường trùng tên cùng một chức năng. Không sửa
schema, entry category, số/tên backpack hoặc Unique_ID.

## Xác minh

- **128 thay đổi so V4.1:** 64 mỗi gói, gồm 7 trường optional mới mỗi gói;
  tổng **3365** giá trị khác original, đếm cả bản sao ở hai gói.
- Giữ nguyên tập 1208/423 tên tệp. Mọi payload ngoài ba bảng giữ từng byte.
- Writer được calibration trên V4.1; giải nén đối chiếu 1631 payload.
  Validator độc lập không import patcher, dùng bộ đọc raw VPP và ElementTree
  để kiểm header, hash tên, offset, padding, kích thước và từng route XML.
- Mọi field/schema/type, ID 0..9, nội dung ngoài phạm vi và full audit
  original/V4.2 đã đối chiếu. **24 so sánh fuel** giữa main/override đều khớp.
  Không có vi phạm min/max mới. Mọi XML sửa hợp lệ.
- credits.xtbl giữ lỗi ký tự có sẵn từ original; không đổi byte.
- **Chưa chạy thử trong game.** Không có thử nghiệm runtime giả lập nào được
  dùng để tuyên bố đã đạt độ cao, thời gian hoặc hỗ trợ AI/NPC.

[Delta V4.1 → V4.2](campaign-v4_2-parameters.csv) ·
[Toàn bộ original → V4.2](campaign-v4_2-parameters-original.csv) ·
[Profile chính xác](campaign-v4_2-policy.json) ·
[Mô hình fuel](campaign-v4_2-fuel-model.csv) ·
[Validation](campaign-v4_2-validation.json) · [Nền V4.1](campaign-v4_1.md).

## Thử trên save phụ

Thử Jetpack từ đầy bình và quan sát hồi khi active; so tốc độ Fleetfoot trên
cùng đoạn đường; thử hủy Rhino ở khu vực trống. Kiểm tra Heal lên bản thân
và NPC bị thương ngoài nhiệm vụ khi có cách quan sát HP; vòng hiệu ứng không
đủ chứng minh HP NPC tăng. Thử Stealth/Vision với AI trước khi dùng trong
nhiệm vụ. Xem hướng dẫn ZIP để biết giới hạn và cách hoàn tác.

```text
c62bfe7224a24f02f2ab910037904128dafe4d1907ba2d7af221d6e6e9172430  misc.vpp_pc
50915f809af4d001da0afeace91a27ced297fd2d1460590d415956e8cc60c595  table.vpp_pc
```
