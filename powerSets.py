# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:46:14 2017

@author: yzamriy

Context: exercises for MIT6.00.2x

Goal: generate power sets
"""

# The below function was provided as an example:
# Suppose we have a generator that returns every combination of objects in one bag. 
# We can represent this as a list of 1s and 0s denoting 
# whether each item is in the bag or not.

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

import itertools 

# generate all combinations of N items in the list
def powerSetIT(items):
    ''' Requires itertools package.
        Goal: generate a power set containing all possible sets of the input list
        Input: list of items
        Output: yields one set at a time
        Details: uses itertools.combinations() method to go through all combinations of items of all possible lengths (between 0 and the length of the input list)
    '''
    # iterates through all possible lengths of sets
    for listlen in range(len(items) + 1):
        # generates tuples with all possible combinations of list items 
        # within specified length ('listlen')
        for oneset in itertools.combinations(items, listlen):
            # returns a tuple
            yield oneset
            

# The below function was written by me for the following assignment:
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
            if (i // (3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3**j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

def yieldAllCombosNBags(items, bags):
    N = len(items)
    complexity = bags + 1
    for i in range(complexity**N):
        allbags = []
        for b in range(bags):
            b = []
            allbags.append(b)
        print('allbags', allbags)
        for j in range(N):
            bag_num = (i // (complexity**j)) % complexity
            if bag_num == 0:
                break
            for b in allbags:
                print('bag n:', bag_num, 'bag index:', allbags.index(b))
                if bag_num == allbags.index(b) + 1:
                    b.append(items[j])
                    break
        yield allbags

items =  ['a','b','c']
onebag = powerSet(items)
twobags = yieldAllCombos(items)
nbags = yieldAllCombosNBags(items, 3)
#next(nbags)    