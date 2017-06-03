import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 48      
LED_PIN        = 18     
LED_FREQ_HZ    = 800000  
LED_DMA        = 5       
LED_BRIGHTNESS = 255     
LED_INVERT     = False   

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def onOff(strip, color):
	for i in range(strip.numPixels()):	
		strip.setPixelColor(i, color)
		strip.show()

# Main program logic:
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		onOff(strip, Color(255, 0, 0))
		time.sleep(1)
		allOff()
