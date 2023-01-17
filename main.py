import psutil
import shutil
from requests import get
import schedule
import time
import telegram as tg


def get_sys_info():
    ip = get('https://api.ipify.org').content.decode('utf8')
    cpu_used = psutil.cpu_percent(interval=1)

    mem_stat = psutil.virtual_memory().percent
    mem_total = psutil.virtual_memory().total / (2**30)
    mem_avi = psutil.virtual_memory().available / (2**30)
    mem_used = psutil.virtual_memory().used / (2**30)

    path = "/"
    disk_stat = shutil.disk_usage(path)
    disk_total = disk_stat.total / (2**30)
    disk_free = disk_stat.free / (2**30)
    disk_used = disk_stat.used / (2**30)

    msg = f'''```
[{ip}]
CPU Used:    {cpu_used}%
Memory Free: {mem_avi:.2f} / {mem_total:.2f} GB
Disk Free:   {disk_free:.2f} / {disk_total:.2f} GB
```'''

    return msg


def job():
    msg = get_sys_info()
    tg.send_md(msg)


if __name__ == '__main__':
    job()
    schedule.every().hour.at(":30").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
