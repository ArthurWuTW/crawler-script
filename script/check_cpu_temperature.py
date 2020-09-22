import re, subprocess

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

temp, msg = check_CPU_temp()

print(temp)
