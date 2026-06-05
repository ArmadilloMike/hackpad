import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.modules.append(KeysScanner(
    pins=[board.D10, board.D9, board.D8, board.D7]
))

keyboard.keymap = [
    [
        KC.LGUI(KC.LSHIFT(KC.S)),       # s4 - D10
        KC.LCTRL(KC.LALT(KC.DELETE)),   # s1 - D9
        KC.LGUI(KC.DOT),                # s2 - D8
        KC.LCTRL(KC.LSHIFT(KC.ESC)),    # s3 - D7
    ]
]

keyboard.go()