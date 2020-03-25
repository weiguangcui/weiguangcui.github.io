---
layout: post
title: Kill series of processes in Linux!
tags: [Linux, Bash]
---

Command to run in terminal:

`
ps -ef | grep "Your job name" | awk '{print $2}' | xargs kill
`

If these task IDs are in a series, for example, from 160000 to 190000, you can simply kill them by

`
kill 1{60000..90000}
`

