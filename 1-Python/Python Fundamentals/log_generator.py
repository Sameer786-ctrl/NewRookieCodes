# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:16:04 2025

@author: sam77
"""

import time
import random

LOG_FILE="C:/1-Python/server.log"
LOG_LEVELS=["INFO","WARNING","ERROR","CRITICAL"]
MESSAGES=[
    "User logges in : user123",
    "High memory usage detected",
    "Databse connection failed:timeout",
    "File uploaded:report.pdf",
    "Server crash detected:restarting",
    "User logged out:user456"
    ]


def generate_logs():
    "continously writes logs every 2 seconds"
    with open (LOG_FILE,"a") as file: #"a" means appended mode
        while True:
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
            log_level=random.choice(LOG_LEVELS)
            message=random.choice(MESSAGES)
            log_entry=f"{timestamp} {log_level} {message}\n"
            file.write(log_entry)
            print(f"Generated Log: {log_entry.strip()}")
            time.sleep(2)
generate_logs()
            
