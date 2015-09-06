__author__ = 'bdeutsch'

import re
import numpy as np
import pandas as pd


# Make a list of all card IDs and create a dataframe
def get_ids(filename):
    # Create an empty list of IDs
    idlist = []
    with open(filename) as f:
        # For each line
        for line in f:
            # Find the entity ids
            m = re.search('[\[ ]id=(\d+) ', line)
            # if one is found
            if m:
                # Check that we haven't found it yet, convert to an integer
                id = int(m.group(1))
                # Add it to the list
                if id not in idlist:
                    idlist.append(id)
    # Sort the ids
    idlist.sort()
    # Convert to dataframe
    df = pd.DataFrame(index=idlist)
    # Rename the index
    df.index.name = "Entity ID"
    # Create an empty column for names
    df["Name"] = np.nan
    df["CardId"] = np.nan
    df["Player"] = np.nan

    #print d
    return df



def import_data(filename, df):
    with open(filename) as f:
        updates = []
        for line in f:
            # Find lists of the innermost nested brackets
            m = re.findall(r"\[([^\[]+?)]", line)
            # If it's not just the command designation bracket ("zone", e.g.)
            if len(m)>1:
                # for each set of bracket contents
                for item in m[1:]:
                    # add to the list of updates
                    updates.append(item)
        for item in updates:
            # find the id
            m = re.search("id=(\d+)", item)
            if m:
                # Assign ID variable
                id = int(m.group(1))

                # find name and assign
                n = re.search("name=(.+?) \w+?=", item)
                if n:
                    name = n.group(1)
                    df.ix[id, "Name"] = name

                # find cardId and assign
                n = re.search("cardId=(\w.+?) ", item)
                if n:
                    cardId = n.group(1)
                    df.ix[id, "CardId"] = cardId

                # find player
                n = re.search("player=(\d)", item)
                if n:
                    player = n.group(1)
                    df.ix[id, "Player"] = player
            # update the dataframe for each update
    return df

# get rid of the "zone" and "power" markers.
# collect the entries into a list

# Call function
df = import_data("test_game", get_ids("test_game"))

pd.set_option('display.max_rows', 200)
print df
#  get_cards('test_game')