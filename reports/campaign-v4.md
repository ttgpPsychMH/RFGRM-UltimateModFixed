# Campaign V4 — dựng lại từ original

V4 dùng hai BACKUP gốc đã xác minh; chỉ giữ cấu hình xe từ V3. Trang bị NPC,
liên kết đội quân, xe spawn và điều kiện mở khóa giữ nguyên dữ liệu gốc.

**[Tải V4](../downloads/Ultimate_Mod_Campaign_v4.zip)** ·
[Báo cáo và mã dựng](../downloads/Ultimate_Mod_Campaign_v4_Reports.zip) ·
[Hướng dẫn đầy đủ](../downloads/HUONG_DAN.txt) ·
[Từng giá trị original → V4](campaign-v4-parameters.csv) ·
[Kiểm tra](campaign-v4-validation.json) · [Policy](campaign-v4-policy.json).

## Cấu hình

| Nhóm | V4 |
|---|---|
| Alec | HP 5500; giới hạn tốc độ 10 m/s; bảo vệ/hồi phục mạnh kiểu V3 |
| HP NPC campaign chính | Guerilla/Civilian ×3; EDF/Marauder ×2 |
| Trang bị NPC, đội hình, loại xe spawn | Original |
| Búa, từng bản thường/nâng cấp/vàng | Player AnimSet: sát thương NPC/xe/default ×3; công trình ×2; tầm/lực gốc |
| Súng cầm tay không có mẫu nổ | NPC/vehicle damage ×3; nhịp bắn/nạp/độ giật gốc |
| Remote, mine, RPG, Gauss/nano/grinder và DLC được chọn | Sát thương NPC/xe ×2; công trình ×1,5; các bán kính tác động dương ×1,5 |
| Thermobaric | Sát thương ×1,5; toàn bộ bán kính gốc, Radius 6,5 m |
| Lực hất nổ, FlinchRadius, hiệu ứng/ID/cờ | Original |
| Xe | Đúng giá trị V3 theo từng gói; các trường tốc độ/động cơ được chọn ×1,5 |
| Delay viện binh | Original ÷2; không tăng số quân mỗi đợt |
| Timer mục tiêu / grace period | ×3; giữ ngưỡng chuyển pha area defense |
| Courier | Chỉ Escape_Speed ÷3; làm tròn lên |
| Phần thưởng | Salvage_Reward dương ×3; morale/control và tiền thưởng chưa rõ loại giữ gốc |
| Đạn | Tổng mang theo, giới hạn nâng cấp, restock, số băng cấp và đạn demolitions ×5; cỡ băng gốc |
| Giá mua/nâng cấp | Cost dương ÷2, làm tròn lên; không giảm chồng difficulty |

Sát thương va chạm và sát thương vụ nổ là hai phần độc lập. Mỗi trường chỉ
nhân một lần; vũ khí có mẫu nổ không nhận thêm hệ số súng ×3. Cờ đạn vô hạn,
giới hạn gắn remote cùng lúc và giá trị cấp nâng cấp giữ gốc.

### Búa

| Bản | DefaultDamage, đòn đứng | StructureDamage | NPCDamage, đòn đứng |
|---|---:|---:|---:|
| Thường | 1500 → 4500 | 1500 → 3000 | 750 → 2250 |
| Nâng cấp 1 | 2000 → 6000 | 2000 → 4000 | 950 → 2850 |
| Nâng cấp 2 | 2500 → 7500 | 2500 → 5000 | 1150 → 3450 |
| Vàng | 5000 → 15000 | 5000 → 10000 | 2300 → 6900 |

Chỉ tăng sát thương tấn công trong `AnimSetName=Player.xtbl`. Các trường sát
thương nhận vào của người chơi được giảm riêng. Không tăng tầm/lực hất hay
sát thương tấn công của animset NPC; liên kết búa vàng và vũ khí búa giữ gốc.

### Nổ

