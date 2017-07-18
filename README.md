# lightBox

lightBox v1.0 is a cardboard prototype using WS2812 RGB Neopixel LEDs, driven by a Raspberry Pi Zero W. Commands are assigned to API endpoints, which allows a web app to control the Neopixels.

### Core Hardware
- RGB LEDs, i.e. WS2812
- Raspberry Pi Zero W
- Adafruit Perma-Proto HAT
- 1x 1N4001 diode
- 1x 1000 µF capacitor
- DC barrel jack adapter
- 12v 3A power supply (requirements vary between LED types)
- Connection wires

### Optional - Casing Hardware
- Project box (the shipping box for the Mag Pi #57 / Google AIY Kit is perfect)
- Diffusing material
- Reflective tape
- Panel mount micro-usb extension
- Pimoroni On/Off Shim
- Rocker switch (wired to On/Off Shim)
- Momentary buttons
- Hot glue
- M2.5 bolts/stand-offs

### Wiring
Adafruit's [Neopixels on Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) guide covers two methods of connecting the Neopixels - the diode method is much simpler, and can be transferred to a mini Perma-Proto HAT.

5m LED strips tend to come with JST SM connectors attached to both ends for factory testing, so the spare male JST wiring can be attached to the HAT to keep everything modular. I've also bought some simple 3-wire JST assemblies for future builds.

### Installation / Setup
Again, Adafruit [covers the installation process]() using the [rpi_W281x library](https://github.com/jgarff/rpi_ws281x), and the `strandtest.py` example is a great platform to build on.

I was only planning to control the Neopixels with buttons (and later remote switches), until I found [neopixel-rpi-web](https://github.com/CYBERRRR/neopixel-rpi-web). The JQuery colour picker plug-in was buggy and possibly deprecated, but I learnt enough from the core structure of the Flask web app that it was fairly simple to throw together a quick interface for control. I've set up some of the functions from `strandtest.py` as endpoints, which also display a webpage when called - to keep a consistent interface, the endpoints just need to return the same `index.html`. Buttons on the webpage in turn link to the API endpoints.

At some point towards the end of the build, the [clean-shutdown](https://github.com/pimoroni/clean-shutdown) daemon that drives the On/Off Shim stopped working, and using it will now shutdown the Pi before it has a chance to boot. Until I've figured out how to stop this, I've added simple shutdown and reboot functions and assigned them to endpoints/web buttons.

The final step was to assign a static IP to the Pi Zero and add a command to crontab to run `lightbox.py` at boot, and the lightBox can now function without any SSH interference.

![lightBox web app](https://res.cloudinary.com/ckirkwood/image/upload/v1497204345/lightBox_WebApp.png)

#### References
- [Adafruit - Neopixels Uberguide](https://learn.adafruit.com/adafruit-neopixel-uberguide/overview)
- [Adafruit - Neopixels on Raspberry Pi Guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)
- [Pimoroni - Mote / Homekit tutorial](https://learn.pimoroni.com/tutorial/sandyj/using-mote-with-homekit-and-siri)
- [Pimoroni - Mote Flask API](https://github.com/pimoroni/mote/blob/master/python/examples/mote-api.py)
- [jgarff - rpi_W281x](https://github.com/jgarff/rpi_ws281x)
- [CYBERRRR - neopixel-rpi-web](https://github.com/CYBERRRR/neopixel-rpi-web)
