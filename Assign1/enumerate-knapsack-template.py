# -*- coding: utf-8 -*-
"""
@author: jhwilck

Algorithm solves with complete enumeration.

"""
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
 
def totalvalue(comb):
    # Calculate the total value and check feasibility of a combination of items.
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= cap else (0, 0)

# Items a collection of = ((Item Name, Volume, Value), ...)

'''
# Data Set 10:
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180
'''

items = (('Item 1', 14, 17), ('Item 2', 14, 80), ('Item 3', 18, 84), ('Item 4', 38, 88), 
         ('Item 5', 49, 32), ('Item 6', 54, 42), ('Item 7', 32, 72), ('Item 8', 27, 24), 
         ('Item 9', 20, 93), ('Item 10', 15, 55), ('Item 11', 34, 32), ('Item 12', 30, 89), 
         ('Item 13', 40, 6), ('Item 14', 53, 28), ('Item 15', 50, 22), ('Item 16', 15, 98), 
         ('Item 17', 23, 44), ('Item 18', 37, 47), ('Item 19', 19, 91), ('Item 20', 45, 76), 
         ('Item 21', 41, 52), ('Item 22', 28, 35), ('Item 23', 22, 57), ('Item 24', 42, 59), 
         ('Item 25', 55, 27), ('Item 26', 19, 64), ('Item 27', 16, 47), ('Item 28', 47, 38), 
         ('Item 29', 37, 90), ('Item 30', 26, 12))
cap = 79


bagged = max( anycomb(items), key=totalvalue)

print("Knapsack contains the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print("For a total value of %i and a total volume of %i" % (val, -wt))

# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)