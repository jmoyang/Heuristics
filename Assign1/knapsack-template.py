# -*- coding: utf-8 -*-
"""
@author: jhwilck

Alogorithm works on a value based by scoring each, akin to
"Calories per ounce."  Simple Ratio.  Best item goes first.
Continue until no items fit.  

"""
# Determine start time
import time
start = time.time()

import pandas as pd

# Sample Data -- insert data here to run a problem.

# Data Set Trial:
    
    
    
# Data Set 10:
items = (
    ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
    )
cap = 6404180

#items = (('Item 1', 47, 62), ('Item 2', 19, 17), ('Item 3', 21, 55), 
 #        ('Item 4', 25, 1), ('Item 5', 11, 25), ('Item 6', 16, 49), 
  #       ('Item 7', 13, 68), ('Item 8', 33, 67), ('Item 9', 30, 98), 
   #      ('Item 10', 34, 42), ('Item 11', 21, 74), ('Item 12', 17, 62), 
    #     ('Item 13', 51, 17), ('Item 14', 42, 29), ('Item 15', 15, 30), 
     #    ('Item 16', 31, 64), ('Item 17', 28, 44), ('Item 18', 30, 64), 
      #   ('Item 19', 31, 22), ('Item 20', 20, 77), ('Item 21', 20, 15), 
       #  ('Item 22', 56, 1), ('Item 23', 12, 89), ('Item 24', 48, 1), 
        # ('Item 25', 22, 92), ('Item 26', 18, 17), ('Item 27', 36, 61), 
         #('Item 28', 34, 78), ('Item 29', 17, 15), ('Item 30', 21, 63))
#cap = 74

# Convert Tuple to Data Frame
df=pd.DataFrame(list(items), columns=["Name","Size","Value"])
  
# Score and sort the dataframe
df['Score']=df['Value']/(df['Size'])
df=df.sort_values('Score',ascending=False)
    
load = 0.0            # current volume in knapsack
value = 0.0           # current value of items in knacksack    
room_remaining=cap    # start with an empty pack

print("Knapsack contains the following items")

while room_remaining > 1:  # any room left in the pack?
       
    # throw out anything too big to fit
    index_names=df[df['Size']>room_remaining].index.tolist()
    df.drop(index_names, inplace=True)
    if df.empty == True :  break      #as a result, if nothing fits, stop here!

    #increment load - first item in inventory
    load=load+df.iloc[0]['Size']
    print(df.iloc[0]['Name'] )
    
    #increment value - first item in inventory
    value=value+df.iloc[0]['Value']

    #update room_remaining
    room_remaining=cap-load
    
    #remove item from inventory -- first item in inventory
    df.drop(df.index[0], inplace=True)
    
print("For a total value of ", value," and a total volume of ", load)

# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)