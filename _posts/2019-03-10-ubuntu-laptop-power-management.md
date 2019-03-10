---
layout: post
title: How to set up the power management for Dell XPS 13 - 3980
tags: [Linux, Ubuntu, power management]
---

Most of these content are copying from [Ubuntu Community Help Wiki](https://help.ubuntu.com/community/PowerManagement/ReducedPower)

Steps for setting pm-utils:
```
sudo apt install pm-utils
```

In order to enter low power mode, run this:
```
sudo pm-powersave true
```

In order to leave low power mode, run this:
```
sudo pm-powersave false
```

To get the power saving mode automatically run (detecting AC power),  create `/etc/udev/rules.d/99-powersave.rules`, and put the following content into this file:
```
SUBSYSTEM=="power_supply", ATTR{online}=="0", RUN+="/usr/sbin/pm-powersave true"
SUBSYSTEM=="power_supply", ATTR{online}=="1", RUN+="/usr/sbin/pm-powersave false"
```
You should be able to see output changes with `tail -f /var/log/pm-powersave.log`

-----

systemd sleep:

You can use pm-utils to manage the system for suspend/sleep/hibernate, see [the doc in archlinux](https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Pm-utils.html) for details.

Ubuntu uses systemd to manage suspend/sleep/hibernate. If `cat /sys/power/mem_sleep` return
```
[s2idle] deep
```
This confirms that the default suspend mode is s2idle (since it is highlighted with brackets).

To permanently fix sleep to `deep`, you should `sudo -H gedit /etc/default/grub`. Replace the line
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```
with
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash mem_sleep_default=deep"
```
Regenerate your grub configuration by run `sudo update-grub`.

However, I failed to make the XPS to hibernate... Keep tracking the problem and will update the fix later.
