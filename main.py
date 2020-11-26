import datetime
import time
import requests

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


while True:
    now = datetime.datetime.now()
    start = datetime.time(8, 0, 0)
    end  = datetime.time(11, 0, 0)
    hr = int(now.strftime("%H"))
    min = int(now.strftime("%M"))
    sec = int(now.strftime("%S"))
    x = datetime.time(hr,min,sec)
    if time_in_range(start,end ,x):
        print("its time.")
        time.sleep(60)
        requests.post("http://localhost:9000/send/email/reminder")
    else:
        print("Its Not Time.")
