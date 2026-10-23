# Búa trong original và Campaign V4: tham số, hoạt ảnh và hướng tinh chỉnh

Đối chiếu từ hai BACKUP gốc và V4 đã phát hành. Đây là báo cáo đọc dữ liệu;
**không thay đổi hai VPP hoặc ZIP mod V4**, chưa kiểm thử hành vi trong game.

- [Toàn bộ 4.977 trường cấu hình trực tiếp, gốc/V4 và giải thích từng trường](hammer-parameters-original-v4.csv).
- [Các đòn búa của người chơi: sát thương, tầm, lực và hoạt ảnh](hammer-moves-original-v4.csv).
- [Mọi cấp nâng cấp búa: giá, Value, điều kiện mở khóa](hammer-upgrades-original-v4.csv).
- [Dữ liệu XML của 294 bản ghi đã chọn, glossary và SHA-256 nguồn](hammer-reference-data.json).
- [Tải toàn bộ báo cáo dạng ZIP](../downloads/RFGRM_Hammer_V4_Reference.zip).

4.977 trường không phải 4.977 nút chỉnh sức mạnh độc lập: có trường văn bản,
tài nguyên hiển thị, animation event và các bản sao DLC. Phạm vi gồm toàn bộ
giá trị lá của các bản ghi búa được chọn trong 17 file cấu hình trực tiếp;
không phải toàn bộ mã engine hoặc dữ liệu nhị phân của mesh/animation.
Các file được chọn giống nhau giữa misc/table ở cả original và V4.

## Vì sao V4 có thể cho cảm giác búa yếu

1. V4 chỉ tăng **NPC/default/vehicle damage ×3, structure damage ×2**.
   V3 từng tăng các nhánh sát thương thường ×50, nâng cấp ×20 và vàng ×100.
   Riêng StructureDamage thường 75000 → 3000, vàng 500000 → 10000 giữa V3/V4.
2. Một số xe vẫn HP ×5 theo cấu hình V3; búa lên xe chỉ ×3. Với đúng những xe
   được tăng HP, tỷ lệ damage/HP mỗi cú chỉ khoảng 3/5 của original trước các
   hệ số khác. Điều này không áp dụng cho mọi xe hoặc suy ra chính xác số cú.
3. Kẻ địch HP ×2; búa NPC damage ×3 nên ưu thế tỷ lệ chỉ khoảng ×1,5 so với
   original trước giáp, difficulty và cơ chế trúng đòn.
4. `Damage_multiplier_melee_heavy_armor=0.6` giữ gốc: schema mô tả hệ số
   sát thương cận chiến lên người mặc giáp nặng trong single player.
   Các hệ số difficulty như enemy damage taken cũng giữ gốc. Không thể coi
   NPCDamage ghi trong bảng là số HP chắc chắn mất sau mọi loại giáp.
5. Tầm, vùng xét trúng, xung lực và animation timing giữ gốc. Tăng damage
   không làm đòn dễ chạm mục tiêu hơn, vung nhanh hơn hoặc hất xa hơn.
   Alec chạy nhanh cũng có thể khiến người chơi dễ chạy lố tầm đánh.

Ví dụ đòn đứng thường: `DefaultDamage=4500`, `NPCDamage=2250`,
`StructureDamage=3000`, `VehicleDamage=750` trong V4. Đây là các nhánh khác
nhau, **không cộng thành một tổng sát thương 10500**. Quy tắc fallback cuối
cùng khi thiếu nhánh cần kiểm tra engine, không suy từ tên trường là đủ.

## Bốn lớp cấu hình cần phân biệt