| Mẫu | Radius gốc → V4 (m) | Crumble gốc → V4 (m) | Mốc ngoài sát thương người gốc → V4 (m) | Human max gốc → V4 | Structure gốc → V4 |
|---|---:|---:|---:|---:|---:|
| rocket | 3.65 → 5.475 | 4.0 → 6 | 6.5 → 9.75 | 1700 → 3400 | 23625 → 35438 |
| remote_charge | 3.0 → 4.5 | 3.75 → 5.625 | 5.5 → 8.25 | 1250 → 2500 | 22500 → 33750 |
| mine | 2.75 → 4.125 | 4.5 → 6.75 | 9.5 → 14.25 | 2500 → 5000 | 20000 → 30000 |
| nano_rifle_exp | 1.2 → 1.8 | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 |
| thermo_rocket | 6.5 → 6.5 | 7 → 7 | 9.5 → 9.5 | 6000 → 9000 | 50000 → 75000 |
| gauss_rifle | 0.85 → 1.275 | 1.4 → 2.1 | 1.45 → 2.175 | 0 → 0 | 6500 → 9750 |
| grinder_explosive | 1.75 → 2.625 | 2.0 → 3 | 3.5 → 5.25 | 1500 → 3000 | 12000 → 18000 |
| gauss_rifle_npc | 0.7 → 1.05 | 1.3 → 1.95 | 1.35 → 2.025 | 0 → 0 | 5000 → 7500 |
| DLC_remote_charge | 3.0 → 4.5 | 3.75 → 5.625 | 5.5 → 8.25 | 1250 → 2500 | 27000 → 40500 |
| DLC_missilepod | 2.0 → 3 | 2.5 → 3.75 | 5.5 → 8.25 | 1000 → 2000 | 15000 → 22500 |

[CSV đầy đủ các mẫu nổ đã chọn](campaign-v4-explosives.csv). Số 0 và sentinel
âm giữ nguyên; không thêm trường vắng mặt. `KnockdownRadius` ở schema này
cũng là Human Damage Radius: `Radius` chính không phải ranh giới mọi tác động.
`FlinchRadius` và `Impulse` giữ gốc, kể cả khi vùng gây sát thương rộng hơn.

**Mẫu dùng chung:** remote_charge còn được turret_supergauss_solo/burst dùng;
rocket còn được các rocket turret dùng. Chỉnh mẫu ảnh hưởng cả các consumer
này. Không tạo mẫu mới, ID mới hoặc tách riêng người chơi.

Mẫu nổ riêng của môi trường, nhiệm vụ, xe tăng và thiết bị NPC như grenade,
shockade, singularity giữ công suất gốc. Gauss/nano/grinder có phần nổ nên
dùng mức thấp hơn súng thường. EDF_Super_Gauss có thể mua trong DLC nên cũng
áp dụng mức nổ này, dù mẫu nổ của nó có hậu tố `_npc`.

## Phạm vi và những điểm cần biết

- Dữ liệu gốc mới: misc SHA-256 `9430a4e158ca914a381bd8474b56224163a4836683f4c9ebb18d6ab8cdcbfc10`;
  table `8bd7205b68ce105e9ad04f495c5570d9e2dc51fec67bc9c1f0889768c2f9aef9`.
- Tất cả bảng trùng giữa hai gói có payload V4 giống nhau, trừ vehicles.xtbl.
  Xe giữ đúng giá trị V3: misc có 423 giá trị đổi (349 tốc độ/động cơ,
  73 HP, 1 ngưỡng tốc độ đánh lái); table vehicles vẫn gốc. Chưa xác nhận
  thứ tự ưu tiên nạp xe của engine.
- DLC offline: `rfg_PC_DLC` cùng cấu hình người chơi. Marauder đồng minh ×3,
  EDF ×2, các tù nhân Guerilla ×3. Hai nhân vật scripted `mis_DLC_Dan` và
  `mis_DLC_RFCommander` giữ HP gốc vì không đủ cơ sở phân loại phe runtime.
  Script có thể đổi phe; không suy rộng Team=Guerilla luôn đồng minh trong DLC.
