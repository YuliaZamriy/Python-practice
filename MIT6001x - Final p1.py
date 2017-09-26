# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:52:34 2017

@author: Zamriyka
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    total = 0
    intPresent = False
    for i in s:
        try:
            total += int(i)
            intPresent = True
        except:
            pass
    if intPresent == False:
        raise ValueError
    else:
        return total
    
#print(sum_digits("a;35d4"))
print(sum_digits("a"))

#%%

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 

    def flatten(t):    
        flat_t = []
        for i in t:
            if isinstance(i, list) or isinstance(i, tuple):
                for j in flatten(i):
                    flat_t.append(j)
            else:
                flat_t.append(i)
    
        return flat_t
    
    return max(flatten(t))

#print(max_val((5, (1,2), [[1],[9]])))
print(max_val((5, (1,2), [[1],[2]])))

#%%

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    key_code = {}
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    
    decoded = []
    for j in code:
        decoded.append(key_code[j])
    
    return (key_code, ''.join(decoded))
    
print(cipher("abcd", "dcba", "dab"))

#%%

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)
    
    def __add__(self, other):
        new = Bag()
        for e in set(self.vals) | set(other.vals):
            new.vals[e] = self.vals.get(e, 0) + other.vals.get(e, 0)
        return new

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        self.vals.pop(e, None) 

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return True if e in self.vals else False
        
#d1 = ASet()
#d1.insert(4)
#d1.insert(4)
#d1.remove(2)
#print(d1)
#d1.remove(4)
#print(d1) 

d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))       
        
#d1 = Bag()
#d1.insert(4)
#d1.insert(4)
#print(d1)
#d1.remove(2)
#print(d1)

#d1 = Bag()
#d1.insert(4)
#d1.insert(4)
#d1.insert(4)
#print(d1.count(2))
#print(d1.count(4))

#a = Bag()
#a.insert(4)
#a.insert(3)
#b = Bag()
#b.insert(4)
#print(a+b)

#a = Bag()
#a.insert(4)
#a.insert(4)
#a.insert(4)
#b = Bag()
#b.insert(2)
#print(a+b)

#%%

