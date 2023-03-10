# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:13:27 2022

@author: J.Mo
"""
import pandas as pd
from itertools import product
from itertools import takewhile
items = (
    ("Item 1", 382745, 825594), 
    ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), 
    ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), 
    ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), 
    ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), 
    ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), 
    ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), 
    ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), 
    ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), 
    ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), 
    ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), 
    ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180


def efficiency(item):
    """Return efficiency of item (its value per unit weight)."""
    return float(item[2]) / float(item[1])

def packing(items=items, max_weight=cap):
    """Return a list of items with the maximum value, subject to the
    constraint that their combined weight must not exceed max_weight.

    """    
    def pack(item):
        # Attempt to pack item; return True if successful.
        if item[1] <= pack.max_weight:
            pack.max_weight -= item[1]
            return True
        else:
            return False

    pack.max_weight = max_weight
    return list(filter(pack, sorted(items, key=efficiency, reverse=True)))



dt= pd.DataFrame(packing(items, cap))


print("For a total value of ", sum(dt[2])," and a total volume of ", sum(dt[1]))