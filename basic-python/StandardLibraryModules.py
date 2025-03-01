# standard library of python has many useful modules
# 1. System & OS => sys, os, shutil, subprocess, platform
# 2. Math & Random => math, random, statistics, decimal, fractions
# 3. Date & Time => datetime, time, calendar
# 4. File Handling => os, shutil, pathlib, csv, json, pickle
# 5. Networking & Internet => requests, socket, urllib, http
# 6. Data Compression => zipfile, gzip, tarfile
# 7. Multithreading & Multiprocessing => threading, multiprocessing
# 8. Regular Expressions => re
# 9. Data structures => collections, heapq, queue
# 10. Cryptography and Security => hashlib, hmac, secrets
# 11. Testing & Debugging => unittest, logging, traceback

# Some Examples
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200 (if successful)

import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")

import sys
print(sys.version)  # Python version
print(sys.platform)  # OS platform (e.g., 'win32', 'linux')

import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Random selection
