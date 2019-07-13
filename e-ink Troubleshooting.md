## Hardware

First we need to make sure that everything is wired up correctly.
The following connections should be made:

 - BREAKOUT.VIN     <-  RPI.3v3 (1)
 - BREAKOUT.3V3     Not connected
 - BREAKOUT.GND     <-  RPI.GND (6)
 - BREAKOUT.SCK     <-  RPI.SPI0 SCLK (23)
 - BREAKOUT.MISO    ->  RPI.SPI0 MISO (21)
 - BREAKOUT.MOSI    <-  RPI.SPI0 MOSI (10)
 - BREAKOUT.ECS     <-  RPI.BCM 27 (13)
 - BREAKOUT.D/C     <-  RPI.BCM 25 (22)
 - BREAKOUT.SRCS    <-  RPI.BCM 22 (15)
 - BREAKOUT.RST     <-  RPI.BCM 23 (16)
 - BREAKOUT.BUSY    ->  RPI.BCM 24 (18)
 - BREAKOUT.ENA     Not connected

Verify that the ribbon cable from the 2.7" display is connected to the Adafruit Breakout board is inserted correctly.

## Raspberry Pi

Verify that SPI is enabled.
Install all the required python libraries.

## Software

Use the following code to test the display:

    import digitalio
    import busio
    import board
    from adafruit_epd.epd import Adafruit_EPD
    
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    ecs = digitalio.DigitalInOut(board.D27)
    dc = digitalio.DigitalInOut(board.D25)
    srcs = digitalio.DigitalInOut(board.D22)
    rst = digitalio.DigitalInOut(board.D23)
    busy = digitalio.DigitalInOut(board.D24)
    
    from adafruit_epd.il91874 import Adafruit_IL91874
    display = Adafruit_IL91874(176, 264, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs, rst_pin=rst, busy_pin=busy)
    
    display.fill(Adafruit_EPD.WHITE)
    
    display.fill_rect(0, 0, 50, 60, Adafruit_EPD.BLACK)
    display.hline(80, 30, 60, Adafruit_EPD.BLACK)
    display.vline(80, 30, 60, Adafruit_EPD.BLACK)
    
    display.display()

May need to run this code as root.