# SoumilHackpad

Blueprint hackpad project repository.

## Project Overview

- Hackpad name: SoumilHackpad
- Creator: soumilvyas1
- Description: Add your short project description here.

## Repository Structure

- `CAD/` - Full assembled hackpad model (`.STEP`, `.STP`, or `.3MF`)
- `PCB/` - PCB source design files (for KiCad: `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`)
- `Firmware/` - Firmware source files (`QMK`, `KMK`, `ZMK`, etc.)
- `production/` - Manufacturing-ready outputs (gerbers, case exports, firmware build)

## Required Design Constraints

- Through-hole Seeed XIAO RP2040 as main MCU
- PCB size <= `100mm x 100mm`
- Case size <= `200mm x 200mm x 100mm`
- Fewer than 16 inputs total
- Approved parts only
- 2-layer PCB only
- 3D printed case parts only (no acrylic/laser-cut parts)

## Submission Checklist

### Source Files

- [ ] `CAD/assembly.step` (or `.stp` / `.3mf`) with PCB and all case parts
- [ ] `PCB/` source files are complete
- [ ] `Firmware/` source files are complete

### Production Files

- [ ] `production/gerbers.zip`
- [ ] `production/Top.step` (or `.stl`)
- [ ] `production/Bottom.step` (or `.stl`)
- [ ] `production/Middle.step` (or `.stl`) if used
- [ ] `production/firmware.uf2` (QMK) or `production/main.py` (KMK)

## Screenshots (Required)

### 1. Overall Hackpad

![Overall Hackpad](Images/Cadpicture.png)

### 2. Schematic

![Schematic](Images/schematicpicture.png)

### 3. PCB

![PCB](Images/pcbpicture.png)

### 4. Case Fit / Assembly

Case fit image not added yet.

## BOM

| Item | Qty | Part Number / Link | Notes |
| --- | --- | --- | --- |
| Seeed XIAO RP2040 (Through-hole, unsoldered) | 1 | Seeed XIAO RP2040 | Main MCU |
| 1N4148 Diodes (through-hole) | 20 | 1N4148 | Through-hole diodes |
| MX-Style switches | 16 | MX-compatible | Main key switches |
| EC11 Rotary encoders | 2 | EC11 | Rotary input |
| 0.91 inch OLED display | 1 | 0.91" I2C OLED | Pin order must be `GND-VCC-SCL-SDA` |
| White blank DSA keycaps | 16 | DSA blank keycaps | For 16-key layout |
| SK6812 MINI-E LEDs | 16 | SK6812 MINI-E | Per-key lighting |
| M3x16mm screws | 4 | M3x16mm | Case assembly |
| M3x5mx4mm heatset inserts | 4 | M3x5mx4mm | Case inserts |

## Ship Post Template

Post this in `#blueprint-drafts` on Slack:

```text
Hackpad name: SoumilHackpad
GitHub Repo: https://github.com/soumil210/SoumilHackpad
Description: <short description of your project>
```

Attach images of your hackpad with the post.

## Final Submission

1. Submit design review from the Blueprint dashboard.
2. Keep this repo up to date with any review feedback.
