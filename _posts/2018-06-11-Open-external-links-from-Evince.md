---
layout: post
title: Open external links (movie) in PDF files through evince in Linux!
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


Update 06/05/2019

Directly insert the movie in your PDF file with `\usepackage{multimedia}`. 
```Latex
\movie[loop,autostart]{\includegraphics[width=0.43\textwidth]{G3X-17-image.pdf}}{NewMDCLUSTER0017.mp4}
```
Place your movie `NewMDCLUSTER0017.mp4` in the same folder of your PDF file, you should be able to see the movie with [`pdfpc`](https://pdfpc.github.io/). Gnome pdf viewer `evince` works fine in normal mode, the movie has problem to show up in presentation mode [see the bug here](https://gitlab.gnome.org/GNOME/evince/issues/869)!
I have `mpv` installed.

For the missing plug-in problem:
```
(evince:24969): EvinceView-WARNING **: 11:17:11.341: Error: Your GStreamer installation is missing a plug-in. (gsturidecodebin.c(988): no_more_pads_full (): /GstPlayBin:playbin0/GstURIDecodeBin:uridecodebin0:
no suitable plugins found:
gstdecodebin2.c(4640): gst_decode_bin_expose (): /GstPlayBin:playbin0/GstURIDecodeBin:uridecodebin0/GstDecodeBin:decodebin0:
no suitable plugins found:
Missing decoder: H.264 (High Profile) (video/x-h264, stream-format=(string)avc, alignment=(string)au, level=(string)3.1, profile=(string)high, codec_data=(buffer)0164001fffe1001a6764001facd940bc17faac0440000003004000000a03c60c658001000668ebe3cb22c0, width=(int)750, height=(int)750, framerate=(fraction)20/1, pixel-aspect-ratio=(fraction)1/1)
)
```
You will need install 'sudo apt install gstreamer1.0-libav gstreamer1.0-gtk3'

