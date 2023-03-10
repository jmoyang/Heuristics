# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:13:27 2022

@author: J.Mo
"""
import pandas as pd

import time
start = time.time()
 #Data Set 10 
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
'''
#Made up data 
items = (('Item 1', 47, 62), ('Item 2', 19, 17), ('Item 3', 21, 55), 
         ('Item 4', 25, 1), ('Item 5', 11, 25), ('Item 6', 16, 49), 
         ('Item 7', 13, 68), ('Item 8', 33, 67), ('Item 9', 30, 98), 
         ('Item 10', 34, 42), ('Item 11', 21, 74), ('Item 12', 17, 62), 
         ('Item 13', 51, 17), ('Item 14', 42, 29), ('Item 15', 15, 30), 
         ('Item 16', 31, 64), ('Item 17', 28, 44), ('Item 18', 30, 64), 
         ('Item 19', 31, 22), ('Item 20', 20, 77), ('Item 21', 20, 15), 
         ('Item 22', 56, 1), ('Item 23', 12, 89), ('Item 24', 48, 1), 
         ('Item 25', 22, 92), ('Item 26', 18, 17), ('Item 27', 36, 61), 
         ('Item 28', 34, 78), ('Item 29', 17, 15), ('Item 30', 21, 63))
cap = 74
'''
    

def item_value(item):
    return item[2] / item[1] #value of the item

def packit(items, cap):
    """Return a list of items with the maximum value, subject to the
    constraint that their combined weight must not exceed max_weight.

    """    
    def bag(item):
        if item[1] <= bag.cap:  #if weight of the item is greater than equal to the max weight,
            bag.cap -= item[1] # subtract the weight from max weight of the bag since the item of the weight is full
            return True
        else:
            return False

    bag.cap= cap
    return pd.DataFrame(filter(bag, sorted(items, key=item_value, reverse=True))) #"filter


dt= packit(items, cap)
packed = dt.values.tolist()

print("Knapsack contains the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in packed)))
print("For a total value of ", sum(dt[2])," and a total volume of ", sum(dt[1]))

# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)