| Lớp | Nơi chứa | Vai trò |
|---|---|---|
| Vũ khí | weapons.xtbl, dlc01_weapons.xtbl | Chọn loại búa, nhóm hoạt ảnh và liên kết đòn đánh |
| Đòn đánh | melee.xtbl, dlc01_melee.xtbl | Sát thương theo mục tiêu, va chạm và xung lực theo animset |
| Hoạt ảnh | player.xtbl, anim_files.xtbl và bản DLC | Gán action sang asset; đánh dấu frame va chạm và trả điều khiển di chuyển |
| Chung/hiển thị/tiến trình | tweak_table, camera_shake, rfg_melee_groups, upgrades, items_* | Giáp, hỗ trợ quay mặt, rung màn hình, hiệu ứng, model và mở khóa |

Alec `rfg_PC` dùng `Anim_Set=Player.xtbl`; `Male.xtbl` trong melee là nhánh
khác, không nên tăng mọi nhánh cùng lúc nếu chỉ muốn tăng búa người chơi.
Nhân vật DLC `rfg_PC_DLC` dùng `Samanya.xtbl`; `samanya.xtbl` có
`Parent_Skeleton=Player`. Dữ liệu cho thấy quan hệ kế thừa animation, nhưng
chưa chứng minh đường fallback chọn damage melee trong engine ở mọi trường hợp DLC.

## Sát thương tất cả đòn búa của Player.xtbl

Mỗi ô là **original → V4**; các con số là dữ liệu cấu hình, không phải kết quả
đã đo sau difficulty/giáp/vật lý. Các đòn tương ứng thường/u1/u2 trong DLC có
cùng các giá trị dưới đây. Bảng CSV còn bao gồm toàn bộ trường khác và DLC.

| Đòn | DefaultDamage | NPCDamage | StructureDamage | VehicleDamage |
|---|---:|---:|---:|---:|
| Thường ngang, side | 1500 → 4500 | 650 → 1950 | 1500 → 3000 | 250 → 750 |
| Thường dọc, vert | 1500 → 4500 | 750 → 2250 | 1500 → 3000 | 250 → 750 |
| Nâng cấp 1 ngang | 2000 → 6000 | 850 → 2550 | 2000 → 4000 | 350 → 1050 |
| Nâng cấp 1 dọc | 2000 → 6000 | 950 → 2850 | 2000 → 4000 | 350 → 1050 |
| Nâng cấp 2 ngang | 2500 → 7500 | 1050 → 3150 | 2500 → 5000 | 450 → 1350 |
| Nâng cấp 2 dọc | 2500 → 7500 | 1150 → 3450 | 2500 → 5000 | 450 → 1350 |
| Vàng ngang | 5000 → 15000 | 2100 → 6300 | 5000 → 10000 | 900 → 2700 |
| Vàng dọc | 5000 → 15000 | 2300 → 6900 | 5000 → 10000 | 900 → 2700 |
| small | 150 → 450 | Không khai báo | Không khai báo | Không khai báo |

`small` là tên bản ghi, không đủ cơ sở gán nó thành nút bấm hoặc kết luận
người chơi thường xuyên dùng nó. Không khai báo khác với có giá trị 0;
chưa xác nhận fallback của ba nhánh thiếu này trong engine.

| Trường sát thương khác | Ý nghĩa / V4 |
|---|---|
| PlayerDamageFromNPC | Sát thương vào người chơi từ NPC; đòn dọc Player 750 → 37,5, ngang 650 → 32,5; không phải damage Alec gây ra |
| PlayerDamageFromPlayer | Schema cho phép khai báo riêng; nếu vắng thì kế thừa PlayerDamageFromNPC theo mô tả schema. Không có trong nhánh búa Player đang xét |
| MeleeMove/DefaultDamage/NPCDamage | Trường cấp ngoài có sẵn từ gốc, thường 150; giữ gốc. Không đồng nhất nó với AnimSet/Damage/NPCDamage |
| MeleeMove/DefaultDamage/PlayerDamage | Trường cấp ngoài vào người chơi: thường dọc 1500 → 75, ngang 1250 → 62,5; V4 giảm riêng |
| MeleeMove/DefaultDamage/OnlineDamage | Trường online cấp ngoài, giữ gốc; không dùng làm hệ số sức mạnh búa offline |

