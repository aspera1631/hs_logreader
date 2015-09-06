__author__ = 'bdeutsch'

import re
import numpy as np
import pandas as pd

# List cards drawn by me and played by opponent
def get_cards(filename):
    # Open the file
    with open(filename) as f:
        mycards = []
        oppcards = []

        for line in f:
            # Generate my revealed card list
            m = re.search('name=(.+)id.+to FRIENDLY HAND', line)
            if m:
                mycards.append(m.group(1))

            n = re.search('name=(.+)id.+to OPPOSING PLAY(?! \(Hero)', line)
            if n:
                oppcards.append(n.group(1))

    for item in mycards:
        print item
    print '\n'
    for item in oppcards:
        print item

# make a list of card IDs and names
def get_ids():
    # Create an empty list of IDs
    idlist = []
    with open('test_game') as f:
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
    d = pd.DataFrame(index=idlist)
    # Rename the index
    d.index.name = "Entity ID"
    # Create an empty column for names
    d["Name"] = np.nan

    #print d
    return d


# make a list of card names only if followed by id
def get_names():
    with open('test_game') as f:
        for line in f:
            # Find the entity ids
            m = re.search('[\[ ]name=([\w ]+?) id=', line)
            if m:
                print m.group(1)

def get_ids_names(df):
    with open('test_game') as f:
        namedict = {}
        for line in f:
            # Find combinations of entities and names
            m = re.search('[\[ ]name=([\w ]+?) id=(\d+)', line)
            if m:
                ent_id = int(m.group(2))
                name = m.group(1)
                df.ix[ent_id, 'Name'] = name
                #print m.group(2), m.group(1)
    return df




idlist = []
with open('test_game') as f:
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


with open('test_game') as f:
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

# get rid of the "zone" and "power" markers.
# collect the entries into a list




# Put card IDs into a DataFrame
#df = get_ids_names(get_ids())

pd.set_option('display.max_rows', 200)
print df
#  get_cards('test_game')