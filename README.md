# hs_logreader
Log file reader for Blizzard's Hearthstone

This project is for interpreting the log file written by Hearthstone.

To configure Hearthstone to record a log, follow the steps here:
http://www.wowhead.com/forums&topic=240410/how-to-full-permanent-logging-of-your-game-history

Note that this does not violate the ToS.



Usage:

The main program is "real_time_cards.py", which assembles a dataframe that looks like this:
                     name    cardId player
1              GameEntity       NaN    NaN
2                  Aspera       NaN    NaN
3           The Innkeeper       NaN    NaN
4            Anduin Wrynn   HERO_09      1
5             Lesser Heal  CS1h_001      1
6       Twilight Guardian    AT_017      1
...
76     Power Word: Shield  CS2_004e      1
77     Twilight Endurance  BRM_004e      1

Where the index is the entity ID assigned by Hearthstone, and the other information is filled in as it is revealed in the game. If "logfile" points to the log and "realtime" is set to True, this dataframe updates in real time. If "realtime" is set to False, the dataframe is assembled all at once from a complete game log.


To do:
Make a deck tracker
Make a GUI
