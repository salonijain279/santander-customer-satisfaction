import sys
import os
import subprocess

pythons = [
    "/Users/dagur/opt/anaconda3/bin/python",
    "/usr/local/bin/python3.9",
    "/Library/Frameworks/Python.framework/Versions/3.11/bin/python3",
    "/usr/bin/python3"
]

for py in pythons:
    print(f"Checking {py}:")
    try:
        res = subprocess.check_output([py, "-c", "import lightgbm; print(lightgbm.__version__)"], stderr=subprocess.STDOUT)
        print(f"  Found lightgbm: {res.decode().strip()}")
    except Exception as e:
        print(f"  NOT FOUND or Error: {e}")
