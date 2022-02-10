"""
Author - Anant Luthra
Date - 8/2/22
Purpose - To make a laptop battery care notifier
"""

import psutil

# Sample...
"""
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

battery = psutil.sensors_battery()
"""



# battery
# sbattery(percent=93, secsleft=16628, power_plugged=False)

# print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))

# charge = 93%, time left = 4:37:08
 

if __name__ == "__main__":
    ...

