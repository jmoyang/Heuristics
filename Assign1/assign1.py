# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 16:58:06 2022

@author: J.Mo
"""

import time
start = time.time()

import pandas as pd

from itertools import combinations

# Data Set 10:
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180
#(Item Name, Volume, Value), ...)
def get_max_value(items, capacity):
    bag = sorted(items, key=lambda item:item[2]/item[1], reverse=True)
    c_item = list()
    profit = 0 
    for data in items: 
        if capacity - data[1]>0:
            capacity -= data[1]
            profit += data[2]
            c_item.append([data[0], data[1], data[2]])
        else: 
            break
    return profit,c_item 
print(get_max_value(items, cap))

# Determine start time
import time
start = time.time()

# Need itertools and combinations to form all combinations of items.
from itertools import combinations
 
def anycomb(items):
    # Creates all possible combinations of items.
    return ( comb
             for r in range(1, len(items)+1)
             for comb in combinations(items, r)
             )
 