# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:42:19 2022

@author: J.Mo
"""

import time
start = time.time()

import pandas as pd
import numpy as np


 
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180





def total_value(items, cap):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) <= cap else 0

def sort (items):
    return sorted(items, key=lambda item:item[2]/item[1], reverse=True)
    
bag = {}
def pack(items, cap):
    if not items:
        return ()
    if (items,cap) not in bag:
        head = items[0]
        tail = items[1:]
        include = (head,) + pack(tail, cap - head[1])
        dont_include = pack(tail, cap)
        if total_value(include, cap) > total_value(dont_include, cap):
            answer = (head,) + pack(tail, cap - head[1])
        else:
            answer = dont_include
        bag[(items,cap)] = answer
    return bag[(items,cap)]
    

 
solution = pack(items, cap)
print("items:")
for x in solution:
    print( x[0])
print ("For a total value of", total_value(solution, cap), "and a total volume of", sum([x[1] for x in solution]))



end = time.time()
print("For a total time in seconds of ")
print(end - start)