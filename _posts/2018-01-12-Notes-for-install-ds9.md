---
layout: post
title: Notes for install ds9 in Linux!
<!-- image: /img/hello_world.jpeg -->
tags: [Linux, ds9, astronomy softwares]
---

Dowload ds9 (source file from SAOImage version 7.6b8) : [http://ds9.si.edu/download/source/ds9.7.6b8.tar.gz](http://ds9.si.edu/download/source/ds9.7.6b8.tar.gz)

required packages:
```
sudo apt install automake autoconf python-dev libssl-dev libxslt1-dev libxml2-dev libz-dev libx11-dev
```

Commands to install:
```
unix/configure
make #(edit Makefile for other options such as prefix)
```

Possible error:
```
tcl.c: In function ‘XPARec_Tcl’:
tcl.c:974:58: error: ‘uintptr_t’ undeclared (first use in this function); did you mean ‘intptr_t’?
       if( !(chan = Tcl_MakeTcpClientChannel((ClientData)(uintptr_t)xpa_cmdfd(xpa))) ){
                                                          ^~~~~~~~~
                                                          intptr_t
tcl.c:974:58: note: each undeclared identifier is reported only once for each function it appears in
```

Solution for this error:
edit the tcl.c file by including this header (from glibc)
```
#include <stdint.h>
```

Wish you can successfully install ds9! 
