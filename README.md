# SkyTrain Wifi Tracker

This is just a silly idea I had. Vancouver's SkyTrains sometimes have working
Wifi, but they often don't. I've often wondered what the actual stats are
regarding Wifi on the SkyTrain (mostly which lines/train generations have the
highest chance of having functional Wifi), so I created this quick script to
track these stats as I commute to and from school.

## Findings

Now that my semester is over, and since I've manually checked (I believe) well
over half of the currently active trains, I have decided that now is the time to
share my findings and quit updating the data.

I have converted all the data into the JSON format and sorted the trains by
their ID number. You can see the data for yourself in `data.json`

Overall, I checked 309 of the (estimated) 500 trains. Here are the specifics of
how they were divided between train generation and line:

| Generation        | Count |
| ----------------- | ----- |
| MKI (1980s)       | 122   |
| MKII (2000s)      | 106   |
| MKIII (2010s)     | 81    |
| EMU (Canada Line) | 0     |

| Line            | Count |
| --------------- | ----- |
| Expo Line       | 247   |
| Millennium Line | 62    |
| Canada Line     | 0     |

---

Across all lines and generations (that I checked) there was a 21% chance that
any given train I boarded would have working Wifi. Here is how that number is
divided between train generation and line:

| Generation        | Wifi Uptime       |
| ----------------- | ----------------- |
| MKI (1980s)       | 0%                |
| MKII (2000s)      | 61%               |
| MKIII (2010s)     | 0%                |
| EMU (Canada Line) | 0% (Never tested) |

| Line            | Wifi Uptime       |
| --------------- | ----------------- |
| Expo Line       | 15%               |
| Millennium Line | 44%               |
| Canada Line     | 0% (Never tested) |

These numbers match up pretty well with my estimates from before I started this
experiment. Shockingly, only the MKII trains _ever_ had working Wifi. The MKI
trains, being old and soon to be replaced, are understandable. However I can't
begin to guess why the newest MKIII trains never had Wifi. I supposed it will
always be a mystery 😅.

## Usage

Just clone the repository and run main.py. I am using Python 3.10 so that I can
use [Pythonista](https://omz-software.com/pythonista/) on my phone to do my
tracking, but anything newer should work as well. I did use type annotations, so
older Python version likely won't work.

Tracking data is kept in a local file (`data.pickle`) so my data won't be shared
in real time. I will do my best to periodically push my data to this repo as a
backup and so that anyone else who actually uses this dumb script doesn't have
to start from scratch.

If you plan to use this project on any platform other than iOS or macOS, you'll
need to add your system's function to clear the screen to the `clear()` function
at the top of the file.
