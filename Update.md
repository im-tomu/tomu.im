---
layout: default
title: Updating Tomu
permalink: /update
---

Your Tomu must be updated in order to work best.  To work with Tomu, you can use an experimental method via Google Chrome, otherwise you must first install `dfu-util`.  With either method updating Tomu is as easy as loading any other program!

## Via Google Chrome

### Get Google Chrome

You might know the drill, visit https://google.com/chrome and grab the right version for your platform or install the FOSS version Chromium from your package manager.

### Update Tomu bootloader

Next visit https://devanlai.github.io/webdfu/dfu-util/ with your Tomu plugged in and select the right vendor ID `0x1209` aka `tapboot` from the prepopulated options or type it and click "Connect". You should see something like ```Name: Tomu Bootloader v2.0-rc4
MFG: Kosagi
Serial: 
DFU: [1209:70b1] cfg=1, intf=0, alt=0, name="Tomu Bootloader v2.0-rc4" serial=""```

Next, download [toboot-boosted.dfu](https://github.com/im-tomu/tomu-bootloader/raw/master/prebuilt/toboot-boosted.dfu).

Finally update your Tomu by browsing to the `toboot-boosted.dfu` file in the "Firmware Download" area of the page and then click "Download" to flash it to the device. Once that completes you can click "Connect" again to verify the version strings changed.

### Upload a program

To configure a program you can try a prebuilt one from the samples page [Samples](http://tomu.im/samples) or compile your own using the directions there. Put it on your Tomu by browsing to the file in the "Firmware Download" area of the page and then click "Download" to flash it to the device. 

Once a program is installed your Tomu will stop blinking red/green (the DFU bootloader indicator) and will blink whatever is coded into the program while executing it. When flashing any sample program it doesn't stick permanently, in this case you can simply unplug/replug the Tomu to get back to the bootloader. With a non-sample application, once it is flashed they are configured to auto-start on power-up, so in order to get back into Bootloader mode to flash something else you must use a tweezer or paperclip across the outer contacts when inserting it into the USB port (it is important that it is shorted during power-up. I've found that putting the Tomu into a USB extension cable or hub so you can short the connection while plugging the cable with your other hand to be easiest.

## Installing dfu-util

The `dfu-util` suite of programs is used to talk to `Toboot`,
the Tomu bootloader.  Most package managers have some form of
`dfu-util` available.

### Ubuntu and Debian

````sh
sudo apt-get install dfu-util
````

Create `/etc/udev/rules.d/10-tomu.rules` and populate it with the following:

````udev
ATTRS{idProduct}=="70b1", ATTRS{idVendor}=="1209", MODE="777"
````

(Note: you can give it a more restrictive mode if you also give it a group that you're in)

### Fedora

````sh
sudo yum install dfu-util
````

### Arch

````sh
sudo pacman -Sy dfu-util
````

### Windows

Download [dfu-util-static.exe](http://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/win32-mingw32/dfu-util-static.exe) from the `dfu-util` repository and rename it to `dfu-util.exe`.  Place it somewhere in your $PATH for convenience.  To build examples, you'll also want to get [dfu-suffix.exe](http://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/win32-mingw32/dfu-suffix.exe) and put it in your $PATH.

### Mac

Install [Homebrew](https://brew.sh/) and run:

````sh
brew install dfu-util
````

## Updating Toboot

Normally, Toboot is unable to overwrite itself.  To work around this, use a "boosted" form of Toboot.

First, determine your current version by running `dfu-util --list`:

````sh
user@machine:~$ dfu-util --list
dfu-util 0.7

Copyright 2005-2008 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2012 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to dfu-util@lists.gnumonks.org

Found DFU: [1209:70b1] devnum=0, cfg=1, intf=0, alt=0, name="Tomu Bootloader v2.0-rc4"
user@machine:~$ 
````

Next, download [toboot-boosted.dfu](https://github.com/im-tomu/tomu-bootloader/raw/master/prebuilt/toboot-boosted.dfu).

Finally, load it using `dfu-util -D toboot-boosted.dfu`:

````sh
user@machine:~$ dfu-util -D toboot-boosted.dfu
dfu-util 0.7

Copyright 2005-2008 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2012 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to dfu-util@lists.gnumonks.org

Opening DFU capable USB device... ID 1209:70b1
Run-time device DFU version 0101
Found DFU: [1209:70b1] devnum=0, cfg=1, intf=0, alt=0, name="Tomu Bootloader v2.0-rc4"
Claiming USB DFU Interface...
Setting Alternate Setting #0 ...
Determining device status: state = dfuIDLE, status = 0
dfuIDLE, continuing
DFU mode device DFU version 0101
Device returned transfer size 1024
Dfu suffix version 100
bytes_per_hash=133
Copying data from PC to DFU device
Starting download: [##################################################] finished!
state(7) = dfuMANIFEST, status(0) = No error condition is present
state(8) = dfuMANIFEST-WAIT-RESET, status(0) = No error condition is present
Done!
user@machine:~$ 
````

You can check to make sure Toboot has updated by looking at the version number returned by `dfu-util --list`:

````sh
user@machine:~$ dfu-util --list
dfu-util 0.7

Copyright 2005-2008 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2012 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to dfu-util@lists.gnumonks.org

Found DFU: [1209:70b1] devnum=0, cfg=1, intf=0, alt=0, name="Tomu Bootloader (5) v2.0-rc6"
user@machine:~$ 
````

## Changes

* **v2.0-rc6**
  * Fix V1 and raw binary data -- now you can load legacy programs
  * Correct an issue that could cause Toboot itself to get overwritten
* **v2.0-rc5**
  * Report the reason for entering Toboot in the device name
* **v2.0-rc4**
  * Initial release on Crowd Supply devices
