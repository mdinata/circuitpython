import gc
import time
import audioio
import digitalio
import board
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

gc.collect()
time.sleep(1)
gc.mem_free()

keymap = {
    "center": Keycode.ENTER,#center
    "right": Keycode.RIGHT_ARROW, #right
    "down": Keycode.DOWN_ARROW, #down
    "left": Keycode.LEFT_ARROW, #left
    "up": Keycode.UP_ARROW, #up
    "power": Keycode.ESCAPE #escape
    }

kbd = Keyboard()

spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

gc.collect()
time.sleep(1)
gc.mem_free()

import pulseio
import time
import adafruit_irremote
from neopixel import NeoPixel
pixels = NeoPixel(board.NEOPIXEL, 10, brightness=.05)

def flash(r,g,b):
    pixels.fill((r, g, b))
    pixels.show()
    time.sleep(0.01)
    pixels.fill((0, 0, 0))
    pixels.show()
    
gc.collect()
time.sleep(1)
gc.mem_free()

pulsein=pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
decoder= adafruit_irremote.GenericDecode()

filename='alert.wav'

def play_file(filename):
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                pass

while True:
    gc.mem_free()
    pulses=decoder.read_pulses(pulsein)

    try:
        received_code=decoder.decode_bits(pulses, debug=False)
    except adafruit_irremote.IRNECRepeatException:
        continue
    except adafruit_irremote.IRDecodeException as e:
        continue

    if received_code == [158, 41, 183, 72]:
        x=keymap['power']
        print("ESCAPE")
        flash(255,0,0)
    if received_code == [158, 41, 95, 160]:
        x=keymap['center']
        print("ENTER")
        flash(255,255,255)
        play_file(filename)
    if received_code == [158, 41, 159, 96]:
        x=keymap['right']
        print("RIGHT")
        flash(0,255,0)
    if received_code == [158, 41, 167, 88]:
        x=keymap['down']
        print("DOWN")
        flash(0,0,255)
    if received_code == [158, 41, 223, 32]:
        x=keymap['left']
        print("LEFT")
        flash(255,255,0)
    if received_code == [158, 41, 39, 216]:
        x=keymap['up']
        print("UP")
        flash(255,0,255)

    gc.collect()
    kbd.press(x)
    time.sleep(0.02)
    kbd.release(x)