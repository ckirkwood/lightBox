import time
from colorsys import hsv_to_rgb, rgb_to_hsv
from flask import Flask, request, render_template, jsonify
from gpiozero import Button
from neopixel import *
import signal
import sys

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 48
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False

# Setup Flask api
app=Flask(__name__)

# Button configuration
button1 = Button(19)
button2 = Button(16)

# Create NeoPixel object, initialise library 
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

# Basic on/off commands (set color to 0, 0, 0 for off)
def onOff(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()

def lights_on(c):
    r, g, b = hex_to_rgb(c)
        for pixel in range(strip.numPixels()):
            strip.set_pixel(pixel, r, g, b)
    strip.show()
    return True

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def get_status():
    global status
    for pixel in range(48):
        if strip.getPixelColor(pixel) != (0, 0, 0):
                status = 1
        else:
                status = 0
    return status

@app.route('/lightBox/api/v1.0/<string:st>', methods=['GET'])
def set_status(st):
    global status, Color
    if st == 'on':
        status = 1
        onOff(strip, Color(255, 255, 255))
    elif st == 'off':
        status = 0        
    elif st == 'status':
        status = get_status()
    return jsonify({'status': status, 'colour': colour})

@app.route("/set_color", methods=['POST'])
def set_color():
	rgb = request.get_json()
	allColor(strip, Color(rgb['r'], rgb['g'], rgb['b']))
	return render_template('index.html'), 204

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Main programme logic

if __name__ == "__main__":
	app.run(host='192.168.1.108', port=80, debug=True)

	colorWipe(strip, Color(0, 0, 255))
	colorWipe(strip, Color(0, 0, 0))

while True:
	if button1.is_pressed == True:
		onOff(strip, Color(255, 255, 255))
	elif button2.is_pressed == True:
		onOff(strip, Color(0, 0, 0))
