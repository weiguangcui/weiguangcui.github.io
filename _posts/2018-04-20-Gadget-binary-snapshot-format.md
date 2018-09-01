---
layout: post
title: Gadget simulation binary snapshot formats
tags: [Simulation, Gadget, snapshot]
---

This post<a href="#note1" id="note1ref"><sup>1</sup></a> lists the data structure of the Gadget binary snapshot.
This data structure also includes the format 2, which has a header.
For the old Gadget-2 snapshot format, please also refer to its documentation.

Please note that there are 6 types of particles, numbered from 0 to 5.
They are gas[0]，dark matter[1]，bulge[2]，disk[3]，star[4], bndry[5] in the Gadget2 snapshots.
But in hydrodynamic simulations, the bndray[5] particles are normally used to save the Black holes[5] particles.
Bulge[2] and disk[3] particles are normally empty in cosmology simulations, and they are normally replaced by low resolution DM particles in zoom-in simulations. **Please always ask your simulation owner for the details of particles types and date (block) formats!**

Here how it is saved (note that ----> and # are the comments):

-------
```
--------> header block (only in format 2)
int32 8   # (exactly 8 saved in 4 bytes)
'HEAD'    # (exactly 4 characters in capital)
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
'POS '    # (exactly 4 characters in capital, it will be filled up with black
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
  the order can be changed and some data blocks may not show up or have
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

<a id="note1" href="#note1ref" font size="3"><sup>1</sup></a>This post is originally wrote on 20 Apr. 2018 and updated later in 31 Aug. 2018.
