---
layout: post
title: Gadget simulation binary snapshot formats
tags: [Simulation, Gadget, snapshot]
---

This post list the data structrue of the Gadget binary snapshot.
This data structure also includes the format 2, which has a header.
For the old Gadget-2 snapshot format, please also refer to its documentation.

Here how it is saved (note that ----> and # are the comments):

-------
```
--------> header block (only in format 2)
int32 8   # (exactly 8 saved in 4 bytes)
'HEAD'    # (exactly 4 characters in captical)
int32 bs  # the data block size in bytes: 8 (two int32 number)
          #    + real data size in bytes (256 for head data) = 264
int32 8   # (exactly 8 saved in 4 bytes)
--------> header block ends

--------> Now the head data is saved the same as the old format
int32 ds  # the real data size in bytes, for head data is fixed to 256 bytes
data      # the saved real data
int32 ds  # again, the same as the ds ahead of the data
--------> Now the head data is ended

--------> header block (only in format 2)
int32 8   # (exactly 8 saved in 4 bytes)
'POS '    # (exactly 4 characters in captical, it will be filled up with black
          #    if less than 4 characters)
int32 bs  # the data block size in bytes: 8 (two int32 number)
          #    + real data size in bytes
int32 8   # (exactly 8 saved in 4 bytes)
--------> header block ends

--------> Now the position data is saved the same as the old format
int32 ds  # the real data size in bytes, for particle position data is
          #    4*3*particle number bytes
data      # the saved real data
int32 ds  # again, the same as the ds ahead of the data
--------> Now the position data is ended

# This will normally continue with data in this order (note with format 2,
  the order can be chagned and some data blocks may not show up or have
  different block names. This is depending on your simulation):

the particle velocity (header block name : 'VEL ')

the particle IDs (header block name : 'ID  ', normally saved in uint32,
some simulation will use long long type, i.e. uint64 in python)

the particle mass (header block name : 'MASS', only the particles have a
zero value in the mass table in the head)

the gas particle internal energy (header block name : 'U   ')

the gas particle density (header block name : 'RHO ')

the gas particle electron number fraction (header block name : 'NE  ')

the gas particle hydrogen number fraction (header block name : 'NH  ')

the gas particle smoothing length (header block name : 'HSML')

the gas particle star formation rate (header block name : 'SFR ')

the star/BH particle age (header block name : 'AGE ')
```

There will be more data blocks with different names, ask your simulator for more information.