- Các entry MP/test, schema và template giữ gốc ngoài dữ liệu xe V3 được
  yêu cầu giữ. Định nghĩa dùng chung vẫn có thể ảnh hưởng chế độ khác;
  bản phát hành dành cho offline, không có kiểm thử multiplayer.
- `Hostage_Kill_Time` 30 → 90, 60 → 180: tăng thời gian trước khi EDF bắt đầu
  giết con tin. Không vô hiệu hóa thất bại do con tin chết hay công trình sập.
- Chỉ tăng trường `Salvage_Reward` rõ loại tiền. Reward của angel_of_mercy
  là morale, của assassin là EDF control nên giữ gốc; Reward mơ hồ khác
  và salvage rơi từ vật liệu không tự tăng.
- Đạn remote 18/30 → 90/150 là lượng mang theo; giới hạn đặt cùng lúc vẫn
  theo cấp nâng cấp gốc. `Magazine_Size`, hệ số pickup/crate difficulty và
  các cờ gốc giữ nguyên để tránh tăng chồng ngoài hệ số đã chọn.
- God config không bảo vệ mọi mục tiêu nhiệm vụ. Đồng minh có HP cao hơn
  nhưng vẫn chịu friendly fire, vật lý, nhà sập và script. Sát thương súng
  dùng chung cũng tăng cho NPC cầm cùng loại, dù loadout vẫn nguyên bản.
- Bán kính ×1,5 có diện tích hình tròn lý thuyết ×2,25; vẫn tránh dùng thuốc
  nổ sát con tin. Reinforcement ÷2 có thể tăng mật độ quân và tải CPU.
- Các xe được giữ HP ×5 từ V3, kể cả xe địch, bền hơn tương đối so với
  súng ×3/nổ ×2; giữ cấu hình xe V3 cũng giữ hệ quả cân bằng này.
- Tốc độ 10 m/s là giới hạn trong bảng, không phải thay đổi riêng tỷ lệ
  walking/running/sprinting. V4 không kèm hoặc chỉnh tiện ích RSL cũ.

## Xác minh bản dựng

- 2947 giá trị thay đổi so với original: misc 1685
  trong 27 bảng; table 1262
  trong 26 bảng. Số này đếm cả hai bản sao
  của bảng chung; không phải số hiệu ứng gameplay độc lập.
- Giữ nguyên tên và số lượng 1208/423 tệp. Đọc độc lập header, hash tên,
  offset, padding, chiều dài; giải nén đối chiếu toàn bộ 1631 payload.
- So sánh mọi đường dẫn XML, công thức, kiểu Int, sentinel, trường văn bản,
  dữ liệu ngoài phạm vi; không có vi phạm min/max mới. Các asset nhị phân
  không đổi. Không thêm tên/tham chiếu nên không mang sang các liên kết
  lỗi do Nexus mod từng tạo; điều này không chứng minh mọi script runtime.
- Mọi XML sửa hợp lệ. Mỗi gói còn lỗi ký tự trong credits.xtbl có sẵn ở
  original, giữ nguyên byte; 422/423 XTBL parse được.
- **Chưa chạy thử trong game.** Chưa xác nhận mọi nhiệm vụ, FPS, vật lý hoặc
  thứ tự nạp; thử giải cứu/hộ tống/demolitions/lái xe trên save phụ trước.

## SHA-256 file game

```text
bd2cec4003673b44a1f17c7319986ccc78ea365ad95b11c0a7dffa01735a5982  misc.vpp_pc
839985e20922972c70f8d0c8bb9bd6f82e575b1657ab58ecfe582733c3ce867b  table.vpp_pc
```

Các báo cáo cân bằng, chuyển động và nổ có chữ V3 trong kho mô tả bản V3.
Báo cáo này và CSV V4 là nguồn đối chiếu cho bản mới.
