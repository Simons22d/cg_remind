# from flask import Flask
# from flask_cors import CORS
import datetime
# import random
import time
import requests

# app = Flask()
# cors = CORS(app)
# app.config["SECRET_KEY"] = random.getrandbits(512)


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
        time.sleep(60*30)
        requests.post("http://localhost:9000/send/email/reminder")





# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(app, 10000, debug=True)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
