---
layout: post
title: Open external links in PDF files through evince in Linux!
tags: [Linux, evince, PDF]
---

Using Beamer to create the link:
```LaTeX
\href{run:/you/dir/movie.avi}{\includegraphics[width=\textwidth]{/your/image/im.png}}
```
Generated file may have the problem to open the link in evince (in my case: ubuntu 18.04):
```
Unable to open external link.
Failed to execute child process “mpv” (Permission denied)".
```
It is the problem of the `AppArmor`.
Edit `sudo vi /etc/apparmor.d/usr.bin.evince` by adding these lines:
```
# for loading movie -- weiguang
/usr/bin/mpv ixr,
```
And reboot. It works for me. :)
