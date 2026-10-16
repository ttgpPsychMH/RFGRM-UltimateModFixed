# Kiểm tra walking / running / sprinting — Campaign v3

**Chưa xác nhận vận tốc thực tế của ba trạng thái có bằng nhau hay không.** Dữ liệu hiện có xác nhận một giới hạn chung và các trạng thái chuyển động riêng; không có ba con số m/s riêng có thể đọc trực tiếp rồi so sánh từ hai VPP.

| Mục | Original | Bản hiện tại, cả misc và table |
|---|---|---|
| `character.xtbl` → `rfg_PC/max_speed` | 5 | 10 |
| Walking / running trong bộ hoạt ảnh rifle | Cùng liên kết `player_move_forward_rfl` | Giữ nguyên |
| Sprinting trong bộ hoạt ảnh rifle | `plyr_rfl_spnt.animx` | Giữ nguyên |

Mô tả schema gốc của `max_speed`: **“Max speed of human in meters/second”**. Đây là giới hạn cấu hình, không đủ chứng minh walking, running và sprinting đều có vận tốc đo được 10 m/s. Việc walk/run dùng chung liên kết hoạt ảnh cũng không chứng minh chúng có cùng vận tốc.

Đã đối chiếu từng byte `player.xtbl`, `anim_blend_trees.xtbl`, `anim_files.xtbl`, `anim_states.xtbl` với original: cả bốn tệp đều giữ nguyên trong từng gói. Các bộ hoạt ảnh súng ngắn, RPG, remote charge, búa, vũ khí nặng, shotgun, grinder, sniper, rail và nano cũng có liên kết walk/run giống nhau và một liên kết sprint riêng. Đây là kiểm tra liên kết hoạt ảnh, không phải phép đo tốc độ.

`weapons.xtbl` còn có `Player_Move_Speed`; mô tả gốc là hệ số tốc độ người chơi khi trang bị vũ khí đó. Các trường này vẫn giữ giá trị original trong cả hai gói. Ví dụ búa thường dùng 1.01. Không suy ra một con số vận tốc cuối cùng bằng cách chỉ nhân 10 với hệ số này, vì chưa xác nhận thứ tự áp dụng hệ số và giới hạn trong engine.

## Có thể chỉnh riêng walking / running / sprinting không?

| Cách chỉnh | Kết quả kiểm tra |
|---|---|
| Sửa `rfg_PC/max_speed` trong VPP | Có trường cấu hình và đơn vị m/s; đây là giới hạn chung đã đổi 5 → 10. |
| Đặt ba tốc độ riêng ngay trong các XTBL hiện có | Chưa tìm thấy ba trường cấu hình tốc độ cho người chơi. Các bảng hoạt ảnh phân biệt trạng thái nhưng không cung cấp ba giá trị m/s riêng. |
| Dùng RSL để đọc/ghi thông số lúc game chạy | API xuất các trường có thể ghi `Player.MaxSpeed`, `Player.MoveSpeed`, `Player.StateSpeedThrottle`, cùng `Player.CurrentMovementState` để nhận diện Walk/Run/Sprint. |
| Tự đổi thông số theo từng trạng thái bằng script/hook | Có các điểm can thiệp để thử triển khai; chưa kiểm chứng việc engine có ghi đè lại hay không, tác động đến chuyển trạng thái, gia tốc hoặc vận tốc cuối cùng. Chưa thể gọi đây là cách chỉnh riêng đã hoạt động trong game. |

Đã rà soát tên trường và mô tả trong 422 XTBL đọc được XML của mỗi gói. Các mục dễ nhầm như `Min_ambient_walk_speed_pct` / `Max_ambient_walk_speed_pct` dành cho hoạt ảnh NPC ambient; `Spread_Multiplier_Run` là hệ số tản đạn khi chạy. Chúng không phải ba tốc độ di chuyển của Alec. `credits.xtbl` có lỗi ký tự gốc, giữ nguyên và không dùng cho kết luận này.

RSL có một tính năng riêng trong **General tweaks → Player move speed override**. Mã nguồn giao diện ghi trực tiếp biến toàn cục `Player_max_movement_speed_override`, và phần trợ giúp nói: “If this is set to 0.0, you'll move at the vanilla speed. If you set it to any other value, you'll move at that speed.” Đây là override tốc độ chung, không phải ba thiết lập theo trạng thái.

Nếu đang dùng RSL hoặc tiện ích khác để ghi tốc độ cố định, nên đưa override này về 0/tắt tiện ích đó khi đo sự khác nhau giữa Run và Sprint. Chưa có bằng chứng người dùng đang bật tính năng này, và đây chưa phải chẩn đoán nguyên nhân cảm giác Shift chỉ nhanh hơn ít. Đặt về 0 chỉ tắt override RSL; các VPP đã mod vẫn đang có `max_speed=10`.

Nguồn đối chiếu thêm: [HumanLua.cpp — các binding đọc/ghi](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/HumanLua.cpp#L76), [GeneralTweaksGui.cpp — speed override và trợ giúp](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/GeneralTweaksGui.cpp#L135), [Bootstrapper.cpp — liên kết biến override](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/Bootstrapper.cpp#L488).

## Cách kiểm tra vận tốc thực nếu đã cài RSL

Mã nguồn RSL công khai các trạng thái `Idle=0`, `Walk=1`, `Run=2`, `Sprint=3` và xuất `CurrentMovementState`, `ActualVelocity`, `ActualVelocityMagnitude`, `MoveSpeed`, `MaxSpeed` sang Lua. Có thể đọc chúng lúc đang chơi trên nền phẳng, cùng vũ khí, cùng hướng, không nhảy hay ngồi, để so sánh sau khi đạt vận tốc ổn định.

Ví dụ đoạn **chỉ đọc**, chạy trong RSL khi đang ở campaign, ghi trạng thái và độ lớn vận tốc vào log:

```lua
if Player ~= nil then
    rsl.Log("state={} actual_velocity_magnitude={} move_speed={} max_speed={}\n",
        Player.CurrentMovementState, Player.ActualVelocityMagnitude,
        Player.MoveSpeed, Player.MaxSpeed)
end
```

Độ lớn vận tốc bao gồm cả thành phần đứng khi rơi/nhảy, nên cần điều kiện nền phẳng để so sánh. Đoạn đọc này chưa được chạy thử trong game ở môi trường hiện tại; không có số đo để khẳng định walking/running/sprinting bằng nhau hoặc chênh bao nhiêu.

Nguồn RSL đối chiếu tại commit `59a47203f01c2a81c175bcce7fe37b105e477784`: [HumanLua.cpp](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/HumanLua.cpp#L76), [HumanMovementStates.lua](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/Core/rfg/HumanMovementStates.lua).

Lần kiểm tra này không sửa các thiết lập di chuyển nhân vật. Campaign v3 chỉ giảm các trường tốc độ/động cơ xe đã chọn về ×1,5 original.