Một số trường cấp ngoài không còn xuất hiện trong TableDescription hiện tại.
Chúng vẫn có trong dữ liệu gốc; không có cơ sở tuyên bố tất cả đều bị engine bỏ qua.

## Tầm và va chạm

Các giá trị sau **original = V4**, giống nhau ở các bản thường/u1/u2/vàng.

| Trường trong Player AnimSet | Ngang | Dọc | small | Chức năng |
|---|---:|---:|---:|---|
| AttackPoint | Weapon | Weapon | Weapon | Xét điểm tiếp xúc tại vũ khí |
| HitRange | 2,0 | 2,2 | 0,5 | Tầm xét trúng; không mặc định cộng mọi chiều với HitRadius để suy ra tầm cuối |
| HitRadius | 0,4 | 0,4 | 0,25 | Bán kính cầu quét va chạm, mét; không phải bán kính nổ |
| HitHeight | 1,4 | 1,3 | 1,4 | Độ cao xét trúng; tác động phụ thuộc hình học/controller |
| SecondaryImpact/HitRange | 1,9 | 2,0 | 0,5 | Tầm kiểm tra va chạm bổ sung từ tâm controller |
| SecondaryImpact/HitHeight | 1,4 | 1,3 | 1,4 | Độ cao kiểm tra phụ tính từ chân nhân vật theo schema |
| HitDirection | (0,0,1) | (0,0,1) | (0,0,1) | Vector hướng tác động; chưa xác nhận hệ trục quy chiếu cuối của engine |

Mở rộng HitRadius giúp dễ trúng vật thể ở cạnh đường vung nhưng có thể chạm
người/vật bên cạnh. Đây không phải công cụ bảo đảm đánh nhiều mục tiêu cùng
lúc hoặc xuyên tường. Khi tăng tầm nên xét cả SecondaryImpact; không chỉ
thay một con số ở weapons.Range_Max.

## Lực va chạm và hất văng

Toàn bộ giá trị sau **giữ gốc trong V4**.

| Bản | ImpactForce ngang/dọc | RagdollImpulse ngang/dọc | AwayImpulseScale ngang/dọc |
|---|---:|---:|---:|
| Thường | 350 / 300 | 140 / 80 | 0,25 / 1,0 |
| Nâng cấp 1 | 400 / 350 | 170 / 110 | 0,25 / 1,0 |
| Nâng cấp 2 | 450 / 400 | 210 / 150 | 0,25 / 1,0 |
| Vàng | 900 / 800 | 420 / 300 | 0,25 / 1,0 |
| small | 350 | 160 | 0,25 |

- **ImpactForce:** schema mô tả xung lực áp lên vật bị đánh, khác với trừ HP.
- **RagdollImpulse:** xung lực lúc bắt đầu ragdoll; tăng nó không tự bảo đảm
  mục tiêu đủ điều kiện ngã hoặc chết, và không bảo đảm xe nặng bay đi.
- **AwayImpulseScale:** thêm thành phần hất ra xa người đánh. Nếu vừa tăng
  force vừa tăng hệ số này, tác động có thể mạnh hơn dự kiến.

Không xác nhận đơn vị lực/khối lượng cuối cùng chỉ từ XML. Lực hất cao có
thể làm mảnh vỡ, xe hoặc NPC va vào mục tiêu nhiệm vụ dù HP damage vừa phải.

## Cờ và hỗ trợ ngắm cận chiến

