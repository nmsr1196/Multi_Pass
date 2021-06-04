"""CircuitPython Essentials NeoPixel example by Adafrut.MultiPass/StuartRiggs5/2021"""

import time
import board
import neopixel
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

# NeoPixels Section
pixel_pin = board.A0
num_pixels = 7
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

# i2c Section for OLED Display
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context for Fhloston Paradise Access
splash = displayio.Group(max_size=10)
display.show(splash)

inner_bitmap = displayio.Bitmap(118, 24, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

time.sleep(.005)

inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)
time.sleep(.005)
text = "A P P R O V E D !"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=15, y=15)
splash.append(text_area)
time.sleep(1)

color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

time.sleep(.5)

inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

# Text Setup for OLED Display for 1 Time Cycle
text = "V A C C I N E ..."
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=15, y=15)
splash.append(text_area)

color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

time.sleep(2)

inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

text = "V  A  L  I  D  !"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=15, y=15)
splash.append(text_area)

color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

# NeoPixel Pattern
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

# NeoPixel Color Selection
TURNBLUE = (0, 0, 255)
TURNOFF = (0, 0, 0)
TURNGREEN = (0, 255, 0)

# Main Loop
while True:
    pass
    color_chase(TURNGREEN, 0.001)  # Increase the number to slow down the color chase
    color_chase(TURNBLUE, 0.002)
    pixels.fill(TURNOFF)
    pixels.show()
    time.sleep(1)
