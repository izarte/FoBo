#!/bin/bash

# Start pin 11
echo 50 > /sys/class/gpio/export
sleep 1s
echo out > /sys/class/gpio/gpio50/direction
echo 1 > /sys/class/gpio/gpio50/value

# Start pin 12
echo 79 > /sys/class/gpio/export
sleep 1s
echo out > /sys/class/gpio/gpio79/direction
echo 1 > /sys/class/gpio/gpio79/value

# Start pin 15
echo 194 > /sys/class/gpio/export
sleep 1s
echo out > /sys/class/gpio/gpio194/direction
echo 1 > /sys/class/gpio/gpio194/value

# Start pin 16
echo 232 > /sys/class/gpio/export
sleep 1s
echo out > /sys/class/gpio/gpio232/direction
echo 1 > /sys/class/gpio/gpio232/value

