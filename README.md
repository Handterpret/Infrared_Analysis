# Infrared_Analysis

This repository contains code and documentation on how to collect data from infrared sensor around the wrist.

## Hardware needed

In this project I will use a clone of Arduino nano with ATMEGA328P and CH340 chip.


We will also use [infrared photodiodes](https://fr.rs-online.com/web/p/photodiodes/6547921/) and [infrared leds](https://fr.rs-online.com/web/p/led-ir/8768767/)
## prerequisite

If you are using CH340 chip (clone of arduino Nano) please download firmware to detect device in Arduino firmware:

Download and install firmware from : 
```
https://drive.google.com/drive/folders/1xc8l1gazUueeBtoYJpTShC4DcPErrreh
```
or other depending on the brand of your nano.

It should now appear fine in [Arduino IDE](https://www.arduino.cc/en/Main/OldSoftwareReleases) under tools => port

## Test realised

To check if your board/leds/photodiodes are ok, please see 
```
unit_test/Blink
```
wiring is as follow : 

- Led on GRND and D2 (cathode)

- Photodiode on 3.3V (cathode) and A0

Excpected output:

- Open serial monitor and you should see a low value then a high value repeatedly
