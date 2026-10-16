# Nhảy cao ×2 / ×3 — tiện ích RSL thử nghiệm

Tiện ích cho **Red Faction Guerrilla Re-Mars-tered, campaign offline**, dùng cùng bản Campaign v2. Không cần thay lại hai VPP.

## Yêu cầu

Cài **RSL 1 (Re-mars-tered Script Loader)** tương thích với phiên bản game đang dùng. Đây là phần phụ thuộc riêng, không nằm trong ZIP tiện ích. Xem [dự án RSL](https://github.com/rfg-modding/RSL) và [hướng dẫn cài đặt của RSL](https://rsl.readthedocs.io/en/latest/Installation.html). Chưa kiểm tra việc cài RSL hay khả năng tương thích với bản game cụ thể của người dùng.

## Cách dùng

1. Chép `RFGRM_Jump.lua` vào thư mục con `RSL/Scripts/RFGRM Jump/` trong thư mục game. Tạo thư mục con nếu cần.
2. Vào campaign. Đảm bảo tùy chọn **Custom player jump height** trong menu General tweaks của RSL đang tắt; tắt các tiện ích nhảy khác trước khi lấy giá trị gốc. Nếu trước đó đã dùng tiện ích chỉnh nhảy, khởi động lại game để lấy lại giá trị chưa bị sửa.
3. Trong giao diện Scripts/Script editor của RSL, chọn và chạy `RFGRM_Jump.lua`. RSL mặc định dùng F1 để mở overlay, F2 cho script editor; phím có thể khác nếu đã tùy chỉnh.
4. Script đọc giá trị `Player.CodeDrivenJumpHeight` đang có, lưu làm mốc rồi đặt hệ số **×2**. Nếu chưa đọc được số dương hợp lệ, script không ghi đè; thử nhảy thường một lần rồi kiểm tra log RSL.
5. Muốn đổi, chạy một trong các lệnh sau trong Lua console của RSL:

```lua
RFGRM_SetJumpMultiplier(2) -- tăng trường độ cao lên 2 lần mốc đã lưu
RFGRM_SetJumpMultiplier(3) -- tăng trường độ cao lên 3 lần mốc đã lưu
RFGRM_SetJumpMultiplier(1) -- trả về mốc đã lưu
```

Chạy lại script hoặc đổi ×2 → ×3 không nhân chồng lên kết quả trước. Muốn gỡ: trả hệ số về 1, thoát game, xóa file script và khởi động lại. Script không tự chạy khi khởi động; cần chọn chạy sau khi vào campaign mỗi lần mở game. Nếu RSL đã bị reset toàn bộ event trong cùng phiên chơi, khởi động lại game trước khi dùng lại tiện ích.

## Phạm vi và giới hạn

- Chỉ ghi trường `CodeDrivenJumpHeight` của `Player` ở mỗi frame; không đổi tốc độ chạy 10 m/s, trọng lực toàn thế giới, HP, súng, xe hoặc hai VPP.
- Nhân **trường độ cao**, không nhân vận tốc bật nhảy. Không giả định giá trị gốc luôn là 1.2 hoặc đơn vị chắc chắn là mét.
- Nếu một mod khác đã chỉnh trường này trước khi chạy script, giá trị đó sẽ trở thành mốc. Khi load lại hoặc đổi nhân vật, script lấy mốc từ đối tượng người chơi mới; nếu trường đang bằng kết quả tiện ích vừa đặt thì giữ mốc cũ để tránh nhân chồng.
- Đã kiểm tra logic Lua với dữ liệu mô phỏng. **Chưa chạy trong game:** chưa xác nhận độ cao đỉnh nhảy thực tế đúng ×2/×3, va chạm trần, hoạt ảnh, tiếp đất hay chuyển màn. Nên thử ×2 trước ở khu đất trống; ×3 có thể vượt vật cản và ảnh hưởng trình tự nhiệm vụ.
- Ngưỡng sát thương rơi trong VPP chưa được nâng theo mức nhảy. Hệ số bảo vệ nhân vật hiện tại không bảo đảm mọi tình huống rơi từ trên cao đều vô hại.

## Cơ sở kỹ thuật

Đối chiếu mã nguồn RSL tại commit `59a47203f01c2a81c175bcce7fe37b105e477784`:

- [GeneralTweaksGui.cpp](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/GeneralTweaksGui.cpp#L132): giao diện “Custom player jump height”.
- [PlayerDoFrame.cpp](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/PlayerDoFrame.cpp#L107): tính năng đó ghi `PlayerPtr->CodeDrivenJumpHeight` mỗi frame.
- [HumanLua.cpp](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/RSL/HumanLua.cpp#L202): xuất trường này sang Lua.
- [DoFrameEventExample.lua](https://github.com/rfg-modding/RSL/blob/59a47203f01c2a81c175bcce7fe37b105e477784/Content/Scripts/Included%20scripts/Examples/DoFrameEventExample.lua): API đăng ký `FrameUpdate`.

Các nguồn này xác nhận điểm chỉnh trong bộ nhớ và API Lua; không thay thế thử nghiệm trong game.
