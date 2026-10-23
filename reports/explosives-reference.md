# Thuốc nổ, RPG và các vũ khí nổ — đối chiếu original

Nguồn là hai BACKUP gốc mới nhất đã được xác thực. Các XTBL tương ứng trong hai gói original giống nhau. **Đây là thông tin để chọn cấu hình mới, chưa áp dụng thay đổi gameplay.** Các con số dưới đây là giá trị cấu hình, không phải số đo sát thương cuối cùng đã thử trong game.

[CSV đầy đủ các mẫu nổ](https://raw.githubusercontent.com/ttgpPsychMH/RFGRM-UltimateModFixed/main/reports/explosives-original-reference.csv) · [JSON](explosives-original-reference.json). Có 94 bản ghi, gồm 79 trong Table và 15 trong TableTemplates; có các mục multiplayer, props, test và kịch bản, không phải 94 loại vũ khí có thể cầm.

## Hai lớp cần phân biệt

1. **`weapons.xtbl` / `dlc01_weapons.xtbl`:** vũ khí, đạn, chế độ bắn, thời gian giữa các phát, thông số bay và damage scaling. Trường `Explosion` liên kết tới một mẫu nổ.
2. **`explosions.xtbl` / `dlc01_explosions.xtbl`:** các vùng ảnh hưởng, damage lên công trình/người/xe, lực hất và hệ số riêng cho player/xe của player.

RPG cầm tay `rpg_launcher` thuộc Entries:Guerilla có `Damage_Scaling_Max/NPC_Damage=0`, `Player_Damage=0` và `Vehicle_Damage=-1`; mẫu vụ nổ là **`rocket`**. Remote charge cũng có NPC_Damage=0 ở lớp này và dùng mẫu **`remote_charge`**. Vì thế, nhân trường NPC_Damage=0 trong bảng vũ khí lên 3 vẫn ra 0, không tự làm mẫu vụ nổ mạnh gấp ba. Giá trị -1 là giá trị đặc biệt cần giữ đúng ngữ nghĩa, không tự đổi thành -3 hoặc coi là không có sát thương.

Không mặc nhiên cộng số damage ở hai bảng thành một công thức chung cho mọi loại đạn. Cách xử lý hit, momentum, falloff và vụ nổ phụ thuộc vũ khí và engine; chưa đo thực tế trong game.

## Các vùng tác động và damage có ý nghĩa khác nhau

| Trường | Ý nghĩa theo schema gốc |
|---|---|
| `Radius` / Blast Radius | Bán kính chính, đơn vị mét; cũng là một mốc điều khiển falloff damage người |
| `CrumbleRadius` | Vùng sát thương phụ làm mảnh kết cấu vỡ/rã mà không áp impulse; là mốc damage tối thiểu tới xe |
| `KnockdownRadius` / Human Damage Radius | Khoảng cách damage người giảm về 0; tên trường không chỉ có nghĩa là làm ngã |
| `FlinchRadius` | Vùng khiến NPC giật mình; không phải damage radius chính |
| `Human_Damage_Max` | Damage người tại tâm vụ nổ |
| `human_damage_min` | Damage người tại Blast Radius, sau đó giảm về 0 ở Human Damage Radius |
| `vehicle_damage_max/min` | Các mốc damage xe riêng |
| `Structural_Damage` | Damage lên vật thể phá hủy; schema ghi cách tính khác với damage người/xe |
| `Impulse` | Lực xung tối đa ở tâm, kg·m/s, giảm về 0 ở mép; tăng damage không có nghĩa phải tăng lực hất |
| `player_mult` | Hệ số riêng trong tính damage tới người chơi |
| `player_veh_mult` | Hệ số cho xe của player; theo schema dùng **thay** player_mult, không nhân hai hệ số này với nhau |

Vì có nhiều vùng khác nhau, Blast Radius 3 m không có nghĩa mọi hiệu ứng dừng ở 3 m. Cũng không so trực tiếp Structural_Damage=22.500 với HP người để kết luận sức mạnh tương đối giữa nhà và người.

## Những giá trị original đáng chú ý

Các bán kính tính bằng mét. Damage là giá trị raw của các trường tương ứng, chưa áp falloff/hệ số/logic vật liệu.

| Mẫu nổ | Blast Radius | CrumbleRadius | Human Damage Radius | Structural_Damage | Human_Damage_Max |
|---|---:|---:|---:|---:|---:|
| Remote charge `remote_charge` | 3 | 3,75 | 5,5 | 22.500 | 1.250 |
| Mìn `mine` | 2,75 | 4,5 | 9,5 | 20.000 | 2.500 |
| RPG thường `rocket` | 3,65 | 4 | 6,5 | 23.625 | 1.700 |
| Thermobaric `thermo_rocket` | 6,5 | 7 | 9,5 | 50.000 | 6.000 |
| Rocket turret EDF `turret_rocket` | 4 | 4,5 | 7,5 | 19.000 | 1.000 |
| Đạn tăng trung `edf_mediumtank_shell` | 3 | 4,5 | 6 | 20.000 | 2.000 |
| Đạn tăng nặng `edf_heavytank_shell` | 3,75 | 5,25 | 8 | 25.000 | 3.000 |
| Remote charge DLC `DLC_remote_charge` | 3 | 3,75 | 5,5 | 27.000 | 1.250 |
| Missile Pod DLC `DLC_missilepod` | 2 | 2,5 | 5,5 | 15.000 | 1.000 |

Thermobaric vốn đã có phạm vi và damage lớn. Nhân cùng một hệ số cho mọi mẫu không tạo ra một mức mạnh tương đương nhau.

## Nếu áp đúng bán kính ×2, damage ×3 từ original

Đây là các phép tính minh họa **có điều kiện**, không phải cấu hình đã chốt hay đã cài:

| Mẫu | Blast Radius dự kiến | CrumbleRadius dự kiến | Structural_Damage dự kiến |
|---|---:|---:|---:|
| Remote charge | 6 m | 7,5 m | 67.500 |
| Mìn | 5,5 m | 9 m | 60.000 |
| RPG thường | 7,3 m | 8 m | 70.875 |
| Thermobaric | 13 m | 14 m | 150.000 |
| Remote charge DLC | 6 m | 7,5 m | 81.000 |

Thermobaric 13 m là **đường kính 26 m** cho vùng Blast Radius; vùng phá phụ 14 m tương ứng đường kính 28 m. Bán kính ×2 bao phủ diện tích hình tròn ×4 về mặt hình học; không có nghĩa damage ở mọi nơi ×4. Trong khu nhà có con tin hoặc xe cần bảo vệ, đây vẫn là mức ảnh hưởng rất lớn.

Khi tăng Radius, còn phải chốt Human Damage Radius và FlinchRadius. Ví dụ remote charge Radius mới 6 m sẽ vượt Human Damage Radius gốc 5,5 m; giữ nguyên toàn bộ các mốc còn lại sẽ thay quan hệ của đường cong falloff. Nếu muốn giữ đúng tỷ lệ vùng tác động gốc, phương án là các bán kính remote charge lần lượt **6 / 7,5 / 11 / 18 m**. Đây là điểm cần xác nhận trong cấu hình mới, không tự áp thêm trong lần cung cấp thông tin này.

## Mẫu nổ dùng chung: chỉnh một tên có thể ảnh hưởng nhiều vũ khí

Đã kiểm tra các liên kết `Explosion` trong bảng vũ khí original:

- **`remote_charge`:** được `charge_placer` dùng, đồng thời `turret_supergauss_solo` và `turret_supergauss_burst` cũng trỏ tới nó; còn `charge_launcher` trong TableTemplates/Entries:Old. Vì vậy, ngay cả “chỉ sửa mẫu remote_charge” cũng chưa chứng minh chỉ thuốc nổ cầm tay của Alec được tăng.
- **`rocket`:** dùng bởi RPG cầm tay và các mục `turret_rocket_standing`, `turret_rocket_vehicle`, `turret_rocket_slow`, `turret_rocket_nogunner`, cùng bản debug.
- **`mine`:** dùng bởi mìn campaign, bản MP override và một turret mang tên TEST.
- **`thermo_rocket`:** dùng bởi thermobaric campaign và bản debug.
- **`DLC_remote_charge`:** liên kết vũ khí tìm được là `mar_charge_placer`.
- **`DLC_missilepod`:** liên kết vũ khí tìm được là `missilepod` của DLC.

Đây là các liên kết trong bảng đã cung cấp, không chứng minh tất cả mục đều xuất hiện trong phần chơi hiện tại, và chưa thống kê lời gọi trực tiếp từ script/executable ngoài các bảng đó.

Muốn tăng riêng vụ nổ cho một bản ghi vũ khí cầm tay mà giữ turret gốc, có thể nghiên cứu tách thành mẫu nổ riêng rồi đổi liên kết của vũ khí đó. Cần kiểm tra tên/ID và khả năng nạp trong game; chưa triển khai. Ngay cả khi tách khỏi turret, NPC nào dùng cùng bản ghi vũ khí cầm tay vẫn có thể hưởng thay đổi. Phân biệt tuyệt đối đạn Alec với đạn NPC cần cách xử lý theo nguồn gây sát thương đã được kiểm chứng.

## Đạn, tốc độ bắn và cách bay là các chỉnh sửa độc lập

| Vũ khí campaign | Băng đạn | Max_Rounds | Max_Rounds_Upgrade | Refire gốc |
|---|---:|---:|---:|---:|
| Remote charge | Không dùng như súng bắn đạn | 18 | 30 | Không suy từ refire của súng |
| Mìn | Không dùng như súng bắn đạn | 8 | 16 | Không suy từ refire của súng |
| RPG thường | 3 | 9 | 18 | 600 ms |
| Thermobaric | 1 | 4 | 8 | 1.500 ms |
| Missile Pod DLC | 9 | 36 | 63 | 200 ms |

`Max_Rounds` là giới hạn lượng đạn player có thể mang, không tự coi là số đạn dự trữ ngoài băng rồi cộng thêm băng. Tăng lượng đạn mang theo không bắt buộc tăng băng đạn, tốc độ bắn, tốc độ bay hoặc bán kính nổ.

RPG gốc có vận tốc phóng 20 m/s, Max_Speed 100; thermobaric 25 và 50. Các cờ projectile khác nhau: RPG nổ khi va chạm; thermobaric có `allow mid air detonation`; remote charge có các cờ bám va chạm và kích nổ khi bị vụ nổ tác động. Không tự thay các cờ này chỉ để tăng damage. Nổ dây chuyền là một lý do nữa khiến tăng vùng ảnh hưởng có thể phá nhiều hơn dự kiến.

Không nên nhân toàn bộ các mẫu nổ chỉ vì chúng nằm trong cùng file. Có mẫu cho xe/thùng chứa và các mục có tên như `raid_demolish_building`, `wmr_bridge`, `mis_dfa_jail`, `mis_sye_plane_exp`; cần rà vai trò kịch bản trước khi đổi. Các giá trị 0, -1 hoặc trường thiếu phải giữ đúng ngữ nghĩa, không tự nhân thành giá trị mới hoặc coi là không có tác dụng.

## Khuyến nghị để chọn phạm vi bản mới

Ưu tiên tách ba quyết định: **thuốc nổ đặt**, **RPG/rocket cầm tay**, và **vụ nổ của NPC/xe/môi trường/kịch bản**. Có thể chọn tăng damage RPG nhưng giữ bán kính gốc; tăng đạn để dùng thoải mái; giữ thermobaric và các mục kịch bản nguyên bản trước. Đây là đề xuất để cân nhắc, chưa thay cho các hệ số người dùng đã yêu cầu.

Đặc biệt, cần xử lý các liên kết dùng chung trước khi tuyên bố “chỉ buff vũ khí Alec”. Giữ player gần như chúa không bảo vệ được con tin, cột nhà hoặc mục tiêu nhiệm vụ khỏi những vùng nổ tăng mạnh.
