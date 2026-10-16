# Tốc độ toàn bộ cấu hình xe — Campaign v2

Đối chiếu hai VPP đang phát hành với hai bản BACKUP original. Tiện ích nhảy RSL không đổi các số liệu này.

- Có **146 cấu hình xe**: 130 trong `vehicles.xtbl`, 16 trong `dlc01_vehicles.xtbl`. Bao gồm biến thể, mục thử nghiệm và xe chưa chắc xuất hiện trong phần chơi đang dùng; không có nghĩa là 146 loại xe khác nhau có thể lái.
- **133** cấu hình khai báo giới hạn tiến riêng; **13** walker/flyer không khai báo trường đó.
- Trong `misc.vpp_pc`: **62** giới hạn tiến tăng ×3, **71** giới hạn tiến còn lại giữ gốc; **6** giới hạn lùi tăng ×3. DLC giữ nguyên.
- Trong `table.vpp_pc`: toàn bộ giới hạn tiến/lùi ở hai bảng xe vẫn bằng original.
- Các giá trị `AIEnforcedMaxSpeed` khai báo riêng (60 cấu hình) giữ nguyên trong cả hai gói. Không thể suy ra AI chắc chắn lái nhanh ×3 từ giới hạn tiến của xe.

**Đây là giới hạn cấu hình, chưa phải tốc độ đo khi lái.** Mô tả gốc của `EnforcedMaxSpeed` ghi rõ đơn vị MPH và giới hạn động cơ Havok/các giới hạn khác có thể khiến xe không đạt tới số này. Động cơ, RPM, số truyền, độ bám, địa hình, lực cản và nhiệm vụ cũng ảnh hưởng tốc độ.

**Hai gói có dữ liệu trùng nhưng khác giá trị.** Chưa xác nhận thứ tự engine ưu tiên nạp chúng, nên báo cáo hiển thị riêng từng gói; chưa thể kết luận mọi xe trong game thực sự chạy theo cột `misc` hay `table` chỉ từ các VPP.

