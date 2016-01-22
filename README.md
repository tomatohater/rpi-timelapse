# Create a time lapse videos with a Raspberry Pi

Use `motion` on a a Raspberry Pi to take awesome time lapse videos.

## Equipment

* Raspberry Pi 2 Model B 1GB
* Logitech HD Pro Webcam C920
* USB Flash Drive 32GB+ (not HDD)
* 16GB MicroSDHC card
* MicroUSB power adapter

During installation only...

* USB keyboard
* USB mouse
* HDMI cable
* External display (HDMI input)

## Setting up the RPi

1. Download and extract Raspbian OS (Wheezy) from https://www.raspberrypi.org/downloads/raspbian/
1. Burn Raspbian OS (Wheezy) onto the microSD card
   `sudo dd bs=1m if=/path/to/2015-05-05-raspbian-wheezy.img of=/dev/rdisk2`
1. Insert microSD card into Raspberry Pi and power it up
1. Run through the install screens. Don't forget to expand the volumes. And localize.
1. Open up a shell and update the packages
    `sudo apt-get update && sudo apt-get upgrade`
1. Install Motion
    `sudo apt-get install motion`

More to come...
