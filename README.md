# PokePiDex
Raspberry Pi Zero Pokedex

## Bill of Materials:
- [3D printed case](https://www.thingiverse.com/thing:3698203)
- 5mm Blue LED
- 5mm Red LED
- 5mm Yellow LED
- 5mm Green LED
- 3mm Red LED x2
- Raspberry Pi Zero

### Power:
- [Adafruit push button power switch](https://www.adafruit.com/product/1400)
- LiPo battery charger from [Sparkfun](https://www.sparkfun.com/products/12711) or [Adafruit](https://www.adafruit.com/product/259)
- [QI wireless charging module](https://www.adafruit.com/product/2114)

### Display:
- [2.7" e-ink display from waveshare](https://www.waveshare.com/product/2.7inch-e-paper.htm)
- [Adafruit e-ink breakout friend with SRAM](https://www.adafruit.com/product/4224)

### Audio:
- Cheap-o earbud speaker
- 10nF-33nF capacitor
- 150 ohm resistor
- 270 ohm resistor
- 10uF capacitor

## Info
- `setup.sh` script sets up raspberry pi settings, not tested yet
- `requirements.txt` intended to list all python modules that must be installed for auto-pip3 setup. Not finished/tested yet. Just trying to keep some sort of list.

## Notes
Might need to switch to paplay, mplayer or ogg123 for audio files in ogg format

### E-Ink Issues
1. Started with Teensyduino with Adafruit e-ink breakout friend and Adafruit 2.13" flexible display. No success
2. Switch to Arduino Uno with same Adafruit breakout + display, still no success. Program hangs forever waiting for idle.
3. Realized for scope purposes + timeline, easier to switch to Raspberry Pi. Had success with PaPirus hat, but need something thinner and more square.
4. Tested RPIzero + python3 + Adafruit breakout + Adafruit display with Blinka.py following tutorials. No change on e-ink.
5. Tried epdtest.py with RPIzero and same Adafruit bits and did not work. Made edits for pi pins with no success
6. Found Waveshare python driver on github via adafruit. Tried that with waveshare 2.7" display and Adafruit breakout. Hung waiting on idle.
7. Got annoyed and swapped pin to be true when busy, no longer hung waiting for idle, and technically completed the whole python script, but no change to display.
8. Waveshare github talks about waveshare HATS with buttons, so need to look at pin logic/number differences in more detail between Adafruit breakout board and Waveshare HAT board
9. Maybe my Adafruit breakout is bad?
10. Or more likely: I have something screwy with how RPIzero pins work that I'm just not understanding so I'm plugging things in wrong/defining pins wrong

## Resources
[Pokemon Cries and Sprites from Veekun](https://github.com/veekun/pokedex)

[Audio Setup and Circuit](https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero/pi-zero-pwm-audio)

[Stereo to Mono audio via software](https://www.tinkerboy.xyz/raspberry-pi-downmixing-from-stereo-to-mono-sound-output/)

[Waveshare display info](https://diyprojects.io/test-waveshare-epaper-eink-2-7-spi-screen-raspberry-pi-python/#.XSPpHuhKiUk)

[Waveshare 2](https://blog.adafruit.com/2018/07/31/e-paper-display-driver-code-for-circuitpython-with-a-fractal-demo/)

[Waveshare 3](https://github.com/gpshead/epaper-circuitpython)
