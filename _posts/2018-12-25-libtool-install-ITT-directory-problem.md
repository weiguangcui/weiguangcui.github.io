---
layout: post
title: The current directory must be set to the ITT directory problem when install libraries with libtool
tags: [Linux, libtool, install, idl]
---

Problems similar to this:
```
libtool --mode=install install -c libgrackle.la /cosma/home/FR/wcui/.local/lib/libgrackle.la
libtool: install: install -c .libs/libgrackle-3.1.so /cosma/home/FR/wcui/.local/lib/libgrackle-3.1.so

The current directory must be set to the ITT directory.
Change the default to the ITT directory and re-run this script.

make: *** [install] Error 1
```

Your $PATH contained the directory where IDL is installed. The problem is that IDL creates its own install tool which is incompatible. Solution is to remove IDL from your search $PATH and re-configure & recompile the code. (Note: you may have to wipe your build directory at start from scratch).
