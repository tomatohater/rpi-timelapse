# Create a time lapse videos with a Raspberry Pi

Use `motion` on a Raspberry Pi to record time lapse videos.

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
* Ethernet internet connection
* External display (HDMI input)

## Setting up the RPi

1. Download and extract Raspbian OS (Wheezy) from https://www.raspberrypi.org/downloads/raspbian/
1. Burn Raspbian OS (Wheezy) onto the microSD card
   `sudo dd bs=1m if=/path/to/2015-05-05-raspbian-wheezy.img of=/dev/rdisk2`
1. Insert microSD card into Raspberry Pi and power it up. Plug in the mouse, keyboard, camera, thumb drive, ethernet.
1. Run through the install screens. Don't forget to expand the volumes. And localize.
1. Open up a shell and update the packages
    `sudo apt-get update && sudo apt-get upgrade`
1. Install Motion
    `sudo apt-get install motion`
1. Clone the contents of this repo into /home/pi/timelapse
1. Make sure the scripts are executable. `chmod a+x scripts/*`
1. Make a target directory for the thumb mount. `sudo mkdir /media/thumb`
1. Add the contents of setup/fstab to the end of /etc/fstab. Reboot.
1. Add the contents of setup/crontab to pi's crontab `crontab -e`
1. Sit back and enjoy. And don't pick your nose... you're on camera now.

More to come...


### Acknowledgements
Special thanks to fellow Huger David Gómez (https://github.com/davegomez/) for just about everything.