| Cờ/trường | Hiện trạng | Ý nghĩa và giới hạn |
|---|---|---|
| structural damage | Có ở nhánh Player của các đòn chính; small không có | Cờ cho xử lý phá công trình; kết quả còn phụ thuộc StructureDamage và engine |
| always knock down | Schema cho phép, chưa bật ở nhánh búa Player | Yêu cầu làm ngã theo cơ chế engine; không tự lọc chỉ quân địch, không cam kết áp dụng mọi actor |
| npc knockback | Schema cho phép, chưa bật | Cờ liên quan đẩy lùi NPC; chi tiết runtime chưa xác minh |
| no orient correction | Schema cho phép, chưa bật | Tên gợi ý bỏ hiệu chỉnh hướng đòn; diễn giải theo tên, chưa xác minh engine |
| continuous damage | Có ở Flags cấp MeleeMove ngoài | Trường cũ; không đủ cơ sở suy ra mỗi frame gây thêm một lần damage |
| shatter | Có ở weapons.Flags | Cờ tên gợi ý xử lý phá vỡ vật liệu; chưa xác nhận đầy đủ semantics, không phải multiplier HP |
| held in left hand | Có ở weapons.Flags | Cờ cách giữ vũ khí; không nên đổi như một cách tăng sát thương |
| disable player cover | Có ở weapons.Flags | Cờ vô hiệu cover khi cầm búa |

Các tweak sau giống nhau ở bảng chính/DLC và **original = V4**; thuộc nhóm
melee dùng chung, không có bằng chứng chúng chỉ áp dụng riêng búa của Alec.

| Tweak | Giá trị | Mô tả từ schema/record |
|---|---:|---|
| Camera_melee_max_turn_rate | 2,5 | Tốc độ người tấn công có thể xoay sau khi bắt đầu đòn; record không ghi đơn vị |
| Camera_melee_turn_distance | 3,75 | Khoảng cách một actor được xét làm mục tiêu melee để hiệu chỉnh hướng |
| Camera_melee_turn_time | 0,3 | Thời gian camera quay về mục tiêu khi melee; không phải cooldown búa |
| Camera_melee_turn_angle | 1,2 rad ≈ 68,75° | Góc tối đa cho phép quay mặt về mục tiêu |
| Melee_running_distance | 1,1 | Ngưỡng khoảng cách để chọn running melee; không phải tốc độ chạy hoặc tầm sát thương cuối |
| Damage_multiplier_melee_heavy_armor | 0,6 | Hệ số cận chiến lên người mặc giáp nặng, single player |
| Ai_cover_dist_melee_no_npc_damage | 20 | Khoảng cách AI tìm cover với vũ khí melee khi NPC damage bị vô hiệu, như trước raid |
| Ai_cover_dist_melee | 15 | Khoảng cách AI tìm cover với vũ khí melee khi bị bắn |
| Mp_melee_structure_multiplier | 2,0 | Hệ số công trình melee multiplayer; không phải đường chỉnh offline được xác minh |
| Salvage_touch_delay_ms | 1000 ms | Thời gian chờ nhặt salvage mới sinh; liên quan loot từ phá công trình bằng búa |

## Các trường của weapons không nên hiểu nhầm

Những giá trị sau giống nhau cho búa thường/vàng, và V4 giữ gốc.

