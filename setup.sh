# Setup SPI control for e-ink display
sudo echo 'dtparam=spi=on' >> /boot/config.txt

# setup device tree overlay gpio pins for pwm for audio
# add to /boot/config.txt
# dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4
sudo echo 'dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4' >> /boot/config.txt

# Force audio to mono
sudo echo '# convert stereo to mono LEFT output

pcm.monocard{
  slave.pcm "hw:N"
  slave.channels 2
  type route
  ttable {
    # Copy both input channels to output channel 0 (Left).
    0.0 1
    1.0 1
    # Send nothing to output channel 1 (Right).
    0.1 0
    1.1 0
  }
}

pcm.!default monocard' > /etc/asound.conf

# Force audio jack sound output
sudo amixer cset numid=3 1

# set hostname as pokedex
sudo echo 'pokedex' > /etc/hostname
sudo nano /etc/hosts

# reboot after all chagnes
sudo reboot