---
layout: post
title: miscellaneous issues with ubuntu 20.04
tags: [latex]
---

# Blue tooth not working properly
sudo nano /var/lib/bluetooth/xx\:xx\:xx\:xx\:xx\:xx/yy\:yy\:yy\:yy\:yy\:yy/info

where xx:xx.... is pc bluetooth address and yy:yy... is the mouse bluetooth address.

In the file, I added the section at the end:

[ConnectionParameters]
MinInterval=6
MaxInterval=7
Latency=0
Timeout=216
You may also need to reconnect the mouse sudo service bluetooth restart
not for my anywhere2...

# Uninstall snap

Refer to this link: [https://www.kevin-custer.com/blog/disabling-snaps-in-ubuntu-20-04/](https://www.kevin-custer.com/blog/disabling-snaps-in-ubuntu-20-04/)
Simple commands:
snap list
sudo snap remove snap-store #all your packages one-by-one
sudo umount /snap/core/xxxx
sudo apt purge snapd
rm -rf ~/snap
sudo rm -rf /snap
sudo rm -rf /var/snap
sudo rm -rf /var/lib/snapd

# zoom fontsize is too small for high-res screen

change the `autoScale` in `~/.config/zoomus.conf` to `true`, then restart zoom.