| Trường | Giá trị | Giải thích |
|---|---:|---|
| Weapon_Class / Ammo_Type | melee_sledgehammer / melee | Chọn đường xử lý cận chiến |
| Trigger_Type | single | Kiểu kích hoạt nút; không khẳng định đổi automatic là búa tự vung đúng |
| Default_Refire_Delay | 0 | **Schema xác nhận bị bỏ qua cho melee**; không thể dùng làm nút tăng tốc búa |
| Range_Max | 1,8 | Tầm NPC cố sử dụng vũ khí; không phải tầm trúng búa người chơi |
| Range_Red | 4,5 | Tầm đổi màu đỏ của reticle; không tăng damage/reach |
| Min/Max_Engagement_Distance | 1,2 / 2,5 | Khoảng cách giao chiến AI mong muốn |
| Player_Move_Speed | 1,01 | Hệ số di chuyển khi cầm búa; không phải tốc độ vung, còn phụ thuộc giới hạn di chuyển engine |
| Damage_Scaling_Max/NPC_Damage, Player_Damage | 0 / 0 | Không có nghĩa búa không gây damage; các nhánh melee có số riêng |
| Vehicle_Damage, Player_Vehicle_Damage | -1 / -1 | Giá trị đặc biệt giữ gốc; không đặt âm thành số nhân/chia tùy ý |
| Magazine_Size, Max_Rounds | 1 / 1 | Schema bỏ qua với melee; tăng thành 999 không làm búa mạnh hơn |
| Num_Magazines, Ammo_Box_Restock | 2 / 0 | Metadata đạn; không phải độ bền búa |
| Acceleration | 0 | Không có bằng chứng đây là gia tốc tay vung |
| Max_AI_Penetrating_Distance | 40 | Chỉ vũ khí xuyên theo schema; không phải búa đánh xuyên 40 m |
| Zoom_Magnification | 1,45 | Thông số zoom nếu trạng thái dùng zoom được kích hoạt; chưa xác nhận búa dùng nó |
| aim_assist | 0,75 | Hệ số hỗ trợ ngắm, schema không giải thích chi tiết tác động lên melee |
| Animation_Group / Melee_Group | Hammer / Sledgehammer | Nhóm animation và nhóm hiệu ứng vật liệu |

Các trường ID, team, inventory/item reference, icon, reticle và prop đeo
được giải thích trong CSV. Unique_ID thường/vàng/DLC lần lượt 69/123/96;
đây là mã định danh, không phải chỉ số sức mạnh.

## Đòn, nâng cấp và model

| Vũ khí | Đòn ngang / đòn dọc |
|---|---|
| sledgehammer | side / vert |
| sledge_upgrade_1 | side_u1 / vert_u1 |
| sledge_upgrade_2 | side_u2 / vert_u2 |
| sledge_upgrade_3 đến _14 | Vẫn side_u2 / vert_u2 |
| golden_hammer | side_gold / vert_gold |
| mar_dlc_sledge | side_u2 / vert_u2 |

Các tên đòn ở bảng là viết gọn của tiền tố `sledgehammer_melee_`.
`StandingPrimary/CrouchingPrimary` trỏ nhánh ngang; `StandingTertiary/
CrouchingTertiary` trỏ nhánh dọc. Chưa gán cứng nút chuột vì phụ thuộc keybind.

**14 bản ghi sledge_upgrade không đồng nghĩa 14 cấp damage.** Các mẫu 3–14
có model/icon/metadata riêng nhưng tham chiếu cùng _u2; chỉ đổi hình không
tự sinh một bộ sát thương mới. Không suy rằng mọi mẫu đều được mở trong
campaign từ việc thấy nó trong file.

Các trường MovingPrimary/MovingSecondary và một số trạng thái cũ vẫn trỏ
`sledgehammer_melee`/`sledgehammer_melee_2`. Không tìm được định nghĩa hai tên
này trong Table của melee.xtbl/dlc01_melee.xtbl đã cung cấp; chúng có sẵn ở
original. Đây là giới hạn đối chiếu, **chưa phải bằng chứng lỗi V4 hoặc đòn
di chuyển chắc chắn không được tăng damage**. Animation còn có variant
Forward/Air; cần quan sát/log runtime để biết đường chọn đòn thực tế.

Trong upgrades, các mức mua búa chính:

| Mục | Cost original → V4 | Value khi mua | Trạng thái cấu hình cần lưu ý |
|---|---:|---:|---|
| sledgehammer | 25 → 13 | 1 | Available=True trong dữ liệu |
| sledgehammer1 | 75 → 38 | 1 | Available=False; Activity_Count=25 giữ gốc |
| sledgehammer2 | 125 → 63 | 2 | Điều kiện/unlock giữ gốc |
| golden_hammer | 1 → 1 | 3 | Available=False; Unlock_Action=Purchased giữ gốc |

