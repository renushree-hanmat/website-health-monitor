import requests
import time
from datetime import datetime

#sites = ["https://google.com", "https://github.com", "https://wikipedia.org"]
sites = ["https://google.com", "https://github.com", "https://wikipedia.org", "https://thissitedoesnotexist12345.com"]

while True:
    for site in sites:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            r = requests.get(site, timeout=5)
            seconds = round(r.elapsed.total_seconds(), 2)
            line = f"{now},{site},UP,{seconds}"
            #print(site, "UP", seconds, "seconds")
        except:
            line = f"{now},{site},DOWN,0"
            print("!!! ALERT: " + site + "is DOWN !!!")
        print(line)
        with open("log.csv", "a") as f:
            f.write(line + "\n")
            #print(site, "DOWN")
    time.sleep(30)