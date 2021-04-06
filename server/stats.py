# -*- coding: utf-8 -*-

import os
import platform
import psutil

# Check usage of CPU, RAM and DISK
cpu = psutil.cpu_percent(interval=4)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/')

# File where stats are been saved
stats_file = '/opt/docker/app_python/data/stats'
with open(stats_file, 'w') as file:
    file.write(os.name + "-"  + platform.system() + "-"  + platform.release() +$
    file.write(str(cpu) + "\n")
    file.write(str(ram)  + "\n")
    file.write(str(round(disk.free / (2**30),1)) + "\n")