`Value` ở đây là mã/cấp lựa chọn, không phải nhân damage ×1/×2/×3. V4 chỉ
giảm Cost dương trong upgrades; Available, Activity_Count, Unlock_Action,
Show_Locked, Also_Unlock_Level giữ gốc. Giá inventory `items_inventory/Cost`
khác (ví dụ thường/vàng=100, không đổi); chưa xác minh nó là giá shop campaign.

items_3d, items_inventory và Visuals chọn mesh, icon, vị trí đeo và cách nhặt.
`Spin_Time=5000` của item không phải thời gian một cú vung. Tên hiệu ứng vật
liệu `invulnerability` của item không chứng minh Alec trở nên bất tử khi nhặt.

## Tốc độ vung và animation event

`player.xtbl` nhóm Hammer ánh xạ:

| Action | Asset |
|---|---|
| melee | plyr_hmr_mele.animx |
| melee2 | plyr_hmr_mele_b.animx |
| melee3 | Cũng plyr_hmr_mele_b.animx |

Các event trong anim_files.xtbl, V4 giữ gốc; bản DLC tương ứng có cùng dữ liệu:

| Asset | impact start | secondary impact | impact end | release movement |
|---|---:|---:|---:|---:|
| plyr_hmr_mele.animx | frame 5 | frame 8 | frame 10 | frame 22 |
| plyr_hmr_mele_b.animx | frame 6 | frame 9 | frame 11 | frame 26 |
| plyr_hmr_crch_mele.animx | frame 5 | Không có event | frame 11 | frame 23 |

- impact start/end đánh dấu cửa sổ xử lý va chạm, không chứng minh mỗi frame
  gây thêm một cú damage. secondary impact liên quan kiểm tra va chạm phụ.
- release movement liên quan trả điều khiển di chuyển; **không tự đồng nhất
  với thời điểm được đánh cú tiếp theo** hoặc thời lượng toàn bộ animation.
- Có variant Forward/Air và các trường Time, Percentage, Playstyle; chưa
  xác minh engine dùng chúng thế nào. Không lấy Time=800 làm bằng chứng
  búa có cooldown 800 ms hoặc chỉ sửa số này sẽ nhanh gấp đôi.
- Muốn tăng tốc vung thật sự phải xác minh playback/timing asset hoặc hook
  runtime. Chưa tìm được một nút tốc độ búa đã xác nhận trong hai VPP.
  Chỉnh frame tùy tiện có thể làm hit xảy ra lệch hình hoặc khó điều khiển.

## Hình ảnh, âm thanh và cảm giác va chạm

- `hammer_impact` là preset của đòn dọc, `hammer_alt_impact` của đòn ngang.
  Các nhóm Wobble, Destabilization, Jitter, Direct, Wander, Oscillation
  và Strength_Graph mô tả rung camera theo thời gian.
- Pitch/Yaw/Roll chỉnh các thành phần rung theo trục; Variation/Frequency
  chỉnh biến thiên/tần số. Strength_Graph có mốc 0 / 0,08 / 0,22 / 0,5;
  Blur và Strong/Weak_Vibration là hiệu ứng màn hình/tay cầm, không phải HP.
- `rfg_melee_groups/Sledgehammer` chọn 17 hiệu ứng theo Flesh, Steel,
  Concrete, Glass, Wood... Đây là ánh xạ hiệu ứng, không phải 17 loại damage.
- Foley và voice line của animation điều khiển tiếng vung/nhân vật; trigger
  Frame, IK và prop attachment cần đồng bộ animation.
- CSV/JSON lưu đầy đủ mọi giá trị gốc/V4 của các preset và event được chọn;
  không tự tăng lực vật lý bằng cách đổi CameraShake hoặc hiệu ứng tia lửa.

## Đề xuất chỉnh búa tiếp theo — chưa áp dụng

Tăng riêng phần người chơi để có cảm giác mạnh, giữ tăng phá hủy ở mức vừa:

