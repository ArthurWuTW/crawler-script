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

    ip = "https://plantmonitor.mooo.com"
    data = "/updatePiCpuTemperature/"+str(temp).replace(".", "%2E")+"%20%27C"

    try:
        r = requests.get(ip+data)
        #r = requests.get(ip+"/writeLogMessage/CPU/%5BPI%5D%20CPU%20Temp%20Updated/LOG")
    except:
        pass
    
    break
    #time.sleep(60)
