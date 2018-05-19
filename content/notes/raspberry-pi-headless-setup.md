+++
title = 'Raspberry Pi Headless Setup'
date = 2018-05-12
draft = false
tags = ["raspberry-pi"]
description = "Perform the following steps on a newly flashed SD card so that it has SSH enabled and connects to a WiFi network on the first boot."
+++
Perform the following steps on a newly flashed SD card so that it has SSH enabled and connects to a WiFi network on the first boot.

### Enable SSH

In the `boot` partition of the SD card, create an empty file named `ssh`.

### Configure WiFi

In the `boot` partition of the SD card, create a file named `wpa_supplicant.conf` using the content below. When the Raspberry Pi boots up the first time, it will copy this file to `/etc/wpa_supplicant/wpa_supplicant.conf` and automatically join the configured network.

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="Your Wifi network name"
    psk="Your WiFi password"
    key_mgmt=WPA-PSK
}
```
