# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkey: Google Chrome web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Windows Chrome', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'Size -', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x202000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000040, 'Tab', [Keycode.CONTROL, 't']),
        (0x000040, 'Private', [Keycode.CONTROL, 'N']),
        # 4th row ----------
        (0x000000, 'Ada', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'www.adafruit.com\t']),   # Adafruit in new window
        (0x800000, 'Digi', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                            'www.digikey.com\t']),   # Digi-Key in new window
        (0x101010, 'Hacks', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'www.hackaday.com\t']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
