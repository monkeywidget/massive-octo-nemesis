Hardware Notes
==============

Proposed Architecture
---------------------

- USB button pad is a monome-compatible
- USB driver etc is backed by Arduino shield
- the Arduino shield is on an Arduino
- Arduino connects to a Raspberry Pi, which is running the DB and app server

Arduinome
---------
- [http://www.hangar.org/wikis/lab/doku.php?id=start:octint Octint]
- http://sourceforge.net/projects/arduinome/
- http://arduinome.sourceforge.net
- Bonome
    - [http://julienbayle.net/works/creation/bonome-arduino-based-rgb-monome-clone/ Bonome]

Other
-----
- http://createdigitalmusic.com/2011/08/it-comes-in-colors-an-rgb-grid-controller-from-livid-rgb-grid-roundup/

Build Guides
============
- http://store.curiousinventor.com/blog/arduinome-case-now-available-build-log/
- http://jellyedwards.blogspot.com/2008_10_01_archive.html
- [http://evilpaul.typepad.com/blog/2009/03/arduinome-10h-completed.html Arduinome 10h]


Button pad shield for Arduino
=============================
- [http://www.elechouse.com/elechouse/index.php?main_page=product_info&products_id=205 RGB Monome sheild]

- previously: a guy called "unsped" made a shield: http://unsped.blogspot.com/2008/12/arduinome-shield.html
   - https://batchpcb.com/pcbs/14287
- Arduinome, Breakout - https://batchpcb.com/pcbs/14288

Getting the pad to the Server
=============================

Let's say the pad is constructed and works!

Given the server and DB run on a Raspberry Pi:

Plan A: Connecting an Arduino to a Raspberry Pi
-----------------------------------------------

The scenario is as described above.

The benefit is "the trail has been blazed" - the [http://julienbayle.net/works/creation/bonome-arduino-based-rgb-monome-clone/ Bonome]
has e=been entirely implemented already

The challenge is to connect (via USB) the Arduino and shield to the Raspberry Pi,
writing the json calls over USB

- http://blog.oscarliang.net/connect-raspberry-pi-and-arduino-usb-cable/
- http://www.doctormonk.com/2012/04/raspberry-pi-and-arduino.html
- http://www.raspberrypi.org/downloads


Plan B: Put a shield on the Raspberry Pi simulating an Arduino
--------------------------------------------------------------

Alternately: stack the Arduino shield on a Raspberry Pu for the button LEDs on that

The challenge here is to rewrite the LED button drivers to work 
through the existing Arduino shield to get to the RPi

- http://www.cooking-hacks.com/documentation/tutorials/raspberry-pi-to-arduino-shields-connection-bridge



 