# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:09:10 2025

@author: sam77
"""

import time
file_path = "C:/1-Python/server.log"

def tail_log_file(file_path):
    with open(file_path, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new logs to be added
                continue
            yield line.strip()  # Yield new log line

for log in tail_log_file(file_path):
    if "ERROR" in log:
        print(f"Alert: {log}")

