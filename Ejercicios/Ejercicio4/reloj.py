import datetime
import os 
import time

def reloj():
    while True:
        os.system("clear")
        tm = datetime.datetime.now()
        print("{}:{}:{}".format(tm.hour, tm.minute, tm.second))
        time.sleep(1)

