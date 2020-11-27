import datetime
import time
import requests


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def is_week_day(this_day):
    return True if  datetime.datetime.isoweekday(this_day) <= 5 else False


while True:
    now = datetime.datetime.now()
    start = datetime.time(8, 0, 0)
    end = datetime.time(16, 0, 0)
    hr = int(now.strftime("%H"))
    min = int(now.strftime("%M"))
    sec = int(now.strftime("%S"))
    x = datetime.time(hr, min, sec)
    print("•••••••••••••")
    if time_in_range(start, end, x) and is_week_day(now):
        print("its time.")
        requests.post("http://192.168.12.200:9000/send/email/reminder")
        time.sleep(60 * 30)
    else:
        print("Its Not Time.")

