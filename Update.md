---
layout: default
title: Updating Tomu
permalink: /update
---

# Installing dfu-util

The `dfu-util` suite of programs is used to talk to `Toboot`,
the Tomu bootloader.  Most package managers have some form of
`dfu-util` available.

## Ubuntu and Debian

````sh
sudo apt-get install dfu-util
````

Create `/etc/udev/rules.d/10-tomu.rules` and populate it with the following:

````udev
ATTRS{idProduct}=="70b1", ATTRS{idVendor}=="1209", \
     MODE="664", GROUP="plugdev"
````

## Fedora

````sh
sudo yum install dfu-util
````

## Arch

````sh
sudo pacman -Sy dfu-util
````

## Windows

Download [dfu-util-static.exe](http://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/win32-mingw32/dfu-util-static.exe) from the `dfu-util` repository and rename it to `dfu-util.exe`.  Place it somewhere in your $PATH for convenience.

## Mac

Install [Homebrew](https://brew.sh/) and run:

````sh
brew install dfu-util
````

# Updating Toboot

Normally, Toboot is unable to overwrite itself.  To work around this, use a "boosted" form of Toboot.

First, determine your current version by running `dfu-util -l`:

````sh
dfu-util -l
````

Next, download [toboot-boosted.dfu](https://github.com/im-tomu/tomu-bootloader/raw/master/prebuilt/toboot-boosted.dfu).

Finally, load it using `dfu-util`:

````sh
dfu-util -D toboot-boosted.dfu
````

You can check to make sure Toboot has updated by looking at the version number returned by `dfu-util -l`:

````sh
dfu-util -l
````