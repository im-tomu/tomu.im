---
layout: default
title: A tiny ARM microprocessor which fits in your USB port.
permalink: /
---

# [Tomu, I'm](https://tomu.im)

[I'm Tomu](https://www.crowdsupply.com/sutajio-kosagi/tomu/), a tiny ARM microprocessor which fits in your USB
port. I have two buttons and two LEDs!

I'm fully open source and am buildable by hobbyists! Designed for 2-factor
authentication, usb experiments, or anything else you can think of.

I'm also available on [Crowd Supply](https://www.crowdsupply.com/sutajio-kosagi/tomu/), fully assembled and tested.

<hr><br><br>

# Getting Started!

Got a Tomu?  Great!  Here's how to get started.  First you need a case, then you need the drivers.

Because Tomu fits entirely inside your USB port, you need something to keep it from falling out.  Early Tomu prototypes were held in place using a business card folded over and wedged in the USB port, but newer releases have support for 3D printed cases.

If you have a 3D printer, [download the .stl file](https://github.com/im-tomu/tomu-hardware/tree/master/case) for the version of Tomu that you have.  The version number is printed on the bottom side with the big USB connections.  Depending on how thick your PCB is, you may need to adjust the FreeCAD file.

For software, Tomu currently uses the SiLabs serial bootloader.  One of the Crowd Supply stretch goals is a universal bootloader based on DFU.

To use the seral bootloader, Windows users will need to install Silabs-CDC_Install.zip, e.g. from [M-Pression](https://www.m-pression.com/solutions/boards/odyssey/odyssey-downloads).  Linux and macOS users do not need to use any special drivers.

1. Enter the bootloader.
  * v0.2 boards require you to connect the C pin to Vcc.
  * v0.3 boards always enter the bootloader
1. Connect a terminal.
  * TeraTerm on Windows is a good choice
  * screen works on Linux and macOS
1. Interact with the bootloader by sending one-character commands:
  * **i** -- show the bootloader version
  * **u** -- upload a new program - send the binary using XMODEM
  * **b** -- boot the current program

<hr><br><br>

# Back Us!

Tomu is [crowdfunding on Crowd Supply](https://www.crowdsupply.com/sutajio-kosagi/tomu/)!  While software is mostly easy to update, hardware is more challenging.  There are several stretch goals as part of the campaign, if we get enough support:

### DFU-compatible Bootloader

We would like a bootloader that gets out of the way and lets you run your normal application without needing to short out the **C** pin every time.  We'd also like to not require drivers, or superuser access, or have to deal with other programs thinking Tomu is a GPS or modem (unless it's behaving like one.)  These are all shortcomings that the current bootloader suffers from.

If enough people back Tomu, we will get a bootloader that supports the standard DFU protocol for updating device firmware easily.

### Injection-Molded Plastic Case

Tomu is tiny, and fits entirely inside your USB port.  USB ports have metal shields around them, so Tomu requires a case both to fit snugly inside the port and to protect the components from shorting out against the shield.

The current solution is to 3D print your own case.  However, with enough backers, we can afford to produce an injection-molded plastic case to include with every Tomu purchased.

<hr><br><br>

# U2F / FIDO Firmware

GNU Chopstx has been ported to Tomu, complete with U2F support.  That means you can use Tomu like any U2F token to add a second authentication factor when you log in.  Chrome supports U2F natively, and Firefox supports it via a flag (and will support it fully in a few months)

### Source

The U2F firmware source is located on Github in [im-tomu/chopstx/u2f](https://github.com/im-tomu/chopstx/tree/efm32/u2f).

### Building

To build the U2F firmware, ensure you have an ARM compiler installed (e.g. *sudo apt install gcc-arm-none-eabi*) as well as Python pip (e.g. *pip install --user --upgrade asn1crypto*), then run:

1. pip install --user --upgrade asn1crypto
1. git clone https://github.com/im-tomu/chopstx.git tomu-u2f
1. cd tomu-u2f/u2f
1. make

### Loading onto Tomu

The build system produces an output file *build/u2f.bin*.  Upload this file to Tomu.

* If using the serial bootloader, type **u** and send the file using XMODEM

<hr><br><br>

# Presentations

{% raw %}
<iframe style="min-height: 400px;" src="https://docs.google.com/presentation/d/1NV4QAr7nQg5OAjLGDzVBely9bvDAFhP1qIqw7IU5Wdk/embed?start=true&loop=true&delayms=3000" frameborder="0" width="100%" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
<br>
<iframe  width="560" height="315" src="https://www.youtube.com/embed/36zcE_C0K2k" frameborder="0" allowfullscreen></iframe>
{% endraw %}

<hr><br><br>

# Help us!

These are currently the top items which need to be done related to the Tomu. If
you help out, [@mithro](https://github.com/mithro) will probably send you a
Tomu device!

### Creating (or porting) a FOSS USB stack to EFM32HG

To make it easy for people to develop new applications for the Tomu, we need a
good USB stack which is compatible with the EFM32HG.

There are a couple of possible options:

 * [Porting LUFA](https://github.com/im-tomu/tomu-samples/issues/2) - Someone
   seems to have already started the EFM32 series, just not the EFM32HG.
 * [Port ChibiOS](https://github.com/im-tomu/tomu-samples/issues/11)
 * Other options?

### QEmu Emulation of the EFM32HG

 * [Code Repo](https://github.com/im-tomu/qemu)

We would like to have good emulation of the features in the EFM32HG309
processor so that people can write software for the board without having to
have the hardware.

The biggest part of this is the emulation of the USB stack.

<hr><br><br>

# Contact

 * [Announcement mailing list](https://groups.google.com/forum/#!forum/tomu-announce/join) - Low traffic list for announcements.
 * [Discussion mailing list](https://groups.google.com/forum/#!forum/tomu-discuss/join) - List for discussing development / new features / etc.
 * [IRC Channel - irc://irc.freenode.net/#tomu](https://webchat.freenode.net/?channels=#tomu) - IRC channel for discussing anything related to the project.

<hr><br><br>

# Tomu Hardware

Built out of a 3d printed part + 2 layer "thin" PCB (0.4mm, 0.6mm or 0.8mm
thick).

Boards have:

 * 6mil traces
 * 6mil clearance
 * 0.3mm drill / 0.6mm vias

All Tomu boards have:

 * At least 2 different color LEDs
 * At least 2 touch buttons

## Tomu

 * **Status**: Hardware complete, simple flashing firmware working. Needs proper
   firmware.
 * [GitHub Repository](https://github.com/im-tomu/tomu-hardware)

### Specs

 * Uses a Silicon Labs Happy Gecko EFM32HG309
   - 25MHz ARM Cortex-M0+
   - 8kb^ RAM
   - 64kb^ Flash
   - USB 2.0 FS and LS

 * Literally 12 parts

### Gerbers

 * [v0.2](https://github.com/im-tomu/tomu-hardware/tree/master/releases/v0.2/gerbers)

The important thing to note is that you need a PCB that is 0.8mm thickness **or
less**. The default thickness is normally 1.0mm and **1.0mm is too thick**.

These gerbers should be possible with the following manufacturers:

 * (Tested) [Hackvana](http://www.hackvana.com/store/)
 * (Undergoing testing) [DirtyPCB](http://dirtypcbs.com/store/pcbs)
 * (Undergoing testing) [Seeed Studio](https://www.seeedstudio.com/fusion_pcb.html)
 * (Yet to be ordered) [OHS Park - 2 Layer 2oz 0.8mm Service](http://docs.oshpark.com/services/two-layer-hhdc/)


# License

The Tomu hardware is under your choice of:

 * the "Creative Commons Attribution-ShareAlike 4.0 International License"
   (CC BY-SA 4.0) full text of this license is included in the LICENSE file
   and a copy can also be found at
   [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
 * the "TAPR Open Hardware License" full text of this license is included
   in the LICENSE file and a copy can also be found at
   [http://www.tapr.org/OHL](http://www.tapr.org/OHL)

Software for Tomu is under various licenses, please consult the license
included with the code.

![Open Source Hardware Certification AU0000001](oshw-au000001.png)
