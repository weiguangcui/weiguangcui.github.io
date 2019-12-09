---
layout: post
title: undefined symbol error for compiling with cython modules
tags: [python, cython]
---

A common error for installed packages (such as [yt](https://yt-project.org/), [caesar](https://bitbucket.org/desika/caesar/)) which use cython to build parts of models:

`python
ImportError: /...**.cpython-36m-x86_64-linux-gnu.so: undefined symbol: __intel_sse2_strchr
`

The solution is installing your package with specified compiler -- icc:

`python
LDSHARED="icc -shared" CC=icc python3 setup.py install --user
`