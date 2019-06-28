#!/usr/bin/env python2.7

from os import path
import sys
import subprocess
import time

if len(sys.argv) < 2:
    exit("No file name provided: Please add a file name to read from.")

file_name = sys.argv[1]

if path.exists(file_name):
    print("Executing " + file_name)
    f = open(file_name, "r")
    for line in f:
        subprocess.call(line)
    f.close()
else:
    print("Please create a " + file_name + " file!") 