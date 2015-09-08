## Reads the log file and announces when a card is played or drawn

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

# Helper function to get the innermost nested strings from each log line
def get_nested(str1):
    m = re.findall(r"\[([^\[]+?)]", str1)
    if len(m)>1:
        strings = []
        for item in m[1:]:
            strings.append(item)
        return strings
    else:
        return None

# Find an item in a log string (innermost nest). If not found, return None
def get_item(item, str1):
    m = re.search("(?<!\w)" + item + "=([^\s].*?)($|\s\w+?=)", str1)
    if m:
        return m.group(1)
    else:
        return

# updates the df with new values
def update_df(update, df, cols):
    changed = False
    # look for id, card name, card ID, and player number.
    id = get_item("id", update)
    # if an ID is found
    if id:
        id = int(id)
        # if we haven't see this entity yet, add it to the dataframe
        if id not in df.index:
            df.loc[id] = np.nan

        # then for each column
        for col in cols:
            # find the value associated with that column
            val = get_item(col, update)
            # if one is found and it is a new update
            if val and df[col][id] != val:
                # update the dataframe
                df.ix[id, col] = val
                changed = True

    if changed:
        return df
    else:
        return None



## Set parameters
#logfile = "/Users/bdeutsch/Library/Logs/Unity/Player.log"
logfile = "test_game"

realtime = False

pd.set_option('display.max_rows', 200)


## Main program

# Make empty DataFrame
df = pd.DataFrame(columns=("name", "cardId", "player"))

if realtime == True:
    logfile = open(logfile, "r")
    loglines = follow(logfile)
else:
    loglines = open(logfile, "r")

for line in loglines:
    # Find any update sub-strings
    updates = get_nested(line)
    # If any updates are found
    if updates:
        # then for each update
        for update in updates:
            # look for id, card name, card ID, and player number.
            cols = ["name", "cardId", "player"]
            # create a new, updated dataframe or fill df2 with "None" if no new updates
            df2 = update_df(update, df, cols)

        # if df2 is a dataframe
        if isinstance(df2, pd.DataFrame):
            # update df and print
            df = df2
            if realtime == True:
                print df.sort()
                print "\n"
if realtime == False:
    print df.sort()
    print "\n"