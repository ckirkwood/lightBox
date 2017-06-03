import time
import sys
from gpiozero import Button
from neopixel import *


# LED strip configuration:
LED_COUNT      = 48
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False

# Button configuration
button1 = Button(19)
button2 = Button(16)

# Basic on/off commands (set color to 0, 0, 0 for off)
def onOff(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

# Main program logic:
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()

	print ('Press Ctrl-C to quit.')

try:
	while True:
    		if button1.is_pressed == True:
			onOff(strip, Color(255, 255, 255))
		elif button2.is_pressed == True:
			onOff(strip, Color(0, 0, 0))
except KeyboardInterrupt():
    sys.exit()
