---
layout: post
title: Problems with wemeet in Linux
gh-username: weiguangcui
gh-repo: weiguangcui/weiguangcui.github.io
gh-badge: [star, fork, follow]
tags: [wemeet, Linux]
comments: false
comments_id: 7
---

After install wemeet in Linux, Ubuntu 24.04 especially, I met some problems:

"检测到窗口系统采用wayland协议，腾讯会议暂不兼容，程序即将退出！"

For this problem, you need to set these environment variables in `/opt/wemeet/wemeetapp.sh`:
```
export XDG_SESSION_TYPE=x11
export EGL_PLATFORM=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAY
unset WAYLAND_DISPLAYCOPY
```
before this line:
```
if [ "$XDG_SESSION_TYPE" = "wayland" ];then
```
No need to do other things. 

Alternativly you can not use the `wayland` environment by editing this file: `/etc/gdm3/custom.conf` like this:
```
WaylandEnable=false
```
This may cause some other problems of the system which requires `wayland` environment.
