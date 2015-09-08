__author__ = 'bdeutsch'

import re


def get_item(item, str1):
    m = re.search("(?<!\w)" + item + "=(.+?)($| \w+?=)", str1)
    if m:
        return m.group(1)
    else:
        return


item = "name"
str1 = "name=Jaina Proudmoore id=36 zone=PLAY zonePos=0 cardId=HERO_08 player=2"

out = get_item(item, str1)

print out