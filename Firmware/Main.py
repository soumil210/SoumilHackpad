import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_rgb_matrix import PegRGBMatrix
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306Driver

keyboard = KMKKeyboard()


keyboard.col_pins = (board.D3, board.D7, board.D8)   # Col 0, Col 1, Col 2
keyboard.row_pins = (board.D0, board.D2, board.D1)   # Row 0, Row 1, Row 2
keyboard.diode_orientation = DiodeOrientation.COL2ROW


rgb = PegRGBMatrix(
    pixel_pin=board.D6,
    num_pixels=9,
)
keyboard.extensions.append(rgb)

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D10, board.D9, None, False),
)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),
]
keyboard.modules.append(encoder_handler)


i2c_bus = busio.I2C(scl=board.D5, sda=board.D4)
oled_driver = SSD1306Driver(128, 32, i2c=i2c_bus)
display = Display(
    display=oled_driver,
    entries=[TextEntry(text="KMK Macropad", x=0, y=0)],
)
keyboard.extensions.append(display)


keyboard.keymap = [
    [
        KC.NUM1, KC.NUM2, KC.NUM3,
        KC.NUM4, KC.NUM5, KC.NUM6,
        KC.NUM7, KC.NUM8, KC.NUM9,
    ]
]

if __name__ == '__main__':
    keyboard.go()