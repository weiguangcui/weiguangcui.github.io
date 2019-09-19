---
layout: post
title: How to set up the power management for Dell XPS 13 - 3980
tags: [Linux, Ubuntu, power management]
---

* Use the Dell OEM Ubuntu ios file to install the ubuntu 18.04LTE.*

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

--------
*Newly update on 19/09/2019*

After several update of the Ubuntu 18.04 system (18.04.3 LTS now), I tried `sudo systemctl hibernate` which works now.

If you have a problem of ```Failed to hibernate system via logind: Sleep verb not supported```, try to disable fastboot in the BIOS and do not use UEFI for disk.
You will also need to increase the swapfile size larger than your laptop memory with these steps:

1. Turn off all swap processes
```
sudo swapoff -a
```

2. Resize the swap
```
sudo dd if=/dev/zero of=/swapfile bs=1G count=8
```

if = input file
of = output file
bs = block size
count = multiplier of blocks

3. Make the file usable as swap
```
sudo mkswap /swapfile
```

4. Activate the swap file
```
sudo swapon /swapfile
```

5. Check the amount of swap available
```
grep SwapTotal /proc/meminfo 
```

6. Try to hibernate your laptop again
```
sudo systemctl hibernate
```

-----
Install tlp and/or powertop to save your buttery cost.

TLP usage: [https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html](https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html)

powertop usage: [https://www.tecmint.com/powertop-monitors-linux-laptop-battery-usage/](https://www.tecmint.com/powertop-monitors-linux-laptop-battery-usage/)

-----
To avoid the wifi random dropping problem:

Try disabling wifi power management by opening ``/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf` and changing
```
wifi.powersave = 3
```
to
```
wifi.powersave = 2
```
Do not set it to 0, which is the default value. From `nm-setting-wireless.h`:
```
/**
 * NMSettingWirelessPowersave:
 * @NM_SETTING_WIRELESS_POWERSAVE_DEFAULT: use the default value
 * @NM_SETTING_WIRELESS_POWERSAVE_IGNORE: don't touch existing setting
 * @NM_SETTING_WIRELESS_POWERSAVE_DISABLE: disable powersave
 * @NM_SETTING_WIRELESS_POWERSAVE_ENABLE: enable powersave
 *
 * These flags indicate whether wireless powersave must be enabled.
 **/
 
typedef enum {
    NM_SETTING_WIRELESS_POWERSAVE_DEFAULT       = 0,
    NM_SETTING_WIRELESS_POWERSAVE_IGNORE        = 1,
    NM_SETTING_WIRELESS_POWERSAVE_DISABLE       = 2,
    NM_SETTING_WIRELESS_POWERSAVE_ENABLE        = 3,
    _NM_SETTING_WIRELESS_POWERSAVE_NUM, /*< skip >*/
    NM_SETTING_WIRELESS_POWERSAVE_LAST          =  _NM_SETTING_WIRELESS_POWERSAVE_NUM - 1, /*< skip >*/
} NMSettingWirelessPowersave;
```

Original post 2019-03-10, updated 2019-07-15, updated again in 2019-09-19