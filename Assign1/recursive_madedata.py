# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:42:19 2022

@author: J.Mo
"""

import time
start = time.time()


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




def total_value(items, cap):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) <= cap else 0


    
bag = {}
def pack(items, cap):
    if not items:
        return ()
    if (items,cap) not in bag:
        initial = items[0]
        later = items[1:]
        put = (initial,) + pack(later, cap - initial[1])
        dont_put = pack(later, cap)
        if total_value(put, cap) > total_value(dont_put, cap):
            result = (initial,) + pack(later, cap - initial[1])
        else:
            result = dont_put
        bag[(items,cap)] = result
    return bag[(items,cap)]
    

 
solution = pack(items, cap)

print ("For a total value of", total_value(solution, cap), "and a total volume of", sum([x[1] for x in solution]))



end = time.time()
print("For a total time in seconds of ")
print(end - start)