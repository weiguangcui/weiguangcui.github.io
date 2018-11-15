---
layout: post
title: Kill series of processes in Linux!
tags: [Linux, evince, PDF]
---

Command to run in terminal:

`
ps -ef | grep "Your job name" | awk '{print $2}' | xargs kill
`
