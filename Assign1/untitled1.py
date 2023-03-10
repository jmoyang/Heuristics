# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:11:11 2022

@author: J.Mo
"""

# Determine start time
import time
start = time.time()
import pandas as pd
# Need itertools and combinations to form all combinations of items.
from itertools import combinations
 
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180



from itertools import takewhile


def item_efficiency(item):
    name, weight, value = item
    return float(value)/float(weight)

                   
def pack_bag(comb):
    name, weight, value = comb
    pack_bag.max_weight -= weight
    return pack_bag.max_weight >=0    

pack_bag.max_weight = cap  # static variable implementation

# pack the most efficient item until pack_bag.max_weight is reached.
pack = list(takewhile(pack_bag, reversed(sorted(items, key=item_efficiency))))



# print output
for item in pack:
    print(item[0])

table = list(zip(*pack))
print("For a total value of %i and a total volume of %i" % (sum(table[2]), sum(table[1])))

# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)

# Items a collection of = ((Item Name, Volume, Value), ...)




