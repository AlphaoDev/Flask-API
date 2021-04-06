# -*- coding: utf-8 -*-

import os
import platform
from pathlib import Path
from flask import Flask, render_template, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

# Declare Flask application
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# API route
@app.route('/api/server/',methods = ['GET'])
def server():
     # Open stats file
     with open("/data/stats","r") as file:
         lines = file.readlines()
         count = 0
         for line in lines:
             if count == 0:
                 os_infos = line.strip()
             elif count == 1:
                 cpu_infos = line.strip()
             elif count == 2:
                 ram_infos = line.strip()
             elif count == 3:
                 disk_infos = line.strip()
             count += 1
             
     # Declare json dictionary
     infos = {
        'OS': os_infos,
        'CPU': cpu_infos,
        'RAM': ram_infos,
        'DISK': disk_infos
     }
     return jsonify(infos)

if __name__ == "__main__":
     # Add job to refresh stats on API
     cron = BackgroundScheduler(daemon = True)
     cron.add_job(server,'cron',second = '*')
     cron.start()
     
     # Run Flask application
     app.run(port = 5000)
