import re, subprocess
import requests
import time

def check_CPU_temp():
    temp = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)
        try:
            temp = float(m.group())
        except:
            pass
    return temp, msg

while True:
    temp, msg = check_CPU_temp()
    print(temp)

    ip = "http://10.1.1.16:8000"
    data = "/cpuTemperature/"+str(temp)

    try:
        r = requests.get(ip+data)
        r = requests.get(ip+"/writeLogMessage/CPU/%5BLOG%5D%20CPU%20Data%20Updated")
    except:
        pass
    break
    #time.sleep(60)
