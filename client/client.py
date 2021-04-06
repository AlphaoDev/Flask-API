# -*- coding: utf-8 -*-

import requests
from tabulate import tabulate
from datetime import date, datetime

# Create or adding stats file to logs folder
def createLogs(os, cpu, ram, disk, os_infos, cpu_infos, ram_infos, disk_infos):
    today = date.today()
    now = datetime.now()
    logs_file = '/logs/{}_{}'.format(today.strftime("%d-%m-%y"),os)
    with open(logs_file,"a") as file:
        file.write("[" + now.strftime("%d/%m/%Y %H:%M:%S") \
                   + "]" + " OS : " + str(os) \
                   + " | CPU : " + str(cpu) \
                   + " | RAM : " + str(ram) \
                   + " | DISK : " + str(disk) \
                   + " | " + os_infos + " " + cpu_infos + " " + ram_infos + " " + disk_infos + "\n")

# Check API and gives informations if there are problems
def checkAPI(url):

    # Warning and critical values
    warning = 70
    critical = 90

    # Declare empty infos
    os_infos = ""
    cpu_infos = ""
    ram_infos = ""
    disk_infos = ""

    # Request API and create a json object
    r = requests.get(url)
    json_data = r.json()

    # Check OS version
    os = json_data["OS"]

    # Check usage of CPU, RAM and DISK
    cpu = float(json_data["CPU"])
    ram = float(json_data["RAM"])
    disk = float(json_data["DISK"])

    if cpu > warning and cpu < critical :
        cpu_infos = "WARNING : The CPU is higher than 70%."
    elif cpu > critical :
        cpu_infos = "CRITICAL : The CPU is higher than 90%."

    if ram > warning and ram < critical :
        ram_infos = "WARNING : The RAM is higher than 70%."
    elif ram > critical :
        ram_infos = "CRITICAL : The RAM is higher than 90%."

    if disk > warning and disk < critical :
        disk_infos = "WARNING : The DISK is higher than 70%."
    elif disk > critical :
        disk_infos = "CRITICAL : The DISK is higher than 90%."

    # Print table (not required)
    #print(f"\nInformations about {url} :\n")
    #print(tabulate([['OS Version', os, os_infos],
    #                ['CPU usage', cpu, cpu_infos],
    #                ['RAM usage', ram, ram_infos],
    #                ['DISK usage', disk, disk_infos]
    #                ],
    #               headers=['Type', 'Value','Information'])+"\n")

    # Call createLogs function
    createLogs(os, cpu, ram, disk, os_infos, cpu_infos, ram_infos, disk_infos)

if __name__ == "__main__":
    # Launch checkAPI function
    checkAPI("http://192.168.1.19:5000/api/server/")