| Nhóm | V4 hiện tại, so original | Mức đề xuất, so original |
|---|---:|---:|
| NPCDamage / DefaultDamage, Player AnimSet | ×3 | ×5 |
| VehicleDamage | ×3 | ×10 để bù nhóm xe HP ×5 |
| StructureDamage | ×2 | ×3; vẫn cần tránh cột/nhà gần con tin |
| HitRange và SecondaryImpact/HitRange | ×1 | ×1,25 |
| HitRadius | ×1 | ×1,25: các đòn chính 0,4 → 0,5 m |
| ImpactForce / RagdollImpulse | ×1 | ×1,5; thử trước với búa vàng vốn có lực cao |
| AwayImpulseScale / HitHeight / hướng tác động | Original | Giữ gốc trước |
| Sát thương nhận vào của Alec | Giảm như V4 | Giữ V4 |
| Animation timing, AI/global melee tweak | Original | Giữ trước khi có thử nghiệm runtime |

Tầm ngang/dọc sẽ thành 2,5/2,75; tầm phụ 2,375/2,5. Các nhánh thường/u1/u2/
vàng đều tính từ số gốc riêng, không nhân nối tiếp từ V4. Đề xuất không hứa
phá mọi xe một cú, tự né đồng minh hoặc bảo đảm mọi nhiệm vụ an toàn.

Nếu thích hất văng hơn là sát thương, nên tăng lực trước ở mức nhỏ rồi thử,
không đồng loạt tăng thêm AwayImpulseScale hoặc bật continuous damage.
Chưa thay các tham số hoặc tạo V4.1 trong lượt phân tích này.

## Những nhóm khác có thể chỉnh để chơi thú vị hơn

| Ý tưởng | Trường đã tìm thấy / mức hiện tại V4 | Hướng thử và tác động |
|---|---|---|
| Nhặt salvage nhanh | Salvage_touch_delay_ms=1000 | Thử 250–500 ms; đây là thời gian chờ nhặt, không phải bán kính hút đồ |
| Giữ salvage sau khi chết | Player_death_salvage_percent_kept=0.0 | Schema mô tả 0=không giữ, 1=giữ hết; có thể thử 0,75–1, cần xác nhận tương tác cơ chế chết/save |
| Ít rung khi đánh/nổ | camera_shake, preset theo từng hành động | Giảm weight camera ở preset liên quan, giữ damage; không mặc định tất cả rung là cùng một trường |
| Cảm giác súng dễ kiểm soát | Spread_Min/Max, Recoil_Kick; V4 giữ gốc | Giảm nhẹ độ tản/giật; định nghĩa vũ khí dùng chung có thể ảnh hưởng NPC |
| Remote chiến thuật | upgrades/remote_charge_count, cấp gốc 2 đến 12 ở campaign chính | Điều chỉnh giới hạn đặt đồng thời riêng với lượng đạn 90/150; nhiều quả có thể cộng dồn phá nhà |
| Dễ đứng trên xe hơn | Human_ragdoll_on_vehicle_speed=8.04672 m/s | Thử tăng nhẹ ngưỡng; chỉ là một điều kiện gây ngã, va chạm bánh xe còn có ngưỡng riêng 0,5 m/s |
| Đỡ bị giáp nặng kháng búa | Damage_multiplier_melee_heavy_armor=0.6 | Thử 0,8–1,0; đây là tweak melee dùng chung, không bảo đảm chỉ tăng búa của Alec |

Các gợi ý đều **chưa áp dụng**. Ưu tiên đổi riêng từng nhóm và thử nhiệm vụ
giải cứu/hộ tống/demolitions trước. Chưa xác minh một nút chỉnh riêng tốc độ
vung búa, tốc độ jetpack hoặc nhảy cao trong các trường đang thống kê;
không suy ra các tính năng đó chỉ từ tên file animation.
