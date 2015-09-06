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

# Put card IDs into a DataFrame
df = get_ids_names(get_ids())

pd.set_option('display.max_rows', 100)
print df