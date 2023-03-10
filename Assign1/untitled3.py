# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 23:19:47 2022

@author: J.Mo
"""
# Determine start time
import time
start = time.time()
from itertools import combinations
import pandas as pd
import numpy as np

items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180




data= pd.DataFrame(list(items), columns=["Name","Size","Value"])
#status = list(len(data))
data["Score"] = data["Value"] / data["Size"]

reason = "Value"  # weight or density
rest = cap
values = 0
data = data.sort_values(by=reason, ascending=False).reset_index().drop(["index"], axis=1)
index = 0


def best_weight(data, reason, rest, values, index):
    #print(reason, rest, values, index)

    if rest < np.min(data.loc[range(index, len(data)), "Size"]) or (index == len(data)):
        return values
    else:
        if rest >= data["Size"][index]:
            rest = rest - data["Size"][index]
            values = values + data["Value"][index]
            index = index + 1
            values=best_weight(data, reason, rest, values, index)
            return values
        else:
            index = index + 1
            values=best_weight(data, reason, rest, values, index)
            return values
yyt = best_weight(data, reason, rest, values, index)
print(yyt)

#print("For a total value of %i and a total volume of %i" % (sum(table[2]), sum(table[1])))

# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)
