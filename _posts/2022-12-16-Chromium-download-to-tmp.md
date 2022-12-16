---
layout: post
title: How to allow Chromium (snap installed) to use /tmp as the download folder
gh-repo: weiguangcui/weiguangcui.github.io
gh-badge: [star, fork, follow]
tags: [Chromium]
comments: true
---

The answer is here:
[https://askubuntu.com/a/1264341](https://askubuntu.com/a/1264341)
with a copy and paste version:
```
mkdir /home/you/tmp
sudo mount --bind /tmp /home/you/tmp/
```

Just force to set Chromium's download folder to the /home/you/tmp

To make it permanent you can add this line to the /etc/fstab:
```
 # <file system> <mount point>   <type>  <options>       <dump>  <pass>
/tmp        /home/you/tmp   auto    bind    0   3

```
and rebuild the initrd with `sudo update-initramfs -u -k all`.