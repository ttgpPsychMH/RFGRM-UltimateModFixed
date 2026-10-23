# Đánh giá cân bằng V3 và hướng giữ sức mạnh người chơi, bảo toàn nhiệm vụ

Mốc phân tích: **Campaign v3 — tốc độ/động cơ xe ×1,5**, đối chiếu trực tiếp với hai file BACKUP original. Đây là báo cáo tư vấn; **chưa thay đổi hai VPP hoặc ZIP bản mod**. Tiện ích nhảy RSL là phần riêng, chưa có bằng chứng người dùng đã cài/bật nên không coi nó là thay đổi sẵn có trong VPP.

**Kết luận:** V3 làm cả người chơi lẫn thế giới xung quanh mạnh và hỗn loạn hơn rất nhiều. Để nhân vật gần như “chúa” mà ít làm lệch nhiệm vụ, nên giữ khả năng chống chịu của người chơi và đưa phá hủy, vũ khí dùng chung, AI, đội tiếp viện, xe nhiệm vụ và điều kiện hoạt động về gần original. Không thể bảo đảm tuyệt đối mọi nhiệm vụ chỉ bằng kiểm tra dữ liệu; chưa chạy game ở môi trường này.

## 1. Phạm vi đã kiểm tra

- `misc.vpp_pc`: 1.208 tệp con, **15 tệp khác original**; 1.936 giá trị XML ở cùng đường dẫn thay đổi, 7 đường dẫn giá trị bị bỏ.
- `table.vpp_pc`: 423 tệp con, **7 tệp khác original**; 368 giá trị XML ở cùng đường dẫn thay đổi, 16 đường dẫn bị bỏ, 1 đường dẫn thêm.
- Tổng cộng **2.304 giá trị XML thay đổi**, 23 đường dẫn bị bỏ và 1 đường dẫn thêm. Các con số tính riêng từng bản sao trong từng gói; có giá trị thuộc multiplayer, test, template, mô tả hoặc editor, không phải 2.304 hiệu ứng độc lập đang hoạt động trong campaign.
- Không thêm/xóa tên tệp con; không sửa tài sản nhị phân khác trong hai gói. Mỗi gói có 422 XTBL qua phân tích XML; `credits.xtbl` có ký tự không hợp lệ từ original, giữ nguyên từng byte.
- Đối chiếu hash của VPP nguồn và nội dung ZIP V3 đang phát hành. Không suy đoán thứ tự engine ưu tiên nạp các bảng trùng nhau.

