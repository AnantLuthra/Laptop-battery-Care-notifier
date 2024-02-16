"""
Author - Anant Luthra
Date - 8/2/22
Purpose - To make a laptop battery care notifier
"""
"""
Basic idea of the system
In this we will use psutil module to get info about battery
that it is plugged in or what is the percentage of the battery
according to that our program will respond and tell use through
voice to plug in or plugg out your laptop pc.
"""

from psutil import sensors_battery
from time import sleep
from plyer import notification
import os

"""
Sample...

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)
    
print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
charge = 93%, time left = 4:37:08
"""

PATH = fr"E:\Python\Python projects\Laptop Battery care"

def notify_user(case):
    """
    This function sends notification in following battery level condition: 
    - Lower limit reached
    - Max limit reached
    """

    os.chdir(PATH)
    path = os.getcwd()
    title = "Battery low!" if case == "min" else "Battery is charged enough!"
    message = "Please plug in the charger as your battery is below 35%, Battery health advice ⚡" if case == "min" else "Please remove your  laptop's charger as your battery charged enough around 85%, Battery health advice ⚡"

    notification.notify(
                title=title,
                message=message,
                app_icon=fr"{path}\assets\{case}.ico",
                timeout=10)

def check():

    while True:

        # Checking battery status
        battery = sensors_battery()
        percent = battery.percent
        pluged = battery.power_plugged

        if percent >= 80 and pluged:
            notify_user("max")

        if percent < 35 and not pluged:
            notify_user("min")
        
        # waiting period of 10 minutes
        sleep(60*10)     


check()
