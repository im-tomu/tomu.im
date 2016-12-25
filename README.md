---
layout: default
title: A tiny ARM microprocessor which fits in your USB port.
---

# [Tomu, I'm](tomu.im)

[I'm Tomu](tomu.im) a tiny ARM microprocessor which fits in your USB port. 
I have two buttons and two LEDs!



{% raw %}
<a href="https://j.mp/tomu-33c3/">
<iframe src="https://docs.google.com/presentation/d/1XT5oWsYzFATEelErZnxvSWVnVSFUm2gO2fWi31SKbWI/embed?start=true&loop=true&delayms=3000" frameborder="0" width="1440" height="839" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</a>
{% endraw %}


# Tomu Hardware

Built out of a 3d printed part + 2 layer "thin" PCB (0.4mm, 0.6mm or 0.8mm
thick).

Both boards have;

 * 6mil traces
 * 6mil clearance
 * 0.3mm drill / 0.6mm vias

All Tomu boards have;

 * At least 2 different color LEDs
 * At least 2 touch buttons

## Tomu

 * [GitHub Repository](https://github.com/im-tomu/tomu-hardware)

### Specs

 * Uses a Silicon Labs Happy Gecko EFM32HG309
  - 25MHz ARM Cortex-M0+
  - 8kb^ RAM
  - 64kb^ Flash
  - USB 2.0

 * Literally 12 Parts
 * BOM ~$10 USD from Digikey (in individual quantities)

### Gerbers

 * [v0.2](https://github.com/im-tomu/tomu-hardware/tree/master/releases/v0.2/gerbers)


## Tomu+

 * [GitHub Repository](https://github.com/im-tomu/tomuplus-hardware)
 * Hardware still under development
 
### Specs

 * Uses a Freescale Semiconductor / NXP Kinetis KL27 (MKL27Z256VFM4)
  - 48MHz ARM Cortex-M0+
  - 32kb^ RAM
  - 256kb^ Flash
  - USB 2.0

 * Optional Atmel ATECC508A Hardware Crypto Chip

 * BOM ~$15 USD from Digikey (in individual quantities)


# Tomu Software

Tomu software is currently under development and needs your help!

# Contact

 * [Announcement mailing list](https://groups.google.com/forum/#!forum/tomu-announce/join) - Low traffic list for announcements.
 * [Discussion mailing list](https://groups.google.com/forum/#!forum/tomu-discuss/join) - List for discussing development / new features / etc.
 * [IRC Channel - irc://irc.freenode.net/#tomu](https://webchat.freenode.net/?channels=#tomu) - IRC channel for discussing anything related to the project.


