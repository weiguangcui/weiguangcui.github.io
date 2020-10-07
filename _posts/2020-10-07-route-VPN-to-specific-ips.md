---
layout: post
title: Set VPN for connecting to only specific IP address
tags: [VPN] [Linux]
---

# The problem

I have multiple VPNs for connecting to different servers. Each only for a specific server. By default, I can only to connect to one VPN at the same time and everything has to go through that VPN. Some VPNs have very low speed with restrictions, for example, can not access to internet besides the server IP.
It was very painful to switch between different VPNs and suffer these restrictions.

# Solver

It turns out to be very easy for solving this problem -- only route your VPN to specific IP addresses.

# Practical steps: using Linux NetworkManager as an example

  1. go to your VPN settings and find the setting for `IPv4`
  2. Inside that setting options, you will find `Routes`, which should be set to `Automatic` by default. Close `Automatic` will allow you add `Address`, `Netmask`, `Gateway`, and `Metric`.
  
  `Address` will be the server IP address or any address that you want to connect with that VPN.
  
  `Netmask` needs to be set to `255.255.255.255`, which means only route to that specific IP `Address`.
  
  `Gateway` is required, but different to each VPN. See step 3 for how to find your `Gateway`.
  
  `Metric` can be left blank. Otherwise, you may want to try 1.
  
  3. Find `Gateway`.
    Connect your VPN *without* previous settings. Open your terminal and type `ifconfig`. You need to look for the lines started with `ppp0:`. For example:
    ```
    ppp0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1400
        inet I.P.Address.  netmask 255.255.255.255  destination Some.I.P.Address
        ppp  txqueuelen 3  (Point-to-Point Protocol)
        RX packets 146  bytes 43076 (43.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 368  bytes 87491 (87.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ```
    The IP address following `destination` is for your `Gateway`.
    
  4. After you fill up the `Gateway`, tick the box for `Use this connection only for resources on its network`, and save the settings by click `Apply`.
  
Enjoy the free internet anywhere!