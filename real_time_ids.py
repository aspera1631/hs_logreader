## Reads the log file in real time and fills the dataframe with card info

__author__ = 'bdeutsch'

import time
import numpy as np
import pandas as pd
import re


# Follow the log and output lines
def follow(filename):
    filename.seek(0, 2)
    while True:
        line = filename.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# get the id
def get_id(line):
    # Find the entity ids
    m = re.search('[\[ ]id=(\d+) ', line)
    # if one is found
    if m:
        # convert to an integer
        id = int(m.group(1))
        return id


# If there's an id in the line, add it to the list if we haven't seen it already.
# Also, check for nested brackets. If we find them, create a stack of updates.
# For each update, run individual functions to find id, name, cardid, player
# For each value, update the df

filename = "/Users/bdeutsch/Library/Logs/Unity/Player.log"

logfile = open(filename, "r")
loglines = follow(logfile)
for line in loglines:
    id = get_id(line)
    if line[0] != '(' and id:
        print id