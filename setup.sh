#!/bin/bash
# Run me with superuser privileges
# Setup SPI control for e-ink display
echo 'dtparam=spi=on' >> /boot/config.txt

# setup device tree overlay gpio pins for pwm for audio
# add to /boot/config.txt
# dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4
echo 'dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4' >> /boot/config.txt

# Force audio to mono on BCM 13
echo '# convert stereo to mono RIGHT output

pcm.monocard{
  slave.pcm "hw:1"
  slave.channels 2
  type route
  ttable {
    # Copy both input channels to output channel 1 (Right).
    0.1 1
    1.1 1
    # Send nothing to output channel 0 (Left).
    0.0 0
    1.0 0
  }
}

pcm.!default monocard' > /etc/asound.conf

# Force audio jack sound output
amixer cset numid=3 1

# set hostname as pokedex
echo 'pokedex' > /etc/hostname
echo '127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters

127.0.1.1       pokedex' > /etc/hosts

# reboot after all chagnes
reboot