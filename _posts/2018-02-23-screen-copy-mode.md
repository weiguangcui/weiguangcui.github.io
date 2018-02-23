---
layout: post
title: GNU screen copy mode
tags: [screen]
---

Active gnu screen copy mode:
'CTRL-A ['

```
h, j, k, l move the cursor line by line or column by column.
0, ^ and $ move to the leftmost column, to the first or last non-whitespace character on the line.
H, M and L move the cursor to the leftmost column of the top, center or bottom line of the window.
+ and - positions one line up and down.
G moves to the specified absolute line (default: end of buffer).
| moves to the specified absolute column.
w, b, e move the cursor word by word.
B, E move the cursor WORD by WORD (as in vi).
C-u and C-d scroll the display up/down by the specified amount of lines while preserving the cursor position. (Default: half screen-full).
C-b and C-f scroll the display up/down a full screen.
g moves to the beginning of the buffer.
% jumps to the specified percentage of the buffer.
```