[CSV toàn bộ khác biệt original → V3](https://raw.githubusercontent.com/ttgpPsychMH/RFGRM-UltimateModFixed/main/reports/campaign-safety-inventory.csv) · [Dữ liệu đối chiếu và mẫu cụ thể](campaign-safety-evidence.json) · [CSV tham chiếu cần xử lý](https://raw.githubusercontent.com/ttgpPsychMH/RFGRM-UltimateModFixed/main/reports/campaign-safety-references.csv).

## 2. Thống kê theo nhóm và mức ảnh hưởng

Các hệ số sau chỉ áp dụng cho những trường đã được chọn, gồm các ngoại lệ búa và trường liên quan đã chốt; không áp dụng đồng loạt cho mọi bản ghi.

| Nhóm | V3 hiện tại | Đánh giá với mục tiêu chơi campaign |
|---|---|---|
| HP nhân vật chính | `rfg_PC`: 550 → 5.500; các bản ghi HP người chơi đã chọn ×10 | Phù hợp mục tiêu gần như chúa; ít trực tiếp làm sập nhà hay giết mục tiêu |
| Sát thương tới người chơi | Các trường đã chọn ÷20, gồm difficulty và sát thương vũ khí tới player; có thể cộng dồn | Phù hợp; đây đã là phần tăng sức mạnh rất lớn, không cần tăng phá hủy để tạo cảm giác bất khả chiến bại |
| Hồi máu/chống chịu | Regen rate ×10; regen delay ÷10; `knock_down_hits` 30 → 300; giảm sát thương rơi, một số hệ số xe | Thường phù hợp; không chứng minh miễn mọi kiểu chết do script, đè, rơi hoặc vật lý |
| Di chuyển/kích thước | `rfg_PC/max_speed` 5 → 10 m/s trong cả hai gói; `Height` misc 1,0, table 1,1; còn một bản ghi MP Mason tốc độ 15 | Không có ba tốc độ walk/run/sprint riêng đã xác nhận. Đi nhanh hơn có thể bỏ xa đoàn hộ tống; kích thước khác nhau không giúp bảo toàn nhiệm vụ |
| HP NPC | Các bản ghi Guerilla/Civilian ×5, EDF/Marauder ×3 | Không chỉ tăng sức mạnh Alec: thay độ bền của mục tiêu, đồng minh, nhân vật kịch bản; một số thử thách dùng vũ khí riêng sẽ khác nhịp |
| Trang bị NPC | Trong misc có 85 bản ghi Guerilla được thêm Gauss thay vũ khí cũ; 2 là biến thể `rfg_PC_*`, 83 là các bản ghi còn lại | Nguy cơ cao: đồng minh có thể phá xe/vật thể hoặc kết liễu mục tiêu quá sớm; không khẳng định mọi bản ghi đều được spawn trong campaign |
| Súng | NPC/vehicle damage và đạn được chọn ×5; refire/reload/cooldown ÷3; tầm/tốc độ đạn ×3; recoil/spread/heat ÷5; nhiều chế độ single → automatic | Nguy cơ cao: nhiều trường dùng chung cho NPC; tăng sát thương và tốc độ bắn có tác động cộng dồn |
| Thay bản chất vũ khí | Nano Rifle trỏ từ `nano_rifle_exp` sang `edf_mediumtank_shell`, single → automatic, delay 350 → 117 ms | Nguy cơ rất cao với vật thể cần giữ: một khẩu súng có hành vi sát thương/nổ kiểu đạn xe tăng, không còn chỉ là chỉnh hệ số |
| Búa | Các trường sát thương thường ×50, nâng cấp ×20 từng bản, vàng ×100, gồm StructureDamage và VehicleDamage; vài trường tầm/lực tác động ×3 | Nguy cơ rất cao: đánh sập trụ, phá xe, làm NPC chết; nâng cấp 1–2 còn yếu hơn búa thường theo công thức đã chọn |
| Thuốc nổ | Các vùng tác động được chọn ×3; damage người/xe/công trình được chọn ×5; impulse không tự động tăng theo các hệ số này | Nguy cơ rất cao, đặc biệt giải cứu trong nhà, hộ tống và bảo vệ công trình |
| Xe | Trong misc: 62 giới hạn tiến và 6 giới hạn lùi ×1,5; 110 trường torque và các trường RPM đã chọn ×1,5; 73 trường HP ×5; một trường lái Max_Speed_Steering 25 → 75 vẫn giữ | Hệ số tốc độ đã nhẹ hơn V2 nhưng HP và một số thông số khác vẫn rất xa gốc; không chỉ xe người chơi đang lái |
| Spawn/đội tiếp viện | 128 thời gian chờ đã chọn ÷3; giữ thay đổi 173 tham chiếu SquadType trong raid và 67 tham chiếu squad_def trong House Arrest ở hai gói | Nguy cơ cao: quân có thể đông hơn và tới sớm hơn; số trường đếm có bản sao ở hai gói, không phải 240 loại đội khác nhau |
| Loại xe xuất hiện | 62 tham chiếu `vehicle_type` trong misc bị thay | Thay traffic/xe của hoạt động; không còn chỉ tăng tốc độ xe cũ; có tham chiếu không tìm thấy định nghĩa |
| Điều kiện hoạt động | Các mốc thời gian được chọn ×3; Required_kills/điều kiện số lượng được chọn ÷3; Escape_Speed courier ÷3; một số ammo/HP xe nhiệm vụ ×5 | Làm khác thiết kế nhiệm vụ, đôi khi dễ hơn nhưng cũng có thể lệch các giai đoạn/cách chơi; một phần nằm trong test/template |
| Kinh tế/tiến trình | Một số salvage reward ×5; ammo pickup/crates ×5; upgrade cost ÷3; morale/control modifier được chọn ×3 | Ít trực tiếp gây nhà sập nhưng làm nhịp mở khóa/tiến trình khác original |

Không tìm thấy thay đổi cờ có tên `infinite`/`unlimited` trong kiểm kê hiện tại của `character.xtbl` và `weapons.xtbl`. Báo cáo này xác nhận các mức tăng đạn, không coi “đạn vô hạn” là tính năng đã được chứng minh chỉ từ hai VPP.

## 3. Vì sao nhiệm vụ giải cứu có thể khó hơn dù Alec rất mạnh?

### A. Nhà và con tin nhận thiệt hại, trong khi người chơi sống sót

Remote charge trong **cả hai gói**:

| Trường | Original | V3 |
|---|---:|---:|
| Blast Radius (`Radius`) | 3 m | 9 m |
| Secondary Damage Radius (`CrumbleRadius`) | 3,75 m | 11,25 m |
| Mốc sát thương người giảm về 0 (`KnockdownRadius`) | 5,5 m | 16,5 m |
| Vùng làm NPC giật mình (`FlinchRadius`) | 9 m | 27 m |
| `Structural_Damage` | 22.500 | 112.500 |
| `Human_Damage_Max` | 1.250 | 6.250 |
| `vehicle_damage_max` | 3.000 | 15.000 |
| `Impulse` | 24.000 | 24.000 |

Bán kính ×3 bao phủ diện tích hình tròn lớn ×9 về mặt hình học; điều đó không có nghĩa engine gây sát thương ×9 ở mọi nơi. Nhưng một vụ nổ có thể chạm nhiều trụ/tường hơn, trong khi sát thương công trình đã ×5. Nhà có thể mất kết cấu và đổ xuống con tin dù người chơi gần như không bị thương.

Năm bản ghi con tin trong nhóm `Hostages` — Jayde, Olga, Torvald, Jake, Jackson — đều có HP 400 → 2.000 trong misc. HP tăng ×5 không bảo vệ tuyệt đối trước vùng sát thương người tối đa 6.250, sập kết cấu, vật lý hoặc lệnh chết của script. Không dùng các con số raw này để khẳng định một NPC nhất định chắc chắn chết sau một vụ nổ: còn falloff, vị trí, hệ số, che chắn và logic engine.

Búa đòn đứng trong `AnimSet Player.xtbl` có **StructureDamage** lần lượt:

| Bản búa | Original | V3 |
|---|---:|---:|
| Thường | 1.500 | 75.000 |
| Nâng cấp 1 | 2.000 | 40.000 |
| Nâng cấp 2 | 2.500 | 50.000 |
| Vàng | 5.000 | 500.000 |

Đây là trường sát thương công trình riêng, không chỉ sát thương lên lính. Chỉ hạ bán kính remote charge sẽ chưa giải quyết búa phá trụ, súng nổ và hỏa lực NPC.

### B. Sát thương và tốc độ bắn nhân chồng

Gauss EDF trong misc: NPC_Damage 95/115 → 475/575; refire 250 → 84 ms. Nếu không bị giới hạn bởi hoạt ảnh/AI/nạp đạn, DPS lý thuyết bằng **5 × 250/84 ≈ 14,88 lần gốc**. Nhiều bản ghi NPC Guerilla đồng thời được đổi sang Gauss. Nếu engine cho sát thương đồng đội hoặc NPC đánh trúng vật thể cần bảo vệ, tăng HP đồng minh ×5 vẫn không tự cân bằng được nguồn sát thương tăng mạnh này.

`NPC_Damage` là trường sát thương tới NPC; không được mặc nhiên hiểu là “chỉ đạn Alec bắn vào kẻ địch”. Dữ liệu này chưa cung cấp bộ lọc đồng minh/kẻ địch cho mọi tình huống. Cũng không giả định mọi loại súng áp dụng hệt các hệ số.

Ngược lại, Alec đã rất khó bị giết. Ví dụ Gauss Player_Damage 50 → 2,5 và difficulty Easy 0,6 → 0,03: nếu cả hai hệ số cùng áp dụng vào một hit, damage tính toán trước các giới hạn/làm tròn của engine giảm từ 30 xuống 0,075, tức ÷400; HP còn ×10. Đây là minh họa điều kiện áp dụng, không phải số hit chịu được đã đo trong game. Không cần DPS/phá hủy ×15/×50 để tạo cảm giác gần như chúa.

### C. Đội to hơn, đến sớm hơn

House Arrest `je_ha_05`, đợt tiếp viện thứ hai: original `basic_squad_4` sau 30 giây; V3 `basic_squad_6` sau 10 giây. `squads.xtbl` xác nhận member_count là 4 và 6. Đội lớn hơn 50%, xuất hiện sớm hơn, trong khi người chơi có thể vẫn đang tìm đường vào nhà/đưa con tin ra.

Không suy ra mọi spawn là bộ đếm lặp vô hạn hoặc cứ ÷3 là số quân/phút chắc chắn ×3: còn lịch đợt, giới hạn NPC và script. Nhưng cấu hình hiện tại đã thay cả thành phần đợt lẫn thời điểm.

### D. HP xe ×5 và thời gian/điều kiện nhiệm vụ cũng đã đổi

HP xe ×5 không giới hạn ở xe Alec lái. Mục tiêu phải phá, xe courier hoặc xe kịch bản có thể bền hơn; tốc độ xe, torque/RPM và courier Escape_Speed cũng đã bị sửa. Một số hoạt động cấp vũ khí/đạn riêng, nên không thể giả định vũ khí nhận được luôn mạnh đủ để bù HP mục tiêu. Giữ vũ khí cũ nhưng chỉ sửa lại timer sẽ không khôi phục toàn bộ trải nghiệm nhiệm vụ.

## 4. Phát hiện về tính đúng dữ liệu phải xử lý trước cân bằng

Trong các trường tham chiếu đã bị mod sửa, có **69 lần tham chiếu không tìm thấy định nghĩa tương ứng trong các bảng base/DLC được cung cấp**:

| Nhóm | misc | table | Ví dụ |
|---|---:|---:|---|
| Đội tiếp viện | 50 | 5 | `basic_squad_10`, `basic_squad_12`, `guerilla_squad_8`, `guerilla_squad_10`, `basic_squad_` |
| Loại xe | 13 | 0 | `Min_ATV_MG3-A_3`, `Min_ATV_MG3-A_2` |
| Vũ khí | 1 | 0 | Dustin_Oasis có `m1gauss_rifle6`, gốc là `m16` |

Tất cả 69 giá trị này đã có trong mod đầu vào và được giữ lại; tên gốc tại các vị trí tương ứng đều có trong catalog đối chiếu. Các số là **lần tham chiếu**, không phải 69 định nghĩa độc lập. Chưa kiểm chứng engine có cơ chế tạo alias, fallback hay xử lý lỗi khi chạy; do đó không khẳng định chắc chắn crash. Tuy nhiên, không nên thêm các đội 10/12 người chỉ để hợp thức hóa tham chiếu trong bản ưu tiên nhiệm vụ: khôi phục tham chiếu original là hướng ít thay đổi nhất.

Các kiểm tra trước của tôi về VPP, XML, công thức và min/max đã bỏ sót loại vấn đề này. Kiểm tra cú pháp XML thành công không chứng minh tên đội, xe và súng đều hợp lệ hoặc nhiệm vụ sẽ hoàn thành.

Ngoài ra, **15 tệp XTBL trùng tên giữa misc và table có nội dung khác nhau**. Ví dụ hai gói cùng có remote charge 9 m, nhưng HP/giới hạn xe, một số NPC, difficulty và hoạt động khác nhau. Đây không tự động là lỗi crash, song chưa xác nhận thứ tự nạp thì không thể lấy một bảng hệ số làm kết quả thực tế cho mọi chế độ.

CSV đầy đủ còn ghi 23 đường dẫn giá trị bị bỏ và 1 đường dẫn thêm — có các cờ/hướng dẫn visual và nội dung editor/props. Không quy tất cả chúng thành lỗi nhiệm vụ. Chúng cho thấy chỉ đọc bảng 2.316 dòng audit cũ chưa phải kiểm kê toàn bộ khác biệt cấu trúc.

## 5. Phương hướng đề xuất: bản campaign ưu tiên hoàn thành nhiệm vụ

Tôi đề nghị dựng một cấu hình mới từ **hai bản original sạch**, rồi áp lại một danh sách thay đổi nhỏ có chủ đích. Điều này tránh kế thừa cả các thay đổi tên/đội/vũ khí ngoài mong muốn. Đây là hướng thay đổi chính sách cũ “giữ mọi chỉnh sửa không phải số của Nexus mod”, chưa được áp dụng trong báo cáo này.

| Nhóm | Cấu hình khuyến nghị ban đầu | Lý do |
|---|---|---|
| HP/giảm damage/hồi máu/chống chịu của Alec | Giữ phần bảo vệ hiện tại: HP ×10, giảm damage tới người chơi và regen như đã chốt | Tạo cảm giác gần như chúa mà ít làm thay đổi thế giới |
| Tốc độ Alec | Giữ giới hạn 10 m/s nếu đang thấy thoải mái; chiều cao trở về 1,0 | Không cần tăng thêm vận tốc/nhảy để tạo sức mạnh; chưa có dữ liệu chứng minh ba trạng thái walk/run/sprint đạt vận tốc riêng |
| Bán kính, sát thương công trình/xe/người và lực nổ dùng chung | Trả original; remote charge 3 / 3,75 / 5,5 / 9 m, Structural_Damage 22.500 | Giữ phạm vi phá hủy quen thuộc; vẫn giữ những trường giảm sát thương riêng tới player |
| Búa: StructureDamage, DefaultDamage, VehicleDamage, tầm và impulse | Trả original, gồm tiến trình nâng cấp/vàng gốc | Tránh một cú phá nhiều kết cấu/xe nhiệm vụ; từ bỏ ×50/×100 công trình trong bản campaign |
| Sát thương NPC của súng/búa và tốc độ bắn | Bắt đầu với original; không tăng đại trà NPC_Damage | Tránh tăng hỏa lực NPC và giết nhầm mục tiêu. Nếu muốn Alec bắn địch mạnh riêng, cần cách phân biệt nguồn bắn/đội đích được kiểm chứng; không giả định một hệ số XML dùng chung làm được |
| Hành vi súng | Trả kiểu bắn/nổ gốc; Nano Rifle dùng `nano_rifle_exp`; giữ đường cong sát thương/tầm/tốc độ đạn gốc | Giữ đúng công cụ được nhiệm vụ cấp và cách engine xử lý chúng |
| Đạn và độ giật | Có thể giữ mức đạn thoải mái, đề xuất tối đa ×3; giảm độ giật nhẹ sau khi kiểm tra phạm vi áp dụng | Tăng tiện nghi thay vì tăng sức phá hủy/DPS cực lớn; không hứa mọi trường chỉ ảnh hưởng Alec |
| HP, trang bị, tốc độ và hành vi NPC | Trả original trong bản kiểm thử đầu tiên | Giữ mục tiêu/nhân vật kịch bản đúng nhịp; sau đó mới cân nhắc HP ×2 cho các con tin cụ thể đã kiểm thử, không bất tử toàn bộ NPC |
| Raid, House Arrest và đội/xe tiếp viện | Khôi phục thời gian, đội, số lượng và loại xe original | Bỏ cả ÷3 delay lẫn đội đông hơn, xử lý các tham chiếu không có định nghĩa |
| Tốc độ/torque/RPM/HP xe toàn thế giới | Original; giữ giảm sát thương riêng cho người chơi khi ở trong xe nếu trường thực sự có phạm vi đó | Để giao thông, truy đuổi, xe mục tiêu và xe được cấp hoạt động sát bản gốc |
| Timer, kill count, ammo cấp cho puzzle, trạng thái hỏng xe và Escape_Speed của hoạt động | Original | Giữ điều kiện thắng/thua và thiết kế thử thách; chỉ tăng timer của một nhiệm vụ cụ thể sau khi có nhu cầu, không chia mọi yêu cầu số lượng |
| Reward/EDF control/morale | Original trong bản nền; có thể salvage ×2 như tùy chọn riêng, không tăng control/morale đại trà | Giữ nhịp giải phóng và mở nhiệm vụ gần bản gốc |
| Hai bản sao dữ liệu và DLC | Áp nhất quán các thay đổi được chọn cho player ở những bản sao cần thiết; giữ nội dung khác theo original của từng gói | Tránh kết quả phụ thuộc thứ tự nạp; không tự nhân một hệ số hai lần; DLC/MP được phân phạm vi riêng |

Ngay cả original cũng cho phép phá nhà có con tin và làm hỏng nhiệm vụ. Bản đề xuất giảm **rủi ro phát sinh do mod**, không biến mọi hành động phá hủy thành an toàn và không thể bảo đảm “không bao giờ thất bại”.

Nếu vẫn muốn búa công trình ×50/×100, nổ 9 m và giao tranh đông, nên giữ thành **bản phá hủy tự do riêng**. Với hai VPP tĩnh chưa có cơ chế đã kiểm chứng để tự đổi toàn bộ thông số khi vào/ra nhiệm vụ; không hứa tự động bảo vệ nhà/con tin theo ngữ cảnh. Hai bộ VPP riêng có thể đổi khi đã thoát game, nhưng không dùng việc đổi file để khẳng định sẽ khôi phục mọi trạng thái đã lưu.

## 6. Trình tự cân bằng và kiểm thử

1. **Đúng dữ liệu trước:** lấy original làm nền; khôi phục tham chiếu đội/xe/vũ khí hợp lệ; kiểm tra tất cả tham chiếu đã sửa, schema, min/max, cấu trúc VPP và nội dung sau giải nén. Các cờ sentinel 0/-1 phải hiểu theo từng trường, không nhân/chia máy móc.
2. **Chỉ áp phần mạnh của người chơi:** HP, giảm sát thương, hồi phục, chống chịu và giới hạn 10 m/s. Giữ điều kiện nhiệm vụ cùng hệ thống thế giới nguyên bản.
3. **Kiểm thử trong game:** ít nhất nhiều nhiệm vụ giải cứu ở khu vực khác nhau; hộ tống/bảo vệ; courier; timed delivery với xe nhiệm vụ; Demolitions Master có vũ khí/đạn giới hạn; một nhiệm vụ cốt truyện nhiều giai đoạn. Kiểm tra nhận nhiệm vụ, trigger, đưa mục tiêu tới nơi, kết thúc, phần thưởng và tải lại save/checkpoint; không chỉ sống sót hoặc giết hết địch.
4. **Thêm tiện nghi từng nhóm:** ammo, giảm recoil, timer riêng nếu cần. Sau mỗi nhóm, lặp lại các ca nhiệm vụ bị tác động; không thêm đồng thời blast radius, DPS, NPC HP và spawn vì sẽ khó tìm nguyên nhân.
5. **Tách RSL khi đo:** thử bản nền trước với override tốc độ cố định, nhảy cao và các tiện ích tương tự đang tắt; sau đó kiểm tra lại khi bật những tiện ích người dùng thực sự muốn dùng.

Chưa có kết quả thực thi các ca game trên. Mọi mức “nguy cơ cao/thấp” trong báo cáo là suy luận dựa trên dữ liệu được trích dẫn, không phải khẳng định nhiệm vụ cụ thể đã được thử và thất bại.
