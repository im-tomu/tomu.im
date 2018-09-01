---
layout: default
title: Tomu Samples
permalink: /samples
---

Tomu is all about being open and hackable.  It's important to have a good starting point.  Below we have a selection of precompiled programs, along with links to their source code.

To try out these samples, download the `.dfu` file and load it with `dfu-util --download`.

Project   | DFU | Description
---------- | -------------- | --------------
**[bare-minimum](https://github.com/im-tomu/tomu-quickstart/tree/master/bare-minimum)** | [bare-minimum.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/bare-minimum.dfu) | Does nothing, forever, without crashing.
**[miniblink](https://github.com/im-tomu/tomu-quickstart/tree/master/miniblink)** | [miniblink.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/miniblink.dfu) | Blink the two LEDs using the SysTick timer.
**[usb-hid](https://github.com/im-tomu/tomu-quickstart/tree/master/usb-hid)** | [usb-hid.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/usb-hid.dfu) | Emulate a USB mouse, and wiggle the cursor back and forth.
**[usb-msc](https://github.com/im-tomu/tomu-quickstart/tree/master/usb-msc)** | [usb-msc.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/usb-msc.dfu) | Emulate a very small "USB Mass Storage" disk drive.
**[usb-midi](https://github.com/im-tomu/tomu-quickstart/tree/master/usb-midi)** | [usb-midi.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/usb-midi.dfu) | Provide a USB MIDI device that continuously sends NoteOn and NoteOff events.
**[usb-cdcacm](https://github.com/im-tomu/tomu-quickstart/tree/master/usb-cdcacm)** | [usb-cdcacm.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/usb-cdcacm.dfu) | Communicate with Tomu over a virtual serial port.
**[opticspy](https://github.com/im-tomu/tomu-quickstart/tree/master/opticspy)**  | [opticspy.dfu](https://github.com/im-tomu/tomu-quickstart/raw/master/prebuilt/opticspy.dfu) | Interactive shell to communicate with an [OpticSpy](http://www.grandideastudio.com/opticspy/)

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

## Compiling Samples

To compile the samples, you will need an ARM compiler, `make`, and `dfu-util`.  The steps to install these files vary depending on your operating system:

Platform   | ARM Toolchain  | Make  | dfu-util
---------- | -------------- | ----- | ----------
**Windows**    | [GNU Arm Embedded Toolchain](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads) | [GNU Win32 Make](http://gnuwin32.sourceforge.net/packages/make.htm) | [precompiled binaries](http://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/win32-mingw32/)
**macOS**      | [GNU Arm Embedded Toolchain](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads) | [Xcode](https://itunes.apple.com/us/app/xcode/id497799835) | [Homebrew](https://brew.sh/) `brew install dfu-util`
**Debian/Ubuntu** | `sudo apt-get install gcc-arm-none-eabi libnewlib-arm-none-eabi` | `sudo apt-get install make` | `sudo apt-get install dfu-util`
**Fedora** | `sudo dnf install arm-none-eabi-newlib arm-none-eabi-gcc-cs-c++` | `sudo dnf install make` | `sudo dnf install dfu-util`
**Arch** | `sudo pacman -S arm-none-eabi-gcc arm-none-eabi-newlib` | `sudo pacman -S make` | `sudo pacman -S dfu-util`

Additionally, you may want to install `git`, or at least have a way to checkout git repositories.

To compile a sample, simply change into its directory and type `make`.  This will produce a variety of files, including a `.dfu` file that you can upload with `dfu-util --download`

## Creating a new Project

To create a new project, simply create a new directory in the `quickstart` directory and copy over the `Makefile` from an existing project.  Then start adding .c files.

To see a simple example of this, look at [bare-minimum](https://github.com/im-tomu/tomu-quickstart/tree/master/bare-minimum), which does nothing but compile and run forever.
