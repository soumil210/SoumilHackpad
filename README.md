# SoumilHackpad

Blueprint hackpad project repository.

## Project Overview

- Hackpad name: SoumilHackpad
- Creator: soumil
- Description: My macropad has 9 keys, a small OLED, and a rotary encoder. I can use it for macros, volume control, or just for fun. :)

## Repository Structure

- `CAD/` - Full assembled hackpad model )
- `PCB/` - PCB source design files 
- `Firmware/` - Firmware source files 
- `production/` - Manufacturing-ready outputs 

## Required Design Constraints

- Through-hole Seeed XIAO RP2040 as main MCU
- PCB size <= `100mm x 100mm`
- Case size <= `200mm x 200mm x 100mm`
- Fewer than 16 inputs total
- Approved parts only
- 2-layer PCB only
- 3D printed case parts only (no acrylic/laser-cut parts)



## Screenshots 

### 1. Overall Hackpad

![Overall Hackpad](Images/Cadpicture.png)

### 2. Schematic

![Schematic](Images/schematicpicture.png)

### 3. PCB

![PCB](Images/pcbpicture.png)


## BOM

| Item | Qty | Notes |
| --- | --- | --- |
| Seeed XIAO RP2040 (Through-hole, unsoldered) | 1 | Main MCU |
| 1N4148 Diodes (through-hole) | 9 | Through-hole diodes |
| MX-Style switches | 9 | Main key switches |
| EC11 Rotary encoders | 1 | Rotary input |
| 0.91 inch OLED display | 1 | Pin order must be `GND-VCC-SCL-SDA` |
| White blank DSA keycaps | 9 | For 16-key layout |
| SK6812 MINI-E LEDs | 9 | Per-key lighting |