[Tải CSV đầy đủ](https://raw.githubusercontent.com/ttgpPsychMH/RFGRM-UltimateModFixed/main/reports/vehicle-speeds.csv) · [CSV nhóm/default](https://raw.githubusercontent.com/ttgpPsychMH/RFGRM-UltimateModFixed/main/reports/vehicle-speed-groups.csv)

## Giới hạn tốc độ tiến của tất cả cấu hình

Mỗi ô là **mph (km/h)**. Dấu **—** nghĩa là không khai báo riêng; không có nghĩa bằng 0 hoặc chắc chắn kế thừa 90 mph. Các cột km/h đã làm tròn đến hai chữ số. Có thể dùng Ctrl+F để tìm ID hoặc tên xe.

### vehicles.xtbl

| ID | Tên trong dữ liệu | Original | misc hiện tại | table hiện tại | misc/gốc |
|---|---|---:|---:|---:|---:|
| MarsRover1 | Maverick | 10 (16.09) | 10 (16.09) | 10 (16.09) | ×1 |
| EDF_APC-A_1 | APC | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_2 | APC2 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_3 | APC3 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_4 | APCClean | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_Gauss | APCGauss | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_Gauss2 | APCGauss2 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_Gauss3 | APCGauss3 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC-A_Gauss4 | APCGaussClean | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC_noturret | APC_noturret | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC_noturret2 | APC_noturret2 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC_noturret3 | APC_noturret3 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC_noturret4 | APC_noturretClean | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_Scout_1 | Kitsune | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_2 | Kitsune2 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_3 | Kitsune3 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_4 | KitsuneCLEAN | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_Gauss | KitsuneGauss | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_Gauss2 | KitsuneGauss2 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_Gauss3 | KitsuneGauss3 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_Scout_Gauss4 | KitsuneGaussCLEAN | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_ScoutNoTurret | KitsuneNoTurret | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_ScoutNTurret2 | KitsuneNoTurret2 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_ScoutNTurret3 | KitsuneNoTurret3 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| Walker_Civilian | Walker Civilian | — | — | — | — |
| Walker_Civilian2 | Walker Civilian2 | — | — | — | — |
| Walker_Civilian3 | Walker Civilian3 | — | — | — | — |
| Mar_Jetter_1 | mar_jetter | 64 (103) | 64 (103) | 64 (103) | ×1 |
| Mar_Raider_1 | Raider | 56 (90.12) | 56 (90.12) | 56 (90.12) | ×1 |
| Col_FixedFlatbed_2 | Flatbed2A | 45 (72.42) | 45 (72.42) | 45 (72.42) | ×1 |
| EDF_HeavyTank-A_1 | HeavyTank | 20 (32.19) | 60 (96.56) | 20 (32.19) | ×3 |
| Civ_ResRunner_1 | ResRunner | 65 (104.61) | 65 (104.61) | 65 (104.61) | ×1 |
| Civ_ResRunner-C_1 | RunnerC | 58 (93.34) | 58 (93.34) | 58 (93.34) | ×1 |
| Civ_ResLuxury-C_1 | LuxuryC | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| Col_Taxi_1 | Taxi | 49 (78.86) | 49 (78.86) | 49 (78.86) | ×1 |
| Col_Taxi_2 | Taxi2 | 49 (78.86) | 49 (78.86) | 49 (78.86) | ×1 |
| Col_Taxi_3 | Taxi3 | 49 (78.86) | 49 (78.86) | 49 (78.86) | ×1 |
| Col_Caravan_1 | Caravan | 40 (64.37) | 40 (64.37) | 40 (64.37) | ×1 |
| Col_Caravan_2 | Caravan2 | 40 (64.37) | 40 (64.37) | 40 (64.37) | ×1 |
| Col_Caravan_3 | Caravan3 | 40 (64.37) | 40 (64.37) | 40 (64.37) | ×1 |
| Col_Mini_Hauler_1 | MiniHauler | 38 (61.16) | 38 (61.16) | 38 (61.16) | ×1 |
| Col_Mini_Hauler_2 | MiniHauler2 | 38 (61.16) | 38 (61.16) | 38 (61.16) | ×1 |
| Col_Mini_Hauler_3 | MiniHauler3 | 38 (61.16) | 38 (61.16) | 38 (61.16) | ×1 |
| EDF_ScoutNTurret4 | KitsuneNoTurretCLEAN | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_StaffCar_1 | Staffcar | 54 (86.9) | 54 (86.9) | 54 (86.9) | ×1 |
| Min_ATV_1 | ATV | 62 (99.78) | 62 (99.78) | 62 (99.78) | ×1 |
| Min_ATV_2 | ATV2 | 62 (99.78) | 62 (99.78) | 62 (99.78) | ×1 |
| Min_ATV_3 | ATV3 | 62 (99.78) | 62 (99.78) | 62 (99.78) | ×1 |
| Min_ATV_MG1 | ATVMG1 | 62 (99.78) | 186 (299.34) | 62 (99.78) | ×3 |
| Min_ATV_MG2 | ATVMG2 | 62 (99.78) | 62 (99.78) | 62 (99.78) | ×1 |
| Min_ATV_MG3 | ATVMG3 | 62 (99.78) | 62 (99.78) | 62 (99.78) | ×1 |
| Min_LightPickup_1 | Bluecrab | 52 (83.69) | 156 (251.06) | 52 (83.69) | ×3 |
| Min_LightPickup_2 | Redcrab | 52 (83.69) | 156 (251.06) | 52 (83.69) | ×3 |
| Min_LightPickup_3 | yellowcrab | 52 (83.69) | 156 (251.06) | 52 (83.69) | ×3 |
| Min_LightPickup_MG1 | BluecrabMG | 52 (83.69) | 156 (251.06) | 52 (83.69) | ×3 |
| Min_LightPickup_MG2 | RedcrabMG | 52 (83.69) | 156 (251.06) | 52 (83.69) | ×3 |
| Min_LightPickup_MG3 | yellowcrabMG | 52 (83.69) | 156 (251.06) | 52 (83.69) | ×3 |
| Min_Rover-A_1 | MiningRover | 53 (85.3) | 159 (255.89) | 53 (85.3) | ×3 |
| Min_Rover-A_2 | MiningRover2 | 53 (85.3) | 159 (255.89) | 53 (85.3) | ×3 |
| Min_Rover-A_3 | MiningRover3 | 53 (85.3) | 159 (255.89) | 53 (85.3) | ×3 |
| Min_Rover-A_MG1 | MiningRoverMG1 | 53 (85.3) | 159 (255.89) | 53 (85.3) | ×3 |
| Min_Rover-A_MG2 | MiningRoverMG2 | 53 (85.3) | 159 (255.89) | 53 (85.3) | ×3 |
| Min_Rover-A_MG3 | MiningRoverMG3 | 53 (85.3) | 159 (255.89) | 53 (85.3) | ×3 |
| Min_Rover-A_DMG1 | MiningRoverDMG1 | 60 (96.56) | 180 (289.68) | 60 (96.56) | ×3 |
| Min_Rover-A_DMG2 | MiningRoverDMG2 | 60 (96.56) | 180 (289.68) | 60 (96.56) | ×3 |
| Min_Rover-A_DMG3 | MiningRoverDMG3 | 60 (96.56) | 180 (289.68) | 60 (96.56) | ×3 |
| Min_Rover-A_DRR1 | MiningRoverDRR1 | 40 (64.37) | 120 (193.12) | 40 (64.37) | ×3 |
| Min_Rover-A_DRR2 | MiningRoverDRR2 | 40 (64.37) | 120 (193.12) | 40 (64.37) | ×3 |
| Min_Rover-A_DRR3 | MiningRoverDRR3 | 40 (64.37) | 120 (193.12) | 40 (64.37) | ×3 |
| Min_Emergency_1 | Emergency | 55 (88.51) | 165 (265.54) | 55 (88.51) | ×3 |
| Min_Jetter_1 | min_jetter | 65 (104.61) | 65 (104.61) | 65 (104.61) | ×1 |
| Min_SupplyTruck_1 | MinSupplyTruck | 44 (70.81) | 44 (70.81) | 44 (70.81) | ×1 |
| EDF_AAXAir_1 | Raven | — | — | — | — |
| EDF_StaffCar_2 | Staffcar2 | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_StaffCar_3 | Staffcar3 | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_StaffCar_Gauss | StaffcarGauss | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_StaffCar_Gauss2 | StaffcarGauss2 | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_StaffCar_Gauss3 | StaffcarGauss3 | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_StaffCar_NoTurret | StaffcarNoTurret | 54 (86.9) | 54 (86.9) | 54 (86.9) | ×1 |
| Min_SupplyTruck_RT | MinSupplyTruckRT | 45 (72.42) | 135 (217.26) | 45 (72.42) | ×3 |
| EDF_HeavyTank-A_2 | HeavyTank2 | 20 (32.19) | 20 (32.19) | 20 (32.19) | ×1 |
| EDF_HeavyTank-A_3 | HeavyTank3 | 20 (32.19) | 20 (32.19) | 20 (32.19) | ×1 |
| EDF_HeavyTank-A_4 | HeavyTankClean | 20 (32.19) | 60 (96.56) | 20 (32.19) | ×3 |
| EDF_MediumTank-A_1 | MediumTank | 25 (40.23) | 75 (120.7) | 25 (40.23) | ×3 |
| EDF_AAXAir_2 | RavenRocket | — | — | — | — |
| EDF_StaffCar_NTurret3 | StaffcarNoTurret3 | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_StaffCar_NTurret2 | StaffcarNoTurret2 | 54 (86.9) | 162 (260.71) | 54 (86.9) | ×3 |
| EDF_Supplytruck_1 | EDFSupplyTruck | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_ABXAir_1 | Pigeon | — | — | — | — |
| Tharsis_gun | Tharsis_Gun | 5 (8.05) | 15 (24.14) | 5 (8.05) | ×3 |
| EDF_Scout_Rocket | KitsuneRocket | 60 (96.56) | 180 (289.68) | 60 (96.56) | ×3 |
| EDF_AAXAir_Gauss | RavenGauss | — | — | — | — |
| Walker_Min | Walker Min | — | — | — | — |
| Min_SupplyTruck_2 | MinSupplyTruck2 | 44 (70.81) | 132 (212.43) | 44 (70.81) | ×3 |
| Min_SupplyTruck_3 | MinSupplyTruck3 | 44 (70.81) | 132 (212.43) | 44 (70.81) | ×3 |
| Walker_Min2 | Walker Min2 | — | — | — | — |
| Walker_Min3 | Walker Min3 | — | — | — | — |
| Walker_Flamer | Walker Flamer | — | — | — | — |
| EDF_MediumTank-A_2 | MediumTank2 | 25 (40.23) | 75 (120.7) | 25 (40.23) | ×3 |
| EDF_MediumTank-A_3 | MediumTank3 | 25 (40.23) | 25 (40.23) | 25 (40.23) | ×1 |
| EDF_ArtTank_1 | ArtTank | 20 (32.19) | 60 (96.56) | 20 (32.19) | ×3 |
| EDF_Supplytruck_2 | EDFSupplyTruck2 | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_Supplytruck_3 | EDFSupplyTruck3 | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_Supplytruck_Gauss | EDFSupplyTruckGauss | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_Supplytruck_Gauss2 | EDFSupplyTruckGauss2 | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_Supplytruck_Gauss3 | EDFSupplyTruckGauss3 | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_Supplytruck_NoTurret | EDFSupplyTruckNoTurret | 37 (59.55) | 37 (59.55) | 37 (59.55) | ×1 |
| EDF_Supplytruck_NTurret2 | EDFSupplyTruckNoTurret2 | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| EDF_Supplytruck_NTurret3 | EDFSupplyTruckNoTurret3 | 37 (59.55) | 111 (178.64) | 37 (59.55) | ×3 |
| Min_SupplyTruck_MG1 | MinSupplyTruckMG1 | 44 (70.81) | 132 (212.43) | 44 (70.81) | ×3 |
| Min_SupplyTruck_MG2 | MinSupplyTruckMG2 | 44 (70.81) | 132 (212.43) | 44 (70.81) | ×3 |
| Min_SupplyTruck_MG3 | MinSupplyTruckMG3 | 44 (70.81) | 132 (212.43) | 44 (70.81) | ×3 |
| Col_TrashTruck_MG1 | TrashTruckMG1 | 42 (67.59) | 126 (202.78) | 42 (67.59) | ×3 |
| Col_TrashTruck_1 | Trash | 42 (67.59) | 126 (202.78) | 42 (67.59) | ×3 |
| Min_DumpTruck_1 | DumpTruck | 32 (51.5) | 96 (154.5) | 32 (51.5) | ×3 |
| Min_DumpTruck_2 | DumpTruck2 | 32 (51.5) | 96 (154.5) | 32 (51.5) | ×3 |
| Min_DumpTruck_3 | DumpTruck3 | 32 (51.5) | 96 (154.5) | 32 (51.5) | ×3 |
| Min_Bulldozer_1 | Bulldozer | 35 (56.33) | 105 (168.98) | 35 (56.33) | ×3 |
| Col_FuelTanker_1 | Tanker | 35 (56.33) | 35 (56.33) | 35 (56.33) | ×1 |
| Col_FuelTanker_2 | Tanker2 | 35 (56.33) | 105 (168.98) | 35 (56.33) | ×3 |
| Col_FuelTanker_3 | Tanker3 | 35 (56.33) | 105 (168.98) | 35 (56.33) | ×3 |
| Col_FixedFlatbed | Flatbed | 35 (56.33) | 35 (56.33) | 35 (56.33) | ×1 |
| Col_FixedFlatbed2 | Flatbed2 | 35 (56.33) | 35 (56.33) | 35 (56.33) | ×1 |
| Col_FixedFlatbed3 | Flatbed3 | 35 (56.33) | 35 (56.33) | 35 (56.33) | ×1 |
| Min_Rover-A_1WK | MiningRoverWK1 | 55 (88.51) | 165 (265.54) | 55 (88.51) | ×3 |
| Min_Rover-A_2WK | MiningRover2WK | 55 (88.51) | 165 (265.54) | 55 (88.51) | ×3 |
| Min_Rover-A_3WK | MiningRover3WK | 55 (88.51) | 165 (265.54) | 55 (88.51) | ×3 |
| EDF_StaffCar_H2H | StaffcarH2H | 50 (80.47) | 150 (241.4) | 50 (80.47) | ×3 |
| EDF_MediumTank-A_4 | MediumTankClean | 25 (40.23) | 75 (120.7) | 25 (40.23) | ×3 |
| EDF_ArtTank_2 | SuperTank | 20 (32.19) | 60 (96.56) | 20 (32.19) | ×3 |

### dlc01_vehicles.xtbl

| ID | Tên trong dữ liệu | Original | misc hiện tại | table hiện tại | misc/gốc |
|---|---|---:|---:|---:|---:|
| EDF_ScoutTrans1 | DLCScoutTrans1 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_ScoutTrans2 | DLCScoutTrans2 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_ScoutTrans3 | DLCScoutTrans3 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |
| EDF_APC_Super_Gauss | APCSuperGauss | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_Flyer_Rocket | FlyerRocket | — | — | — | — |
| Mar_chomper | Chomper | 52 (83.69) | 52 (83.69) | 52 (83.69) | ×1 |
| Mar_chomper_MG | ChomperMG | 52 (83.69) | 52 (83.69) | 52 (83.69) | ×1 |
| Mar_chomper_MGWing | ChomperMGWing | 52 (83.69) | 52 (83.69) | 52 (83.69) | ×1 |
| Mar_chomper_Harp | ChomperHarp | 52 (83.69) | 52 (83.69) | 52 (83.69) | ×1 |
| Mar_stomper_MG | StomperMG | 47 (75.64) | 47 (75.64) | 47 (75.64) | ×1 |
| EDF_APC_Super_Gauss2 | APCSuperGauss2 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC_Super_Gauss3 | APCSuperGauss3 | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| EDF_APC_Super_Gauss4 | APCSuperGaussClean | 46 (74.03) | 46 (74.03) | 46 (74.03) | ×1 |
| Mar_Walker | Mar_Walker | — | — | — | — |
| DLC_Dans_Tank | HeavyTank | 20 (32.19) | 20 (32.19) | 20 (32.19) | ×1 |
| EDF_ScoutTrans4 | DLCScoutTrans4 | 63 (101.39) | 63 (101.39) | 63 (101.39) | ×1 |

## Những giới hạn lùi đã thay đổi

Đơn vị **mph (km/h)**. Các giới hạn lùi khai báo khác giữ gốc; xem CSV để có toàn bộ giá trị và các trường không khai báo riêng.

| ID | Original | misc hiện tại | table hiện tại |
|---|---:|---:|---:|
| EDF_HeavyTank-A_1 | 20 (32.19) | 60 (96.56) | 20 (32.19) |
| Col_Mini_Hauler_1 | 15 (24.14) | 45 (72.42) | 15 (24.14) |
| Col_Mini_Hauler_2 | 15 (24.14) | 45 (72.42) | 15 (24.14) |
| EDF_HeavyTank-A_2 | 20 (32.19) | 60 (96.56) | 20 (32.19) |
| Tharsis_gun | 5 (8.05) | 15 (24.14) | 5 (8.05) |
| Min_Bulldozer_1 | 35 (56.33) | 105 (168.98) | 35 (56.33) |

## Nhóm xe và dữ liệu mặc định

`vehicle_groups.xtbl` và `vehicle_defaults.xtbl` không đổi giữa gốc và hai gói mod. Small/Medium/Large có giới hạn tiến riêng 60/50/45; Tank/Flyer/Mech không có. Bản ghi `Vehicle Defaults` có giới hạn tiến 90, lùi 35. Không áp các con số này như tốc độ thực tế của walker/flyer: dữ liệu hiện có chưa xác nhận cách các lớp xe đặc biệt sử dụng chúng.

## Lưu ý khi đọc kết quả

- Tăng mô-men xoắn hoặc RPM có thể làm xe tăng tốc khác đi ngay cả khi giới hạn tốc độ tiến vẫn giữ gốc. CSV kèm torque, Min/Max RPM để đối chiếu; không dùng RPM để tự suy ra vận tốc tối đa.
- `Max_Speed_Steering` là thông số điều khiển lái, không dùng thay cho giới hạn tốc độ xe trong bảng.
- Các override của nhiệm vụ, tốc độ điều khiển AI và trạng thái vật lý có thể ảnh hưởng vận tốc thực; chưa chạy game để đo chúng.

## Nguồn và kiểm tra

Đọc trực tiếp hai VPP hiện tại bằng bộ kiểm tra cấu trúc độc lập; đối chiếu tập ID và giá trị với original. Công thức quy đổi: 1 mph = 1.609344 km/h = 0.44704 m/s. Không sửa bất kỳ dữ liệu game nào khi lập báo cáo.

SHA-256 của VPP nguồn:

- `misc.vpp_pc`: `9dcd2d8311ccd03b65617659328479971fbc830d57175019591f97440004be58`
- `table.vpp_pc`: `b15464c257faf1fc0f8005970f33896126cf7f43d73e7fe81b518c18a91c31c7`
