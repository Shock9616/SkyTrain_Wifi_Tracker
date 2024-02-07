# SkyTrain Wifi Tracker

This is just a silly idea I had. Vancouver's SkyTrains sometimes have working
Wifi, but they often don't. I've often wondered what the actual stats are
regarding Wifi on the SkyTrain (mostly which lines/train generations have the
highest chance of having functional Wifi), so I created this quick script to
track these stats as I commute to and from school.

## Usage

Just clone the repository and run main.py. I am using Python 3.10 so that I can
use [Pythonista](https://omz-software.com/pythonista/) on my phone to do my
tracking, but anything newer should work as well. I did use type annotations, so
older Python version likely won't work.

Tracking data is kept in a local file (`data.pickle`) so my data won't be shared
in real time. I will do my best to periodically push my data to this repo as a
backup and so that anyone else who actually uses this dumb script doesn't have
to start from scratch.
