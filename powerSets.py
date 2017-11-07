# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:46:14 2017

@author: yzamriy

Context: exercises for MIT6.00.2x

Goal: generate power sets
"""

# this function was provided as an example
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

# this function was written by me for the following assignment
# Write a generator that returns every arrangement of items such that each is 
# in one or none of two different bags. Each combination should be given 
# as a tuple of two lists, the first being the items in bag1, 
# and the second being the items in bag2.

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if i//3**j % 3 == 1:
                bag1.append(items[j])
            elif i//3**j%3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

items =  ['a','b']
onebag = powerSet(items)
twobags = yieldAllCombos(items)

#next(x)    